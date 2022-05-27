import datetime
import time


def calculate_waiting_time(nt: datetime.datetime) -> int:
    ret_time = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 6,
                                 30, 0) - nt
    ret_time = ret_time.seconds
    ret_time = ret_time / 60
    ret_time = round(ret_time)
    return ret_time


while True:
    now_time = datetime.datetime.now()  # 获取当前时间
    if now_time.hour == 0 and now_time.minute == 0:  # 如果到时间了
        with open('bread.txt', 'w') as bread:
            bread.write('0')
    else:
        time.sleep(calculate_waiting_time(now_time))
