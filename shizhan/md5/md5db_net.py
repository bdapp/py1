#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import re
from socket import error as SocketError
from cookielib import CookieJar
import tools

class MD5:
    def __init__(self):
        self.baseUrl = 'http://md5db.net/view/'
        self.tool = tools.Tool()

    def md5(self, value):
        try:
            print '\n***** ' + self.baseUrl + ' *****'

            # proxy = urllib2.ProxyHandler({'http': '' + ip + ''})
            # opener = urllib2.build_opener(proxy)

            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'),
                ('Host', 'md5db.net'),
                ('DNT', '1')
            ]


            r = opener.open(self.baseUrl + value, timeout=10)
            d = r.read()

            pattern = re.compile('</thead>(.*?)</table>', re.S)
            res = re.search(pattern, d).group(1).strip()
            if res.find('<b>')!= -1:
                p = re.compile('<b>(.*?)</b>', re.S)
                res = re.search(p, res).group(1).strip()
                s = self.tool.replace(res)
                print s
                return True

            else:
                print 'Word not found !'
                return False



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
            print 'Exception' + e
            return False



