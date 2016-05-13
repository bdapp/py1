# -*- coding:utf-8 -*-
import urllib2
import re
import os

class PENGFU:
    def __init__(self):
        self.baseUrl = 'http://www.pengfu.com/pictag_267_'
        self.page = 1

    def start(self):
        for x in range(10):
            url = self.baseUrl + str(self.page) + '.html'
            self.page += 11
            self.getGif(url)

    def getGif(self, url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            result = response.read()
            self.getSubUrl(result)
        except urllib2.HTTPError, e:
            print e.code
            print e.reason

    def getSubUrl(self, html):
        pattern = re.compile('<dt><a onclick="_gaq.push.*?title="(.*?)".*?href="(.*?)"', re.S)
        items = re.findall(pattern, html)
        for x in items:
            print x[0] + '\t' + x[1]
            self.getSubHtml(x[0], x[1])

    def getSubHtml(self, title, url):
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            result = response.read()
            self.getImageUrl(result, title)
        except urllib2.HTTPError, e:
            print e.code
            print e.reason

    def getImageUrl(self, html, title):
        pattern = re.compile('<div class="imgbox">.*?src="(.*?)"', re.S)
        gifUrl = re.search(pattern, html)
        self.downGif(title, gifUrl.group(1))

    def downGif(self, name, url):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        result = response.read()
        with open('/home/ubt/peng/' + name + '.gif', 'wb') as f:
            f.write(result)

pengfu = PENGFU()
pengfu.start()