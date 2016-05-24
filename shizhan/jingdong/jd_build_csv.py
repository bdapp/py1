# -*- coding:utf-8 -*-

import urllib2
import re
import csv
from socket import error as SocketError
import codecs
import time


class JD:
    def __init__(self):
        # 手机分类页面
        self.baseUrl = 'http://list.jd.com/list.html?cat=9987%2C653%2C655&go=0'
        # 手机品牌名称
        self.fileNameList = []
        # 产品参数
        self.paramList = []


    # 开启网络请求
    def requestOpener(self, url):
        flag = 0
        while True:
            try:
                opener = urllib2.build_opener(urllib2.HTTPHandler())
                if flag != 0:
                    opener.addheaders = [('User_Agent',
                                          'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')]
                else:
                    opener.addheaders = [('User_Agent',
                                          'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0')]
                response = opener.open(url, timeout=20)
                return response.read()
            except urllib2.HTTPError, e:
                print e.code
                #return ''
            except urllib2.URLError, e:
                print e.reason
                #return ''
            except SocketError, e:
                print 'SocketError: ' + str(e.errno)
                #return ''
            flag += 1
            time.sleep(3)
            if flag == 3:
                return ''

    # 创建文件
    def createCSV(self, name):
        #print name
        try:
            with open(name, 'ab') as f:
                f.write(codecs.BOM_UTF8)
                w = csv.writer(f, dialect='excel')
                w.writerow([])

            self.fileNameList.append(name)
        except Exception:
            print '创建文件失败'

    # 写入文件
    def writeCSV(self, file, boo):
        try:
            with open(file, 'ab') as f:
                f.write(codecs.BOM_UTF8)
                w = csv.writer(f, dialect='excel')
                if boo:
                    w.writerow(['品牌','型号','价格','上市年份','上市月份','操作系统',
                               '操作系统版本','CPU品牌','CPU型号','CPU核数',
                               'GPU','机身内存','运行内存','最大存储扩展',
                               '屏幕尺寸','分辨率','后置摄像头','前置摄像头',
                                '链接','备注','店铺','评价'])

                for x in self.paramList:
                    #print x
                    w.writerow(x)
        except Exception:
            print '写入数据失败'


    # 打开产品详情页获取参数
    def getDetailParame(self, content, url, name, comment, shop, price):
        p1 = re.compile('<td class=.*?tdTitle.*?>(.*?)<.*?<td>(.*?)<', re.S)
        r1 = re.findall(p1, content)

        parameDict = {}
        parames = []
        for i in r1:
            parameDict[i[0]] = i[1]

        #print len(parameDict)
        parames.append(parameDict.get('品牌',''))
        parames.append(parameDict.get('型号',''))
        parames.append(price)
        parames.append(parameDict.get('上市年份',''))
        parames.append(parameDict.get('上市月份',''))
        parames.append(parameDict.get('操作系统',''))
        parames.append(parameDict.get('操作系统版本',''))
        parames.append(parameDict.get('CPU品牌',''))
        parames.append(parameDict.get('CPU型号',''))
        parames.append(parameDict.get('CPU核数',''))
        parames.append(parameDict.get('GPU',''))
        parames.append(parameDict.get('机身内存',''))
        parames.append(parameDict.get('运行内存',''))
        parames.append(parameDict.get('最大存储扩展',''))
        parames.append(parameDict.get('屏幕尺寸',''))
        parames.append(parameDict.get('分辨率',''))
        parames.append(parameDict.get('后置摄像头',''))
        parames.append(parameDict.get('前置摄像头',''))
        parames.append('http:'+url)
        parames.append(name)
        parames.append(shop)
        parames.append(comment)

        self.paramList.append(parames)
        #print len(self.paramList)
        #print '获取完成'


    # 获取产品价格
    def getPrice(self, id):
        co = self.requestOpener(
            'http://p.3.cn/prices/get?type=1&area=1_72_2799&pdtk=&pduid=360917087&pdpin=&pdbp=0&skuid=J_' + id + '&callback=cnp')
        if co != '':
            p = re.compile('"p":"(.*?)"', re.S)
            r = re.search(p, co)
            return r.group(1)
        else:
            return ''


    # 获取产品ID
    def getProductId(self, url):
        try:
            p = re.compile('/.*?/(\d.*?).htm', re.S)
            r = re.search(p, url)
            return r.group(1)
        except Exception:
            print '获取产品ID失败'
            return ''



    # 获取每个产品的详情页链接
    def getDetailUrl(self, content):
        try:
            pattern = re.compile('<div class="p-icons J-pro-icons".*?href="(.*?)".*?<em>(.*?)</em>.*?#comment">(.*?)<.*?data-shop_name="(.*?)"', re.S)
            items = re.findall(pattern, content)
            for i in items:
                print 'url----: ' + i[0] + ' name-----: ' + i[1]
                id = self.getProductId(i[0])
                if id != '':
                    price = self.getPrice(id)
                    co = self.requestOpener('http://item.m.jd.com/ware/detail.json?wareId=' + id)
                    if co != '':
                        self.getDetailParame(co, i[0], i[1], i[2], i[3], price)

        except Exception:
            print '获取产品链接失败'


    # 开始执行任务
    def start(self, fromPge, toPge):

        for i in range(fromPge, toPge+1):
            print '第' + str(i) + '页扫描开始～～～～～～～～～～～～～～～～'
            content = self.requestOpener(self.baseUrl + str(i))
            self.getDetailUrl(content)
            if i==fromPge:
                self.writeCSV(True)
            else:
                self.writeCSV(False)
            self.paramList = []


    # 获取产品分页码和url
    def getPerProduct(self, url):
        try:
            content = self.requestOpener(url)
            #print content
            pattern = re.compile('<span class="fp-text">.*?<i>(.*?)</i>.*?class="hide ">0</a>.*?href="(.*?)"',re.S)
            res = re.search(pattern, content)
            return res
        except Exception:
            print '获取手机的分页信息异常'
            return None


    # 根据分页获取每页数据
    def getPgeProducts(self, url, file):
        res = self.getPerProduct(url)
        # 处理有分页情况
        if res != None:
            print res.group(1) + res.group(2)
            num = res.group(1)
            url = res.group(2)
            url = url.replace('page=1', 'page=')

            for i in range(1, int(num) + 1):
                u = url.replace('page=', 'page=' + str(i))
                print u
                content = self.requestOpener('http://list.jd.com' + u)
                self.getDetailUrl(content)
                if i == 1:
                    self.writeCSV(file, True)
                else:
                    self.writeCSV(file, False)
                self.paramList = []
        else:
            content = self.requestOpener('http://list.jd.com' + url)
            self.getDetailUrl(content)
            self.writeCSV(file, True)
            self.paramList = []





    def index(self):
        startTime = time.time()

        content = self.requestOpener(self.baseUrl)
        p = re.compile('data-initial=\'.*?href="(.*?)".*?title="(.*?)"', re.S)
        s = re.findall(p, content)
        for i in s:
            print i[0] + ' tt ' + i[1]
            file_name = './file/'+i[1]+'.csv'
            #self.createCSV(file_name)
            self.getPgeProducts('http://list.jd.com' + i[0], file_name)

        print '总共用时' + str(time.time() - startTime)




jd = JD()
#jd.start(1, 4)
jd.index()