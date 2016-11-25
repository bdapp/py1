#! /usr/bin/python
# -*- coding:utf-8 -*-


import urllib2
import re
from socket import error as SocketError
from cookielib import CookieJar
import time
import gzip, zlib
import json

import time


class STOCK_LIST:

    def httpConnect(self, url):
        try:
            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)
            opener.addheaders = [('User_Agent',
                                  'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36')]

            o = opener.open(url, timeout=10)
            d = o.read()
            # print d
            return d

        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return ''
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return ''
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return ''
        except Exception as e:
            print 'Exception' + str(e.message)
            return ''


    # 应用宝数据
    def queryQQ(self):
        try:
            print '------- 应用宝 --------'
            url1 = "http://mapp.qzone.qq.com/cgi-bin/mapp/mapp_info?type=appinfo&appid=1103834165&packageName=&platform=touch&network_type=unknown&resolution=360x640"
            url2 = "http://mapp.qzone.qq.com/cgi-bin/mapp/mapp_getcomment?type=myapp_all_comment&appid=1103834165&pkgname=com.cashlai.cashlaipro&pageNo=1&pageSize=10&need_score=1&platform=touch&network_type=unknown&resolution=360x640"
            # 下载量
            downJson = self.httpConnect(url1)
            downData = json.loads(downJson)
            print '下载量： ' + str(downData['app'][0]['userCount'])

            # 评论数
            commentJson = self.httpConnect(url2)
            commentJson = commentJson.replace(';', '')
            commentData = json.loads(commentJson)
            print '评论数： ' + str(commentData['data']['yyb_comment']['voteCount'])

        except Exception as e:
            print 'Exception' + str(e.message)


    # 360手机助手
    def query360(self):
        try:
            print '------- 360手机助手 --------'
            downUrl = 'http://openbox.mobilem.360.cn/iservice/getAppDetail?sort=1&pname=com.cashlai.cashlaipro'
            commentUrl = 'http://comment.mobilem.360.cn/comment/getCommentTags?objid=2433147'

            # 下载量
            downJson = self.httpConnect(downUrl)
            downData = json.loads(downJson)
            print '下载量： ' + str(downData['data'][0]['download_times'])

            # 评论数
            commentJson = self.httpConnect(commentUrl)
            commentData = json.loads(commentJson)
            print '评论数： ' + str(commentData['data']['score']['num'])

        except Exception as e:
            print 'Exception' + str(e.message)


    # 小米应用
    def queryXiaoMi(self):
        try:
            print '------- 小米应用 --------'
            commentUrl = 'https://app.market.xiaomi.com/apm/app/package/com.cashlai.cashlaipro?os=1.1.1&clientId=cfcd208495d565ef66e7dff9f98764da&sdk=19'

            #评论数
            commentJson = self.httpConnect(commentUrl)
            commentData = json.loads(commentJson)
            print '评论数： ' + str(commentData['app']['ratingTotalCount'])

        except Exception as e:
            print 'Exception' + str(e.message)


    # OPPO
    def queryOPPO(self):
        try:
            print '------- OPPO --------'
            url = 'http://store.oppomobile.com/product/0010/683/951_1.html'
            data = self.httpConnect(url)

            r = re.compile('个评分.*?&nbsp;&nbsp;(.*?)下载.*?', re.S)
            d = re.search(r, data)
            print '下载量： ' + str(d.group(1))

            # 评论数
            cUrl = 'http://store.oppomobile.com/comment/list.json?id=10683951'
            commentJson = self.httpConnect(cUrl)
            commentData = json.loads(commentJson)
            print '评论数： ' + str(commentData['totalNum'])

        except Exception as e:
            print 'Exception' + str(e.message)


    #豌豆荚
    def queryWanDouJia(self):
        try:
            print '------- 豌豆荚 --------'
            url = 'http://www.wandoujia.com/apps/com.cashlai.cashlaipro'
            data = self.httpConnect(url)

            r = re.compile('UserDownloads.*?>(.*?)</i>.*?#comments.*?<i>(.*?)</i>', re.S)
            d = re.findall(r, data)

            for i in d:
                print '下载量： ' + i[0]
                print '评论数： ' + i[1]
        except Exception as e:
            print 'Exception' + str(e.message)


    # 安智市场
    def queryAnZhi(self):
        try:
            print '------- 安智市场 --------'
            downUrl = 'http://www.anzhi.com/soft_2721997.html'
            downData = self.httpConnect(downUrl)

            downRe = re.compile('<span class="spaceleft">下载：(.*?)</span></li>', re.S)
            downValue = re.search(downRe, downData)
            print '下载量： ' + str(downValue.group(1))

            commentUrl = 'http://www.anzhi.com/comment.php?softid=2721997&packagename=com.cashlai.cashlaipro'
            commentData = self.httpConnect(commentUrl)

            commentRe = re.compile('position:relative;">评论\((.*?)\)', re.S)
            commentValue = re.search(commentRe, commentData)
            print '评论数： ' + str(commentValue.group(1))
        except Exception as e:
            print 'Exception' + str(e.message)


    # 魅族
    def queryMeiZu(self):
        try:
            print '------- 魅族 --------'
            downUrl = 'http://app.meizu.com/apps/public/detail?package_name=com.cashlai.cashlaipro'
            downData = self.httpConnect(downUrl)

            downRe = re.compile('<div class="app_content"><span>(.*?)</span>', re.S)
            downValue = re.search(downRe, downData)
            print '下载量： ' + str(downValue.group(1))

            commentUrl = 'http://app.meizu.com/apps/public/evaluate/list?app_id=1998192&start=0&max=10'
            commentData = self.httpConnect(commentUrl)

            commentJson = json.loads(commentData)
            commentValue = commentJson['value']['totalCount']

            print '评论数： ' + str(commentValue)

        except Exception as e:
            print 'Exception' + str(e.message)



    # 联想乐商店
    def queryLenovo(self):
        try:
            print '------- 联想乐商店 --------'
            downUrl = 'http://www.lenovomm.com/appdetail/com.cashlai.cashlaipro/0'
            downData = self.httpConnect(downUrl)

            downRe = re.compile('<span class="fgrey5">下载：(.*?)安装</span>', re.S)
            downValue = re.search(downRe, downData)
            print '下载量： ' + str(downValue.group(1))

            commentUrl = 'http://www.lenovomm.com/getappscore.do?pn=com.cashlai.cashlaipro&vc=0'
            commentData = self.httpConnect(commentUrl)

            commentJson = json.loads(commentData)
            commentValue = commentJson['numberOfTotal']

            print '评论数： ' + str(commentValue)
        except Exception as e:
            print 'Exception' + str(e.message)


    # PP助手（UC、淘宝）
    def queryPP(self):
        try:
            print '------- PP助手、UC、淘宝 --------'
            Url = 'http://www.25pp.com/android/detail_6570417/'
            Data = self.httpConnect(Url)

            r = re.compile('<div class="app-comment-count">(.*?)&nbsp;人评论.*?<div class="app-downs">(.*?)下载', re.S)
            v = re.findall(r, Data)
            for i in v:
                print '下载量： ' + str(i[1])
                print '评论数： ' + str(i[0])
        except Exception as e:
            print 'Exception' + str(e.message)


    # 木蚂蚁
    def queryMuMaYi(self):
        try:
            print '------- 木蚂蚁 --------'
            downUrl = 'http://m.mumayi.com/1110987'
            downData = self.httpConnect(downUrl)

            downRe = re.compile('<i class=\'guan\'>.*?<span>(.*?)下载</span>', re.S)
            downValue = re.search(downRe, downData)
            print '下载量： ' + str(downValue.group(1))

            commentUrl = 'http://changyan.sohu.com/api/2/topic/comments?client_id=cyrVcox5h&page_size=30&topic_id=1484249370&page_no=1'
            commentData = self.httpConnect(commentUrl)

            commentJson = json.loads(commentData)
            commentValue = commentJson['cmt_sum']

            print '评论数： ' + str(commentValue)
        except Exception as e:
            print 'Exception' + str(e.message)


    # 搜狗手机助手
    def querySogou(self):
        try:
            print '------- 搜狗手机助手 --------'
            downUrl = 'http://zhushou.sogou.com/apps/detail/558863.html'
            downData = self.httpConnect(downUrl)

            downRe = re.compile('<p class="count">.*?<span>(.*?)下载</span>', re.S)
            downValue = re.search(downRe, downData)
            print '下载量： ' + str(downValue.group(1))

            commentUrl = 'http://changyan.sohu.com/api/3/topic/liteload?client_id=cyr5wmvpO&page_size=10&hot_size=5&topic_source_id=558863'
            commentData = self.httpConnect(commentUrl)

            commentJson = json.loads(commentData)
            commentValue = commentJson['cmt_sum']

            print '评论数： ' + str(commentValue)
        except Exception as e:
            print 'Exception' + str(e.message)



ls = STOCK_LIST()

ls.queryQQ()
ls.query360()
ls.queryXiaoMi()
ls.queryOPPO()
ls.queryWanDouJia()
ls.queryAnZhi()
ls.queryMeiZu()
ls.queryLenovo()
ls.queryPP()
ls.queryMuMaYi()
ls.querySogou()

