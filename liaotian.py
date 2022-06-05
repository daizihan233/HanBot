import random
import time

import setproctitle
from flask import Flask, request

import api
from func import *
from var import *

app = Flask(__name__)


@app.route('/', methods=["POST"])
def post_data():
    blacklist = [  # 不处理这些人的消息
        2854196310,  # Q群管家
        3578255926,  # 机器人
        2293800985,  # 机器人
        2396349635,  # 屑
        2609948707,  # 屑
        3561922003,  # 屑+机器人
        1950770034,  # 机器人
        2749234809,  # 机器人
        3547783949,  # 机器人
        80000000,  # 匿名消息
    ]
    if request.get_json().get('message_type') == 'group' and not (
            request.get_json().get('sender').get('user_id') in blacklist):  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        msg_id = request.get_json().get('message_id')  # 获取消息id
        print(message)
        if str(message)[:len('[CQ:at,qq=748029973] ')] == '[CQ:at,qq=748029973] ' and gid != 532094038:
            message = str(message)[len('[CQ:at,qq=748029973] '):]
            message = message.lstrip(' ')
            print(message)
            api.keyword(message, uid, gid, msg_id)  # 将 Q号和原始信息传到我们的后台
        elif str(message)[:len('[CQ:at,qq=748029973]')] == '[CQ:at,qq=748029973]' and gid != 532094038:
            message = str(message)[len('[CQ:at,qq=748029973]'):]
            message = message.lstrip(' ')
            print(message)
            api.keyword(message, uid, gid, msg_id)  # 将 Q号和原始信息传到我们的后台

        else:
            if '咕' in message:
                api.keyword(message, uid, gid)
            elif message in repeat and gid != 936389498 and gid != 532094038:
                api.keyword(message, uid, gid)
            elif '吃了:)' == message or '没吃:(' == message and gid != 532094038:
                api.keyword(message, uid, gid)
            elif ("病毒库" == message or "群文件" == message) and gid == 764869658:
                api.keyword(message, uid, gid)
            elif re_match(re_die, message):
                api.keyword(message, uid, gid)
            elif message == '图' or message == '鸡汤' or message == 'muteme' or message.split(' ')[0] in [
                '来份面包',
                '给你面包',
                '面包库存'
            ] or message == '心理疏导':
                api.keyword(message, uid, gid)
    elif request.get_json().get('request_type') == 'group':
        gid = request.get_json().get('group_id')
        comment = str(request.get_json().get('comment')).split('\n')[1][3:]
        t = request.get_json().get('sub_type')
        flag = request.get_json().get('flag')
        uid = request.get_json().get('user_id')
        print(gid, comment, t, flag, uid, flush=True)
        if gid == 788328739 and t == 'add':
            add_group_automatic_consent(gid, uid, comment,
                                        ['WindowsSetup2010', '1511907771', 'UID1511907771',
                                         'UID:1511907771', 'MEMZ567'], flag, t)
        elif gid == 833645046 and t == 'add':
            add_group_automatic_consent(gid, uid, comment, ['三星'], flag, t)
        elif gid == 934645530 and t == 'add':
            add_group_automatic_consent(gid, uid, comment, ['123'], flag, t)
        elif gid == 1042872173 and t == 'add':
            add_group_automatic_consent(gid, uid, comment, ['2020417'], flag, t)
        else:
            print(gid, t, flush=True)
    elif (request.get_json().get('target_id') == 748029973 or request.get_json().get(
            'target_id') == 2265453790) and request.get_json().get('group_id') != 532094038:  # 如果机器人被戳
        tmp_file = open('zu_an_time.txt', 'r')
        zu_an_time = tmp_file.read().split(' ')
        c = int(zu_an_time[0])
        print(zu_an_time)
        t = time.time() - float(zu_an_time[1])
        tmp_file.close()
        print(c, t)
        tmp_file = open('zu_an_time.txt', 'w')
        if c < 5:
            random.shuffle(herbalist)
            send(random.choice(herbalist), request.get_json().get('group_id'))
            tmp_file.write('{} {}'.format(c + 1, time.time()))
        elif t >= 60 * 60:
            random.shuffle(herbalist)
            send(random.choice(herbalist), request.get_json().get('group_id'))
            tmp_file.write('{} {}'.format(0, time.time()))
        tmp_file.close()
    elif request.get_json().get('notice_type') == 'group_increase':
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('user_id')
        if gid == 764869658:
            send(msg='''\n中国青年计算机爱好者联盟 （CEA）群文件说明
China Young Computer Enthusiast Alliance Group File Description
--------------------------------------------------------
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
PS：密码均为 CEA
--------------------------------------------------------
CN-yxy：https://pan.bilnn.cn/s/
软件安装包（定期更新）：k3JLIw
群主自制の软件：peJyCE
单文件软件：l1JecM
清华大学计算机系网络课程：m4JWCx
各类激活工具（定期更新）：xDLkcA
CMD批处理：8Yw9ib
注：群主自制の软件每次下载2积分
      CMD批处理教程每次下载1积分
    （毕竟是劳动成果，支持一下嘻嘻）
工具支持：比邻云盘
--------------------------------------------------------
群共享文件
https://share.weiyun.com/XvQofEc0
文件分享上传：http://inbox.weiyun.com/UN5lAjrn
工具支持：腾讯微云''',
                 gid=gid, uid=uid)
        elif gid == 535979960:
            welcome = [
                '欢迎 :)',
                ':)',
                'ohhhhhhhhhhhhhhh，有新人欸',
                'Hi~',
                '你好！',
                '你好啊！别潜水哦~',
                'hi，这里是setup的小群，一些奇奇怪怪反正别问的问题，不要把群号告诉任何人，谢谢啦~'
            ]
            send(msg=random.choice(welcome),
                 gid=gid,
                 uid=uid)
        elif gid == 788328739:
            print('788328739群成员增加！')
            fuck_file = open('fucklist', 'r')
            fuck = fuck_file.readlines()
            fuck_file.close()
            admin_file = open('admin.txt', 'r', encoding='UTF-8')
            for i in range(len(fuck)):
                fuck[i] = fuck[i].strip('\n')
            if str(uid) in fuck:
                if not (str(request.get_json().get('operator_id')) in admin_file.read().split('\n')):
                    print('Fuck! 哪个傻逼让你进来的？')
                    send('cnmd，谁让你进来的？？？滚！你个死马玩意儿', gid, uid)
                    tick(gid, uid)
            admin_file.close()
        elif gid == 532094038:
            send('[CQ:image,file=file:///C:/FromHanTools/liaotian/img/jiki.jpg]', gid)
    # 如果监测到改名，且不是留空
    elif request.get_json().get('notice_type') == 'group_card' and request.get_json().get('card_new') != '':
        rs = '未知 - none'
        rule = '无'
        ok_file = open('ok_name.txt', 'r', encoding='UTF-8')
        for i in ok_file.read().split('\n'):
            if re.match(i, request.get_json().get('card_new')) is not None:
                rs = '正面 - positive'
                rule = f'白：{i}'
                break
        ok_file.close()
        no_file = open('noname.txt', 'r', encoding='UTF-8')
        for i in no_file.read().split('\n'):
            if re.match(i, request.get_json().get('card_new')) is not None:
                rs = '负面 - negative'
                rule = f'黑：{i}'
                break
        no_file.close()
        s = '未知 - none'
        ret = {
            'Positive': 0,
            'Neutral': 0,
            'Negative': 0
        }
        if rs == '未知 - none':
            ret = tencent_api(str(request.get_json().get('card_new')).lower())  # 将改的名字发送至腾讯云进行情感分析
            print(ret)
            if ret['Sentiment'] == 'positive':  # 如果是正面情绪
                s = '正面 - positive'
            elif ret['Sentiment'] == 'negative':  # 如果是负面情绪
                s = '负面 - negative'
            else:  # 如果是中性
                s = '中性 - neutral'
            rs = s
        #  发送一条消息到我自己的后台
        ssend(f'【改名监测（Beta+）】\n'
              f'[群号]: {request.get_json().get("group_id")}\n'
              f'[Ｑ号]: {request.get_json().get("user_id")}\n'
              f'[新的]: {request.get_json().get("card_new")}\n'
              f'[旧的]: {request.get_json().get("card_old")}\n'
              f'[规则]: {rule}\n'
              f'[初判]: {s}\n'
              f'[终判]: {rs}\n'
              f'[正面]: {ret["Positive"]}\n'
              f'[中性]: {ret["Neutral"]}\n'
              f'[负面]: {ret["Negative"]}', 183713750)
        if request.get_json().get('group_id') in [
            788328739,
            751210750,
            833645046,
            744591068,
            936389498,
            902202817,
            535979960
        ]:
            if rs == '负面 - negative':  # 为负面情绪
                # 则把昵称改回来
                asyncio.run(set_group_card(request.get_json().get('card_old'),
                                           request.get_json().get('group_id'),
                                           request.get_json().get('user_id')))
                # 并发送一条消息到这个群
                send(f'【改名监测（Beta+）】\n'
                     f'[群号]: {request.get_json().get("group_id")}\n'
                     f'[Ｑ号]: {request.get_json().get("user_id")}\n'
                     f'[新的]: {request.get_json().get("card_new")}\n'
                     f'[旧的]: {request.get_json().get("card_old")}\n'
                     f'[规则]: {rule}\n'
                     f'[初判]: {s}\n'
                     f'[终判]: {rs}\n'
                     f'[正面]: {ret["Positive"]}\n'
                     f'[中性]: {ret["Neutral"]}\n'
                     f'[负面]: {ret["Negative"]}',
                     request.get_json().get('group_id'))
    elif request.get_json().get('notice_type') == 'group_ban':
        if request.get_json().get('sub_type') == 'ban' and request.get_json().get('group_id') == 473185911:
            send('【禁言】\n'
                 '[操作者]: {}\n'
                 '[被禁言]: {}\n'
                 '[时　长]: {}秒'.format(request.get_json().get('operator_id'),
                                     request.get_json().get('user_id'),
                                     request.get_json().get('duration')),
                 request.get_json().get('group_id'))
    return 'OK'


if __name__ == '__main__':
    proc_title = "liaotian-bot / liaotian.py"
    setproctitle.setproctitle(proc_title)
    app.run(debug=True, host='127.0.0.1', port=8000, threaded=True)
