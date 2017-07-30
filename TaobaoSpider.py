# coding:utf-8

import requests
import json
import re

class Taobao(object):
    # a spider to get item information in taobao

    def __init__(self, key):
        self.url = "https://s.taobao.com/search?q=" + key

    def getinfo(self):
        # get item lists

        url = self.url
        data = requests.get(url).text
        items = re.findall('g_page_config =(.+)', data)
        items = items.pop().strip()
        items = items[0 : -1]
        items = json.loads(items)
        lists = items['mods']['itemlist']['data']['auctions']

        # output to a file
        count = 0
        fout = open('data/Taobaoitems.json', 'w', encoding = 'utf-8')

        # get information
        for item in lists[1:]:
        
            iteminfo = {}

            count += 1

            iteminfo['num'] = count
            iteminfo['picture'] = item['pic_url'][2:]
            iteminfo['title'] = item['raw_title']
            iteminfo['shop'] = item['nick']
            iteminfo['price'] = item['view_price']
            iteminfo['location'] = item['item_loc']
            iteminfo['sales'] = item['view_sales']
            iteminfo['url'] = item['comment_url'][2:]
    
            encodedjson = json.dumps(iteminfo)
            fout.write(encodedjson)
            fout.write("\n\n")

        # end
        fout.close()

    def readinfo(self):
        # get info to a object

        fout = open('data/Taobaoitems.json', 'r', encoding = 'utf-8')
        data = fout.read()
        return data