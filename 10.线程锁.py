#加锁只是让全局变量受保护，所以关于修改全局变量的操作会变慢
#但是线程还是使其他不需要全局变量的操作速度变快了！！！！
import threading,time
lock=threading.Lock()
ticket=20
def sell():
    global ticket #没有这句话会报错
    while True:
        #操作1
        #操作2
        lock.acquire() #加锁
        if ticket>0:
            ticket-=1
            time.sleep(1)
            print(f'{threading.current_thread().name}卖出一张票，还剩{ticket}张')
            lock.release()
        else:
            lock.release()
            print('票卖完了')
            break

t1=threading.Thread(target=sell,name='1号机')
t2=threading.Thread(target=sell,name='2号机')
t1.start()
t2.start()


