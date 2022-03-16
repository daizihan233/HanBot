import os
import random
import urllib
from urllib import parse

import aiohttp
import asyncio
import requests


def isexists_dir_create(path):
    if not os.path.exists(path):
        open(path, 'w', encoding='utf-8').close()


def send(msg, gid, uid=None):
    async def is_at(msg, gid, uid):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'send_group_msg', 'params': {
                    'group_id': gid,  # 往这个群发条消息
                    'message': '[CQ:at,qq=' + str(uid) + ']' + msg  # 消息内容
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


def send_114514(msg, gid, uid):
    async def send(msg, gid, uid):
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect('ws://127.0.0.1:6700/api') as ws:
                await ws.send_json({'action': 'send_group_msg', 'params': {
                    'group_id': gid,  # 往这个群发条消息
                    'message': uid + msg  # 消息内容
                }})
                data = await ws.receive_json()
        return data

    asyncio.run(send(msg, gid, uid))


def keyword(msg: str, uid, gid):
    if msg == '' or msg == ' ':
        send('嘿！这里是菜单\n'
             '[00] help\n'
             '语法：@机器人 help [指令]\n'
             '即可查看相关文档\n'
             '所有在这个菜单中没有的都可以在此指令中找到\n'
             '[01] 咕咕咕\n'
             '[02] 黑名单\n'
             '[03] 加群自动同意\n'
             '[04] 特定关键词复读\n'
             '[05] 聊天\n'
             '[06] 祖安戳一戳 / 祖安我 / 祖安@...\n'
             '当你戳一戳机器人或at机器人说“祖安我”、“祖安屑”、“祖安@...”的时候机器人会对你/另一个人会说一句祖安话\n'
             '[07] 申请管理员\n'
             '算是个申请攻略吧\n'
             '[08] 百度\n'
             '[09] 哔哩哔哩\n'
             '[10] 前科查询\n'
             '【功能未开发完善】'
             '语法：@机器人 前科查询 [QQ号]\n'
             '为什么你/他/她/它会被加进黑名单？一查就知道！\n'
             '[11] bb\n'
             '语法：@机器人 bb\n'
             '你就可以看见作者的小声bb'
             , gid, uid)
    else:
        if msg[:4] == 'help':
            command = msg[5:]
            print(command)
            if command == '咕咕咕':
                send('\n请说：咕咕咕（当然也可以是任何数量个咕）', gid, uid)
            elif command == '黑名单':
                send('\n注意：此程序对空格尤为敏感\n'
                     '注意：您必须有机器人管理员权限才能执行此功能\n'
                     'Tips：机器人管理员申请请 @机器人 申请管理员\n'
                     '语法1：@机器人【空格】黑名单【空格】@...（直接@）\n'
                     '语法2：@机器人【空格】黑名单【空格】...（QQ号）', gid, uid)
            elif command == '加群自动同意':
                if gid == 907112053 or gid == 833645046:
                    send('\n当有人加群时如果答案正确则自动同意，\n'
                         '否则就发消息提示', gid, uid)
                else:
                    send('\n【Warning：本群不适配此功能】\n'
                         '当有人加群时如果答案正确则自动同意，\n'
                         '否则就发消息提示', gid, uid)
            elif command == '特定关键词复读':
                send('\n无需@，一条消息必须只包含关键词\n'
                     '支持的关键词（“ | ”分割）：\n'
                     'e | 额 | 呃 | 。 | w | www | 114514 | 1145141919810 | [CQ:face,id=298] | [CQ:face,id=277] | '
                     '[CQ:face,id=178]\n '
                     '比如你说“额”，机器人就会说“额”，但你说“额额“、”额啊“是不会复读的', gid, uid)
            elif command == '聊天':
                send('\n必须@，@尽量置前，不要加回复，尽量不要加表情，直接说内容\n'
                     '使用的小i机器人API', gid, uid)
            elif command == '百度':
                send('\n让我帮你百度一下 :)\n'
                     '百度对您来讲就这么难吗？？？\n'
                     '语法：@机器人【空格】百度【空格】...（要搜的东西）\n'
                     '把最后机器人发出来的网址发给你爱提问的朋友 :)\n', gid, uid)
            elif command == '哔哩哔哩':
                send('参见指令“百度”', gid, uid)
            else:
                send('未查找到此指令的文档！', gid, uid)
        elif msg[:4] == '前科查询':
            qq = msg[5:]
            print(qq)
            fucker = []
            with open('fucker.txt', 'r'):
                pass
        elif msg == 'bb':
            send('\n========\n'
                 'https://github.com/daizihan233/HanBot \n'
                 '↑ 这是这个机器人的代码，欢迎Star！\n'
                 'https://www.hantools.top\n'
                 '↑ 自己闲着蛋疼用GitHub Pages、Girdea、lin作出的网站\n'
                 '↑ 爱看不看吧（\n'
                 '========\n'
                 'GitHub上不去就下载：https://gitee.com/docmirror/dev-sidecar\n'
                 '注意：请仔细阅读文档，否则可能会出现意想不到的问题\n'
                 '其它问题请联系作者QQ：183713750\n'
                 '========\n'
                 '公告：https://shimo.im/docs/KqHXw8XrrwpXqGY9/', gid, uid)
        elif msg == '申请管理员':
            if str(uid) + '\n' in open('admin.txt', 'r', encoding='UTF-8').readlines():
                send('\n啊嘞？发生了一个错误！\n'
                     '>>> Error: already an administrator\n'
                     '>>> 错误：已是管理员\n'
                     '183713750 <<<<< look here!\n'
                     '如果你觉得这个错误不应该发生那就加他！\n'
                     '将这个错误发给他！', gid, uid)
            else:
                send('\n183713750 <<< 加他！\n'
                     '👆 这个是机器人的开发\n'
                     '👇 申请攻略：\n'
                     '👉 详细地说明原因\n'
                     '👉 保证不会恶意操作\n'
                     '👉 保证保证不会滥用职权\n'
                     '👉 已知如果滥用此权限会被撤销\n'
                     '👉 已知在有前科的时候重新申请通过的概率会降低\n'
                     '👉 已知申请成功的概率不是100%', gid, uid)
        elif ("群文件" == msg or "病毒库" == msg) and gid == 764869658:
            send(msg=
                 '''\n中国青年计算机爱好者联盟 （CEA）
China Young Computer Enthusiast Alliance

CN-xzf：https://xzfyyds.lanzoui.com/
OS相关:b02omemwh
浏览器(不经常更新):b02ok1xof
病毒库：b02ojc61a
OS激活相关：b02ojcf0d
驱动相关：b02ojckud
远程控制：b02ojcr4j
杀菌相关：b02ojnape
技术资料：b02ojnaxc
其他：b02ojj7kh
工具支持：蓝奏云 
PS：密码均为 666
群文件
https://share.weiyun.com/XvQofEc0
文件分享上传：http://inbox.weiyun.com/UN5lAjrn
工具支持：腾讯微云''',
                 gid=gid, uid=uid)
        elif msg[:3] == '百度 ':
            msg = msg.split(' ')
            if len(msg) <= 1:
                send('www.baiidu.com', uid, gid)
            else:
                msg.pop(0)
                url = 'https://baidu.physton.com/?q=' + parse.quote(''.join(msg))
                send(url, gid, uid)
        elif msg[:5] == '哔哩哔哩 ':
            msg = msg.split(' ')
            if len(msg) <= 1:
                send('www.bilibili.com', uid, gid)
            else:
                msg.pop(0)
                url = 'https://www.bilitools.top/t/1/?k=' + parse.quote(''.join(msg))
                send(url, gid, uid)
        elif "祖安我" in msg or "祖安屑" in msg or (uid == 2396349635 and gid == 336578274):
            send(requests.get('https://fun.886.be/api.php?level=max').text, gid)
        elif "祖安[CQ:at,qq=" in msg:
            msg = msg.split()
            msg[0] = msg[0].strip('祖安')
            for i in msg:
                if '[CQ:at,qq=' in i:
                    send_114514(requests.get('https://fun.886.be/api.php?level=max').text, gid, i)
        elif ("黑名单" in msg) and ("[CQ:at,qq=" in msg):
            if str(uid) + '\n' in open('admin.txt', 'r', encoding='UTF-8').readlines():
                if len(str(msg).split(' ')) != 2:
                    send('error: 语法错误！应该只有2个空格', gid, uid)
                else:
                    tmp = str(msg).split(' ')
                    try:
                        tmp = tmp[-1][len('[CQ:at,qq='):-1]
                        tmp = int(tmp)
                        if tmp < 10000:
                            send('\n啊嘞？发生一个错误！\n'
                                 '>>> Error: UID minimum is 10000\n'
                                 '>>> 错误：QQ号最小为'
                                 '183713750 <<<<< look here!\n'
                                 '如果你觉得这个错误不应该发生那就加他！\n'
                                 '将这个错误发给他！', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == uid:
                            send('\nctmd！发生一个错误！\n'
                                 '>>> Error: this uid cannot be added\n'
                                 '>>> 错误：此人无法添加'
                                 '183713750 <<<<< 你tmd瞅这里！\n'
                                 '如果你觉得这个错误不应该发生那就加他！\n'
                                 '将这个错误发给他！', gid, uid)
                        else:
                            f = str(str(msg).split(' ')[-1])[len('[CQ:at,qq='):-1]
                            fuck = open('fucklist', 'r').readlines()
                            for i in range(len(fuck)):
                                fuck[i] = fuck[i].strip('\n')

                            if f in fuck:
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '{} 已在黑名单'.format(f.strip())))
                            else:
                                open('fucklist', 'a').write(f + '\n')
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '已添加 {} 至黑名单'.format(f)))
                    except:
                        send('error: 类型错误！QQ应该是int类型，但程序无法将其转为int', gid, uid)
            else:
                if len(str(msg).split(' ')) != 3:
                    send('error: 语法错误！您不是机器人的管理员，需要填写理由（将语法更改为@机器人【空格】黑名单【空格】@...【空格】您的理由）应该至少有3个空格', gid, uid)
                else:
                    tmp = str(msg).split(' ')
                    try:
                        tmp = tmp[-2][len('[CQ:at,qq='):-1]
                        tmp = int(tmp)
                        if tmp < 10000:
                            send('\n啊嘞？发生一个错误！\n'
                                 '>>> Error: UID minimum is 10000\n'
                                 '>>> 错误：QQ号最小为'
                                 '183713750 <<<<< look here!\n'
                                 '如果你觉得这个错误不应该发生那就加他！\n'
                                 '将这个错误发给他！', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == uid:
                            send('\nctmd！发生一个错误！\n'
                                 '>>> Error: this uid cannot be added\n'
                                 '>>> 错误：此人无法添加'
                                 '183713750 <<<<< 你tmd瞅这里！\n'
                                 '如果你觉得这个错误不应该发生那就加他！\n'
                                 '将这个错误发给他！\n'
                                 '淦他*的！\n'
                                 '（恭喜你发现了一个彩蛋）', gid, uid)
                        else:
                            f = str(str(msg).split(' ')[-2])[len('[CQ:at,qq='):-1]
                            r = str(str(msg).split(' ')[-1])
                            fuck = open('fucklist', 'r').readlines()
                            for i in range(len(fuck)):
                                fuck[i] = fuck[i].strip('\n')

                            if f in fuck:
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '{} 已在黑名单'.format(f)))
                            else:
                                requests.get('http://127.0.0.1:5700/send_private_msg?user_id=183713750&message='
                                             '【黑名单】\n'
                                             '[GID]: {}\n'
                                             '[UID]: {}\n'
                                             '[Black]: {}\n'
                                             '[Reason]: {}'.format(gid, uid, f, r))
                                send('已发送至后台，等待人工审核', gid, uid)
                    except:
                        send('error: 类型错误！QQ应该是int类型，但程序无法将其转为int', gid, uid)


        elif "黑名单" in msg:
            if ((str(uid) + '\n') in open('admin.txt', 'r', encoding='UTF-8').readlines()):
                print('admin')
                if len(str(msg).split(' ')) != 2:
                    send('error: 语法错误！应该只有2个空格', gid, uid)
                else:
                    tmp = str(msg).split(' ')
                    try:
                        tmp = tmp[-1]
                        tmp = int(tmp)
                        if tmp < 10000:
                            send('error: 参数错误！QQ号最小应该是10000', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == uid:
                            send('error: 参数错误！无法添加此人', gid, uid)
                        else:
                            f = str(str(msg).split(' ')[-1]) + '\n'
                            fuck = open('fucklist', 'r').readlines()
                            if f in fuck:
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '{} 已在黑名单\n'
                                                                    '（如果发现恶意添加请尽快联系HanTools删除）'.format(f)))
                            else:
                                open('fucklist', 'a').write(f + '\n')
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '已添加 {} 至黑名单\n'
                                                                    '（如果发现恶意添加请尽快联系HanTools删除）'.format(f)))
                    except:
                        send('error: 类型错误！QQ应该是int类型，但程序无法将其转为int', gid, uid)
            else:
                print('not admin')
                print(str(msg).split(' '))
                if len(str(msg).split(' ')) != 3:
                    send('error: 语法错误！您不是机器人的管理员，需要填写理由（将语法更改为@机器人【空格】黑名单【空格】...【空格】您的理由）应该至少有3个空格', gid, uid)
                else:
                    tmp = str(msg).split(' ')
                    try:
                        tmp = tmp[-2]
                        tmp = int(tmp)
                        if tmp < 10000:
                            send('error: 参数错误！QQ号最小应该是10000', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == uid:
                            send('error: 参数错误！无法添加此人', gid, uid)
                        else:
                            f = str(str(msg).split(' ')[-2])
                            r = str(str(msg).split(' ')[-1])
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
                                requests.get('http://127.0.0.1:5700/send_private_msg?user_id=183713750&message='
                                             '【黑名单】\n'
                                             '[GID]: {}\n'
                                             '[UID]: {}\n'
                                             '[Black]: {}\n'
                                             '[Reason]: {}'.format(gid, uid, f, r))
                                send('已发送至后台，等待人工审核', gid, uid)
                    except:
                        send('error: 类型错误！QQ应该是int类型，但程序无法将其转为int', gid, uid)

        elif '咕' in msg:
            msg = str(msg).count('咕')
            isexists_dir_create('gugu{}.txt'.format(gid))
            with open('gugu{}.txt'.format(gid), 'r+', encoding='utf-8') as f:
                t = f.read()
                if t == '':
                    t = 0
                print('t: {}, msg: {}'.format(t, msg))
                import re
                t = int(re.findall(r'\d+', str(t))[0]) + msg
                tmp_file = open('gugu{}.txt'.format(gid), 'w')
                tmp_file.write('')
                tmp_file.close()
                f.write(str(t))
            requests.get('http://127.0.0.1:5700/send_group_msg?'
                         'group_id={0}&'
                         'message=鸽子'
                         '{1}'.format(gid, '您可以咕 {0} 天了').format(t))
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
            msg = urllib.parse.quote(msg)
            ret = requests.get(
                'http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A'
                '%228819ee11968945c2b10da5c81b4d5bbf%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A'
                '%22c15603528da245a2ade587e4d061725b%22%2C%22body%22%3A%7B%22content%22%3A%22' + msg +
                '%22%7D%2C%22type%22%3A%22txt%22%7D&ts=1644758917124').text
            import re
            a = re.findall(r'\"content\":\"(.+?)\\r\\n\"', ret)[-1]
            a = a.replace('\\n', '\n').replace('\\r', '')
            if a != 'defaultReply':
                re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                                  'group_id={0}&'
                                  'message=[CQ:at,qq={1}] '
                                  '{2}'.format(gid, uid, a))
            else:
                a = [  # 无语时的自动回复
                    '额......',
                    'az',
                    '我去Cedar Point坐过山车去了，总比你在这聊天刺激多了',
                    '你需要快车道吗？',
                    '你的机器人暂时崩溃，请换个问题QAQ',
                    '对此时，我表示无法表达',
                    '不会，请换(￣个￣)',
                    '我不知道 :(',
                    '我不知道，但是我知道我是机器人',
                    '额这个，我不会，滚',
                    '我不会，长大后再学习 :)',
                    'e，这个事情你可以去问问其他人，不要让我来嘛(ᗒᗨᗕ)',
                    '机器人系统崩溃(ᗒᗨᗕ)',
                    '哇，你竟然难倒我了，真厉害(≧▽≦)',
                    '鬼'
                ]
                re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                                  'group_id={0}&'
                                  'message=[CQ:at,qq={1}] '
                                  '{2}'.format(gid, uid, random.choice(a)))
            print('requests_get: {0}'.format(re))
            print('send: {0}'.format(a))
