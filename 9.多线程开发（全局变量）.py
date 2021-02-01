import threading,time
ticket=20
def sell():
    global ticket #没有这句话会报错
    while True:
        if ticket>0:
            ticket-=1
            time.sleep(1)
            print(f'{threading.current_thread().name}卖出一张票，还剩{ticket}张')
        else:
            print('票卖完了')
            break
t1=threading.Thread(target=sell,name='1号机')
t2=threading.Thread(target=sell,name='2号机')
t1.start()
t2.start()


