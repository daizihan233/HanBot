import gc
import random

import psutil
import setproctitle
from flask import Flask, request

import api
import func
import var
from richc import console

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_data():
    import time
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
        2425669802,  # 机器人
        2810482259,  # 机器人
        3563191526,  # 机器人
        3563191526,  # 寄器人
        3604629098,  # 寄器人
        2286003479,  # 机器人
        3594648576,  # 机器人
        3573523379,  # 机器人
        2142127814,  # 机器人
        80000000,  # 匿名消息
    ]
    # console.print(request.get_json())
    if request.get_json().get('message_type') == 'group' and request.get_json().get('sender').get(
            'user_id') not in blacklist:  # 如果是群聊信息
        gid = request.get_json().get('group_id')  # 获取群号
        uid = request.get_json().get('sender').get('user_id')  # 获取信息发送者的 QQ号码
        message = request.get_json().get('raw_message')  # 获取原始信息
        msg_id = request.get_json().get('message_id')  # 获取消息id
        console.print(message)
        if (not func.is_admin(uid)) or (func.is_debug()):
            if func.is_member(gid, uid):
                if gid == 780779026:
                    func.img_safe(message, msg_id, 'htb1', gid)
                elif gid in [
                    904362227,
                    971741566,
                    378235245
                ]:
                    func.img_safe(message, msg_id, 'yihuv1', gid)
        if uid in [
            # 3358907393
        ]:
            if func.is_member(gid, uid):
                func.del_msg(msg_id)
        elif str(gid) in func.safe_file_read('del_msg_grp').split('\n'):
            if func.is_member(gid, uid):
                with open('mgc.txt', 'r', encoding="UTF-8") as f:
                    fl = (f.read().split('\n'))
                    for t in fl:
                        if t in message:
                            func.del_msg(msg_id)
                            break
        robot_qq_id = [
            "[CQ:at,qq=748029973]",
            '[CQ:at,qq=2265453790]',

        ]
        flag = True
        # console.print(message[:3])
        for i in robot_qq_id:
            if str(message)[:len(i)] == i or str(message)[:len(i + ' ')] == i + ' ':
                flag = False
                message = str(message)[len('[CQ:at,qq=748029973] '):]
                message = message.lstrip(' ').rstrip(' ').replace('   ', ' ').replace('  ', ' ')
                console.print(message)
                api.keyword(message, uid, gid, msg_id)  # 将 Q号和原始信息传到我们的后台

        if (('咕' in message and gid not in [
            747458571
        ]) or (
                    message in var.repeat and gid not in [
                936389498,
                493253441,
                688340171,
                904362227,
                971741566,
                378235245
            ]) or (
                    ("病毒库" == message or "群文件" == message) and gid == 764869658) or (
                    func.re_match(var.re_die, message)) or (
                    message == '鸡汤' or message == 'muteme' or message.split(' ')[0] in [
                '来份面包',
                '给你面包',
                '面包库存'
            ] or message == '心理疏导') or (gid == 747458571 and message in [
            '查询哈奶啤含金量',
            '查询哈奶啤粉丝数',
            '鸡典正统是？',
            '主页',
        ]) or (message[:3] == '主页-')) and flag:
            api.keyword(message, uid, gid, msg_id)
    elif request.get_json().get('request_type') == 'group':
        t = request.get_json().get('sub_type')
        # 因群解散现注释此代码以备份
        # if gid == 788328739 and t == 'add':
        #     add_group_automatic_consent(gid, uid, comment,
        #                                 ['WindowsSetup2010', '1511907771', 'UID1511907771',
        #                                  'UID:1511907771', 'MEMZ567'], flag, t)
        if t == 'invite':
            func.quick_operation(request.get_json(), {
                "approve": True
            })
        else:
            gid = request.get_json().get('group_id')
            comment = str(request.get_json().get('comment')).split('\n')[1][3:]
            flag = request.get_json().get('flag')
            uid = request.get_json().get('user_id')
            console.print(gid, comment, t, flag, uid, flush=True)
            if gid == 833645046 and t == 'add':
                func.add_group_automatic_consent(gid, uid, comment, ['三星'], flag, t)
            elif gid == 934645530 and t == 'add':
                func.add_group_automatic_consent(gid, uid, comment, ['123'], flag, t)
            elif gid == 1042872173 and t == 'add':
                func.add_group_automatic_consent(gid, uid, comment, ['2020417'], flag, t)
            elif gid == 744591068 and t == 'add':
                lel = func.get_lock_level()
                if lel == 1:
                    func.add_grouper(flag, t, False)
                    func.send(f'因入群通道封锁，该入群请求被拒绝。\n'
                              f'用户：{uid}\n'
                              f'Flag：{flag}\n'
                              f'信息：{comment}\n'
                              f'\n'
                              f'{func.get_lock_detailed(lel)}', gid)
                else:
                    func.send(f'发现加群请求\n'
                              f'用户：{uid}\n'
                              f'Flag：{flag}\n'
                              f'信息：{comment}', gid)
            else:
                console.print(gid, t, flush=True)
    elif (request.get_json().get('target_id') == 748029973 or request.get_json().get(
            'target_id') == 2265453790) and (
            str(request.get_json().get('group_id')) not in func.safe_file_read('no_gan.txt').split('\n')):  # 如果机器人被戳
        tmp_file = open('zu_an_time.txt', 'r', encoding='UTF-8')
        zu_an_time = tmp_file.read().split(' ')
        c = int(zu_an_time[0])
        console.print(zu_an_time)
        t = time.time() - float(zu_an_time[1])
        tmp_file.close()
        console.print(c, t)
        if c < 5:
            tmp_file = open('zu_an_time.txt', 'w', encoding='UTF-8')
            random.shuffle(var.herbalist)
            func.send(random.choice(var.herbalist), request.get_json().get('group_id'))
            tmp_file.write('{} {}'.format(c + 1, time.time()))
        elif t >= 60 * 60:
            tmp_file = open('zu_an_time.txt', 'w', encoding='UTF-8')
            random.shuffle(var.herbalist)
            func.send(random.choice(var.herbalist), request.get_json().get('group_id'))
            tmp_file.write('{} {}'.format(0, time.time()))
        tmp_file.close()
    elif request.get_json().get('notice_type') == 'group_recall':
        gid = request.get_json().get("group_id")
        if str(gid) in open('delmsgstat', 'r', encoding='UTF-8').read().split('\n'):
            op_id = request.get_json().get("operator_id")
            op_name = func.send_ws(
                "get_group_member_info",
                {
                    "group_id": gid,
                    "user_id": op_id,
                    "no_cache": True
                }
            )
            op_name = op_name["data"]["nickname"] if op_name["data"]["card"] == '' else op_name["data"]["card"]
            g_name = func.send_ws(
                "get_group_info",
                {
                    "group_id": gid,
                    "no_cache": True
                }
            )["data"]["group_name"]
            msg = func.send_ws(
                "get_msg", {
                    "message_id": request.get_json().get("message_id")
                })
            uid = request.get_json().get("user_id")
            u_name = msg["data"]["sender"]["nickname"]
            # if uid != 748029973 and op_id != 748029973:
            st = f'发生时间：{func.datetime.datetime.fromtimestamp(request.get_json().get("time")).strftime("%Y-%m-%d %H:%M:%S")}\n' \
                 f'群聊名称/ID：{g_name}（{gid}）\n' \
                 f'操作者昵称/ID：{op_name}（{op_id}）\n' \
                 f'执行者昵称/ID：{u_name}（{uid}）\n' \
                 f'是否为主动撤回：{"是" if op_id == uid else "否"}\n' \
                 f'消息内容：{msg["data"]["message"]}'

            for i in func.safe_file_read('delmsgcallback').split('\n'):
                func.send(st, int(i))
                console.print('发送给：', i)
            console.print(st)
    elif request.get_json().get('notice_type') == 'group_increase':
        gid = request.get_json().get('group_id')
        uid = request.get_json().get('user_id')
        if gid == 764869658:
            func.send(msg='''\n中国青年计算机爱好者联盟 （CEA）群文件说明
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
                '你好啊！别潜水哦~'
            ]
            func.send(msg=random.choice(welcome),
                      gid=gid,
                      uid=uid)
        elif gid == 1042872173:
            fuck_file = open('fucklist', 'r')
            fuck = fuck_file.readlines()
            fuck_file.close()
            admin_file = open('admin.txt', 'r', encoding='UTF-8')
            for i in range(len(fuck)):
                fuck[i] = fuck[i].strip('\n')
            if str(uid) in fuck:
                if request.get_json().get('operator_id') != 183713750:
                    console.print('Fuck! 哪个傻逼让你进来的？')
                    func.send('一路走好，再也不见~~~', gid, uid)
                    func.tick(gid, uid)
            else:
                func.send(f'Hello，[CQ:at,qq={uid}]！\n'
                          f'    欢迎成为瑾梦的一名正式的组员，在这里只要不违反相关的条例你大可以放开了聊！希望你在瑾梦能有一个美好的记忆\n'
                          f'        ——瑾梦特别行动小组组长 白狐', gid)
            admin_file.close()
        # 因群解散现注释此代码以备份
        # elif gid == 788328739:
        #     console.print('788328739群成员增加！')
        #     fuck_file = open('fucklist', 'r')
        #     fuck = fuck_file.readlines()
        #     fuck_file.close()
        #     admin_file = open('admin.txt', 'r', encoding='UTF-8')
        #     for i in range(len(fuck)):
        #         fuck[i] = fuck[i].strip('\n')
        #     if str(uid) in fuck:
        #         if not (str(request.get_json().get('operator_id')) in admin_file.read().split('\n')):
        #             console.print('Fuck! 哪个傻逼让你进来的？')
        #             send('cnmd，谁让你进来的？？？滚！你个死马玩意儿', gid, uid)
        #             tick(gid, uid)
        #     admin_file.close()

        elif gid == 744591068:
            console.print('744591068群成员增加！')
            lel = func.get_lock_level()
            if lel == 1:
                func.tick(gid, uid)
                func.send(f'因群封锁 {uid} 被踢出'
                          f'{func.get_lock_detailed(lel)}', gid)
            elif lel == 2:
                if func.is_admin(request.get_json().get('operator_id')):
                    func.tick(gid, uid)
                    func.send(f'因群封锁 {uid} 被踢出'
                              f'{func.get_lock_detailed(lel)}', gid)
            elif lel == 3:
                if request.get_json().get('operator_id') == 0:
                    func.tick(gid, uid)
                    func.send(f'因群封锁 {uid} 被踢出'
                              f'{func.get_lock_detailed(lel)}', gid)
            elif lel == 4:
                if request.get_json().get('operator_id') != 0 and (
                        not (func.is_admin(request.get_json().get('operator_id')))):
                    func.tick(gid, uid)
                    func.send(f'因群封锁 {uid} 被踢出'
                              f'{func.get_lock_detailed(lel)}', gid)
            elif lel == 5:
                if func.is_fucker(uid):
                    func.tick(gid, uid)
                    func.send(f'因群封锁 {uid} 被踢出'
                              f'{func.get_lock_detailed(lel)}', gid)
            elif lel == 6:
                if func.is_fucker(uid) and (not (func.is_admin(request.get_json().get('operator_id')))):
                    func.tick(gid, uid)
                    func.send(f'因群封锁 {uid} 被踢出'
                              f'{func.get_lock_detailed(lel)}', gid)
        elif gid == 747458571:
            func.send('[CQ:image,file=file:///C:/FromHanTools/liaotian/img/jiki.jpg]', gid)
    elif request.get_json().get('notice_type') == 'client_status':
        d = request.get_json().get('client')
        o = request.get_json().get('online')
        console.print('机器人在其他设备登录！')
        if d["app_id"] not in [537124039]:
            func.send(f'HanBot 在其他客户端的在线状态发生了变更！\n'
                      f'[CQ:at,qq=183713750] 请检查是否为异常登录！！！'
                      f'状态：{"在线" if o else "离线"}\n'
                      f'客户端ID：{d["app_id"]}\b'
                      f'设备名称：{d["device_name"]}\n'
                      f'设备类型：{d["device_kind"]}\n', 744591068)
    # 加好友
    elif request.get_json().get('notice_type') == 'request' and request.get_json().get('request_type') == 'friend':
        func.quick_operation(request.get_json(), {
            'approve': True
        })
    # 如果监测到改名，且不是留空
    elif request.get_json().get('notice_type') == 'group_card' and request.get_json().get('card_new') != '':
        if request.get_json().get('group_id') in [
            # 788328739,  <-- 因群解散现注释此代码以备份
            751210750,
            833645046,
            744591068,
            936389498,
            902202817,
            535979960,
            1042872173
        ]:
            tmp_file = open('rename.txt', 'r', encoding='UTF-8')
            re_name_time = tmp_file.read().split(' ')
            c = int(re_name_time[0])
            console.print(re_name_time)
            t = float(re_name_time[1])
            bt = float(re_name_time[2])
            f = int(re_name_time[-1])
            tmp_file.close()
            console.print(c, t, bt)
            tmp_file.close()
            rs = '未知 - none'
            rule = '无'
            fl = True
            if ((time.time() - bt) <= (60 * 30)) or (c >= 3 and (time.time() - t) <= 60 * 3):
                tmp_file = open('rename.txt', 'w', encoding='UTF-8')
                rule = '强制封锁状态'
                rs = '负面 - negative'
                tmp_file.write('{} {} {} 1'.format(c + 1, time.time(), time.time()))
                tmp_file.close()
                fl = False
            else:
                ok_file = open('ok_name.txt', 'r', encoding='UTF-8')
                for i in ok_file.read().split('\n'):
                    if func.is_match(i, request.get_json().get('card_new'), request.get_json().get('card_new')):
                        rs = '正面 - positive'
                        rule = f'白：{i}'
                        break
                ok_file.close()
                no_file = open('noname.txt', 'r', encoding='UTF-8')
                for i in no_file.read().split('\n'):
                    if func.is_match(i, request.get_json().get('card_new'), request.get_json().get('card_new')):
                        rs = '负面 - negative'
                        rule = f'黑：{i}'
                        break
                no_file.close()
                if f:
                    tmp_file = open('rename.txt', 'w', encoding='UTF-8')
                    tmp_file.write('0 {} {} 0'.format(time.time(), time.time()))
                    tmp_file.close()
            s = '未知 - none'
            ret = {
                'Positive': 0,
                'Neutral': 0,
                'Negative': 0
            }
            if rs == '未知 - none':
                ret = func.tencent_api(str(request.get_json().get('card_new')).lower())  # 将改的名字发送至腾讯云进行情感分析
                console.print(ret)
                if ret['Sentiment'] == 'positive':  # 如果是正面情绪
                    s = '正面 - positive'
                elif ret['Sentiment'] == 'negative':  # 如果是负面情绪
                    s = '负面 - negative'
                else:  # 如果是中性
                    s = '中性 - neutral'
                rs = s
            if fl:
                tmp_file = open('rename.txt', 'w', encoding='UTF-8')
                tmp_file.write('{} {} {} {}'.format(c + 1 if time.time() - t <= 60 * 3 and (time.time() - bt) > (
                        60 * 30) else 1, t if time.time() - t <= 60 * 3 else time.time(), bt, f))
                tmp_file.close()
            #  发送一条消息到我自己的后台
            func.ssend(f'【改名监测（Beta+）】\n'
                       f'[群号]: {request.get_json().get("group_id")}\n'
                       f'[Ｑ号]: {request.get_json().get("user_id")}\n'
                       f'[新的]: {request.get_json().get("card_new")}\n'
                       f'[旧的]: {request.get_json().get("card_old")}\n'
                       f'[规则]: {rule}\n'
                       f'[初判]: {s}\n'
                       f'[终判]: {rs}\n'
                       f'[正面]: {ret["Positive"]}\n'
                       f'[中性]: {ret["Neutral"]}\n'
                       f'[负面]: {ret["Negative"]}\n'
                       f'[数值]: {re_name_time}', 183713750)

            if rs == '负面 - negative':  # 为负面情绪
                # 则把昵称改回来
                func.asyncio.run(func.set_group_card(request.get_json().get('card_old'),
                                                     request.get_json().get('group_id'),
                                                     request.get_json().get('user_id')))
                # 并发送一条消息到这个群
                func.send(f'【改名监测（Beta+）】\n'
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
    if psutil.virtual_memory().percent > 60:
        gc.collect()

    return 'OK'


if __name__ == '__main__':
    proc_title = "liaotian-bot / liaotian.py"
    setproctitle.setproctitle(proc_title)
    app.run(debug=True, host='127.0.0.1', port=8000, threaded=True)
