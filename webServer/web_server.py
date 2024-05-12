#!coding=utf-8
import os
import socket
import re
from multiprocessing import Process

HTML_ROOT_DIR = "/Users/tongqing/PycharmProjects/pythonWCGI/Views"

class HTTPServer(object):
    def __init__(self):
        '''初始化方法'''
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        '''开始方法'''
        self.server_socket.listen(128)
        print('服务器等待客户端连接...')
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("[%s, %s]用户连接上了" % client_address)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()

    def handle_client(self, client_socket):
        '''处理客户端请求'''
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        print("received data:", request_data.decode('utf-8'))
        request_lines = request_data.splitlines()
        # 输出每行信息
        for line in request_lines:
            print(line)
        request_start_line = request_lines[0]
        print("*" * 10)
        print(request_start_line.decode('utf-8'))
        # 使用正则表达式，提取用户请求的文件名称
        file_name = re.match(r'GET\s+([^ ]+)\s+HTTP', request_start_line.decode('utf-8')).group(1)
        print("file_name"*10,file_name)
        # 如果文件名是根目录，设置文件名为file_name
        if file_name == '/' or file_name == '':
            file_name = '/index.html'
        # 打开文件，提取内容
        try:
            file = open(HTML_ROOT_DIR + file_name, 'rb')
        except IOError:
            response_start_line = 'HTTP/1.1 404 Not Found\r\n'
            response_headers = 'Content-Type: text/html\r\n\r\n'
            response_body = "This file is not found!"
        else:
            # 读取文件内容
            print("**********received file!******")
            file_data = file.read()
            file.close()
            response_start_line = 'HTTP/1.1 200 OK\r\n'
            response_headers = 'Content-Type: text/html\r\n'
            response_body = file_data.decode("utf-8")
        response = response_start_line + response_headers + "\r\n" + response_body
        print("response data:", response.encode('utf-8'))
        client_socket.send(response.encode('utf-8'))
        client_socket.close()

    def bind(self, port):
        self.server_socket.bind(('', port))

def main():
    """主函数"""
    http_server = HTTPServer()
    http_server.bind(8000)
    try:
        http_server.start()
    except:
        http_server.server_socket.close()

if __name__ == '__main__':
    main()