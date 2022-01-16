from fake_useragent import UserAgent
import aiohttp
import asyncio


def send(msg, gid, uid=None):
    async def is_at(msg, gid, uid):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'send_group_msg', 'params': {
                    'group_id': gid,  # 往这个群发条消息
                    'message': '[CQ:at,qq=' + uid + ']' + msg  # 消息内容
                }})
                data = await ws.receive_json()
        return data

    async def no_at(msg, gid):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'send_group_msg', 'params': {
                    'group_id': gid,  # 往这个群发条消息
                    'message': msg  # 消息内容
                }})
                data = await ws.receive_json()
        return data

    if uid is not None:
        asyncio.run(is_at(msg, gid, uid))
    else:
        asyncio.run(no_at(msg, gid))


def keyword(msg, uid, gid):
    import requests
    import json
    if msg == '' or msg == ' ':
        send('嘿！这里是菜单\n'
             '[1] 咕咕咕\n'
             '（部分群可用，无需@）\n'
             '[2] 黑名单\n'
             '语法1：@机器人 黑名单 @...（直接@）\n'
             '语法2：@机器人 黑名单 ...（QQ号）\n'
             '[3] 加群自动同意\n'
             '（部分群可用，无需@，自动检测）\n'
             '[4] 特定关键词复读\n'
             '（无需@，一条消息必须只包含关键词）\n'
             '支持的关键词（“ | ”分割）：\n'
             'e | 额 | 呃 | 。 | w | www | 114514 | 1145141919810 | [CQ:face,id=298] '
             '| [CQ:face,id=277] | [CQ:face,id=178]\n'
             '[5] 聊天\n'
             '（必须@，不要加回复，尽量不要加表情，直接说内容）\n'
             '使用青云客机器人API\n'
             '[6] 祖安戳一戳\n'
             '当你戳一戳机器人的时候他会说一句祖安话',
             gid, uid)
    else:
        if "admin set 咕咕咕 " in msg and (uid == 183713750 or uid == 2443818489):
            with open('gugu.txt', 'w') as file:
                file.write(str(int(msg.strip("admin set 咕咕咕 "))))

            send('您可以咕 {0} 天了'.format(str(int(msg.strip("admin set 咕咕咕 ")))),
                 gid)
        elif "admin set 咕咕咕 " in msg and (uid != 183713750 and uid != 2443818489):
            requests.get('http://127.0.0.1:5700/send_group_msg?'
                         'group_id={0}&'
                         'message=[CQ:at,qq={1}]'
                         '{2}'.format(gid, uid, '你不是机器人的开发者/管理，权限不足，无法完成此操作'))
        elif ("黑名单" in msg) and ("[CQ:at,qq=" in msg):
            f = str(str(msg).split(' ')[-1])[len('[CQ:at,qq='):-1]
            fuck = open('fucklist', 'r').readlines()
            for i in range(len(fuck)):
                fuck[i] = fuck[i].strip('\n')

            if f in fuck:
                requests.get('http://127.0.0.1:5700/send_group_msg?'
                             'group_id={0}&'
                             'message=[CQ:at,qq={1}] '
                             '{2}'.format(gid, uid, '{} 已在黑名单\n'
                                                    '（如果发现恶意添加请尽快联系HanTools删除）'.format(f)))
            else:
                if f != 183713750 and f != 898140027:
                    open('fucklist', 'a').write(f + '\n')
                    requests.get('http://127.0.0.1:5700/send_group_msg?'
                                 'group_id={0}&'
                                 'message=[CQ:at,qq={1}] '
                                 '{2}'.format(gid, uid, '已添加 {} 至黑名单\n'
                                                        '（如果发现恶意添加请尽快联系HanTools删除）'.format(f)))
        elif "黑名单" in msg:
            f = str(str(msg).split(' ')[-1])
            fuck = open('fucklist', 'r').readlines()
            open('fucklist', 'a').write(f + '\n')
            if f in fuck:
                requests.get('http://127.0.0.1:5700/send_group_msg?'
                             'group_id={0}&'
                             'message=[CQ:at,qq={1}] '
                             '{2}'.format(gid, uid, '{} 已在黑名单\n'
                                                    '（如果发现恶意添加请尽快联系HanTools删除）'.format(f)))
            else:
                requests.get('http://127.0.0.1:5700/send_group_msg?'
                             'group_id={0}&'
                             'message=[CQ:at,qq={1}] '
                             '{2}'.format(gid, uid, '已添加 {} 至黑名单\n'
                                                    '（如果发现恶意添加请尽快联系HanTools删除）'.format(f)))
        elif gid == 623377914 and ('咕' in msg):
            msg = str(msg).count('咕')
            with open('gugu.txt', 'r') as file:
                gu = int(file.readlines()[0])
            gu = gu + msg
            with open('gugu.txt', 'w') as file:
                file.write(str(gu))
            requests.get('http://127.0.0.1:5700/send_group_msg?'
                         'group_id={0}&'
                         'message=鸽子'
                         '{1}'.format(gid, '您可以咕 {0} 天了').format(gu))
        elif gid == 623377914 and ('咕' in msg):
            msg = str(msg).count('咕')
            with open('gugu.txt', 'r') as file:
                gu = int(file.readlines()[0])
            gu = gu + msg
            with open('gugu.txt', 'w') as file:
                file.write(str(gu))
            send('鸽子 {1}'.format(gid, '您可以咕 {0} 天了').format(gu), gid)
        elif "e" == msg or "额" == msg or "呃" == msg or "。" == msg or "w" == msg or \
                "www" == msg or msg == "114514" or msg == "1145141919810" or \
                msg == '[CQ:face,id=298]' or msg == '[CQ:face,id=178]' or msg == '[CQ:face,id=277]' or \
                msg == '？' or msg == '?' or msg == '草':
            send(msg, gid)
        elif gid == 623377914 and uid == 2443818489:
            if msg == '吃了:)':
                requests.get('http://127.0.0.1:5700/send_group_msg?'
                             'group_id={0}&'
                             'message='
                             '{1}'.format(gid, ':)'))
            elif msg == '没吃:(':
                requests.get('http://127.0.0.1:5700/send_group_msg?'
                             'group_id={0}&'
                             'message='
                             '{1}'.format(gid, ':('))
        elif msg == '粉丝监测':
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message=[CQ:at,qq={1}] '
                              '{2}'.format(gid, uid, '您可以去找HanTools（183713750）接入机器人'))
            print('request:', re)

        else:
            for i in range(999):
                msg = str(msg).strip("[CQ:face,id=" + str(i) + "]")
            a = requests.get("https://api.qingyunke.com/api.php?key=free&appid=0&msg=" + msg.replace("+", "加"))
            a = json.loads(a.text)
            print(a)
            a = a['content'].replace("{br}", "\n").replace("菲菲", "我").replace("{face:1}", "[CQ:face,id=1]")
            for i in range(999):
                msg = str(a).replace('{face:' + str(i) + '}', "[CQ:face,id=" + str(i) + "]")
            print('msg: {0}'.format(msg))
            print('uid: {0}'.format(uid))
            print('gid: {0}'.format(gid))
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message=[CQ:at,qq={1}] '
                              '{2}'.format(gid, uid, a))
            re = re.text
            print('requests_get: {0}'.format(re))
            print('send: {0}'.format(a))
