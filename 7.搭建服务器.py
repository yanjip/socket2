import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('39.102.43.100',9090))

s.listen(128)
client_socket,client_addr=s.accept()
data=client_socket.recv(1024).decode()

client_socket.send('HTTP/1.1 200 OK\n'.encode())
client_socket.send('content-type:text/html\n'.encode())
client_socket.send('\n'.encode())

client_socket.send('你终于看到我了'.encode())

# print(f'接收到客户端为{client_addr[0]},端口号为{client_addr[1]}的数据,内容是：{data}')