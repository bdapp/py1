# -*- coding:utf-8 -*-

import urllib2
import re
from socket import error as SocketError

'''
爱卡汽车--车型、价格大全
'''

class XCAR:
    def __init__(self):
        self.baseUrl = 'http://newcar.xcar.com.cn'

    # 开启网络请求
    def requestOpener(self, url):
        try:
            opener = urllib2.build_opener(urllib2.HTTPHandler())
            opener.addheaders = [('User_Agent',
                                  'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')]
            response = opener.open(url, timeout=20)
            return response.read()
        except urllib2.HTTPError, e:
            print e.code
            return ''
        except urllib2.URLError, e:
            print e.reason
            return ''
        except SocketError, e:
            print 'SocketError: ' + str(e.errno)
            return ''


    def writeFile(self, name, price, isType):
        with open('./file/car.txt', 'ab+') as f:
            if isType:
                f.write('\n----------- '+name+' -----------\n')
            else:
                f.write(name + '\t' + price + '\n')

    def getInfo(self, content):
        #print content
        p = re.compile('<h6><a.*?title="(.*?)".*?class="cokh">.*?<i>(.*?)</i>', re.S)
        items = re.findall(p, content)
        for i in items:
            self.writeFile(i[0], i[1], False)


    def start(self, url):
        content = self.requestOpener(url);
        self.getInfo(content)


    def getPerCarDetail(self, url):
        try:
            content = self.requestOpener(url)
            p = re.compile('<a href="javascript:;" class="updowm"></a>(.*?)class="updowm"', re.S)
            s = re.search(p, content)
            p2 = re.compile('href="(.*?)"', re.S)
            s2 = re.findall(p2, s.group(1))
            for i in s2 :
                self.start(self.baseUrl + i)
        except Exception:
            print url + '没有分页'
            self.start(url)

    # 查推荐
    def index(self):
        content = self.requestOpener(self.baseUrl)
        p = re.compile('<tr id="pbid_ulV" >.*?<p(.*?)</p>', re.S)
        s = re.search(p, content)
        p2 = re.compile('href="(.*?)">(.*?)</a>', re.S)
        s2 = re.findall(p2, s.group(1))
        for i in s2:
            self.writeFile(i[1], None, True)
            self.getPerCarDetail(i[0])

    # 查全部
    def index2(self):
        content = self.requestOpener(self.baseUrl)
        p1 = re.compile('<td align="right" class="bortom" valign="top" style="padding-top:5px;">.*?<p(.*?)</p>', re.S)
        s = re.findall(p1, content)
        for a in s:
            p2 = re.compile('href="(.*?)">(.*?)</a>', re.S)
            s2 = re.findall(p2, a)
            for i in s2:
                self.writeFile(i[1], None, True)
                self.getPerCarDetail(i[0])


xcar = XCAR()
xcar.index2()