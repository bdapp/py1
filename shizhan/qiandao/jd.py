#! /usr/bin/python
# -*- coding:utf-8 -*-

import urllib2
import urllib
import re
from socket import error as SocketError
from cookielib import CookieJar


class JD_SIGN:
    def __init__(self):
        self.baseUrl = 'http://ld.m.jd.com/SignAndGetBeans/signStart.action?sid=8c4dc9886cb46670d751acfdd7826ddw'


    def sign(self, value):
        try:
            print '\n***** ' + self.baseUrl + ' *****'


            # proxy = urllib2.ProxyHandler({'http': 'http://61.159.253.30:8888'})
            # opener = urllib2.build_opener(proxy) e79d101fb5ac18204fae68bfe62ca94w

            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieHandle)

            opener.addheaders = [
                ('User-Agent', 'jdapp;android;5.0.1;4.1.1;000000000000000-080027f6c482;network/wifi;osp/android;apv/5.0.1;osv/4.1.1;uid/000000000000000-080027f6c482;pv/560.27;psn/560|000000000000000-080027f6c482;psq/26;ref/;pap/JA2015_311210|5.0.1|ANDROID;usc/;usp/;umd/;utr/;adk/;ads/;Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; Samsung Galaxy S3 - 4.1.1 - API 16 - 720x1280 Build/JRO03S) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),
                ('Referer', 'http://ld.m.jd.com/userBeanHomePage/getLoginUserBean.action?sid=8c4dc9886cb46670d751acfdd7826ddw'),
                ('Host', 'ld.m.jd.com'),
                ('X-Requested-With', 'XMLHttpRequest'),
                ('Connection', 'keep-alive'),
                ('Pragma', 'no-cache'),
                ('Cache-Control', 'no-cache'),
                ('Accept', 'application/json, text/javascript, */*; q=0.01')
            ]

            formdata = {
                '__EVENTTARGET':'',
                '__EVENTARGUMENT':'',
                '__VIEWSTATE':'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',
                '__VIEWSTATEGENERATOR':'CA0B0334',
                'ctl00$ContentPlaceHolder1$TextBoxInput':value,
                'ctl00$ContentPlaceHolder1$InputHashType':'md5',
                'ctl00$ContentPlaceHolder1$Button1':'解密',
                'ctl00$ContentPlaceHolder1$HiddenField1':'0',
                'ctl00$ContentPlaceHolder1$HiddenField2':'UkxxXcF/6Pzwi5Ab+EJZP83y+H7SsCjcWxCQ2tK6iwiig7VX9gSP8sTN1XYAf/2/'
            }
            data_encoded = urllib.urlencode(formdata)

            r = opener.open(self.baseUrl, timeout=10)
            d = r.read()


            print d

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
            print 'Exception' + e
            return False


jd = JD_SIGN();
jd.sign('')
