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
        self.baseUrl = 'http://md5.navisec.it/search'
        self.tool = tools.Tool()

    def md5(self, value):
        try:
            print '\n***** ' + self.baseUrl + ' *****'

            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            # proxy = urllib2.ProxyHandler({'http': 'http://58.59.68.91:9797'})
            # opener = urllib2.build_opener(proxy, cookieHandle)

            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'),
                ('Referer', 'http://md5.navisec.it/search'),
                ('Origin', 'http://md5.navisec.it'),
                ('Host', 'md5.navisec.it'),
                ('DNT', '1')
            ]

            o = opener.open(self.baseUrl, timeout=10)
            d = o.read()

            p = re.compile('name="_token" value="(.*?)"', re.S)
            r = re.search(p, d)
            token = r.group(1).strip()

            formdata = {
                '_token': token,
                'hash': value
            }
            data_encoded = urllib.urlencode(formdata)

            o = opener.open(self.baseUrl, data_encoded, timeout=10)
            d = o.read()

            pattern = re.compile('解密结果：.*?</code>', re.S)
            res = re.search(pattern, d).group(0).strip()

            s = self.tool.replace(res)
            print s

            if s.find('未能解密')!=-1 or s.find('积分')!=-1:
                return False
            else:
                return True


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


