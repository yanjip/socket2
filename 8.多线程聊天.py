# -*-coding:utf-8-*-
import socket,threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('192.168.137.1',8080)) #绑定自己的ip地址，同理客户端也是绑定自己的ip
def send():
    while True:
        msg=input('输入内容：')

        s.sendto(msg.encode('gbk'),('192.168.137.1',9090))
        if msg=='q':
            break

def rec():
    while True:
        data, addr = s.recvfrom(1024)
        print('从{}地址，{}端口号，接收到的消息是{}'.format(addr[0],addr[1],data.decode('gbk')))

t1=threading.Thread(target=send)
t2=threading.Thread(target=rec)
t1.start()
t2.start()