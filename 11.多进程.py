import multiprocessing,time
def sing(m):
    for i in range(m):
        time.sleep(0.5)
        print('正在唱歌！')


def dance(n):
    for i in range(n):
        time.sleep(0.5)
        print('正在跳舞！')

if __name__=='__main__':
    m1=multiprocessing.Process(target=sing,args=(20,))#参数作为元组放在args里面！！！！！！
    m2=multiprocessing.Process(target=dance,args=(20,))

    m1.start()
    m2.start()