import asyncio
import datetime
import fcntl
import json
import os
import random
import re
import time

import aiohttp
import imagehash
import numpy as np
import redis
import requests
from PIL import Image
from chinese_calendar import is_workday

from richc import console


def isexists_dir_create(path):
    if not os.path.exists(path):
        open(path, 'w', encoding='utf-8').close()


def send_114514(msg, gid, uid):
    async def s(m, g, u):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'send_group_msg', 'params': {
                    'group_id': g,  # 往这个群发条消息
                    'message': u + m  # 消息内容
                }})
                data = await ws.receive_json()
        return data

    asyncio.run(s(msg, gid, uid))


def tick(gid, uid):
    def t(g, u):
        tmp = requests.get(f'http://127.0.0.1:5700/set_group_kick?group_id={g}&user_id={u}')
        data = tmp.text
        return json.loads(data)

    console.print(t(gid, uid))


def donot_processing_plus_group(flag, t, reason):
    async def nppg(f, s, r):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': '/set_group_add_request', 'params': {
                    'flag': f,
                    'sub_type': s,
                    'reason': r
                }})
                data = await ws.receive_json()
        return data

    asyncio.run(nppg(flag, t, reason))


def add_group_automatic_consent(gid, uid, comment, right, flag, t):
    console.print('发现 {} 的加群请求！'.format(gid))
    # 将所有元素全部大写，方便检测
    for i in range(len(right)):
        right[i] = right[i].upper()
    fuck = open('fucklist', 'r').readlines()
    for i in range(len(fuck)):
        fuck[i] = fuck[i].strip('\n')
    if str(uid) in fuck:
        donot_processing_plus_group(flag, t, '「自动操作」由于在黑名单中，所以拒绝了您的加群请求')
        send(gid=gid, msg='各位管理员请注意！！！\n'
                          '[Robot][Event] 加群事件\n'
                          'QQ号：{0}\n'
                          '答案：{1}\n'
                          '机器人一次未审核通过，因为此人在黑名单内\n'
                          '执行操作：拒绝'.format(uid, comment))
    else:
        if comment.upper() in right:
            requests.get('http://127.0.0.1:5700/set_group_add_request?'
                         'flag={0}&'
                         'sub_type={1}&'
                         'approve=true'.format(flag, t))
            send(gid=gid, msg='[Robot][Event] 加群事件\n'
                              'QQ号：{0}\n'
                              '答案：{1}\n'
                              '机器人一次审核通过！\n'
                              '执行操作：通过'.format(uid, comment))
        else:
            send(gid=gid, msg='各位管理员请注意！！！\n'
                              '[Robot][Event] 加群事件\n'
                              'QQ号：{0}\n'
                              '答案：{1}\n'
                              '机器人一次审核未通过\n'
                              '请管理员尽快进行二次审核！\n'
                              '执行操作：（无操作）'.format(uid, comment))


async def set_group_card(card, gid, uid):
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
            await ws.send_json({'action': 'set_group_card', 'params': {
                'group_id': gid,  # 在这个群里
                'user_id': uid,  # 把这个人的昵称
                'card': card  # 设为这个
            }})
            data = await ws.receive_json()
    return data


def tencent_api(word):
    import json
    from tencentcloud.common import credential
    from tencentcloud.common.profile.client_profile import ClientProfile
    from tencentcloud.common.profile.http_profile import HttpProfile
    from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
    from tencentcloud.nlp.v20190408 import nlp_client, models
    try:
        cred = credential.Credential(open('cloud', 'r').read().split(' ')[0], open('cloud', 'r').read().split(' ')[1])
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        req = models.SentimentAnalysisRequest()
        params = {
            "Text": word,
            "Mode": "3class"
        }
        req.from_json_string(json.dumps(params))

        resp = client.SentimentAnalysis(req)
        return json.loads(resp.to_json_string())

    except TencentCloudSDKException as err:
        console.print(err)


def send(msg, gid, uid=None):
    async def is_at(m, g, u):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'send_group_msg', 'params': {
                    'group_id': g,  # 往这个群发条消息
                    'message': '[CQ:at,qq=' + str(u) + ']' + m  # 消息内容
                }})
                data = await ws.receive_json()
        return data

    async def no_at(m, g):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'send_group_msg', 'params': {
                    'group_id': g,  # 往这个群发条消息
                    'message': m  # 消息内容
                }})
                data = await ws.receive_json()
        return data

    if uid is not None:
        tmp = asyncio.run(is_at(msg, gid, uid))
    else:
        tmp = asyncio.run(no_at(msg, gid))
    console.print(tmp)
    return tmp


