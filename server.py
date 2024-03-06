import socket

# 服务器IP地址和端口号
server_ip = '127.0.0.1'
server_port = 8080

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP地址和端口号
server_socket.bind((server_ip, server_port))

# 监听连接
server_socket.listen(1)

print("等待客户端连接...")

while True:
    # 接受客户端连接
    client_socket, addr = server_socket.accept()
    print("连接来自: ", addr)

    # 接收客户端发送的数据
    data = client_socket.recv(1024).decode('utf-8')
    print("接收到的数据: ", data)

    # 发送反馈给客户端
    response = "Hello, client!"
    client_socket.send(response.encode('utf-8'))

    # 关闭连接
    client_socket.close()
