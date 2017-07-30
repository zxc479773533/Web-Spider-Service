# coding:utf-8

import requests
import json
import re

def Taobao(key):
    # A spider to get information of key in Taobao

    url = "https://s.taobao.com/search?q=" + key

    # get item lists
    data = requests.get(url).text
    items = re.findall('g_page_config =(.+)', data)
    items = items.pop().strip()
    items = items[0 : -1]
    items = json.loads(items)
    lists = items['mods']['itemlist']['data']['auctions']

    # output to a file
    count = 0
    fout = open('Taobaoitems.json', 'w', encoding = 'utf-8')

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