#! /usr/bin/python
# -*- coding:utf-8 -*-


import urllib2
import re
from socket import error as SocketError
from cookielib import CookieJar
import subprocess
import os
import time


class STOCK:

    def __init__(self):

        self.baseUrl = 'http://hq.sinajs.cn/list='


    def wang(self, value):
        try:
            # print '\n***** ' + self.baseUrl + ' *****'

            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36')
            ]

            url = self.baseUrl +value
            o = opener.open(url, timeout=10)
            d = o.read()

            pattern = re.compile('(.*?),', re.S)
            results = re.findall(pattern, d)

            price = round(float(results[3]), 2)
            money = round(float(results[3])-float(results[2]), 2)
            percent = round(float(money)/float(results[2])*100, 2)
            time = results[31]

            if money >0:
                # os.system('clear')
                 print '\033[1;31;40m'
            else:
                # os.system('clear')
                 print '\033[1;32;40m'

            print str(price) + '\t' + str(money) + '\t' + str(percent) + '\t' + time;


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
            print 'Exception' + str(e.message)
            return False




lf = STOCK()
while(0<1):
    time.sleep(3)
    lf.wang('sz000014')

