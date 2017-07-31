# coding:utf-8

import requests
import json

class Toutiao(object):
    # a spider to get focus news in "Today's focus News"
    
    def __init__(self):
        self.url = "http://www.toutiao.com/api/pc/focus/"
        self.root_url = "http://www.toutiao.com"

    def getinfo(self):
        # get news lists

        url = self.url
        data = requests.get(url).text
        data = json.loads(data)
        lists = data['data']['pc_feed_focus']

        # output to a file
        count = 0
        fout = open('data/Toutiaonews.json', 'w', encoding = 'utf-8')

        # get information
        for news in lists:

            newsinfo = {}

            count += 1

            newsinfo['num'] = count
            newsinfo['title'] = news['title']
            newsinfo['picture'] = news['image_url']
            newsinfo['url'] = self.root_url + news['image_url']

            encodedjson = json.dumps(newsinfo)
            fout.write(encodedjson)
            fout.write('#\n\n')

        # end
        fout.close()

    def readinfo(self):
        # get info to a object

        fout = open('data/Toutiaonews.json', 'r', encoding = 'utf-8')
        data = fout.read()
        return data

obj_spider = Toutiao()
obj_spider.getinfo()
info = obj_spider.readinfo()
print(info)