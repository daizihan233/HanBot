import random

from fake_useragent import UserAgent


def keyword(msg, uid, gid):
    import requests
    import json
    if msg == '' or msg == ' ':
        re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                          'group_id={0}&'
                          'message=[CQ:at,qq={1}] '
                          '{2}'.format(gid, uid, '嘿！这里是菜单\n'
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
                                                 '[5] 聊天'
                                                 '（必须@，不要加回复，尽量不要加表情，直接说内容）\n'
                                                 '使用青云客API，很智障\n'
                                                 '[6] 随机圣诞树（圣诞特供）\n'
                                                 '@机器人 随机圣诞树\n'
                                                 '像上面这样，你就能随机获得一棵圣诞树！'))
    else:
        if "admin set 咕咕咕 " in msg and (uid == 183713750 or uid == 2443818489):
            with open('gugu.txt', 'w') as file:
                file.write(str(int(msg.strip("admin set 咕咕咕 "))))
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message=鸽子'
                              '{1}'.format(gid, '您可以咕 {0} 天了').format(str(int(msg.strip("admin set 咕咕咕 ")))))
        elif "admin set 咕咕咕 " in msg and (uid != 183713750 and uid != 2443818489):
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message=[CQ:at,qq={1}]' 
                              '{2}'.format(gid, uid, '你不是机器人的开发者/管理，权限不足，无法完成此操作'))
        elif msg == '随机圣诞树':  # 如果机器人被戳
            list = [
                '你在买圣诞树回来的路上下雨了，圣诞树滴着一氧化二氢，但你把它用吹风机烘干了',  # 一氧化二氢 = 水
                '不知道为什么，圣诞树上出现了许多的氰化钾，幸运的是好像被一氧化二氢冲没了',  # 氰化钾：剧毒，白色粉末
                '一棵很正常的圣诞树',
                'wow，你手气真好，这是一棵幸运值100%的圣诞树，你的幸运值%2B%2B！',
                '嗯...这是一棵...114514形状的圣诞树',
                '哇！金色的圣诞树',
                '这个圣诞树很特殊，会在1s内化成氧',  # 氧：氧气
                'NB的圣诞树',
                '转移！这棵圣诞树可以将你的厄运转移到你最讨厌的人身上',
                '净化！这棵圣诞树可以净化掉所有的厄运',
                '芜湖~ 起飞！这棵圣诞树可以完成你最想完成的愿望',
                '这棵圣诞树会变成你最想要的东西',
            ]
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message='
                              '{1}'.format(gid,
                                           random.choice(list)))
        elif "黑名单 [CQ:at,qq=" in msg:
            f = str(msg)[len('黑名单 [CQ:at,qq='):].strip(']')
            fuck = open('fucklist', 'r').readlines()
            for i in range(len(fuck)):
                fuck[i] = fuck[i].strip('\n')

            if f in fuck:
                re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                                  'group_id={0}&'
                                  'message=[CQ:at,qq={1}] '
                                  '{2}'.format(gid, uid, '{} 已在黑名单\n'
                                                         '（如果发现恶意添加请尽快联系HanTools删除）'.format(f)))
            else:
                if f != 183713750 and f != 898140027:
                    open('fucklist', 'a').write(f + '\n')
                    re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                                      'group_id={0}&'
                                      'message=[CQ:at,qq={1}] '
                                      '{2}'.format(gid, uid, '已添加 {} 至黑名单\n'
                                                             '（如果发现恶意添加请尽快联系HanTools删除）'.format(f)))
        elif "黑名单 " in msg:
            f = str(msg).strip('黑名单 ')
            fuck = open('fucklist', 'r').readlines()
            open('fucklist', 'a').write(f+'\n')
            if f in fuck:
                re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                                  'group_id={0}&'
                                  'message=[CQ:at,qq={1}] '
                                  '{2}'.format(gid, uid, '{} 已在黑名单\n'
                                                         '（如果发现恶意添加请尽快联系HanTools删除）'.format(f)))
            else:
                re = requests.get('http://127.0.0.1:5700/send_group_msg?'
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
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
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
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message=鸽子'
                              '{1}'.format(gid, '您可以咕 {0} 天了').format(gu))
        elif "e" == msg or "额" == msg or "呃" == msg or "。" == msg or "w" == msg or \
                    "www" == msg or msg == "114514" or msg == "1145141919810" or \
                    msg == '[CQ:face,id=298]' or msg == '[CQ:face,id=178]' or msg == '[CQ:face,id=277]' or\
                msg == '？' or msg == '?' or msg == '草':
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message='
                              '{1}'.format(gid, msg))
        elif msg == '粉丝监测':
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message=[CQ:at,qq={1}] '
                              '{2}'.format(gid, uid, '您可以去找HanTools（183713750）接入机器人'))
            print('request:', re)

        else:
            headers = {
                'User-Agent': UserAgent().rget
            }
            for i in range(999):
                msg = str(msg).strip("[CQ:face,id="+str(i)+"]")
            a = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg="+msg.replace("+", "加"),
                             headers=headers)
            a = json.loads(a.text)
            print(a)
            a = a['content'].replace("{br}", "\n").replace("菲菲", "我").replace("{face:1}", "[CQ:face,id=1]")
            for i in range(999):
                msg = str(a).replace('{face:'+str(i)+'}', "[CQ:face,id="+str(i)+"]")
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


def flag_w(msg, uid, gid):
    import requests
    if msg == '关机':
        if flag() == 0:
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message=[CQ:at,qq={1}] '
                              '{2}'.format(gid, uid, '机器人现已处于关机状态，无需再次关机'))
            print('request:', re)
        else:
            with open('flag.txt', 'w', encoding='UTF-8') as f:
                f.write('0')
            re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                              'group_id={0}&'
                              'message=[CQ:at,qq={1}] '
                              '{2}'.format(gid, uid, '机器人已关机'))
            print('request:', re)
    elif msg == '开机':
        # if flag() == 1:
        #     re = requests.get('http://127.0.0.1:5700/send_group_msg?'
        #                       'group_id={0}&'
        #                       'message=[CQ:at,qq={1}] '
        #                       '{2}'.format(gid, uid, '机器人已经处于开机状态，无需再次开机'))
        #     print('request:', re)
        # else:
        #     with open('flag.txt', 'w', encoding='UTF-8') as f:
        #         f.write('1')
        #     re = requests.get('http://127.0.0.1:5700/send_group_msg?'
        #                       'group_id={0}&'
        #                       'message=[CQ:at,qq={1}] '
        #                       '{2}'.format(gid, uid, '机器人已开机'))
        re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                          'group_id={0}&'
                          'message=[CQ:at,qq={1}] '
                          '{2}'.format(gid, uid, '机器人开机功能已被禁用'))
        print('request:', re)


def flag():
    with open('flag.txt', 'r', encoding='UTF-8') as f:
        return int(f.readline())
