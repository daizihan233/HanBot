import asyncio
import datetime
import json
import os
import re

import aiohttp
import numpy as np
import requests
from chinese_calendar import is_workday


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

    print(t(gid, uid))


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
    print('发现 {} 的加群请求！'.format(gid))
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
        print(err)


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
    print(tmp)
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
    return j.join(re.compile('[0-9]+').findall(s))


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
        print()
        print(f'{ts} = {ans}')
        return f'{ts} = {ans}'

    return print_yajuu(i, yajuu)


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
    print(tmp)
    return tmp


def get_bread():
    with open('bread.txt', 'r', encoding='utf-8') as f:
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
        f.write(n)
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