def forbidden_words(gid, uid, tim=11 * 86400 + 4 * 3600 + 51 * 60):
    async def fw(g, u, t):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'set_group_ban', 'params': {
                    'group_id': g,
                    'user_id': u,
                    'duration': t
                }})
                data = await ws.receive_json()
        return data

    asyncio.run(fw(gid, uid, tim))


def get_all_number(s: str, j: str = ''):
    return j.join(re.compile('\\d+').findall(s))


def odor_digital_demonstrator(i):
    yajuu = {
        0: '1+1+4-5-1**4',
        1: '1+1+4-5*1**4',
        2: '1+1+4-5+1**4',
        3: '1+1-4+5*1**4',
        4: '1+1+4-5-1+4',
        5: '1+1+4-5+1*4',
        6: '1+1+4+5-1-4',
        7: '1+1+4+5-1*4',
        8: '1+1+4+5+1-4',
        9: '1+1*4+5-1**4'
    }

    def print_yajuu(s, dic):
        ts = s
        ans = ''
        while s >= 10:
            digi = np.floor(np.log10(s))
            tmp = s % 10 ** digi
            ans += '(%s)*(1+1+4+5-1**4)**(%s)+' % (dic[(s - tmp) / 10 ** digi], dic[digi])
            s -= s - tmp
        ans += dic[s]
        console.print()
        console.print(f'{ts} = {ans}')
        return f'{ts} = {ans}'

    return print_yajuu(i, yajuu)


def is_fucker(uid):
    return str(uid) in safe_file_read('fucklist').split('\n')


def ssend(msg, uid, gid=None):
    async def in_gid(m, u, g):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'send_msg', 'params': {
                    'user_id': u,
                    'group_id': g,
                    'message': m
                }})
                data = await ws.receive_json()
        return data

    async def not_in_gid(m, u):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'send_msg', 'params': {
                    'user_id': u,
                    'message': m
                }})
                data = await ws.receive_json()
        return data

    if gid is not None:
        tmp = asyncio.run(in_gid(msg, uid, gid))
    else:
        tmp = asyncio.run(not_in_gid(msg, uid))
    console.print(tmp)
    return tmp


def get_bread():
    with open('bread.txt', 'r', encoding='utf-8') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        bread = f.read()
    return int(bread)


def get_bread_mode():
    """
    0: 停工
    1: 工厂模式
    2: 现做模式
    """
    with open('mode_bread.txt', 'r', encoding='utf-8') as f:
        bread_mode = f.read()
    return int(bread_mode)


def set_bread_mode(mode: int):
    with open('mode_bread.txt', 'w', encoding='utf-8') as f:
        f.write(str(mode))


def add_bread(num):
    n = str(get_bread() + num)
    with open('bread.txt', 'w', encoding='utf-8') as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        f.write(n)
        fcntl.flock(f, fcntl.LOCK_UN)
    del n


def is_workday_now():
    return is_workday(  # 是工作日吗？
        datetime.datetime(  # 哪一天？
            datetime.datetime.now().year,  # 今天是哪一年？
            datetime.datetime.now().month,  # 今天是哪一月？
            datetime.datetime.now().day  # 今天是哪一天？
        )
    )


# 正则匹配
def re_match(pattern, string):
    return re.match(pattern, string) is not None


def get_hit():
    hit = json.loads(requests.get("https://v1.hitokoto.cn/").text)
    return hit["hitokoto"], hit["from"]


def get_bili(uid):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="97", "Chromium";v="97"',
        'DNT': '1',
        'sec-ch-ua-mobile': '?0',
        'Client-Version': '2.6.11b',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62',
        'Client': 'web',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,nl;q=0.5',
    }
    followers = json.loads(requests.get(f'https://api.bilibili.com/x/relation/stat?vmid={uid}').text)['data'][
        "follower"]
    temp = json.loads(requests.get(f'https://api.bilibili.com/x/space/upstat?mid={uid}', headers=headers, cookies={
        'SESSDATA': '1eafea96,1671373904,d5f6b*61'
    }).text)
    console.print(temp)
    if temp['code'] == 0:
        likes = temp['data']['likes']
        archive = temp['data']['archive']['view']
        msg = 'Good! 程序完美运行！'
    else:
        likes = 0
        archive = 0
        msg = f'Fuck! 程序发生未知错误：{temp["code"]}'
    if temp['code'] == -412:
        msg = '如果你看见这条消息证明请求被叔叔拦截了 :)'
    return {
        'f': followers,
        'l': likes,
        'a': archive,
        'm': msg
    }


