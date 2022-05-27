import datetime
import logging
import random
import time

from func import *

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] %(message)s')
logger = logging.getLogger()
logger.addHandler(logging.FileHandler('bread_log.txt', 'a', 'utf-8'))
logger.setLevel(logging.DEBUG)
try:
    while True:
        if 8 < datetime.datetime.now().hour:
            if get_bread() <= 300:
                bread = random.randint(1, 5)
                tim = random.randint(60, 120)
                logger.info(f'{tim} 秒 之后，将完成 {bread} 份 面包的制作')
                time.sleep(tim)
                with open('bread.txt', 'r', encoding='utf-8') as f:
                    bread_num = int(f.read())
                    logger.debug(f'当前面包数量为 {bread_num} 份')
                logger.info(f'{bread} 份面包已经制作完成')
                bread += bread_num
                logger.debug(f'写入文件：{bread}')
                with open('bread.txt', 'w', encoding='utf-8') as f:
                    f.write(str(bread))
                logger.debug(f'写入成功')
            else:
                logger.warning('面包已满，等待中')
                time.sleep(60 * 60)
        else:
            logger.warning('停产中')
            time.sleep(60 * 60 * 4)
except Exception:
    logger.critical('出现异常，程序终止', exc_info=True)
