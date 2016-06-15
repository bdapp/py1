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
        self.baseUrl = 'http://md5decrypt.net/en/'
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
                ('Referer', 'http://md5decrypt.net/en/'),
                ('Origin', 'http://md5decrypt.net'),
                ('Host', 'md5decrypt.net'),
                ('DNT', '1')
            ]

            formdata = {
                'hash':value,
                'decrypt':'Decrypt'
            }
            data_encoded = urllib.urlencode(formdata)

            r = opener.open(self.baseUrl, data_encoded, timeout=10)
            d = r.read()

            pattern = re.compile('<div id="ads_results">.*?<br/>(.*?)<br/>', re.S)
            res = re.search(pattern, d).group(1).strip()

            s = self.tool.replace(res)
            print s

            if s.find(':')!=-1:
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
            print 'Exception' + e.message
            return False


