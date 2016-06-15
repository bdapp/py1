#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re
from socket import error as SocketError
from cookielib import CookieJar
import tools
import base64

class MD5:
    def __init__(self):
        self.tokenUrl = 'http://www.md5decrypt.org/'
        self.baseUrl = 'http://www.md5decrypt.org/index/process'
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
                ('Referer', 'http://www.md5decrypt.org/'),
                ('Origin', 'http://www.md5decrypt.org'),
                ('Host', 'www.md5decrypt.org'),
                ('DNT', '1')
            ]

            o = opener.open(self.tokenUrl, timeout=10)
            d = o.read()

            p = re.compile('var jscheck=\'(.*?)\'', re.S)
            r = re.findall(p, d)
            token = r[1]

            formdata = {
                'jscheck': token,
                'value': base64.b64encode(value),
                'operation': 'MD5D'
            }
            data_encoded = urllib.urlencode(formdata)

            o = opener.open(self.baseUrl, data_encoded, timeout=10)
            d = o.read()

            pattern = re.compile('"body":"(.*?)","error":"(.*?)"', re.S)

            res = re.search(pattern, d).group(1).strip() + re.search(pattern, d).group(2).strip()

            s = self.tool.replace(res)
            print s

            if len(re.search(pattern, d).group(1).strip())>0 :
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



