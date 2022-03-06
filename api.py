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


def keyword(msg: str, uid, gid):
    if msg == '' or msg == ' ':
        send('嘿！这里是菜单\n'
             '[00] help\n'
             '语法：@机器人 help [指令]\n'
             '即可查看相关文档\n'
             '[01] 咕咕咕\n'
             '请说：咕咕咕（当然可以是任何数量个咕）\n'
             '[02] 黑名单\n'
             '注意：此程序对空格尤为敏感\n'
             '注意：您必须有机器人管理员权限才能执行此功能\n'
             '语法1：@机器人【空格】黑名单【空格】@...（直接@）\n'
             '语法2：@机器人【空格】黑名单【空格】...（QQ号）\n'
             '[03] 加群自动同意\n'
             '（部分群可用）\n'
             '[04] 特定关键词复读\n'
             '（无需@，一条消息必须只包含关键词）\n'
             '支持的关键词（“ | ”分割）：\n'
             'e | 额 | 呃 | 。 | w | www | 114514 | 1145141919810 | [CQ:face,id=298] '
             '| [CQ:face,id=277] | [CQ:face,id=178]\n'
             '[05] 聊天\n'
             '（必须@，@尽量置前，不要加回复，尽量不要加表情，直接说内容）\n'
             '使用小i机器人API\n'
             '[06] 祖安戳一戳 / 祖安我 / 祖安@...\n'
             '当你戳一戳机器人或at机器人说“祖安我”、“祖安屑”的时候机器人会对你/另一个人会说一句祖安话\n'
             '[07] 申请管理员\n'
             '注：是机器人管理员，不是群管理员\n'
             '语法：@机器人 申请管理员\n'
             '[08] 百度\n'
             '让我帮你百度一下 :)\n'
             '百度对您来讲就这么难吗？？？\n'
             '语法：@机器人【空格】百度【空格】...（要搜的东西）\n'
             '把最后机器人发出来的网址发给你爱提问的朋友 :)\n'
             '[09] 哔哩哔哩\n'
             '让我帮你哔哩哔哩一下 :)\n'
             '[10] 改名监测\n'
             '（部分群可用）'
             '========\n'
             'https://github.com/daizihan233/HanBot 这是这个机器人的代码，欢迎Star！\n'
             '========\n'
             '总有人问：“GitHub上不去怎么办？”\n'
             '请下载：https://gitee.com/docmirror/dev-sidecar\n'
             '注意：请仔细阅读文档，否则可能会出现意想不到的问题\n'
             '其它问题请联系作者QQ：183713750\n'
             '========\n'
             '公告：https://shimo.im/docs/KqHXw8XrrwpXqGY9/'
             , gid, uid)
    else:
        if msg == '申请管理员':
            send('183713750 <<< 加他！\n'
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
                 '''\nCN-xzf：https://xzfyyds.lanzoui.com/
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
        #  (uid == 2396349635 and gid == 336578274) 表示 如果 2396349635（QQ号） 在 336578274（QQ群） 里发了一条消息
        elif "祖安我" in msg or "祖安屑" in msg or (uid == 2396349635 and gid == 336578274):
            if uid == 2396349635 and gid == 336578274:  # 见上面那条注释
                # 从这个 API 获取一个祖安话，然后 @他 并发出去
                send(requests.get('https://fun.886.be/api.php?level=max').text, gid, uid)
            else:  # 如果是其他人
                # 从这个 API 获取一个祖安话，然后发出去
                send(requests.get('https://fun.886.be/api.php?level=max').text, gid)
        elif ("黑名单" in msg) and ("[CQ:at,qq=" in msg):
            if str(uid) + '\n' in open('admin.txt', 'r', encoding='UTF-8').readlines():
                if len(str(msg).split(' ')) != 2:
                    send('error: 语法错误！应该至少有2个空格', gid, uid)
                else:
                    tmp = str(msg).split(' ')
                    try:
                        tmp = tmp[-1][len('[CQ:at,qq='):-1]
                        tmp = int(tmp)
                        if tmp < 10000:
                            send('error: 参数错误！QQ号最小应该是10000', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == uid:
                            send('error: 参数错误！无法添加此人', gid, uid)
                        else:
                            f = str(str(msg).split(' ')[-1])[len('[CQ:at,qq='):-1]
                            fuck = open('fucklist', 'r').readlines()
                            for i in range(len(fuck)):
                                fuck[i] = fuck[i].strip('\n')

                            if f in fuck:
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '{} 已在黑名单'.format(f)))
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
                            send('error: 参数错误！QQ号最小应该是10000', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == uid:
                            send('error: 参数错误！无法添加此人', gid, uid)
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
                    send('error: 语法错误！应该至少有2个空格', gid, uid)
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
                a = [
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
