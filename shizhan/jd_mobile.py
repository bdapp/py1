# -*- coding:utf-8 -*-

import urllib2
import re
import csv
from socket import error as SocketError
import codecs
import time


class JD:
    def __init__(self):
        self.baseUrl = 'http://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_18374&area=12,978,3391&go=0&JL=6_0_0&ms=6&page='
        self.file = '/home/ubt/mm_xiaomi.csv'
        self.paramList = []


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


    # 写入文件
    def writeCSV(self, boo):
        try:
            with open(self.file, 'ab') as f:
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

        print len(parameDict)
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
        print len(self.paramList)
        print '获取完成'


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
        startTime = time.time()
        for i in range(fromPge, toPge+1):
            print '第' + str(i) + '页扫描开始～～～～～～～～～～～～～～～～'
            content = self.requestOpener(self.baseUrl + str(i))
            self.getDetailUrl(content)
            if i==fromPge:
                self.writeCSV(True)
            else:
                self.writeCSV(False)
            self.paramList = []
        print '总共用时' + str(time.time()-startTime)

jd = JD()
jd.start(1, 3)