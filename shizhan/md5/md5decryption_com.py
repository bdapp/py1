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
        self.baseUrl = 'http://md5decryption.com/'
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
                ('Referer', 'http://md5decryption.com/'),
                ('Origin', 'http://md5decryption.com'),
                ('Host', 'md5decryption.com'),
                ('DNT', '1')
            ]

            formdata = {
                'hash':value,
                'submit':'Decrypt It!'
            }
            data_encoded = urllib.urlencode(formdata)

            r = opener.open(self.baseUrl, data_encoded, timeout=10)
            d = r.read()

            if d.find('font size=\'2\'') != -1:
                pattern = re.compile('font size=\'2\'>(.*?)</font>', re.S)
                res = re.search(pattern, d).group(1).strip()
                s = self.tool.replace(res)
                print s
                return True
            else:
                print 'Sorry, this MD5 hash wasn\'t found in our database'
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


