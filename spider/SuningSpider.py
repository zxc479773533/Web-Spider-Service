# coding:utf-8

import requests
import json
from bs4 import BeautifulSoup

class Suning(object):
    # a spider to get item informatin in suning

    def __init__(self, key):
        self.url = "https://search.suning.com/" + key + "/"

    def getinfo(self):
        # get item lists

        url = self.url
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'lxml')
        items = soup.select("div.li-bg > div.product-box > div.res-img")

        # output to a file
        count = 0
        fout = open('data/Suningitems.json', 'w', encoding = 'utf-8')

        # get information
        for i in range(0, len(items)):

            iteminfo = {}

            count += 1

            iteminfo['num'] = count
            iteminfo['picture'] = items[i].find('img').get('src2')[2:]
            iteminfo['title'] = items[i].find('a').get('title')
            iteminfo['url'] = items[i].find('a').get('href')[2:]

            encodedjson = json.dumps(iteminfo)
            fout.write(encodedjson)
            fout.write('#\n\n')

        # end
        fout.close()

    def readinfo(self):
        # get info to a object

        fout = open('data/Suningitems.json', 'r', encoding = 'utf-8')
        data = fout.read()
        return data