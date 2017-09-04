from multiprocessing import Pool
import time
import os


def test():
    # print("--------进程池中的进程--pid = %d，皮皮岛= %d--" % (os.getpgid(), os.getppid()))
    for i in range(3):
        print("---%d---" % i)
        time.sleep(1)
    return "haha"


def test2(args):
    print("------callback fun---pid=%d" % os.getpid())
    print("------callback args---args=%s" % args)


mPool = Pool(3)
mPool.apply_async(func=test, callback=test2)
time.sleep(5)
print("------主进程-----pid = %d-----" % os.getpid())
