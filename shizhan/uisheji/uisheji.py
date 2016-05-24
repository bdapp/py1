# -*- coding:utf-8 -*-

# UI设计网--手机UI展示
import urllib
import urllib2
import re
import os
import time
from socket import error as SocketError


class UI:
    def __init__(self):
        self.baseUrl = 'http://www.uisheji.com/mui/page/'
        self.baseFolder = '/home/ubt/图片/UISHEJI1/'
        self.folder = ''

    # 开启网络请求
    def requestOpener(self, url):
        try:
            opener = urllib2.build_opener(urllib2.HTTPHandler())
            opener.addheaders = [('User_Agent',
                                  'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1')]
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


    # 下载图片
    def downPic(self, path):
        try:
            list = path.split('/')
            urllib.urlretrieve(path, self.folder + '/' + list[len(list)-1])
        except Exception:
            print '下载图片异常'


    # 筛选图片链接
    def getPicUrl(self, content):
        try:
            pattern = re.compile('<div id="projectpost">.*?<img.*?src="(.*?)"', re.S)
            path = re.search(pattern, content)
            print '图片地址： ' + path.group(1)
            self.downPic(path.group(1))
        except Exception:
            print '筛选图片链接正则异常'


    # 获取图片所在页面
    def getPicPge(self, url):
        print url
        content = self.requestOpener(url);
        if content != '':
            self.getPicUrl(content)


    # 获取内页数量
    def getAllPicPgeUrl(self, content):
        try:
            pattern = re.compile('<div class="pagination">.*?>(\d+)</a></div>', re.S)
            x = re.search(pattern, content)
            print 'This page number: ' + x.group(1)
            return x.group(1)
        except Exception:
            # 没有分页默认第1页
            return 1


    # 获取内页的所有链接
    def getSubPgeUrl(self, url):
        request = self.requestOpener(url)
        if request !='':
            pageSize = int(self.getAllPicPgeUrl(request))
            for x in range(1, pageSize+1):
                self.getPicPge(url + '/' + str(x))


    # 新建图片保存目录
    def mkdirPic(self, name):
        self.folder = self.baseFolder + name
        isExists = os.path.exists(self.folder)
        if not isExists:
            os.makedirs(self.folder)


    # 获取内页链接
    def getPgeUrl(self, content):
        try:
            pattern = re.compile('<!--  这段代码会去找第一个上传的图片缩略图.*?<a href="(.*?)".*?title="(.*?)"', re.S)
            items = re.findall(pattern, content)
            for x in items:
                self.mkdirPic(x[1])
                self.getSubPgeUrl(x[0])
        except Exception:
            print '获取内面链接正则出错'


    # 打开主题页
    def openPage(self, url):
            request = self.requestOpener(url)
            if request != '' :
                self.getPgeUrl(request)


    # 程序开始
    def start(self, fromPage, toPage):
        sTime = time.time()
        while True:
            print '第' + str(fromPage) + '页扫描开始～'
            url = self.baseUrl + str(fromPage)
            self.openPage(url)
            fromPage += 1
            if fromPage > toPage:
                break
        eTime = time.time()
        print '\n===== 总耗时：' + str(eTime - sTime) + ' =====\n'


ui = UI()
ui.start(1, 50)