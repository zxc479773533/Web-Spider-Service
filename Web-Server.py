# coding:utf-8

import socket
import TaobaoSpider
import JingDongSpider

def create_socket(address, port):
    # creat socket and listen    

    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind((address, port))
    listen_socket.listen(5)
    print('Serving HTTP on port {}'.format(port))
    return listen_socket

def accept_key(listen_socket):
    # get key

    while True:
        sock, address = listen_socket.accept()
        print('Accept connection from {}'.format(address))
        data = sock.recv(65536)
        print(data)
        data = data.decode()
        handle_spider(sock, address, data)

def handle_spider(sock, address, data):
    try:
        start_spider(sock, data)

    except EOFError:
        print('Client scoket to {} has closed'.format(address))

    except Exception as e:
        print("Client {} error: {}".format(address, e))

    finally:
        sock.close()

def start_spider(sock, data):
    # start spider according to key

    data = data.split(' ', data.count(' '))

    mode = data[0]
    key = data[1]

    print(mode)
    print(key)

    if (mode == 'taobao'):
        obj_spider = TaobaoSpider.Taobao(key)
        obj_spider.getinfo()
        info = obj_spider.readinfo()
    
    elif(mode == 'jingdong'):
        obj_spider = JingDongSpider.Jingdong(key)
        obj_spider.getinfo()
        info = obj_spider.readinfo()
    
    answer = 'HTTP/1.1 200 OK\n\n' + info
    sock.sendall(answer.encode())

if __name__=="__main__":
    listener = create_socket('', 8000)
    accept_key(listener)