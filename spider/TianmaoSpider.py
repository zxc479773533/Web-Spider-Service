# coding:utf-8

'''Because of the Tianmao's anti-spider method, this spider is in vain.'''

import requests
import json
from bs4 import BeautifulSoup
from selenium import webdriver

class Tianmao(object):
    # a spider to get item information in taobao

    def __init__(self, key):
        self.url = "https://list.tmall.com/search_product.htm?q=" + key

    def getinfo(self):
        #get itemlists

        url = self.url
        data = requests.get(url).text
        soup = BeautifulSoup(data, "lxml")
        pictureandurl = soup.select("div.product-iWrap > div.productImg-wrap")[1:]
        title = soup.select("div.product-iWrap > p.productTitle")[1:]
        price = soup.select("div.product-iWrap > p.productPrice")[1:]
        shop = soup.select("div.product-iWrap > div.productShop")[1:]
        sales = soup.select("div.product-iWrap > p.productStatus")[1:]

        # output to a file
        count = 0
        fout = open('../data/Tianmaoitems.json', 'w', encoding = 'utf-8')

        # get information
        for i in range(0, len(title)):

            iteminfo = {}

            count += 1
            
            iteminfo['num'] = count
            ##iteminfo['picture'] = pictureandurl[i].find('img').get('src')[2:]
            iteminfo['title'] = title[i].find('a').get('title')
            iteminfo['price'] = price[i].find('em').get_text()
            iteminfo['shop'] = shop[i].find('a').get_text()
            iteminfo['sales'] = sales[i].find('span').get_text()
            iteminfo['url'] = pictureandurl[i].find('a').get('href')[2:]

            encodejson = json.dumps(iteminfo)
            fout.write(encodejson)
            fout.write('#\n\n')

        # end
        fout.close()

    def readinfo(self):
        # get info to a object

        fout = open('../data/Tianmaoitems.json', 'r', encoding = 'utf-8')
        data = fout.read()
        if len(data) == 0:
            data = "404 not found"
        return data