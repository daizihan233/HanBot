import random

import requests
from flask import Flask, request
import aiohttp
import asyncio
import api

app = Flask(__name__)


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
            "Flag": 2,
            "Mode": "3class"
        }
        req.from_json_string(json.dumps(params))

        resp = client.SentimentAnalysis(req)
        return json.loads(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


@app.route('/', methods=["POST", 'WebSocket'])
def post_data():
    blacklist = [
        2854196310,
        3578255926
    ]
    if request.get_json().get('message_type') == 'group' and not (
            request.get_json().get('sender').get('user_id') in blacklist):  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        print(message)
        if '[CQ:at,qq=748029973] ' in message:
            message = str(message)[len('[CQ:at,qq=748029973] '):]
            print(message)
            api.keyword(message, uid, gid)  # 将 Q号和原始信息传到我们的后台
        elif '[CQ:at,qq=748029973]' in message:
            message = str(message)[len('[CQ:at,qq=748029973]'):]
            print(message)
            api.keyword(message, uid, gid)  # 将 Q号和原始信息传到我们的后台
        else:
            if '咕' in message:
                api.keyword(message, uid, gid)
            elif "e" == message or "额" == message or "呃" == message or "。" == message or "w" == message or \
                    "www" == message or message == "114514" or message == "1145141919810" or \
                    message == '[CQ:face,id=298]' or message == '[CQ:face,id=178]' or message == '[CQ:face,id=277]' or \
                    message == '？' or message == '?' or message == '草':
                api.keyword(message, uid, gid)
            elif '吃了:)' == message or '没吃:(' == message:
                api.keyword(message, uid, gid)
            elif ("病毒库" == message or "群文件" == message) and gid == 764869658:
                api.keyword(message, uid, gid)
            elif uid == 2396349635 and gid == 336578274:
                api.keyword(message, uid, gid)
    elif request.get_json().get('request_type') == 'group':
        gid = request.get_json().get('group_id')
        comment = str(request.get_json().get('comment')) \
                      .split('\n')[1][3:] \
            .upper()
        t = request.get_json().get('sub_type')
        flag = request.get_json().get('flag')
        uid = request.get_json().get('user_id')
        print(gid, comment, t, flag, uid, flush=True)
        if gid == 907112053 and t == 'add':
            print('发现 907112053 的加群请求！')
            if comment == 'MEMZ123' or comment == '1511907771' or comment == 'UID1511907771' or \
                    comment == 'WINDOWSSETUP2010':
                fuck = open('fucklist', 'r').readlines()
                for i in range(len(fuck)):
                    fuck[i] = fuck[i].strip('\n')
                if str(uid) in fuck:
                    requests.get('http://127.0.0.1:5700/send_group_msg?'
                                 'group_id={0}&'
                                 'message='
                                 '{1}'.format(gid, '各位管理员请注意！！！\n'
                                                   '[Robot][Event] 加群事件\n'
                                                   'QQ号：{0}\n'
                                                   '答案：{1}\n'
                                                   '机器人一次审核通过，但此人在黑名单内\n'
                                                   '请管理员尽快进行二次审核！'.format(uid, comment)))
                else:
                    re = requests.get('http://127.0.0.1:5700/set_group_add_request?'
                                      'flag={0}&'
                                      'sub_type={1}&'
                                      'approve=true'.format(flag, t))
                    requests.get('http://127.0.0.1:5700/send_group_msg?'
                                 'group_id={0}&'
                                 'message='
                                 '{1}'.format(gid, '[Robot][Event] 加群事件\n'
                                                   'QQ号：{0}\n'
                                                   '答案：{1}\n'
                                                   '机器人一次审核通过！'.format(uid, comment)))
            else:
                requests.get('http://127.0.0.1:5700/send_group_msg?'
                             'group_id={0}&'
                             'message='
                             '{1}'.format(gid, '各位管理员请注意！！！\n'
                                               '[Robot][Event] 加群事件\n'
                                               'QQ号：{0}\n'
                                               '答案：{1}\n'
                                               '机器人一次审核未通过\n'
                                               '请管理员尽快进行二次审核！'.format(uid, comment)))
        elif gid == 833645046 and t == 'add':
            print('发现 833645046 的加群请求！')
            if comment == '三星':
                fuck = open('fucklist', 'r').readlines()
                for i in range(len(fuck)):
                    fuck[i] = fuck[i].strip('\n')
                if str(uid) in fuck:
                    requests.get('http://127.0.0.1:5700/send_group_msg?'
                                 'group_id={0}&'
                                 'message='
                                 '{1}'.format(gid, '各位管理员请注意！！！\n'
                                                   '[Robot][Event] 加群事件\n'
                                                   'QQ号：{0}\n'
                                                   '答案：{1}\n'
                                                   '机器人一次审核通过，但此人在黑名单内\n'
                                                   '请管理员尽快进行二次审核！'.format(uid, comment)))
                else:
                    re = requests.get('http://127.0.0.1:5700/set_group_add_request?'
                                      'flag={0}&'
                                      'sub_type={1}&'
                                      'approve=true'.format(flag, t))
                    requests.get('http://127.0.0.1:5700/send_group_msg?'
                                 'group_id={0}&'
                                 'message='
                                 '{1}'.format(gid, '[Robot][Event] 加群事件\n'
                                                   'QQ号：{0}\n'
                                                   '答案：{1}\n'
                                                   '机器人一次审核通过！'.format(uid, comment)))
            else:
                requests.get('http://127.0.0.1:5700/send_group_msg?'
                             'group_id={0}&'
                             'message='
                             '{1}'.format(gid, '各位管理员请注意！！！\n'
                                               '[Robot][Event] 加群事件\n'
                                               'QQ号：{0}\n'
                                               '答案：{1}\n'
                                               '机器人一次审核未通过\n'
                                               '请管理员尽快进行二次审核！'.format(uid, comment)))
        # elif gid == 623377914 and t == 'add':
        #     print('发现 623377914 的加群请求！')
        #     if comment == 'UID589370259' or comment == '589370259':
        #         fuck = open('fucklist', 'r').readlines()
        #         for i in range(len(fuck)):
        #             fuck[i] = fuck[i].strip('\n')
        #         if str(uid) in fuck:
        #             requests.get('http://127.0.0.1:5700/send_group_msg?'
        #                          'group_id={0}&'
        #                          'message='
        #                          '{1}'.format(gid, '各位管理员请注意！！！\n'
        #                                            '[Robot][Event] 加群事件\n'
        #                                            'QQ号：{0}\n'
        #                                            '答案：{1}\n'
        #                                            '机器人一次审核通过，但此人在黑名单内\n'
        #                                            '请管理员尽快进行二次审核！'.format(uid, comment)))
        #         else:
        #             re = requests.get('http://127.0.0.1:5700/set_group_add_request?'
        #                               'flag={0}&'
        #                               'sub_type={1}&'
        #                               'approve=true'.format(flag, t))
        #             with open('233.log', 'w') as f:
        #                 f.write(str(re.text))
        #             requests.get('http://127.0.0.1:5700/send_group_msg?'
        #                          'group_id={0}&'
        #                          'message='一次审核通过！'.format(uid, comment)))
        #     else:
        #         requests.get('http://127.0.0.1:57
        #         #                          '{1}'.format(gid, '[Robot][Event] 加群事件\n'
        #         #                                            'QQ号：{0}\n'
        #         #                                            '答案：{1}\n'
        #         #                                            '机器人00/send_group_msg?'
        #                      'group_id={0}&'
        #                      'message='
        #                      '{1}'.format(gid, '各位管理员请注意！！！\n'
        #                                        '[Robot][Event] 加群事件\n'
        #                                        'QQ号：{0}\n'
        #                                        '答案：{1}\n'
        #                                        '机器人一次审核未通过\n'
        #                                        '请管理员尽快进行二次审核！'.format(uid, comment)))
        else:
            print(gid, t, flush=True)
    elif request.get_json().get('target_id') == 748029973:  # 如果机器人被戳
        herbalist = [  # 祖安语录
            '[CQ:image,file=file:///C:/FromHanTools/liaotian/img/jb.jpg]',
            '你刚出生就被你父母抛弃不得不去乞讨结果乞讨到了一盆屎然后尼玛你爹被杀你又被人贩子带去解剖这就是你的傻逼一生',
            '你就是歌姬吧',
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
            'nmd再戳我一下试试！',
            '滚',
            '哎wcnmlgbd鬼！',
            'fuck you',
            '哎我cnmd谁tmd叫你m的让你sb戳我的？！！！',
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
            '我屮艸芔茻你妈的',
            'G他N的,一大逼抖子呼死你',
            requests.get('https://fun.886.be/api.php?level=max').text
        ]
        random.shuffle(herbalist)
        send(random.choice(herbalist), request.get_json().get('group_id'))
    elif request.get_json().get('notice_type') == 'group_increase':
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('user_id')
        if gid == 764869658:
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
            if gid == 535979960:
                l = [
                    '欢迎 :)',
                    ':)',
                    'ohhhhhhhhhhhhhhh，有新人欸',
                    'Hi~',
                    '你好！',
                    '你好啊！别潜水哦~',
                    'hi，这里是setup的小群，一些奇奇怪怪反正别问的问题，不要把群号告诉任何人，谢谢啦~'
                ]
                send(msg=random.choice(l),
                     gid=gid,
                     uid=uid)
    # 如果监测到改名，且不是留空
    elif request.get_json().get('notice_type') == 'group_card' and request.get_json().get('card_new') != '':
        ret = tencent_api(request.get_json().get('card_new'))  # 将改的名字发送至腾讯云进行情感分析
        print(ret)
        if ret['Sentiment'] == 'positive':  # 如果是正面情绪
            s = '正面 - positive'
        elif ret['Sentiment'] == 'negative':  # 如果是负面情绪
            s = '负面 - negative'
        else:  # 如果是中性
            s = '中性 - neutral'
        #  发送一条消息到我自己的后台
        requests.get('http://127.0.0.1:5700/send_private_msg?user_id=183713750&message='
                     '【改名监测（Beta%2B）】\n'  # %2B == "+"
                     '[群号]: {}\n'
                     '[Ｑ号]: {}\n'
                     '[新的]: {}\n'
                     '[旧的]: {}\n'
                     '[状态]: {}\n'
                     '[正面]: {}\n'
                     '[中性]: {}\n'
                     '[负面]: {}\n'.format(request.get_json().get('group_id'), request.get_json().get('user_id'),
                                         request.get_json().get('card_new'), request.get_json().get('card_old'),
                                         s, ret['Positive'], ret['Neutral'], ret['Negative']))
        # 如果是 907112053（群号） 发生了此事件
        if request.get_json().get('group_id') == 907112053:
            if s == '负面 - negative':  # 且为负面情绪
                # 则把昵称改回来
                asyncio.run(set_group_card(request.get_json().get('card_old'),
                                           907112053,
                                           request.get_json().get('user_id')))
                # 并发送一条消息到这个群
                send('【改名监测（Beta+）】\n'
                     '[群号]: {}\n'
                     '[Ｑ号]: {}\n'
                     '[新的]: {}\n'
                     '[旧的]: {}\n'
                     '[状态]: {}\n'
                     '[正面]: {}\n'
                     '[中性]: {}\n'
                     '[负面]: {}\n'.format(request.get_json().get('group_id'), request.get_json().get('user_id'),
                                         request.get_json().get('card_new'), request.get_json().get('card_old'),
                                         s, ret['Positive'], ret['Neutral'], ret['Negative'])
                     , 907112053)
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)  # 此处的 host和 port对应上面 yml文件的设置
