import urllib.parse

from fake_useragent import UserAgent


def keyword(msg, uid, gid):
    import requests
    import json
    if msg == '' or msg == ' ':
        re = requests.get('http://127.0.0.1:5700/send_group_msg?'
                          'group_id={0}&'
                          'message=[CQ:at,qq={1}] '
                          '{2}'.format(gid, uid, '你说啥？我没听清'))
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
