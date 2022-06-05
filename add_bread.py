import logging
import random
import time

from func import *


def running():
    while True:
        if 8 <= datetime.datetime.now().hour:
            if get_bread() < 300:
                bread = random.randint(1, 5) if is_workday_now() else random.randint(50, 100)
                tim = random.randint(60, 120)
                logger.info(f'{tim} 秒 之后，将完成 {bread} 份 面包的制作')
                time.sleep(tim)
                if get_bread() + bread > 300:
                    actual_bread = 300 - get_bread()
                else:
                    actual_bread = bread
                with open('bread.txt', 'r', encoding='utf-8') as f:
                    bread_num = int(f.read())
                    logger.debug(f'当前面包数量为 {bread_num} 份')
                logger.info(f'{bread} 份面包已经制作完成，其中 {bread - actual_bread} 份被抛弃，剩余 {actual_bread} 份')
                bread += bread_num
                logger.debug(f'写入文件：{actual_bread}')
                with open('bread.txt', 'w', encoding='utf-8') as f:
                    f.write(str(actual_bread + bread_num))
                logger.debug(f'写入成功')
            else:
                logger.warning('面包已满，等待中')
                time.sleep(60 * 10)
        else:
            logger.warning('停产中')
            time.sleep(60 * 60 * 4)


def except_run():
    try:
        running()
    except KeyboardInterrupt:
        logger.error('KeyboardInterrupt: 程序已经被终止，但被拦截', exc_info=True)
        except_run()
    except ValueError:
        logger.error('ValueError: 发送错误，但被拦截', exc_info=True)
        except_run()
    except FileNotFoundError:
        logger.error('FileNotFoundError: 文件不存在，但被拦截', exc_info=True)
        except_run()
    except Exception as e:
        print('Error is', e)
        logger.critical('出现异常，程序终止', exc_info=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] %(message)s')
    logger = logging.getLogger()
    logger.addHandler(logging.FileHandler('bread_log.txt', 'a', 'utf-8'))
    logger.setLevel(logging.DEBUG)
    except_run()
