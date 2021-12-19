import datetime
import time

time_d_old = datetime.datetime.now().day
while True:
    time_d = datetime.datetime.now().day
    if time_d != time_d_old:
        time_d_old = time_d_old
        with open('qd.txt', 'r+', encoding='UTF-8') as f:  # 打开记录文件
            file_text = f.readlines()  # 读取文件
        for index in range(len(file_text)):
            temp = file_text[index].strip('\n').split(' ')
            file_text[index] = temp[0] + ' ' + str(int(temp[1])) + ' ' + '0'
    time.sleep(60*30)
