#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re
from socket import error as SocketError
from cookielib import CookieJar
import tools

class MD5:
    def __init__(self):
        self.baseUrl = 'http://md5.gromweb.com/?md5='
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
                ('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'),
                ('Referer', 'http://md5.gromweb.com/'),
                ('Host', 'md5.gromweb.com'),
                ('DNT', '1')
            ]

            r = opener.open(self.baseUrl + value, timeout=10)
            d = r.read()

            if d.find('long-content string') != -1:
                pattern = re.compile('<em class="long-content string">(.*?)</em>', re.S)
                res = re.search(pattern, d).group(1).strip()
                s = self.tool.replace(res)
                print s
                return True
            else:
                print 'no reverse string was found.'
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