def match_group(p: str, s: str):
    t = re.compile(p).match(s)
    if t is not None:
        return t.group()
    else:
        return ''


def all_prohibitions(gid, t):
    async def st(gi, ti):
        async def start(g):
            async with aiohttp.ClientSession() as session:
                async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                    await ws.send_json({'action': 'set_group_whole_ban', 'params': {
                        'group_id': g,
                        'enable': True  # 消息内容
                    }})
                    data = await ws.receive_json()
            return data

        async def closed(g):
            async with aiohttp.ClientSession() as session:
                async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                    await ws.send_json({'action': 'set_group_whole_ban', 'params': {
                        'group_id': g,
                        'enable': False  # 消息内容
                    }})
                    data = await ws.receive_json()
            return data

        await start(gi)
        time.sleep(ti)
        await closed(gi)

    asyncio.run(st(gid, t))


def is_admin(uid):
    return str(uid) in safe_file_read("admin.txt").split('\n')


def is_match(p: str, s: str, t) -> bool:
    return match_group(p, s) == t if re_match(p, s) is not None else False


def send_ws(node: str, jsn: dict) -> dict:
    async def f(n, j):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': n, 'params': j})
                data = await ws.receive_json()
        return data

    return asyncio.run(f(node, jsn))


def sensitive_words(s: str, st: str):
    return st in s


def del_msg(msg_id):
    async def d(mi):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'delete_msg', 'params': {
                    'message_id': mi
                }})

    asyncio.run(d(msg_id))


def safe_file_read(filename: str, encode: str = "UTF-8"):
    with open(filename, 'r', encoding=encode) as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        tmp = f.read()
    return tmp


def safe_file_write(filename: str, s, mode: str = "w", encode: str = "UTF-8"):
    if 'b' not in mode:
        with open(filename, mode, encoding=encode) as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            f.write(s)
    else:
        with open(filename, mode) as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
            f.write(s)


def get_lock_level():
    return safe_file_read('lock')


def add_grouper(flag, typ, stat: bool = True):
    async def y(f, t, s):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'set_group_add_request', 'params': {
                    'flag': f,
                    'sub_type': t,
                    'approve': s
                }})

    asyncio.run(y(flag, typ, stat))


def get_lock_detailed(level: int):
    return '''1. 强·不允许入群
封锁整个入群通道，禁止任何人入群、邀请
（尽管由最高苏维埃特批也不彳亍，一般用于很严重的事件）''' if level == 1 else '''2. 不允许入群
封锁除特批外的其他入群通道，通过群成员邀请进入的一律拦截
（特批的判定是由机器人管理员邀请进群的一律视为特批）''' if level == 2 else '''3. 弱·不允许入群·普通
封锁普通入群通道，邀请由管理员审核并放行''' if level == 3 else '''4. 弱·不允许入群
封锁普通群成员邀请入群通道''' if level == 4 else '''5. 黑名单拦截
拦截所有黑名单人员''' if level == 5 else '''6. 监视模式
监视入群事件，黑名单人员不放行，除特批外''' if level == 6 else '''7. 放行模式
不进行任何监视与处理'''


def sf(g):
    t_s_ret = send_ws('get_group_member_list', {
        "group_id": g
    })['data']
    for i in t_s_ret:
        if is_fucker(i):
            tick(g, i)


def quick_operation(context, operation):
    send_ws(".handle_quick_operation", {
        "context": context,
        "operation": operation
    })


def modify_list_at_file(filename: str, s):
    t = safe_file_read(filename).split('\n')
    if str(s) not in t:
        t.append(s)
    else:
        t.remove(s)
    t = list(map(str, t))
    safe_file_write(filename, '\n'.join(t))
    return True if str(s) in t else False


