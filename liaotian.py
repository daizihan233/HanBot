import random

import requests
from flask import Flask, request

import api

app = Flask(__name__)


def test(send_text):
    return True


@app.route('/', methods=["POST"])
def post_data():
    if request.get_json().get('message_type') == 'group':  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        print(message)
        if '[CQ:at,qq=748029973] ' in message:
            message = str(message)[len('[CQ:at,qq=748029973] '):]
            print(message)
            if test(message):
                api.keyword(message, uid, gid)  # 将 Q号和原始信息传到我们的后台
        elif '[CQ:at,qq=748029973]' in message:
            message = str(message)[len('[CQ:at,qq=748029973]'):]
            print(message)
            if test(message):
                api.keyword(message, uid, gid)  # 将 Q号和原始信息传到我们的后台
        else:
            if '咕' in message:
                api.keyword(message, uid, gid)
            elif "e" == message or "额" == message or "呃" == message or "。" == message or "w" == message or \
                    "www" == message or message == "114514" or message == "1145141919810" or \
                    message == '[CQ:face,id=298]' or message == '[CQ:face,id=178]' or message == '[CQ:face,id=277]' or\
                message == '？' or message == '?' or message == '草':
                api.keyword(message, uid, gid)
    elif request.get_json().get('request_type') == 'group':
        gid = request.get_json().get('group_id')
        comment = str(request.get_json().get('comment')) \
            .strip('问题：群主的B站UID/抖音号是？ 答案：') \
            .strip('问题：群主的B站UID/抖音号是？\n答案：') \
            .strip('问题：群主的B站UID/抖音号是？')\
            .strip('\n答案：')\
            .strip('答案：')\
            .strip('\n')\
            .upper()
        t = request.get_json().get('sub_type')
        flag = request.get_json().get('flag')
        uid = request.get_json().get('user_id')
        print(gid, comment, t, flag, uid, flush=True)
        with open('233.log', 'w') as f:
            f.write(str(requests))
        if gid == 907112053 and t == 'add':
            print('发现 907112053 的加群请求！')
            if comment == 'MEMZ123' or comment == '1511907771' or comment == 'UID1511907771':
                fuck = open('fucklist', 'r').readlines()
                for i in range(len(fuck)):
                    fuck[i] = fuck[i].strip('\n')
                if str(uid) in fuck:
                    re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                                      'group_id={0}&'
                                      'message='
                                      '{1}'.format(gid, '各位管理员请注意！！！\n'
                                                        '[Robot][Event] 加群事件\n'
                                                        'UID：{0}\n'
                                                        'Comment：{1}\n'
                                                        '机器人一次审核通过，但此人在黑名单内\n'
                                                        '请管理员尽快进行二次审核！'.format(uid, comment)))
                else:
                    re = requests.get('http://127.0.0.1:5700/set_group_add_request?'
                                      'flag={0}&'
                                      'sub_type={1}&'
                                      'approve=true'.format(flag, t))
                    with open('233.log', 'w') as f:
                        f.write(str(re.text))
                    re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                                      'group_id={0}&'
                                      'message='
                                      '{1}'.format(gid, '[Robot][Event] 加群事件\n'
                                                        'UID：{0}\n'
                                                        'Comment：{1}\n'
                                                        '机器人一次审核通过！'.format(uid, comment)))
            else:
                re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                                  'group_id={0}&'
                                  'message='
                                  '{1}'.format(gid, '各位管理员请注意！！！\n'
                                                    '[Robot][Event] 加群事件\n'
                                                    'UID：{0}\n'
                                                    'Comment：{1}\n'
                                                    '机器人一次审核未通过\n'
                                                    '请管理员尽快进行二次审核！'.format(uid, comment)))
        else:
            print(gid, t, flush=True)
    elif request.get_json().get('target_id') == 748029973:  # 如果机器人被戳
        herbalist = [             # 祖安语录
            'nmd再戳我一下试试！',
            '滚',
            '哎wcnmlgbd鬼！',
            'fuck you',
            '哎我cnmd谁tmd叫你m的让你sb戳我的？！！！',
            # 从这一行开始，均为 苏孝泽 提供
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
            '伞兵',
            '伞兵一号SB的你准备趋势',
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
        re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                          'group_id={0}&'
                          'message='
                          '{1}'.format(request.get_json().get('group_id'),  # （群号）发送到对应的群里
                                       random.choice(herbalist)))           # （消息内容）在祖安语录里随机选一条
    # 这里是正在开发的代码，碰这里的代码的人死马（除了开发）
    elif request.get_json().get('notice_type') == 'group_decrease':
        sub_type = request.get_json().get('sub_type')
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('user_id')
        opid = request.get_json().get('operator_id')
        if sub_type == 'leave':
            sub_type = '主动退群'
        elif sub_type == 'kick':
            sub_type = '被操作者踢出'
        elif sub_type == 'kick_me':
            sub_type = '机器人账号被踢'
        re = requests.get('http://127.0.0.1:5700/send_private_msg?'
                          'user_id={0}&'
                          'message='
                          '{1}'.format(183713750, '[Robot][Log-WARN] 群成员减少\n'
                                                  '[类　型]: {0}\n'
                                                  '[群　号]: {1}\n'
                                                  '[操作者]: {2}\n'
                                                  '[用　户]: {3}'
                                       .format(sub_type,
                                               gid,
                                               opid,
                                               uid)))
    elif request.get_json().get('notice_type') == 'group_increase':
        sub_type = request.get_json().get('sub_type')
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('user_id')
        opid = request.get_json().get('operator_id')
        if sub_type == 'approve':
            sub_type = '管理员同意入群'
        elif sub_type == 'invite':
            sub_type = '管理员邀请入群'
        re = requests.get('http://127.0.0.1:5700/send_private_msg?'
                          'user_id={0}&'
                          'message='
                          '{1}'.format(183713750, '[Robot][Log-WARN] 群成员增加\n'
                                                  '[类　型]: {0}\n'
                                                  '[群　号]: {1}\n'
                                                  '[操作者]: {2}\n'
                                                  '[用　户]: {3}'
                                       .format(sub_type,
                                               gid,
                                               opid,
                                               uid)))
    elif request.get_json().get('notice_type') == 'group_ban':
        sub_type = request.get_json().get('sub_type')
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('user_id')
        opid = request.get_json().get('operator_id')
        if sub_type == 'ban':
            sub_type = '进行禁言'
        elif sub_type == 'lift_ban':
            sub_type = '解除禁言'
        re = requests.get('http://127.0.0.1:5700/send_private_msg?'
                          'user_id={0}&'
                          'message='
                          '{1}'.format(183713750, '[Robot][Log-WARN] 禁言\n'
                                                  '[类　型]: {0}\n'
                                                  '[群　号]: {1}\n'
                                                  '[操作者]: {2}\n'
                                                  '[用　户]: {3}'
                                       .format(sub_type,
                                               gid,
                                               opid,
                                               uid)))
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)  # 此处的 host和 port对应上面 yml文件的设置
