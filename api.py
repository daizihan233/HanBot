import os
import random
import aiohttp
import asyncio


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


def keyword(msg, uid, gid):
    import requests
    import json
    if msg == '' or msg == ' ':
        send('嘿！这里是菜单\n'
             '[1] 咕咕咕\n'
             '请说：咕咕咕（当然可以是任何数量个咕）\n'
             '[2] 黑名单\n'
             '注意：此程序对空格尤为敏感\n'
             '注意：您必须有机器人管理员权限才能执行此功能，否则机器人不会理你\n'
             '语法1：@机器人【空格】黑名单【空格】@...（直接@）\n'
             '语法2：@机器人【空格】黑名单【空格】...（QQ号）\n'
             '[3] 加群自动同意\n'
             '（部分群可用，无需@，自动检测）\n'
             '[4] 特定关键词复读\n'
             '（无需@，一条消息必须只包含关键词）\n'
             '支持的关键词（“ | ”分割）：\n'
             'e | 额 | 呃 | 。 | w | www | 114514 | 1145141919810 | [CQ:face,id=298] '
             '| [CQ:face,id=277] | [CQ:face,id=178]\n'
             '[5] 聊天\n'
             '（必须@，@尽量置前，不要加回复，尽量不要加表情，直接说内容）\n'
             '使用青云客机器人API\n'
             '[6] 祖安戳一戳 / 祖安我\n'
             '当你戳一戳机器人或at机器人说“祖安我”的时候他会说一句祖安话\n'
             '[7] 申请管理员\n'
             '注：是机器人管理员，不是群管理员'
             '语法：@机器人 申请管理员'
             '========\n'
             'https://github.com/daizihan233/HanBot 这是这个机器人的代码，欢迎Star！',
             gid, uid)
    else:
        if msg == '申请管理员':
            requests.get('http://127.0.0.1:5700/send_private_msg?user_id=183713750&message='
                         '【机器人管理员申请】\n'
                         '[GID]: {}\n'
                         '[UID]: {}'.format(gid, uid))
            send('申请成功！ヾ(≧▽≦*)o请不要短时间内重复申请哦！开发能在后台看见哒~重复申请的话不会更快处理！！！（超大声）', gid, uid)
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
https://share.weiyun.com/VglthxSV
    工具支持：腾讯微云''',
                 gid=gid, uid=uid)
        elif "祖安我" in msg:
            herbalist = [  # 祖安语录
                '你妈死了',
                '爪巴',
                '傻逼一个',
                '114514',
                '1919810',
                '1145141919810',
                '1919810114514',
                '1145141919810HOM',
                '和你聊天真开心,送你一朵玫瑰花',
                '先辈送福,新年快乐',
                'nmd再@我一下试试！',
                '滚',
                '哎wcnmlgbd鬼！',
                'fuck you',
                '哎我cnmd谁tmd叫你m的让你个sb@我的？！！！',
                'gun，傻逼',
                '你礼貌吗？',
                '脑残',
                '操你妈',
                '艹',
                '我日你先人',
                '我他娘的谢谢你啊',
                '我********************',
                '你是来吃屎的吧',
                '一路走好，SB',
                '你是啥玩意',
                '你妈补天',
                'TMD',
                'CAO',
                '大雨治水',
                '你没妈',
                '你没妈',
                '马牛逼刚吃屎，你个马怂逼',
                'SB',
                '你死的好惨啊',
                '孝出强大',
                '宁真是个大孝子啊',
                '你好骚啊',
                '骚年，你爷爷在这',
                '试试就逝世',
                '全场目光向我看齐，我宣布一件事：你是傻逼',
                '傻逼一号SB的你准备趋势',
                '我操你妈',
                '我不是人，但你绝对是狗',
                '人家走到女生面前是夸好帅，而你走过去，会被骂变态',
                '你好甩啊',  # 甩在南京话里指250
                '去你妈',
                '学校是我家，文明去你妈',
                '学校是我家，文明靠大家',
                '250',
                '我屮艸芔茻你妈的'
            ]
            send(random.choice(herbalist), gid)
        elif ("黑名单" in msg) and ("[CQ:at,qq=" in msg) and ((str(uid) + '\n') in
                                                           open('admin.txt', 'r', encoding='UTF-8').readlines()):
            if len(str(msg).split(' ')) != 2:
                send('error: 语法错误！应该至少有2个空格', gid, uid)
            else:
                tmp = str(msg).split(' ')
                try:
                    tmp = tmp[-1][len('[CQ:at,qq='):-1]
                    tmp = int(tmp)
                    if tmp < 10000:
                        send('error: 参数错误！QQ号最小应该是10000', gid, uid)
                    else:
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
                except:
                    send('error: 类型错误！QQ应该是int类型，但程序无法将其转为int', gid, uid)


        elif "黑名单" in msg and ((str(uid) + '\n') in open('admin.txt', 'r', encoding='UTF-8').readlines()):
            if len(str(msg).split(' ')) != 2:
                send('error: 语法错误！应该至少有2个空格', gid, uid)
            else:
                tmp = str(msg).split(' ')
                try:
                    tmp = tmp[-1]
                    tmp = int(tmp)
                    if tmp < 10000:
                        send('error: 参数错误！QQ号最小应该是10000', gid, uid)
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
                open('gugu{}.txt'.format(gid), 'w').close()
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
