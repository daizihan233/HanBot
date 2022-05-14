import asyncio
import json
import os
import re

import aiohttp
import requests


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