def match_and_replace(mat: str, text: str, retext: str):
    mt = re.match(mat, text)
    if mt is not None:
        if mt.group(1) is not None:
            return re.sub(mat, retext.format(mt.group(1)), text)
    else:
        return text
    return re.sub(mat, retext, text)


def match_list(p, s):
    return re.compile(p).findall(s)


def tencent_image_api(url, biz):
    import json
    from tencentcloud.common import credential
    from tencentcloud.common.profile.client_profile import ClientProfile
    from tencentcloud.common.profile.http_profile import HttpProfile
    from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
    from tencentcloud.ims.v20201229 import ims_client, models
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey,此处还需注意密钥对的保密
        # 密钥可前往https://console.cloud.tencent.com/cam/capi网站进行获取
        cred = credential.Credential(open('cloud', 'r').read().split(' ')[0], open('cloud', 'r').read().split(' ')[1])
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ims.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = ims_client.ImsClient(cred, "ap-beijing", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.ImageModerationRequest()
        params = {
            "BizType": biz,
            "FileUrl": url
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个ImageModerationResponse的实例，与请求对象对应
        resp = client.ImageModeration(req)
        console.print(resp.to_json_string())
        # 输出json格式的字符串回包
        t = json.loads(resp.to_json_string())
        return t['Suggestion'], t['Label'], t['RequestId']
    except TencentCloudSDKException as err:
        console.print(err)
        return 'Pass'


def img_safe(msg, msg_id, biz, gid):
    mlist = match_list(r'\[CQ:image,.*]', msg)
    for im in mlist:
        im = im.strip('[]')
        im = im.split(',')[1:]
        imurl = None
        fl = False
        for imtl in im:
            if imtl[:4] == 'url=':
                imurl = imtl[4:]
            if imtl[:9] == 'subType=0':
                fl = True
        if fl and imurl is not None:
            console.print('检测到图片：', imurl)
            safe_file_write('tmp114.png', requests.get(imurl).content, 'wb')
            dh = str(imagehash.dhash(Image.open('tmp114.png')))
            # 检查Redis中是否存在该图片的hash值
            p = redis.ConnectionPool(host='43.155.62.167', port=6379, decode_responses=True)
            r = redis.Redis(connection_pool=p)
            if r.hexists('imh', dh):
                console.print('该图片已存在，获取Redis中的信息')
                dhu = r.hget('imh', dh)
                dhu = dhu.split(',')
                console.print('Redis中的信息-dhu：', dhu)
                console.print('Redis中的信息-dh：', dh)
                ta = (dhu[0], "(From Redis, it's UNKNOW)", dhu[1])
            else:
                ta = tencent_image_api(imurl, biz)
                r.hset('imh', dh, f'{ta[0]},{ta[2]},{imurl}')
                r.hset('imh', ta[2], f'{dh}')
                console.print(ta)
            if ta[0] == 'Block':  # 确定
                del_msg(msg_id)  # 撤回
                send(f'图片ID：{ta[2]}\n'
                     f'一眼丁真，鉴定为：{ta[1]}', gid)  # ta[1] == 消息类别
            elif ta[0] == 'Review':  # 疑似
                send(f'[CQ:reply,id={msg_id}]\n'
                     f'图片ID：{ta[2]}\n'
                     f'#NSFW Not Safe For Work 警告\n'
                     f'此消息疑似含有 {ta[1]} 内容\n'
                     f'建议由人工识别过后再做出处理', gid)


def is_debug():
    return True if safe_file_read('isd.on') == '1' else False


def is_member(gid: int, uid: int) -> bool:
    d = send_ws('get_group_member_info', {
        "group_id": gid,
        "user_id": uid,
        "no_cache": random.choice([True, False])
    })
    try:
        return True if d['data']['role'] == 'member' else False
    except TypeError:
        console.print(d)


def is_bot(uid) -> bool:
    p = redis.ConnectionPool(host='43.155.62.167', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=p)
    dhu = r.hget('isbot', uid)
    if dhu is None:
        s_bot(uid, [1, time.time()])
        return False


def f_bot(uid) -> bool:
    ...


def s_bot(uid, v):
    p = redis.ConnectionPool(host='43.155.62.167', port=6379, decode_responses=True)
    r = redis.Redis(connection_pool=p)
    r.hset('isbot', str(uid), str(v))
