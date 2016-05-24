# -*- coding:utf-8 -*-

# 来福 搞笑GIF
import urllib
import urllib2
import re
import os
import cookielib

class LFGIF:
    def __init__(self):
        self.baseUrl = 'http://www.laifudao.com/tupian/gaoxiaogif_3.htm'
        self.cookie = cookielib.CookieJar
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'ww3.sinaimg.cn',
            'If-Modified-Since': 'Mon, 08 Jul 2013 18:06:40 GMT',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
            }
        self.postData = urllib.urlencode({
            '': ''
        })

    # 打开请求
    def getResponse(self):
        try:
            request = urllib2.Request(url = self.baseUrl, headers = self.headers)
            response = urllib2.urlopen(request)

            #response = self.opener.open(request)
            return response.read()
        except urllib2.HTTPError, err:
            print err.code
            print err.reason
            return ''

    # 获取筛选内容
    def getTitle(self, content):
        pattern = re.compile('<img alt="(.*?)".*?data-gif="(.*?)"', re.S)
        items = re.findall(pattern, content)

        for i in items:
            self.downFile(i[0], i[1])

    # 下载GIF图片
    def downFile(self, name, url):
        print url
        folder = './gif/'
        isExist = os.path.exists(folder)
        if not isExist :
            os.makedirs(folder)

        u = urllib.urlopen(url)
        data = u.read()

        f = open(folder + name + '.gif', 'wb')
        f.write(data)
        f.close()



    def getGif(self):
        content = self.getResponse()
        self.getTitle(content)



lfGif = LFGIF()
lfGif.getGif()