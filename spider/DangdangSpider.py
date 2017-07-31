# coding:utf-8

import requests
import json
from bs4 import BeautifulSoup

class Dangdang(object):
    # a spider to get item information in dangdang

    def __init__(self, key):
        self.url = "http://search.dangdang.com/?key=" + key + "&act=input"

    def getinfo(self):
        # get item lists

        url = self.url
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'lxml')
        head = soup.select("ul.bigimg > li > a")[1:]
        price = soup.select("ul.bigimg > li > p.price")[1:]

        # output to a file
        count = 0
        fout = open('../data/Dangdangitems.json', 'w', encoding = 'utf-8')

        # get information
        for i in range(0, min(len(head), len(price))):

            iteminfo = {}

            count += 1

            iteminfo['num'] = count
            iteminfo['picture'] = head[i].find('img').get('data-original')
            iteminfo['title'] = head[i].get('title')
            iteminfo['price'] = price[i].find('span').get_text()[1:]

            encodedjson = json.dumps(iteminfo)
            fout.write(encodedjson)
            fout.write('#\n\n')

        # end
        fout.close()

    def readinfo(self):
        # get info to a object

        fout = open('../data/Dangdangitems.json', 'r', encoding = 'utf-8')
        data = fout.read()
        return data