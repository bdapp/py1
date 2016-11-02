#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re
from socket import error as SocketError
from cookielib import CookieJar
import time


class JD_SIGN:
    def __init__(self):
        self.baseUrl = 'http://amdc.m.taobao.com/amdc/mobileDispatch?appkey=21646297&platform=android&v=3.1&deviceId=V1AAExIhl2wDAJwcljCgUyyx'


    def sign(self, value):
        try:
            print '\n***** ' + self.baseUrl + ' *****'


            # proxy = urllib2.ProxyHandler({'http': 'http://61.159.253.30:8888'})
            # opener = urllib2.build_opener(proxy) e79d101fb5ac18204fae68bfe62ca94w

            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            opener.addheaders = [
                ('User-Agent', 'Dalvik/1.6.0 (Linux; U; Android 4.1.1; Samsung Galaxy S3 - 4.1.1 - API 16 - 720x1280 Build/JRO03S)'),
                ('Host', 'amdc.m.taobao.com'),
                ('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8'),
                ('Connection', 'close'),
                ('Accept', 'gzip')
            ]

            formdata = {
                'sid':'127378332',
                'signType':'sec',
                'preIp':'106.11.12.92%3B106.11.16.95%3B106.11.16.97%3B106.11.62.99%3B113.107.235.241%3B113.107.239.110%3B114.80.174.54%3B121.14.24.254%3B121.14.89.240%3B121.9.212.240%3B140.205.16.81%3B140.205.160.63%3B140.205.163.80%3B183.61.180.200%3B183.61.180.236%3B183.61.181.250%3B183.61.241.250%3B42.120.188.9',
                'connMsg':'%5B%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22http%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22amdc.m.taobao.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A0%2C%22ip%22%3A%22140.205.160.63%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22gw.alicdn.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A16%2C%22ip%22%3A%22121.9.212.240%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22gw.alicdn.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A12%2C%22ip%22%3A%22121.9.212.240%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22gw.alicdn.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A7%2C%22ip%22%3A%22121.9.212.240%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22dorangesource.alicdn.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A31%2C%22ip%22%3A%22114.80.174.54%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22g.tbcdn.cn%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A9%2C%22ip%22%3A%22183.61.241.250%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22at.alicdn.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A4%2C%22ip%22%3A%22121.14.89.240%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22gw.alicdn.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A5%2C%22ip%22%3A%22121.9.212.240%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22dorangesource.alicdn.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A33%2C%22ip%22%3A%22114.80.174.54%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22g.tbcdn.cn%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A13%2C%22ip%22%3A%22183.61.241.250%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22at.alicdn.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A7%2C%22ip%22%3A%22121.14.89.240%22%7D%2C%7B%22ret%22%3Atrue%2C%22port%22%3A80%2C%22protocol%22%3A%22spdy%22%2C%22netType%22%3A%22WIFI%22%2C%22host%22%3A%22gw.alicdn.com%22%2C%22netIp%22%3A%22121.34.125.180%22%2C%22rt%22%3A18%2C%22ip%22%3A%22121.9.212.240%22%7D%5D',
                'cv':'1',
                'appName':'taobao_android',
                'sign':'0756f1bd0f71f8474854dd37d900a31d8df2e81a',
                'platformVersion':'4.1.1',
                'bssid':'01%3A80%3Ac2%3A00%3A00%3A03',
                'netType':'WIFI',
                't':'1466145584422',
                'appVersion':'5.8.0',
                'domain':'unszacs.m.taobao.com%20g.tbcdn.cn%20gw.alicdn.com%20unitapi.m.yao.95095.com%20g.alicdn.com%20maps.googleapis.com%20h5.m.taobao.com%20upload.m.taobao.com%20img.alicdn.com%20ditu.google.cn%20unszapi.m.yao.95095.com%20www.taobao.com%20mobilegw.alipay.com%20unitacs.m.taobao.com%20maps.gstatic.com%20hws.m.taobao.com%20amdc.m.taobao.com%20log.mmstat.com%20csi.gstatic.com%20ynuf.alipay.com%20appdownload.alicdn.com%20gtms03.alicdn.com%20dorangesource.alicdn.com%20fonts.googleapis.com%20api.m.yao.95095.com%20gtms01.alicdn.com%20wgo.mmstat.com%20api.m.taobao.com%20adash.m.taobao.com%20login.m.taobao.com%20acs.m.taobao.com%20fonts.gstatic.com',
                'channel':'231200'
            }
            data_encoded = urllib.urlencode(formdata)

            r = opener.open(self.baseUrl, data_encoded, timeout=10)
            d = r.read()


            print d

            cuT = time.localtime()
            print cuT

            # {"status": 1, "dayslist": [17], "todayGetBeansCounts": 2}


        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return False
        except Exception as e:
            print 'Exception' + e.message
            return False


jd = JD_SIGN();
jd.sign('')
