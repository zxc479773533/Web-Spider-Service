# coding:utf-8

import socket
import TaobaoSpider
import JingDongSpider
import DangdangSpider
import ToutiaoSpider
from urllib import parse

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
        data = sock.recv(65536).decode()
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

    data = data.split(' ', data.count(' ') + 1)
    string = parse.unquote(data[1])[1:]
    string = string.split(' ', data.count(' ') + 1)

    mode = string[0]
    key = string[1]

    print("Mode choose: " + mode + " key words: " + key)

    if (mode == '淘宝' or mode == 'taobao' or mode == 'Taobao' or mode == 'TAOBAO' or mode == 'TB'):
        obj_spider = TaobaoSpider.Taobao(key)
        obj_spider.getinfo()
        info = obj_spider.readinfo()
    
    elif (mode == '京东' or mode == 'jingdong' or mode == 'Jingdong' or mode == 'JINGDONG' or  mode == 'JD'):
        obj_spider = JingDongSpider.Jingdong(key)
        obj_spider.getinfo()
        info = obj_spider.readinfo()

    elif (mode == '当当' or mode == 'dangdang' or mode == 'Dangdang' or mode == 'DANGDANG'):
        obj_spider = DangdangSpider.Dangdang(key)
        obj_spider.getinfo()
        info = obj_spider.readinfo()

    elif (mode = '今日头条' or '头条' or '头条新闻' or '新闻'):
        obj_spider = ToutiaoSpider.Toutiao()
        obj_spider.getinfo()
        info = obj_spider.readinfo()
    
    else:
        info = "<h1>Key words syntax error!</h1>"
    
    answer = 'HTTP/1.1 200 OK\n\n' + info
    sock.sendall(answer.encode())

if __name__=="__main__":
    print('Start web spider service')
    listener = create_socket('', 8000)
    accept_key(listener)