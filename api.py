import datetime
import json
import os
import random
import time
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
             '语法：@机器人 help [指令名称]\n'
             '即可查看相关文档\n'
             '所有在这个菜单中没有的都可以在此指令中找到\n'
             '[01] 咕咕咕\n'
             '[02] 黑名单\n'
             '[03] 加群自动同意\n'
             '[04] 特定关键词复读\n'
             '[05] 聊天\n'
             '[06] 祖安\n'
             '[07] 申请管理员\n'
             '[08] 百度\n'
             '[09] 哔哩哔哩\n'
             '[10] pi\n'
             '[11] 突发恶疾\n'
             '[12] bb\n'
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
            elif command == '突发恶疾':
                send('\n语法：@机器人 突发恶疾 人名\n'
                     '即可获得一条发病文案', gid, uid)
            elif command == 'pi':
                send('估算圆周率前6位，感谢 GitHub@123Windows31 提供的代码', gid, uid)
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
            elif command == '祖安':
                send('\n对机器人说“祖安我”、“祖安屑”就可以让机器人祖安你，想祖安其他人的话就对机器人说“祖安@...”\n'
                     '还有一种触发方式：在群内戳一戳机器人\n'
                     '注意：吸取主号的教训，祖安功能每分钟在所有群只能触发两次，否则不会鸟你', gid, uid)
            else:
                send('未查找到此指令的文档！', gid, uid)
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
        elif msg[:2] == '百度':
            msg = msg.split(' ')
            if len(msg) == 1:
                send('www.baiidu.com', uid, gid)
            else:
                msg.pop(0)
                url = 'https://baidu.physton.com/?q=' + parse.quote(' '.join(msg))
                send(url, gid, uid)
        elif msg[:4] == '哔哩哔哩':
            msg = msg.split(' ')
            if len(msg) <= 1:
                send('www.bilibili.com', uid, gid)
            else:
                msg.pop(0)
                url = 'https://www.bilitools.top/t/1/?k=' + parse.quote(''.join(msg))
                send(url, gid, uid)
        elif msg == 'pi':
            DARTS = 1000 * 1000
            hits = 0.0
            start = time.perf_counter()
            for i in range(1, DARTS + 1):
                x, y = random.random(), random.random()
                dist = pow(x ** 2 + y ** 2, 0.5)
                if dist <= 1.0:
                    hits = hits + 1
            pi = 4 * (hits / DARTS)
            print("圆周率值是:{}".format(pi))
            print("运行时间是:{:.5f}s".format(time.perf_counter() - start))
            send('\n'
                 '圆周率前6位估算：{}\n'
                 '本次估算共耗时：{:.5f}s'.format(pi, time.perf_counter() - start), gid, uid)
        elif "祖安我" in msg or "祖安屑" in msg or (uid == 2396349635 and gid == 336578274):
            c = int(open('zu_an_time.txt', 'r').read().split()[0])
            t = time.time() - float(open('zu_an_time.txt', 'r').read().split()[1])
            print(c, t)
            if c < 5:
                send(requests.get('https://fun.886.be/api.php?level=max').text, gid)
                open('zu_an_time.txt', 'w').write('{} {}'.format(c+1, time.time()))
            elif t >= 60*60:
                send(requests.get('https://fun.886.be/api.php?level=max').text, gid)
                open('zu_an_time.txt', 'w').write('{} {}'.format(0, time.time()))
        elif "祖安[CQ:at,qq=" in msg:
            c = int(open('zu_an_time.txt', 'r').read().split()[0])
            t = time.time() - float(open('zu_an_time.txt', 'r').read().split()[1])
            print(c, t)
            if c < 5:
                msg = msg.split()
                msg[0] = msg[0].strip('祖安')
                if '[CQ:at,qq=' in msg[0]:
                    send_114514(requests.get('https://fun.886.be/api.php?level=max').text, gid, msg[0])
                open('zu_an_time.txt', 'w').write('{} {}'.format(c + 1, time.time()))
            elif t >= 60*60:
                msg = msg.split()
                msg[0] = msg[0].strip('祖安')
                if '[CQ:at,qq=' in msg[0]:
                    send_114514(requests.get('https://fun.886.be/api.php?level=max').text, gid, msg[0])
                open('zu_an_time.txt', 'w').write('{} {}'.format(0, time.time()))
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
                                 '>>> 错误：QQ号最小为10000'
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
        elif msg[:4] == '突发恶疾':  # 突发恶疾生成器
            name = msg.split()
            print(name)
            name.pop(0)
            name = ' '.join(name)  # 获取人名
            print(name)
            lis = [  # 模板
                # 取自 @IS-4/114514 的消息
                f'{name}？{name}……{name}！{name}你带我走吧{name}😭你带我走吧😭{name}你带我走吧等等……{name}……{name}？{name}嘿嘿嘿……🤤🤤我的'
                f'{name}🤤{name}嘿嘿嘿……我的{name}🤤🤤，{name}……嘿嘿嘿……我的{name}🤤等等……{name}？{name}！不对，我不曾拥有{name}……{name}你'
                f'带我走吧{name}😭你带我走吧{name}😭你带我走吧😭等等……{name}？{name}……🤤🤤嘿嘿嘿嘿我的{name}🤤{name}是我的，你们不许看😭我鲨了你！',
                # 取自 Bilibili@闹闹 的动态（643333801201631252）
                f'我好喜欢{name}呀🥰🥰🥰{name}来PUA我吧🤤呜呜呜😭😭😭不是{name}的错，是我自愿的😭😭😭',
                # 取自 Bilibili@闹闹 的动态（643333801201631252）下用户 UID298283272 的评论
                f'我好喜欢{name}呀🥰🥰🥰{name}来rua我吧🤤呜呜呜😭😭😭不是{name}的错，是我自愿的😭😭😭',
                # 取自 @IS-4/114514 的消息
                f'{name}……我的{name}……🤤',
                # 取自 @IS-4/114514 的消息
                f'嘿嘿……{name}🤤',
                # 取自 某个群 的投稿
                f'嘿嘿我的{name}，我的西幻风格魔法学徒{name}，这小短袜这手套这炫彩大尾巴我现在就想把他摁在草丛里薅光他的毛嘿嘿嘿嘿嘿嘿嘿嘿嘿嘿'
                f'嘿嘿嘿嘿嘿🥵🥵🥵🥵🥵🥵🥵🥵🥵',

                f'请您枪毙我吧🤤请您枪毙我吧请您枪毙我吧🤤…请您亲手毙了我吧🤤嘿嘿我的{name}嘿嘿我的{name}你带我去杀侯淑林吧{name}请您亲手肃反'
                f'我吧🤤{name}，等等，这是我的{name}你不许看这是我的{name}你不许看这是我的{name}你不许看这是我的{name}你不许看这是我的'
                f'{name}你不许看这是我的{name}你不许看这是我的{name}你不许看等等我从来没拥有过{name}我的{name}🤤{name}我的{name}🤤{name}'
                f'我的{name}🤤{name}我的{name}🤤{name}我的{name}🤤{name}我的{name}🤤{name}我的{name}🤤{name}我的{name}🤤{name}我的{name}',

                f'嘿嘿嘿🤤真想把{name}的勋章和军服全脱了🤤把{name}绑在一边让{name}一边哭一边被我雷普🤤再把{name}的6b47头盔和6b45-1m防弹'
                f'衣扔到一边🤤然后在{name}面前把{name}最讨厌的聚合物弹夹塞进{name}们下面和{name}最爱的ak-12里面🤤 '
                
                f'好像要♡好像要{name}的大几把啊♡'
                
                f'{name}{random.choice(["哥哥", "姐姐"])}，给我吃你的几把吧♡'
            ]
            send(random.choice(lis), gid)  # 随机选择模板并发送
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
