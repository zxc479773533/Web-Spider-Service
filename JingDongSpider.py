# coding:utf-8

import requests
import json
from bs4 import BeautifulSoup

class Jingdong(object):
     # a spider to get item information in jingdong

    def __init__(self, key):
        self.url = "https://search.jd.com/Search?keyword=" + key + "&enc=utf-8&wq=bjbdn&pvid=655a2bdf356d4f8fb4391feb843f584a"

    def getinfo(self):
        # get item lists

        url = self.url
        data = requests.get(url).text.encode('latin1').decode('utf-8')
        soup = BeautifulSoup(data,'lxml')
        pictureandurl = soup.select("div.gl-i-wrap > div.p-img")[1:]
        title = soup.select("div.gl-i-wrap > div.p-name")[1:]
        price = soup.select("div.gl-i-wrap > div.p-price")[1:]

        # output to a file
        count = 0
        fout = open('data/Jingdongitems.json', 'w', encoding = 'utf-8')

        # get information
        for i in range(0,len(title)):
        
            iteminfo = {}

            count += 1

            iteminfo['num'] = count
            #iteminfo['picture'] = pictureandshop[i].find('img').get('src')[2:]
            iteminfo['title'] = title[i].find('em').get_text()
            if (price[i].find('i') is None):
                count -= 1
                continue
            iteminfo['price'] = price[i].find('i').get_text()
            iteminfo['url'] = pictureandurl[i].find('a').get('href')[2:]
    
            encodedjson = json.dumps(iteminfo)
            fout.write(encodedjson)
            fout.write('#\n\n')

        # end
        fout.close()

    def readinfo(self):
        # get info to a object

        fout = open('data/Jingdongitems.json', 'r', encoding = 'utf-8')
        data = fout.read()
        return data