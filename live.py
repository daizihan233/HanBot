import logging
import time

import bilibili_api.exceptions.LiveException
from bilibili_api import live, sync

import func

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] - [%(name)s] - [%(levelname)s] - %(message)s')

live_room = live.LiveDanmaku(25312800)


def send_group(msg: str, gid, call: int = 10):
    data = None
    for _ in range(call):
        data = func.send(msg, gid)
        if data['data'] is not None:
            break
    return data


def send_private_letter(msg: str, uid, call: int = 10):
    data = None
    for _ in range(call):
        data = func.ssend(msg, uid)
        if data['data'] is not None:
            break
    return data


@live_room.on('LIVE')
async def live_start():
    logging.info('直播开始')
    st = f'{func.datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S")}\n' \
         f'哈奶啤开起了直播！\n' \
         f'>>> https://live.bilibili.com/25312800'
    data = send_group(st, 747458571)
    logging.info(f'已向群 {747458571} 发送通知：\n{data}')
    data = send_private_letter(st, 183713750)
    logging.info(f'已向用户 {183713750} 发送通知：\n{data}')


while True:
    try:
        logging.info('开始监听直播')
        sync(live_room.connect())
    except bilibili_api.exceptions.LiveException.LiveException:
        logging.warning('直播异常（因模块产生）\n', exc_info=True)
        print("bilibili_api.exceptions.LiveException.LiveException")
    except Exception as err:
        if err != KeyboardInterrupt:
            logging.error('直播异常（未知原因）\n', exc_info=True)
            print("Exception：", err)
        else:
            logging.warning('直播异常（用户中断）\n')
            print("KeyboardInterrupt")
            exit(130)
