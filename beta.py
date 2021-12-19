def run():
    import random
    import time

    import requests
    import json

    mj = open('m.json', 'r').read()

    l = {}
    t = json.loads(requests.get('http://localhost:5700/get_group_member_list?group_id=907112053').text)
    for i in t['data']:
        if i['card'] == '':
            print('昵称未设置！{0} '.format(i['user_id']), end='')
            r = requests.get('http://localhost:5700/get_group_member_info?group_id=907112053&user_id={0}'
                             .format(i['user_id'])).text
            r = json.loads(r)['data']['nickname']
            l[i['user_id']] = r
            print(r)
        else:
            print('昵称已设置！{0} {1}'.format(i['user_id'], i['card']))
            l[i['user_id']] = i['card']
    open('m.json', 'w').write(json.dumps(l))
    print('昵称收集完成！')


    while True:
        m = json.load(open('m.json', 'r'))
        s = 0
        l = {}
        t = json.loads(requests.get('http://localhost:5700/get_group_member_list?group_id=907112053').text)
        for i in t['data']:
            if i['card'] == '':
                print('昵称未设置！{0} '.format(i['user_id']), end='')
                r = requests.get('http://localhost:5700/get_group_member_info?group_id=907112053&user_id={0}'
                                 .format(i['user_id'])).text
                r = json.loads(r)['data']['nickname']
                l[i['user_id']] = r
                print(r)
            else:
                print('昵称已设置！{0} {1}'.format(i['user_id'], i['card']))
                l[i['user_id']] = i['card']
        print('昵称收集完成！')
        open('m.json', 'w').write(json.dumps(l))
        if len(l) == len(m):
            for i in m:
                flag = 0
                for j in l:
                    if l[i] == m[j]:
                        flag = 1
                if not flag:
                    s += 1
                    requests.get('http://localhost:5700/set_group_card?'
                                 'group_id=907112053&'
                                 'user_id={0}&'
                                 'card={1}'.format(i, i[i]))
                    l[i] = i[i]
                    open('m.json', 'w').write(json.dumps(l))
            print('昵称对比完成！')
            requests.get('http://127.0.0.1:5700/send_group_msg?'
                         'group_id={0}&'
                         'message=[Robot][INFO] 群昵称暴力修复\n'
                         '此次共修复 {1} 个人的昵称'.format(907112053, s))
        else:
            run()

        ri = random.randint(60*1,60*10)
        print('Sleep:', ri)
        time.sleep(ri)
run()