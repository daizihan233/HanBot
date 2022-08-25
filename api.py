import json
import urllib
from urllib import parse

import redis

import func
import var
from richc import console


def keyword(msg: str, uid, gid, msg_id):
    import random
    import requests
    import time

    if '咕' in msg and gid not in [
        747458571
    ]:
        msg = str(msg).count('咕')
        func.isexists_dir_create('gugu{}.txt'.format(gid))
        with open('gugu{}.txt'.format(gid), 'r+', encoding='utf-8') as f:
            t = f.read()
            if t == '':
                t = 0
            console.print('t: {}, msg: {}'.format(t, msg))
            import re
            t = int(re.findall(r'\d+', str(t))[0]) + msg
            tmp_file = open('gugu{}.txt'.format(gid), 'w')
            tmp_file.write('')
            tmp_file.close()
            f.write(str(t))
        if msg >= 200:
            func.del_msg(msg_id)
        requests.get('http://127.0.0.1:5700/send_group_msg?'
                     'group_id={0}&'
                     'message=鸽子'
                     '{1}'.format(gid, '您可以咕 {0} 天了').format(t))
    if msg == '' or msg == ' ':
        func.send('https://bot.hantools.top/',
                  gid, uid)
    else:
        if msg[:4] == 'help':
            command = msg[5:]
            console.print(command)
            if command == '咕咕咕':
                func.send('\n请说：咕咕咕（当然也可以是任何数量个咕）', gid, uid)
            elif command == '黑名单':
                func.send('\n注意：此程序对空格尤为敏感\n'
                          '注意：您必须有机器人管理员权限才能执行此功能\n'
                          'Tips：机器人管理员申请请 @机器人 申请管理员\n'
                          '语法1：@机器人【空格】黑名单【空格】@...（直接@）\n'
                          '语法2：@机器人【空格】黑名单【空格】...（QQ号）\n'
                          '注意：这将影响到加群自动同意，请谨慎操作\n'
                          '注意：在部分群内已经适配完成加黑自动踢人（需要管理+适配）\n'
                          '注意：在部分群已修补可绕过黑名单的漏洞（需要管理+适配）', gid, uid)
            elif command == '加群自动同意':
                func.send('\n当有人加群时如果答案正确则自动同意，\n'
                          '否则就发消息提示（需要适配）', gid, uid)
            elif command == '禁言':
                func.send('\n注意：这需要群管理\n'
                          '注意：这需要机器人管理员权限\n'
                          '注意：此程序对空格尤为敏感\n'
                          '语法1：@机器人【空格】禁言【空格】@...（直接@）\n'
                          '语法2：@机器人【空格】禁言【空格】...（QQ号）', gid, uid)
            elif command == '':
                func.send('\n语法：@机器人 help [指令名称]\n'
                          '即可查看相关文档\n'
                          '所有在这个菜单中没有的都可以在此指令中找到', gid, uid)
            elif command == 'bb':
                func.send('看见作者的小声bb', gid, uid)
            elif command == '论证':
                func.send('\n恶臭数字论证器！\n'
                          '语法：@机器人 论证 [数字]\n'
                          '代码由 GitHub@123Windows31 提供', gid, uid)
            elif command == '解禁':
                func.send('\n注意：这需要群管理\n'
                          '注意：这需要机器人管理员权限\n'
                          '注意：此程序对空格尤为敏感\n'
                          '语法1：@机器人【空格】解禁【空格】@...（直接@）\n'
                          '语法2：@机器人【空格】解禁【空格】...（QQ号）', gid, uid)
            elif command == '清屏':
                func.send('\n注意：这需要机器人管理\n'
                          '这将发送500个换行符', gid, uid)
            elif command == '突发恶疾':
                func.send('\n语法：@机器人 突发恶疾 人名\n'
                          '即可获得一条发病文案', gid, uid)
            elif command == '鸡汤':
                func.send('不用@，你可以获得一碗心灵鸡汤', gid, uid)
            elif command == 'pi':
                func.send('估算圆周率前6位，感谢 GitHub@123Windows31 提供的代码', gid, uid)
            elif command == '播放音乐':
                func.send('\n语法：@机器人【空格】播放音乐【空格】音乐名称\n'
                          '如果不填音乐名称则返回“推荐新音乐”中的第一个歌曲\n'
                          '使用的平台：网易云音乐', gid, uid)
            elif command == '特定关键词复读':
                func.send(f'\n无需@，一条消息必须只包含关键词\n'
                          f'支持的关键词（“ | ”分割）：\n'
                          f'{" | ".join(var.repeat)}\n'
                          f'比如你说“额”，机器人就会说“额”，但你说“额额“、”额啊“是不会复读的', gid, uid)
            elif command == '聊天':
                func.send('\n必须@，@尽量置前，不要加回复，尽量不要加表情，直接说内容\n'
                          '使用的小i机器人API', gid, uid)
            elif command == '百度':
                func.send('\n让我帮你百度一下 :)\n'
                          '百度对您来讲就这么难吗？？？\n'
                          '语法：@机器人【空格】百度【空格】...（要搜的东西）\n'
                          '把最后机器人发出来的网址发给你爱提问的朋友 :)\n', gid, uid)
            elif command == '哔哩哔哩':
                func.send('参见指令“百度”', gid, uid)
            elif command == '祖安':
                func.send('\n对机器人说“祖安我”、“祖安屑”就可以让机器人祖安你，想祖安其他人的话就对机器人说“祖安@...”\n'
                          '还有一种触发方式：在群内戳一戳机器人\n'
                          '注意：吸取主号的教训，祖安功能每分钟在所有群只能触发两次，否则不会鸟你', gid, uid)
            else:
                func.send('未查找到此指令的文档！', gid, uid)
        elif msg == 'bb':
            func.send('啥也没有 :)', gid, uid)
        elif msg == '鸡汤':
            hit = func.json.loads(requests.get("https://v1.hitokoto.cn/").text)
            func.send(
                f'{hit["hitokoto"]}\n'
                f'{"    " * 4 if hit["length"] <= 10 else "    " * 6}——{hit["from"]}',
                gid
            )
        elif msg[:7] == 'addname':
            tmp = msg.split(" ")
            tmp.pop(0)
            ok_file = open('ok_name.txt', 'a', encoding='UTF-8')
            ok_file.write(f'\n{" ".join(tmp)}')
            ok_file.close()
            func.send('彳亍', gid, uid)
        elif msg[:4] == '给你面包':
            c = msg.count('🍞')
            flag = False
            b = func.get_bread()
            if c == 0:
                c = int(func.get_all_number(msg))
                flag = True
            if b < 1024 and b + c <= 1024:
                func.add_bread(c)
                func.send(f'听我说谢谢你（库存+{c}，现在库存为{func.get_bread()}）', gid, uid)
            else:
                func.send('库存满了或者装不下（', gid, uid)
            if c > 50 and not flag:
                requests.get('http://127.0.0.1:5700/delete_msg?message_id={}'.format(msg_id))
        elif msg == 'debug':
            if func.is_admin(uid):
                if func.safe_file_read('isd.on') == '1':
                    func.safe_file_write('isd.on', '0')
                    func.send('已关', gid, uid)
                else:
                    func.safe_file_write('isd.on', '1')
                    func.send('已开', gid, uid)
        elif msg[:2] == '检测':
            msg = msg.strip('\n')
            mlist = func.match_list(r'\[CQ:image,.*\]', msg)
            console.print(mlist)
            for im in mlist:
                im = im.strip('[]')
                im = im.split(',')[1:]
                for imtl in im:
                    if imtl[:4] == 'url=':
                        imurl = imtl[4:]
                        console.print('检测到图片：', imurl)
                        ta = func.tencent_image_api(imurl, '')
                        console.print(ta)
                        if ta[0] == 'Block':  # 确定
                            func.send(f'[CQ:reply,id={msg_id}]腾讯云默认策略，检测鉴定为：【确定】含有{ta[1]}内容',
                                      gid)  # ta[1] == 消息类别
                        elif ta[0] == 'Review':  # 疑似
                            func.send(f'[CQ:reply,id={msg_id}]'
                                      f'腾讯云默认策略，检测鉴定为：【疑似】含有{ta[1]}内容', gid)
                        else:
                            func.send(f'[CQ:reply,id={msg_id}]'
                                      f'腾讯云默认策略，检测鉴定为：【确定】图片内容安全', gid)
        elif msg[:4] == '监听撤回':
            if func.is_admin(uid):
                msg = msg.split(' ')
                msg.pop(0)
                tf = func.safe_file_read('delmsgstat').split('\n')
                if len(msg) == 0:
                    if str(gid) in tf:
                        func.modify_list_at_file('delmsgstat', str(gid))
                        func.send(f'好了\n'
                                  f'执行操作：\n'
                                  f'监听事件 撤回事件 关 gid:{gid}', gid, uid)
                    else:
                        tf.append(str(gid))
                        open('delmsgstat', 'a', encoding='UTF-8').write("\n".join(tf))
                        func.send(f'好了\n'
                                  f'执行操作：\n'
                                  f'监听事件 撤回事件 开 gid:{gid}', gid, uid)
                elif len(msg) == 1:
                    if msg[0] == '开':
                        if str(gid) in tf:
                            func.send('你开过了\n'
                                      '执行操作：\n'
                                      '忽略', gid, uid)
                        else:
                            func.modify_list_at_file('delmsgstat', str(gid))
                            func.send(f'好了\n'
                                      f'执行操作：'
                                      f'监听事件 撤回事件 开 gid:{gid}', gid, uid)
                    elif msg[0] == '关':
                        if str(gid) in tf:
                            func.modify_list_at_file('delmsgstat', str(gid))
                            func.send(f'好了\n'
                                      f'执行操作：\n'
                                      f'监听事件 撤回事件 关 gid:{gid}', gid, uid)
                        else:
                            func.send('你就没开\n'
                                      '执行操作：\n'
                                      '忽略', gid, uid)
                elif len(msg) == 2:
                    g = msg[1]
                    if msg[0] == '开':
                        if str(g) in tf:
                            func.send('你开过了\n'
                                      '执行操作：\n'
                                      '忽略', gid, uid)
                        else:
                            func.modify_list_at_file('delmsgstat', str(g))
                            func.send(f'好了\n'
                                      f'执行操作：'
                                      f'监听事件 撤回事件 开 gid:{g}', gid, uid)
                    elif msg[0] == '关':
                        if str(g) in tf:
                            func.modify_list_at_file('delmsgstat', str(g))
                            func.send(f'好了\n'
                                      f'执行操作：\n'
                                      f'监听事件 撤回事件 关 gid:{g}', gid, uid)
                        else:
                            func.send('你就没开\n'
                                      '执行操作：\n'
                                      '忽略', gid, uid)
            else:
                func.send('你想干嘛？', gid, uid)
        elif msg[:4] == '全体禁言':
            if func.is_admin(uid):
                t = func.get_all_number(msg.split(' ')[1], ' ').split(' ')
                t.reverse()
                t = list(map(int, t))
                tl = len(t)
                ti = 0
                ti += t[0]
                if tl >= 2:
                    ti += t[1] * 60
                if tl >= 3:
                    ti += t[2] * 60 * 60
                if tl >= 4:
                    ti += t[3] * 60 * 60 * 24
                func.all_prohibitions(gid, ti)
            else:
                func.send('鬼！', gid, uid)
        elif msg == '别骂我':
            if func.is_admin(uid):
                t = func.modify_list_at_file('no_gan.txt', str(gid))
                if t:
                    func.send('OK', gid, uid)
                else:
                    func.modify_list_at_file('no_gan.txt', str(gid))
                    func.send('OK', gid, uid)
        elif msg == '快骂我':
            if func.is_admin(uid):
                t = func.modify_list_at_file('no_gan.txt', str(gid))
                if not t:
                    func.send('OK', gid, uid)
                else:
                    func.modify_list_at_file('no_gan.txt', str(gid))
                    func.send('OK', gid, uid)
        elif msg == '关键词撤回':
            if func.is_admin(uid):
                t = func.modify_list_at_file('del_msg_grp', str(gid))
                func.send(f'好了\n'
                          f'执行操作：\n'
                          f'关键词撤回 {"开" if t else "关"}', gid, uid)
        elif msg[:4] == '加新词 ':
            if func.is_admin(uid):
                t = func.modify_list_at_file('mgc.txt', ' '.join(msg.split(' ')[1:]))
                if t:
                    func.send('OK', gid, uid)
                else:
                    func.modify_list_at_file('mgc.txt', ' '.join(msg.split(' ')[1:]))
                    func.send('OK', gid, uid)
        elif msg[:3] == '删词 ':
            if func.is_admin(uid):
                t = func.modify_list_at_file('mgc.txt', ' '.join(msg.split(' ')[1:]))
                if not t:
                    func.send('OK', gid, uid)
                else:
                    func.modify_list_at_file('mgc.txt', ' '.join(msg.split(' ')[1:]))
                    func.send('OK', gid, uid)
        elif msg[:7] == '切换面包厂模式':
            tmsg = msg.split(' ')
            if len(tmsg) == 1:
                if func.get_bread_mode() == 0:
                    func.set_bread_mode(1)
                    func.send('已将 停工 切换为 工厂模式', gid, uid)
                elif func.get_bread_mode() == 1:
                    func.set_bread_mode(2)
                    func.send('已将 工厂模式 切换为 现做模式', gid, uid)
                elif func.get_bread_mode() == 2:
                    func.set_bread_mode(1)
                    func.send('已将 现做模式 切换为 工厂模式', gid, uid)
            elif len(tmsg) == 2:
                if tmsg[1] == '停工':
                    func.set_bread_mode(0)
                elif tmsg[1] == '工厂模式':
                    func.set_bread_mode(1)
                elif tmsg[1] == '现做模式':
                    func.set_bread_mode(2)
        elif msg[:6] == 'noname':
            tmp = msg.split(" ")
            tmp.pop(0)
            no_file = open('noname.txt', 'a', encoding='UTF-8')
            no_file.write(f'\n{" ".join(tmp)}')
            no_file.close()
            func.send('彳亍', gid, uid)
        elif msg.split(' ')[0] == '来份面包':
            msg = msg.split(' ')
            if len(msg) > 2 or len(msg) < 1:
                func.send('你妈的，参数都错了，你让我咋做？', gid, uid)
            else:
                try:
                    if len(msg) != 1:
                        int(msg[1])
                except Exception:
                    func.send('你妈的，参数都错了，你让我咋做？', gid, uid)
                else:
                    if len(msg) == 1:
                        msg.append('1')
                    br = func.get_bread()
                    if br >= int(msg[1]):
                        if len(msg) == 2:
                            if int(msg[1]) < 1:
                                func.send('【错误】Sorry，您的订单量太小，请调整参数再试一次', gid, uid)
                            else:
                                if int(msg[1]) <= 100:
                                    if func.get_bread() == br:
                                        tmp = func.send('🍞' * int(msg[1]), gid, uid)
                                    else:
                                        tmp = {"data": "None"}
                                    if tmp['data'] is None:
                                        if func.get_bread() == br:
                                            tmp = func.send(f'🍞*{int(msg[1])}', gid, uid)
                                            n = str(br - int(msg[1]))
                                            func.safe_file_write("bread.txt", n)
                                            del n
                                            if tmp['data'] is None:
                                                func.send('【错误】Sorry，您的订单量太大或太小，请调整参数再试一次，也可能是由于北京的疫情原因，暂时停止了生产（指'
                                                          '风控），您可以稍等一会儿（也可能是几天）后再来购买', gid, uid)
                                    else:
                                        if func.get_bread() == br:
                                            n = str(br - int(msg[1]))
                                            func.safe_file_write("bread.txt", n)
                                            del n
                                else:
                                    if func.get_bread() == br:
                                        func.send(f'🍞*{int(msg[1])}', gid, uid)
                                        n = str(br - int(msg[1]))
                                        func.safe_file_write("bread.txt", n)
                                        del n
                    else:
                        func.send(f'【错误】Sorry，您的订单量太大，库存仅有 {br} 份面包，请等一会儿', gid, uid)
        elif msg == '面包库存':
            func.send(f'面包库存：{func.get_bread()}', gid, uid)
        elif msg == '申请管理员':
            admin = open('admin.txt', 'r', encoding='UTF-8')
            if str(uid) + '\n' in admin.readlines():
                func.send('\n啊嘞？发生了一个错误！\n'
                          '>>> Error: already an administrator\n'
                          '>>> 错误：已是管理员\n'
                          '183713750 <<<<< look here!\n'
                          '如果你觉得这个错误不应该发生那就加他！\n'
                          '将这个错误发给他！', gid, uid)
            else:
                func.send('\n183713750 <<< 加他！\n'
                          '👆 这个是机器人的开发\n'
                          '👇 申请攻略：\n'
                          '👉 详细地说明原因\n'
                          '👉 保证不会恶意操作\n'
                          '👉 保证保证不会滥用职权\n'
                          '👉 已知如果滥用此权限会被撤销\n'
                          '👉 已知在有前科的时候重新申请通过的概率会降低\n'
                          '👉 已知申请成功的概率不是100%', gid, uid)
            admin.close()
        elif msg[:3] == '封锁 ':
            if gid == 744591068:
                if func.is_admin(uid):
                    tmp = msg.split(' ')
                    level = int(tmp[1])
                    if level <= 4:
                        func.sf(gid)
                    if level <= 7:
                        func.safe_file_write('lock.txt', str(level))
                        func.send(f'封锁已开启\n'
                                  f'{func.get_lock_detailed(level)}', gid, uid)
                else:
                    func.send('你不是管理员，无法使用此命令', gid, uid)
        elif ("群文件" == msg or "病毒库" == msg) and gid == 764869658:
            func.send(msg='''中国青年计算机爱好者联盟 （CEA）群文件说明
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
        elif msg[:2] == '百度':
            msg = msg.split(' ')
            if len(msg) == 1:
                func.send('www.baiidu.com', uid, gid)
            else:
                msg.pop(0)
                url = 'https://baidu.physton.com/?q=' + parse.quote(' '.join(msg))
                func.send(url, gid, uid)
        elif msg[:2] == '论证':
            tmsg: list = msg.split(' ')
            console.print(tmsg)
            if len(tmsg) != 2:
                func.send('屑，检查一下你的参数再说罢', gid, uid)
            else:
                try:
                    tmsg[1] = int(tmsg[1])
                    console.print(tmsg)
                    func.send(func.odor_digital_demonstrator(tmsg[1]), gid, uid)
                except Exception as e:
                    console.print("报错：", e)
                    func.send('屑，你类型传错辣', gid, uid)
        elif msg == '运行状态':
            t = func.send_ws('get_status', {})["data"]
            console.print(t)
            ts = t['stat']
            func.send(f'BOT是否在线：{"是" if t["good"] else "否"}\n'
                      f'收到的数据包总数：{ts["packet_received"]}\n'
                      f'发送的数据包总数：{ts["packet_sent"]}\n'
                      f'数据包丢失总数：{ts["packet_lost"]}\n'
                      f'接受信息总数：{ts["message_received"]}\n'
                      f'发送信息总数：{ts["message_sent"]}\n'
                      f'TCP 链接断开次数：{ts["disconnect_times"]}\n'
                      f'账号掉线次数：{ts["lost_times"]}\n'
                      f'最后一条消息时间：{func.datetime.datetime.fromtimestamp(ts["last_message_time"]).strftime("%Y-%m-%d %H:%M:%S")}',
                      gid)
        elif msg[:4] == '哔哩哔哩':
            msg = msg.split(' ')
            if len(msg) <= 1:
                func.send('www.bilibili.com', uid, gid)
            else:
                msg.pop(0)
                url = 'https://www.bilitools.top/t/1/?k=' + parse.quote(''.join(msg))
                func.send(url, gid, uid)
        elif msg[:6] == 'clean ':
            t = msg.split(' ')
            t = t[1]
            t = t.split('-')
            if len(t) != 5:
                func.send('@机器人 clean 图片ID', gid, uid)
                return
            else:
                console.print(t)
                if len(t[0]) != 8 or \
                        len(t[1]) != 4 or \
                        len(t[2]) != 4 or \
                        len(t[3]) != 4 or \
                        len(t[4]) != 12:
                    func.send('@机器人 clean 图片ID', gid, uid)
                    return
            p = redis.ConnectionPool(host='43.155.62.167', port=6379, decode_responses=True)
            r = redis.Redis(connection_pool=p)
            console.print('-'.join(t))
            tt = r.hget('imh', '-'.join(t))
            r.hdel('imh', '-'.join(t))
            r.hdel('imh', tt)
            func.send('OK', gid, uid)
        elif msg[:5] == 'safe ':
            t = msg.split(' ')
            t = t[1]
            t = t.split('-')
            if len(t) != 5:
                func.send('@机器人 safe 图片ID', gid, uid)
                return
            else:
                if len(t[0]) != 8 or \
                        len(t[1]) != 4 or \
                        len(t[2]) != 4 or \
                        len(t[3]) != 4 or \
                        len(t[4]) != 12:
                    func.send('@机器人 safe 图片ID', gid, uid)
                    return
            p = redis.ConnectionPool(host='43.155.62.167', port=6379, decode_responses=True)
            r = redis.Redis(connection_pool=p)
            ttr = r.hget('imh', "-".join(t))
            tr = r.hget('imh', ttr).split(',')
            r.hset('imh', ttr, f'Pass,{tr[1]},{tr[2]}')
            func.send(f'OK\n'
                      f'建议私发至 183713750 \n'
                      f'[CQ:image,file={tr[2]}]', gid, uid)
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
            console.print("圆周率值是:{}".format(pi))
            console.print("运行时间是:{:.5f}s".format(time.perf_counter() - start))
            func.send('\n'
                      '圆周率前6位估算：{}\n'
                      '本次估算共耗时：{:.5f}s'.format(pi, time.perf_counter() - start), gid, uid)
        elif "祖安我" in msg or "祖安屑" in msg and (str(gid) not in func.safe_file_read('no_gan.txt').split('\n')):
            zu_an_file = open('zu_an_time.txt', 'r', encoding='UTF-8')
            zu_an_time = zu_an_file.read().split(' ')
            c = int(zu_an_time[0])
            console.print(zu_an_time)
            t = time.time() - float(zu_an_time[1])
            console.print(c, t)
            zu_an_file.close()
            tl = var.herbalist
            random.shuffle(tl)
            if c <= 5:
                zu_an_file = open('zu_an_time.txt', 'w', encoding='UTF-8')
                func.send(random.choice(tl), gid)
                zu_an_file.write('{} {}'.format(c + 1, time.time()))
            elif t >= 60 * 60:
                zu_an_file = open('zu_an_time.txt', 'w', encoding='UTF-8')
                func.send(random.choice(tl), gid)
                zu_an_file.write('0 {}'.format(time.time()))
            zu_an_file.close()
        elif "祖安[CQ:at,qq=" in msg and (str(gid) not in func.safe_file_read('no_gan.txt').split('\n')):
            zu_an_file = open('zu_an_time.txt', 'r', encoding='UTF-8')
            zu_an_time = zu_an_file.read().split(' ')
            c = int(zu_an_time[0])
            console.print(zu_an_time)
            t = time.time() - float(zu_an_time[1])
            console.print(c, t)
            zu_an_file.close()
            tl = var.herbalist
            random.shuffle(tl)
            if c <= 5:
                zu_an_file = open('zu_an_time.txt', 'w', encoding='UTF-8')
                msg = msg.split(' ')
                msg[0] = msg[0].strip('祖安 ')
                if '[CQ:at,qq=' in msg[0]:
                    func.send_114514(random.choice(tl), gid, msg[0])
                zu_an_file.write('{} {}'.format(c + 1, time.time()))
            elif t >= 60 * 60:
                zu_an_file = open('zu_an_time.txt', 'w', encoding='UTF-8')
                msg = msg.split(' ')
                msg[0] = msg[0].strip('祖安 ')
                if '[CQ:at,qq=' in msg[0]:
                    func.send_114514(random.choice(tl), gid, msg[0])
                zu_an_file.write('0 {}'.format(time.time()))
            zu_an_file.close()
        elif func.re_match(var.re_die, msg):
            hit = func.get_hit()
            func.send(f'\n'
                      f'您看起来对世界很失望？\n'
                      f'oh，我的朋友，别伤心了\n'
                      f'如果可以改变结果那就努力让它好起来。\n'
                      f'如果不能改变结果那为何不以摆烂终结？\n'
                      f'好好活着，就是对人生最好的答卷\n'
                      f'我知道，你可能被所有人嘲笑过\n'
                      f'我知道，你可能被所有人践踏过\n'
                      f'我知道，你可能被所有人欺骗过\n'
                      f'我知道，你可能没别人口中那样幸福\n'
                      f'不过没有关系，我也是这样\n'
                      f'如果你还想不开，那就试试找一个只有自己一个人的地方\n'
                      f'然后坐下来，细细品尝一块美味的蛋糕\n'
                      f'或许能让你尝到人生的新滋味\n'
                      f'{hit[0]} ——{hit[1]}\n'
                      f'希望你能快乐地，向你的人生递交一份满意的答卷\n'
                      f'你不孤单，还有我们！\n'
                      f'如果你需要心理疏导，可以发送“心理疏导”', gid, uid)
        elif msg == '鸡典正统是？':
            func.send('哈奶啤！', gid)
        elif msg == '查询哈奶啤粉丝数':
            func.send(f'我们最最最最最可爱的哈奶啤达成{round(func.get_bili(400507605)["f"] / 10000, 1)}w'
                      f'粉丝了，与此同时鸡典官号只有{round(func.get_bili(261453718)["f"] / 10000, 1)}w粉丝，哈哈😄，黄狗不如哈奶啤一根'
                      f'（如果你发现值为0时，那就证明请求被叔叔拦截了）', gid)
        elif msg == '查询哈奶啤含金量':
            b = func.get_bili(400507605)
            func.send(f'累计播放量：{b["a"]}\n'
                      f'累计点赞量：{b["l"]}\n'
                      f'{b["m"]}', gid)
        elif msg == '心理疏导':
            func.send('''心理咨询热线汇总：
1，【全国24小时心理危机干预热线】
电话：400-161-9995
2，【学生专线】
400-161-9995  按1
3，【抑郁专线】
400-161-9995  按2
4，【生命热线】
400-161-9995  按3
5，【中国心理危机与自杀干预中心救助热线】
电话：010-62715275
6，【北京危机干预中心】
电话：010-82951332
7，【上海市危机干预中心】
电话：021-64383562
8，【广州市心理危机干预中心热线】
电话：020-81899120
9，【南京自杀干预中心救助热线】
 电话：16896123（24小时）
10，【杭州心理研究与干预中心救助热线】
电话：（0571）85029595（24小时）
11，【武汉市精神卫生中心咨询热线】
电话：（027）85844666（8：00-21：00）
（027）51826188
18，【深圳心理危机干预热线（康宁医院）】
电话：（0755）25629459
19，【天津市心理危机干预热线】
电话：（022）88188858
20，【四川省心理危机干预中心热线】
电话：（028）87577510/87528604
21，【重庆市心理危机干预中心热线】
电话：（023）66644499
22，【青岛市心理危机干预中心自杀干预热线】
电话：86669120
（8：30－11：00，13：30－16：00）
23，【石家庄心理危机干预热线】
电话：（0311）6799116
24，【长春市心理援助热线】
电话:（0431）86985000（24小时）
（0431）86985333（8:00-16:00）
25，【南京生命求助热线】电话（025）86528082''', gid)
        elif msg == '图' and gid != 747458571:
            tim = time.perf_counter()
            if gid != 858583205:
                n = random.randint(1, var.nn)
                if n == var.nn:
                    ret_api = random.choice(var.api_list_r18)
                else:
                    ret_api = random.choice(var.api_list_r0)
            else:
                t = var.api_list_r0 + var.api_list_r18
                random.shuffle(t)
                ret_api = random.choice(t)
            ret = None
            try:
                if not ret_api[3] and not ret_api[4]:
                    if ret_api[2] is None and ret_api[1] is not None:
                        ret = requests.get(
                            ret_api[0],
                            verify=False
                        )
                        res = func.json.loads(
                            ret.text
                        )[ret_api[1]]
                    elif ret_api[1] is None:
                        res = requests.get(
                            ret_api[0],
                            verify=False
                        ).text
                    else:
                        ret = requests.get(
                            ret_api[0],
                            verify=False
                        )
                        res = func.json.loads(
                            ret.text
                        )[ret_api[2]][ret_api[1]]
                    if res[:2] == '//':
                        res = 'https:' + res
                    console.print(res)
                elif ret_api[4]:
                    ret = requests.get(
                        ret_api[0],
                        verify=False
                    ).text[ret_api[1]]
                    res = requests.get(
                        ret,
                        verify=False
                    ).content
                    with open('temp.jpg', 'wb') as f:
                        f.write(res)
                    res = 'file:///' + func.os.path.dirname(func.os.path.abspath(__file__)).replace('\\',
                                                                                                    '/') + '/temp.jpg'
                else:
                    res = requests.get(
                        ret_api[0],
                        verify=False
                    ).content
                    with open('temp.jpg', 'wb') as f:
                        f.write(res)
                    res = 'file:///' + func.os.path.dirname(func.os.path.abspath(__file__)).replace('\\',
                                                                                                    '/') + '/temp.jpg'
                func.send(  # f'{n}\n'
                    f'[CQ:image,file={res}]', gid)
            except func.json.decoder.JSONDecodeError:
                console.print(f'API             : {ret_api[0]}')
                try:
                    console.print(f'HTTP Status Code: {ret.status_code}')
                except NameError:
                    console.print('HTTP Status Code: None')
                console.print(f'JSON            : {ret}')
                console.print('ERROR            : json.decoder.JSONDecodeError')
            console.print(ret_api)
            tim_n = time.perf_counter() - tim
            console.print(tim_n)
            if tim_n <= 1:
                console.print(f'{ret_api[0]} is very fast! 5x')
            elif tim_n <= 2:
                console.print(f'{ret_api[0]} is fast! 4x')
            elif tim_n <= 4:
                console.print(f'{ret_api[0]} is normal! 3x')
            elif tim_n <= 10:
                console.print(f'{ret_api[0]} is slow! 2x')
            elif tim_n > 10:
                console.print(f'{ret_api[0]} is very slow! 1x')
        elif msg == 'muteme':
            t = random.randint(0, 514)
            if t < 60:
                t = 0
            func.forbidden_words(gid, uid, t)
            func.send(f'{f"宁被禁言 {t} s" if t > 0 else "无  事  发  生"}', gid, uid)
        elif ("黑名单" in msg) and ("[CQ:at,qq=" in msg) and gid != 747458571:
            admin = open('admin.txt', 'r', encoding='UTF-8')
            if str(uid) in admin.read().split('\n'):
                if len(str(msg).split(' ')) != 2:
                    func.send('error: 语法错误！应该只有2个空格', gid, uid)
                else:
                    tmp = str(msg).split(' ')
                    try:
                        tmp = tmp[-1][len('[CQ:at,qq='):-1]
                        tmp = int(tmp)
                        if tmp < 10000:
                            func.send('\n啊嘞？发生一个错误！\n'
                                      '>>> Error: UID minimum is 10000\n'
                                      '>>> 错误：QQ号最小为'
                                      '183713750 <<<<< look here!\n'
                                      '如果你觉得这个错误不应该发生那就加他！\n'
                                      '将这个错误发给他！', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == 2265453790 or tmp == uid or tmp in admin:
                            func.send('\nctmd！发生一个错误！\n'
                                      '>>> Error: this uid cannot be added\n'
                                      '>>> 错误：此人无法添加\n'
                                      '183713750 <<<<< 你tmd瞅这里！\n'
                                      '如果你觉得这个错误不应该发生那就加他！\n'
                                      '将这个错误发给他！', gid, uid)
                        else:
                            f = str(str(msg).split(' ')[-1])[len('[CQ:at,qq='):-1]
                            fuck_file = open('fucklist', 'r')
                            fuck = fuck_file.read().split("\n")
                            if f in fuck:
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '{} 已在黑名单'.format(f.strip())))
                                func.tick(gid, f)
                            else:
                                fuck_a = open('fucklist', 'a')
                                fuck_a.write(f + '\n')
                                fuck_a.close()
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '已添加 {} 至黑名单'.format(f)))
                                func.tick(gid, f)
                            fuck_file.close()
                    except:
                        func.send('error: 类型错误！QQ应该是int类型，但程序无法将其转为int', gid, uid)

            else:
                if len(str(msg).split(' ')) != 3:
                    func.send(
                        'error: 语法错误！您不是机器人的管理员，需要填写理由（将语法更改为@机器人【空格】黑名单【空格】@...【空格】您的理由）应该至少有3个空格',
                        gid, uid)
                else:
                    tmp = str(msg).split(' ')
                    try:
                        tmp = tmp[-2][len('[CQ:at,qq='):-1]
                        tmp = int(tmp)
                        if tmp < 10000:
                            func.send('\n啊嘞？发生一个错误！\n'
                                      '>>> Error: UID minimum is 10000\n'
                                      '>>> 错误：QQ号最小为10000'
                                      '183713750 <<<<< look here!\n'
                                      '如果你觉得这个错误不应该发生那就加他！\n'
                                      '将这个错误发给他！', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == 2265453790 or tmp == uid or tmp == admin:
                            func.send('\nctmd！发生一个错误！\n'
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
                            fuck_file = open('fucklist', 'r')
                            fuck = fuck_file.read().split("\n")
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
                                func.send('已发送至后台，等待人工审核', gid, uid)
                            fuck_file.close()
                    except:
                        func.send('error: 类型错误！QQ应该是int类型，但程序无法将其转为int', gid, uid)
            admin.close()
        elif msg[:4] == '撤回回调':
            tl = str(msg).split(' ')
            if func.is_admin(uid):
                func.send("OK: 已添加" if func.modify_list_at_file('delmsgcallback', tl[1]) else "OK: 已删除", gid, uid)
            else:
                func.send('你就是歌姬吧', gid, uid)
        elif "黑名单" in msg and gid != 747458571:
            admin = open('admin.txt', 'r', encoding='UTF-8')
            if (str(uid) + '\n') in admin.readlines():
                console.print('admin')
                if len(str(msg).split(' ')) != 2:
                    func.send('error: 语法错误！应该只有2个空格', gid, uid)
                else:
                    tmp = str(msg).split(' ')
                    try:
                        tmp = tmp[-1]
                        tmp = int(tmp)
                        if tmp < 10000:
                            func.send('error: 参数错误！QQ号最小应该是10000', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == uid:
                            func.send('error: 参数错误！无法添加此人', gid, uid)
                        else:
                            f = str(str(msg).split(' ')[-1])
                            fuck_file = open('fucklist', 'r')
                            fuck = fuck_file.read().split("\n")
                            if f in fuck:
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '{} 已在黑名单\n'
                                                                    '（如果发现恶意添加请尽快联系HanTools删除）'.format(
                                    f)))
                                func.tick(gid, f)
                            else:
                                fuck_a = open('fucklist', 'a')
                                fuck_a.write(f + '\n')
                                requests.get('http://127.0.0.1:5700/send_group_msg?'
                                             'group_id={0}&'
                                             'message=[CQ:at,qq={1}] '
                                             '{2}'.format(gid, uid, '已添加 {} 至黑名单\n'
                                                                    '（如果发现恶意添加请尽快联系HanTools删除）'.format(
                                    f.strip('\n'))))
                                func.tick(gid, f)
                    except:
                        func.send('error: 类型错误！QQ应该是int类型，但程序无法将其转为int', gid, uid)
            else:
                console.print('not admin')
                console.print(str(msg).split(' '))
                if len(str(msg).split(' ')) != 3:
                    func.send(
                        'error: 语法错误！您不是机器人的管理员，需要填写理由（将语法更改为@机器人【空格】黑名单【空格】...【空格】您的理由）应该至少有3个空格',
                        gid, uid)
                else:
                    tmp = str(msg).split(' ')
                    try:
                        tmp = tmp[-2]
                        tmp = int(tmp)
                        if tmp < 10000:
                            func.send('error: 参数错误！QQ号最小应该是10000', gid, uid)
                        elif tmp == 183713750 or tmp == 748029973 or tmp == 2265453790 or tmp == 2265453790 or tmp == uid:
                            func.send('error: 参数错误！无法添加此人', gid, uid)
                        else:
                            f = str(str(msg).split(' ')[-2])
                            r = str(str(msg).split(' ')[-1])
                            fuck_file = open('fucklist', 'r')
                            fuck = fuck_file.read().split("\n")

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
                                func.send('已发送至后台，等待人工审核', gid, uid)
                    except:
                        func.send('error: 类型错误！QQ应该是int类型，但程序无法将其转为int', gid, uid)
            admin.close()
        elif msg[:3] == '删黑 ':
            admin = open('admin.txt', 'r')
            if str(uid) in admin.read().split('\n'):
                lst = open('C:/FromHanTools/liaotian/fucklist', 'r').read().rstrip('\n').lstrip('\n').split('\n')
                while True:
                    try:
                        lst.remove('')
                    except Exception as e:
                        console.print(e)
                        break
                t = list(map(int, lst))
                if uid in t:
                    t.remove(uid)
                    open('C:/FromHanTools/liaotian/fucklist', 'w').write('\n'.join(list(map(str, t))) + '\n')
                    func.send('OK!', gid, uid)
                else:
                    func.send('你妈，此人不存在', gid, uid)
            else:
                func.send('没权限你bb啥', gid, uid)
        # elif "e" == msg or "额" == msg or "呃" == msg or "。" == msg or "w" == msg or \
        #         "www" == msg or msg == "114514" or msg == "1145141919810" or \
        #         msg == '[CQ:face,id=298]' or msg == '[CQ:face,id=178]' or msg == '[CQ:face,id=277]' or \
        #         msg == '？' or msg == '?' or msg == '草' or msg == 'c' or:
        elif msg in var.repeat:
            func.send(msg, gid)
        elif msg.replace(" ", '').lower() == 'windows2000的留言' or msg.replace(" ", '').lower() == 'windows2000的遗言':
            """ 汉吐司备忘录 """
            # 请勿利用此信息骚扰他人！！！
            # 请勿利用此信息骚扰他人！！！
            # 请勿利用此信息骚扰他人！！！
            # Windows 2000 账号1 : 2548452533
            # Windows 2000 账号2 : 2533898108
            # 2kBot QQ账号       : 2810482259
            # 2kBot 开源项目地址   : https://github.com/Abjust/2kbot/
            # 请勿利用此信息骚扰他人！！！
            # 请勿利用此信息骚扰他人！！！
            # 请勿利用此信息骚扰他人！！！
            """ 你来到了一个神奇的地方！ """
            func.send('''Windows 2000对Setup群的留言
对我而言，我曾一直觉得Setup群是个适合我的地方，我的直觉也的确没有错，Setup群确实是个好地方，我在里面学到了不少东西，并且跟群友相谈甚欢。但是，因为群里包括群主在内的不少人和我一样，都饱受抑郁症或者精神心理疾病的困扰，以至于我在面对他们慢慢开始伤害自己的时候，或者说甚至打算终结自己的时候，却显得格外无能。我的一句“赶紧去看医生吧”，此刻显得苍白无力，我理解他们第一次求助，羞于启齿不敢告诉家里人。我不是不能理解群友们的心情，或者自身的悲惨经历。但是对我而言，我真的一时间难以接受这么多负面倾诉。我不是心理咨询师，我对心理学的掌握也有限，其实说是在，我自己也是个病人，我是个双相情感障碍患者，我也是第一次面对这种情况。每次遇到这种情况，我总是想着怎么逃避现实，仿佛精神分裂般，总是觉得事情没有发生，一切都是梦境罢了。我也希望是这样，但是发生的事情终归是发生了，我不可能凭主观意识去改变。
有时候我深感愧疚，不为什么，就为病情。不说世界上的人，就群友来说，群里比我惨的大有人在，有些没事，有些是抑郁症，像我这样得双相情感障碍的基本没有。我会自行反思，自己是不是太矫情、懦弱了，是不是抗压能力太差了呢？我怀疑过自己是假抑郁，认为自己不过是在博同情、骗流量。没错，就连我自己都不相信我自己了，那还有谁会相信这么拙劣的谎言？我感觉自己什么都是装出来的，我没有一样是真的，我只是在不懂装懂，我只是在夸大自己的苦楚和不幸，丝毫没有考虑别人的感受。我就是个精致的利己主义者，自私自利，只考虑自己的感受，特别不要脸。
我知道如果我离开，那就更加坚定我就是只顾自己的人，但是有时候我真的接受不了现实，我真的很想逃离现实，跟社会隔离开来，我不知道为什么我一直想这样，我也控制不了我自己，唉，现实就是那么残酷又无情，或许别人的痛苦是真正的不幸，我得病只是我活该，是我应有的惩罚，如果真是这么说，我也认罪认罚了。说实话，来了群之后，我的事情就特别的多，我不断地给群里的人制造麻烦，做过的错事实在是太多了，实在是不可饶恕。
对不起，Setup群的各位群友们，我觉得我应该就我给你们制造的麻烦，以及我对你们的欺骗谢罪，我可能真的值得离开，如果我离开了，希望你们不要挂念我，我就是个罪人，没什么值得纪念的地方。
——Windows 2000

我们会永远记住你的，你的存在为世界增添了一份色彩，加油！Windows 2000！
——HanTools对Windows 2000留言的回复

这条留言将永远合法地封存在HanBot的代码中（已征求编写者的意见，遵照原文，仅对格式进行了修改），同样也是对那些患有精神疾病的人一个提醒：你的存在为世界增添了一份色彩！不要气馁，你还有大把时间，好好挥洒你的青春吧，就现在！
''', gid)
        elif msg[:2] == '禁言':
            msg = msg.split(' ')
            admin = open('admin.txt', 'r')
            if str(uid) in admin.read().split('\n'):
                if func.get_all_number(msg[1]) != uid:
                    if len(msg) == 3:
                        func.forbidden_words(gid, func.get_all_number(msg[1]), int(msg[2]) * 60)
                        func.send(f'已尝试将其禁言 {msg[2]} 分钟，请按实际效果为准', gid, uid)
                    elif len(msg) == 2:
                        func.forbidden_words(gid, func.get_all_number(msg[1]))
                        func.send('已尝试将其禁言 11 天 4 小时 51 分钟，请按实际效果为准', gid, uid)
                    else:
                        func.send('error: 参数过多/过少', gid, uid)
                else:
                    func.send('为什么会有人自己禁言自己啊（恼）', gid, uid)
            else:
                func.send('error: 没有权限', gid, uid)
            admin.close()
        elif msg[:2] == '解禁':
            msg = msg.split(' ')
            admin = open('admin.txt', 'r')
            if str(uid) in admin.read().split('\n'):
                if len(msg) == 2:
                    func.forbidden_words(gid, func.get_all_number(msg[1]), 0)
                    func.send('已尝试将其解除禁言，请按实际效果为准', gid, uid)
                else:
                    func.send('error: 参数过多/过少', gid, uid)
            else:
                func.send('error: 没有权限', gid, uid)
            admin.close()
        elif msg[:4] == '播放音乐':
            msg = msg.split(' ')
            msg.pop(0)
            tm = ' '.join(msg)
            if len(msg) == 0:
                tm = ''
            if tm != '':
                ret = requests.get(f'http://music.cyrilstudio.top/search?keywords={tm}').text
                ret = func.json.loads(ret)
                if ret['code'] == 200:
                    func.send(f'[CQ:music,type=163,id={ret["result"]["songs"][0]["id"]}]', gid)
                else:
                    func.send(f'\nerror: 没有找到相关音乐/API错误\n'
                              f'HTTP状态码：{ret["code"]}', gid, uid)
            else:
                func.send(
                    f'[CQ:music,type=163,id={func.json.loads(requests.get("http://music.cyrilstudio.top/personalized/newsong").text)["result"][0]["id"]}]',
                    gid)

        elif msg == '清屏':
            admin = open('admin.txt', 'r')
            if str(uid) in admin.read().split('\n'):
                func.send('\n' * 500, gid)
            else:
                func.send('error: 没有权限', gid, uid)
            admin.close()
        elif msg[:5] == '突发恶疾 ':  # 突发恶疾生成器
            name = msg.split(' ')
            console.print(name)
            name.pop(0)
            name = ' '.join(name)  # 获取人名
            console.print(name)
            if name == '':
                name = '你'
            func.send(random.choice(var.lis).format(name=name), gid)  # 随机选择模板并发送
        elif msg[:2] == '主页':
            cook = {
                "sid": "jqvas78t",
                "DedeUserID": "501081702",
                "DedeUserID__ckMd5": "ce3eb711028fad3c",
                "SESSDATA": "f6e25483%2C1671372319%2C5da10*61",
                "bili_jct": "8ff2f79b587b231238d7c4d7874d1175"
            }
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive"
            }

            n_d = "\\n"
            n_o = "\n"
            flag = True
            is_uid = False
            if '-' in msg:
                flag = False
                msg = msg.split('-')
                console.print(msg)
                msg.pop(0)
                msg = '-'.join(msg)
                if msg[:3].lower() == 'uid':
                    is_uid = True
                    msg = msg[3:]
            else:
                msg = ''
            if flag:
                dog = json.loads(
                    requests.get(
                        f'https://api.bilibili.com/x/space/acc/info?mid={316810418}&jsonp=jsonp',
                        headers=headers,
                        cookies=cook
                    ).text
                )['data']
                console.print(dog)
                happy = json.loads(
                    requests.get(
                        f'https://api.bilibili.com/x/space/acc/info?mid={400507605}&jsonp=jsonp',
                        headers=headers,
                        cookies=cook
                    ).text
                )['data']
                console.print(happy)
                jiki = json.loads(
                    requests.get(
                        f'https://api.bilibili.com/x/space/acc/info?mid={261453718}&jsonp=jsonp',
                        headers=headers,
                        cookies=cook
                    ).text
                )['data']
                func.send(f"【黄狗 - 主页信息】\n"
                          f"昵称：{dog['name']}\n"
                          f"性别：{dog['sex']}\n"
                          f"签名：{dog['sign'].replace(n_d, ' ').replace(n_o, ' ')}\n"
                          f"粉丝数：{int(json.loads(requests.get(f'https://api.bilibili.com/x/relation/stat?vmid=316810418').text)['data']['follower'])} 个\n"
                          f"粉丝牌：{dog['fans_medal']['medal']['medal_name'] if dog['fans_medal']['medal'] is not None else ''}{f'''（{dog['fans_medal']['medal']['level'] if dog['fans_medal']['medal'] is not None else ''}级）''' if dog['fans_medal']['medal'] is not None else ''}（{f'''UID{dog['fans_medal']['medal']['uid']}''' if dog['fans_medal']['medal'] is not None else '暂无'}）\n"
                          f"会员等级：{dog['vip']['label']['text'] if dog['vip']['label']['text'] != '' else '普通用户'}\n"
                          f"用户等级：LV{dog['level']}\n"
                          f"UID：{316810418}\n"
                          f"头像：\n"
                          f"[CQ:image,file={dog['face']}]\n"
                          f"去看看：https://space.bilibili.com/316810418\n"
                          f"【哈奶啤 - 主页信息】\n"
                          f"昵称：{happy['name']}\n"
                          f"性别：{happy['sex']}\n"
                          f"签名：{happy['sign'].replace(n_d, ' ').replace(n_o, ' ')}\n"
                          f"粉丝数：{int(json.loads(requests.get(f'https://api.bilibili.com/x/relation/stat?vmid=400507605').text)['data']['follower'])} 个\n"
                          f"粉丝牌：{happy['fans_medal']['medal']['medal_name'] if happy['fans_medal']['medal'] is not None else ''}{f'''（{happy['fans_medal']['medal']['level'] if happy['fans_medal']['medal'] is not None else ''}级）''' if happy['fans_medal']['medal'] is not None else ''}（{f'''UID{happy['fans_medal']['medal']['uid']}''' if happy['fans_medal']['medal'] is not None else '暂无'}）\n"
                          f"会员等级：{happy['vip']['label']['text'] if happy['vip']['label']['text'] != '' else '普通用户'}\n"
                          f"用户等级：LV{happy['level']}\n"
                          f"UID：{400507605}\n"
                          f"头像：\n"
                          f"[CQ:image,file={happy['face']}]\n"
                          f"去看看：https://space.bilibili.com/400507605\n"
                          f"【鸡典官号 - 主页信息】\n"
                          f"昵称：{jiki['name']}\n"
                          f"性别：{jiki['sex']}\n"
                          f"签名：{jiki['sign'].replace(n_d, ' ').replace(n_o, ' ')}\n"
                          f"粉丝数：{int(json.loads(requests.get(f'https://api.bilibili.com/x/relation/stat?vmid=261453718').text)['data']['follower'])} 个\n"
                          f"粉丝牌：{jiki['fans_medal']['medal']['medal_name'] if jiki['fans_medal']['medal'] is not None else ''}{f'''（{jiki['fans_medal']['medal']['level'] if jiki['fans_medal']['medal'] is not None else ''}级）''' if jiki['fans_medal']['medal'] is not None else ''}（{f'''UID{jiki['fans_medal']['medal']['uid']}''' if jiki['fans_medal']['medal'] is not None else '暂无'}）\n"
                          f"会员等级：{jiki['vip']['label']['text'] if jiki['vip']['label']['text'] != '' else '普通用户'}\n"
                          f"用户等级：LV{jiki['level']}\n"
                          f"UID：{261453718}\n"
                          f"头像：\n"
                          f"[CQ:image,file={jiki['face']}]\n"
                          f"去看看：https://space.bilibili.com/261453718",
                          gid)
            else:
                try:
                    if not is_uid:
                        stmp = json.loads(
                            requests.get(
                                f"https://api.bilibili.com/x/web-interface/search/type?__refresh__=true&_extra=&context=&page=1&page_size=36&"
                                f"order=&duration=&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword={msg}&"
                                f"category_id=&search_type=bili_user&order_sort=0&user_type=0&dynamic_offset=0&preload=true&com2co=true",
                                headers=headers,
                                cookies=cook
                            ).text
                        )['data']['result'][0]['mid']
                    else:
                        stmp = msg
                    tmp = json.loads(
                        requests.get(
                            f'https://api.bilibili.com/x/space/acc/info?mid={stmp}&jsonp=jsonp',
                            headers=headers,
                            cookies=cook
                        ).text
                    )['data']
                    func.send(f"【主页信息】\n"
                              f"昵称：{tmp['name']}\n"
                              f"性别：{tmp['sex']}\n"
                              f"签名：{tmp['sign'].replace(n_d, ' ').replace(n_o, ' ')}\n"
                              f"粉丝数：{int(json.loads(requests.get(f'https://api.bilibili.com/x/relation/stat?vmid=' + str(stmp)).text)['data']['follower'])} 个\n"
                              f"粉丝牌：{tmp['fans_medal']['medal']['medal_name'] if tmp['fans_medal']['medal'] is not None else ''}{f'''（{tmp['fans_medal']['medal']['level'] if tmp['fans_medal']['medal'] is not None else ''}级）''' if tmp['fans_medal']['medal'] is not None else ''}（{f'''当前展示的''' if tmp['fans_medal']['medal'] is not None else '暂无'}）\n"
                              f"会员等级：{tmp['vip']['label']['text'] if tmp['vip']['label']['text'] != '' else '普通用户'}\n"
                              f"用户等级：LV{tmp['level']}\n"
                              f"UID：{stmp}\n"
                              f"头像：\n"
                              f"[CQ:image,file={tmp['face']}]\n"
                              f"去看看：https://space.bilibili.com/{stmp}",
                              gid)
                except KeyError:
                    func.send(f'未搜索到结果：{msg}', gid)
        else:
            if msg[:6] == '聊天 学习 ':
                li = msg.split(' ')
                li.pop(0)
                li.pop(0)
                if len(li) != 2:
                    func.send('你他妈就没感觉哪不对吗？', gid, uid)
                else:
                    requests.post('http://www.tuling123.com/v1/kb/import', data=func.json.dumps({
                        "apikey": "3c0f165bea4b4636a939a89a723cf41d",
                        "data": {
                            "list": [
                                {"question": li[0], "answer": li[1]}
                            ]}
                    }), headers={
                        "Content-Type": "application/json"
                    })
                    func.send('彳亍', gid, uid)
            else:
                if gid not in [
                    493253441,
                    904362227,
                    971741566,
                    378235245
                ]:
                    ret = requests.post('http://openapi.turingapi.com/openapi/api/v2', data=func.json.dumps({
                        "perception": {
                            "inputText": {
                                "text": msg
                            }
                        },
                        "userInfo": {
                            "apiKey": "3c0f165bea4b4636a939a89a723cf41d",
                            "userId": str(uid),
                            "groupId": str(gid)
                        }
                    }), headers={
                        "Content-Type": "application/json"
                    })
                    ret = func.json.loads(ret.text)
                    if ret['intent']['code'] == 10004:
                        res = ''
                        for i in ret['results']:
                            res += i['values'][i['resultType']]
                        func.send(res, gid, uid)
                    else:
                        console.print(func.json.dumps(ret, indent=4))
                        msg = urllib.parse.quote(msg)
                        ret = requests.get(
                            'http://nlp.xiaoi.com/robot/webrobot?&callback=__webrobot_processMsg&data=%7B%22sessionId%22%3A'
                            '%228819ee11968945c2b10da5c81b4d5bbf%22%2C%22robotId%22%3A%22webbot%22%2C%22userId%22%3A'
                            '%22c15603528da245a2ade587e4d061725b%22%2C%22body%22%3A%7B%22content%22%3A%22' + msg +
                            '%22%7D%2C%22type%22%3A%22txt%22%7D&ts=1644758917124').text
                        import re
                        a = re.findall(r'\"content\":\"(.+?)\\r\\n\"', ret)[-1]
                        a = a.replace('\\n', '\n').replace('\\r', '').replace('\\t', '\t')
                        if a != 'defaultReply':
                            requests.get('http://127.0.0.1:5700/send_group_msg?'
                                         'group_id={0}&'
                                         'message=[CQ:at,qq={1}] '
                                         '{2}'.format(gid, uid, a))
                        else:
                            func.send(
                                func.match_and_replace(
                                    "\\{face:[0-9]\\}",
                                    (func.json.loads(
                                        requests.get(
                                            'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + urllib.parse.quote(
                                                msg)
                                        ).text
                                    )['content']).replace("【换行】", '\n').replace("\\n", '\n'),
                                    "[CQ:face,id={}]"
                                ),
                                gid, uid
                            )
