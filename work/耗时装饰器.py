"""
构建一个计算函数运行时间的装饰器
"""
import timeit
import time

def timeer(func):
    def inner():
        elapsed_time = timeit.timeit(stmt=func,number=1)
        print('耗时:',elapsed_time)
    return inner


def spend_time(func):
    def wrapper(*args,**kwargs):
        ts=time.time()
        res=func(*args,**kwargs)
        ct=time.time()-ts
        print("[%s]运行时间：[%s]秒" % (func.__name__, ct))
        return res
    return wrapper()


@spend_time
def demo():
    print('hahah')


if __name__ == '__main__':
    demo()