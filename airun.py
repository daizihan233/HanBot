import ctypes
import datetime
import inspect
import re
import subprocess
import threading
import time

state = True


class TheBotIsForcedOffline(Exception):
    pass


class UnKnowError(Exception):
    pass


def run_command(command, cwd, kill_t=None, ret=True, s_out=True):
    r = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE if s_out else None,
                         stderr=subprocess.STDOUT if s_out else None, cwd=cwd)
    if kill_t is None:
        r.wait()
    else:
        time.sleep(kill_t)
        r.kill()
    if ret and s_out:
        return r.stdout.read().decode('utf-8')


class Bot1:
    def __init__(self):
        pass

    @staticmethod
    def run():
        global state
        state = True
        cmd = ['go.exe', 'faststart']
        run_command(cmd, cwd='C:/FromHanTools/bot/', s_out=False)
        print('go-cqhttp 出现错误！正在捕获15s内的日志')
        e_log = run_command(cmd, cwd='C:/FromHanTools/bot/', kill_t=15)
        print(e_log)
        print('抓取完成，开始分析错误并尝试解决')
        catch = re.compile('.*\\[.*] \\[FATAL]: .*').search(e_log)
        if catch is not None:
            catch = catch.group().split(': ')
            catch.pop(0)
            catch = ':'.join(catch).strip(' ')
            print(f'发现错误：\n{catch}')
            if catch == '账号被冻结':
                print('分析结果：账号被冻结\n'
                      '解决方案：切换至Bot2')
                raise TheBotIsForcedOffline('账号被冻结')
            else:
                print('错误未能被分析，尝试重启Bot1')
                raise RuntimeError('未能被分析的错误')
        else:
            print(f'【警告】未能复现错误，尝试重新启动Bot1\n')
            print('catch:', re.match('.*\\[.*] \\[FATAL]: .*', e_log))
            print('')
            raise UnKnowError('未能复现错误')


class Bot2:
    def __init__(self):
        pass

    @staticmethod
    def run():
        global state
        state = False
        cmd = ['go.exe', 'faststart']
        run_command(cmd, cwd='C:/FromHanTools/bot2/', s_out=False)
        print('go-cqhttp 出现错误！正在捕获15s内的日志')
        e_log = run_command(cmd, cwd='C:/FromHanTools/bot2/', kill_t=15)
        print(e_log)
        print('抓取完成，开始分析错误并尝试解决')
        catch = re.compile('.*\\[.*] \\[FATAL]: .*').search(e_log)
        if catch is not None:
            catch = catch.group().split(': ')
            catch.pop(0)
            catch = ':'.join(catch).strip(' ')
            print(f'发现错误：\n{catch}')
            if catch == '账号被冻结':
                print('分析结果：账号被冻结\n'
                      '解决方案：切换至Bot1')
                raise TheBotIsForcedOffline('账号被冻结')
            else:
                print('错误未能被分析，尝试重启Bot2')
                raise RuntimeError('未能被分析的错误')
        else:
            print(f'【警告】未能复现错误，尝试重新启动Bot2\n')
            print('catch:', re.match('.*\\[.*] \\[FATAL]: .*', e_log))
            print('')
            raise UnKnowError('未能复现错误')


def run_main():
    while True:
        try:
            Bot1.run()
        except TheBotIsForcedOffline:
            try:
                Bot2.run()
            except TheBotIsForcedOffline or RuntimeError or UnKnowError:
                pass
        except RuntimeError or UnKnowError:
            pass


def calculate_waiting_time(nt: datetime.datetime) -> int:
    ret_time = datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 0,
                                 0, 0) - nt
    ret_time = ret_time.seconds
    ret_time = ret_time / 60
    ret_time = round(ret_time)
    if ret_time == 0:
        return 1
    return ret_time


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


if __name__ == '__main__':
    a = threading.Thread(target=run_main)
    a.start()
    while True:
        if datetime.datetime.now().hour == 0 and datetime.datetime.now().minute <= 1 and not state:
            stop_thread(a)
            a.start()
        time.sleep(1)
