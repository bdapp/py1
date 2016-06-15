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
        self.tokenUrl = 'http://md5.sssie.com/'
        self.baseUrl = 'http://md5.sssie.com/decode'
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
                ('Referer', 'http://md5.sssie.com/'),
                ('Origin', 'http://md5.sssie.com'),
                ('Host', 'md5.sssie.com'),
                ('DNT', '1')
            ]

            o = opener.open(self.tokenUrl, timeout=10)
            d = o.read()

            p = re.compile('name="csrf_token".*?value="(.*?)"', re.S)
            r = re.search(p, d)
            token = r.group(1).strip()

            formdata = {
                'csrf_token': token,
                'type': 'md5',
                'password': value,
                'submit': 'md5解密'
            }
            data_encoded = urllib.urlencode(formdata)

            o = opener.open(self.baseUrl, data_encoded, timeout=10)
            d = o.read()

            pattern = re.compile('id="home_index_div_dialog">(.*?)</div>', re.S)

            res = re.search(pattern, d).group(1).strip()

            s = self.tool.replace(res)
            print s

            if s.find('恭喜')!=-1:
                return True
            else:
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
            print 'Exception' + str(e.message)
            return False


