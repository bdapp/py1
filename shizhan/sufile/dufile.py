# -*- coding:utf-8 -*-

# 下载http://www.dufile.com/
# 网站是以Cookie来限制同时下载数量

import urllib2
import urllib
import random
import re
from socket import error as SocketError
from cookielib import CookieJar


class DUFILE:

    def __init__(self):
        # 代理地址
        self.PROXY_IP = '120.52.72.58:80'
        # 验证码页
        self.CODE_URL = 'http://dufile.com/downcode.php'

        self.user_agents = [
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36',
            'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+',
            'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+',
            'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true',
            'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)',
            'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        ]

    # 打开验证码页面，获取cookie
    def start(self):
        try:
            fileID = raw_input('The file id is: ')
            # 配置代理
            proxy = urllib2.ProxyHandler({'http': '' + self.PROXY_IP + ''})
            # 配置Cookie
            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            # 走代理和带cookie
            # oo = urllib2.build_opener(proxy, cookieHandle)
            # 只带cookie
            oo = urllib2.build_opener(cookieHandle)
            # 随机获取userAgent
            user_agent = random.choice(self.user_agents)
            oo.addheaders = [
                ('User-agent', user_agent),
                ('Referer', 'http://dufile.com/file/' + fileID + '.html'),
                ('Host', 'www.dufile.com'),
                ('Origin', 'http://www.dufile.com'),
                ('DNT', '1')
            ]

            r = oo.open(self.CODE_URL, timeout=10)
            d = r.read()

            with open('./code.jpg', 'wb') as f:
                f.write(d)

            code = raw_input('input code:')

            self.getDown(oo, code, fileID)

        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return False

        return True


    # 验证输入的验证码
    def VerifyCode(self, oo, code, fileID):
        try:
            formData = {"action": 'yz', "id": fileID, "code": code}
            data_encoded = urllib.urlencode(formData)
            r = oo.open(self.CODE_URL, data_encoded, timeout=10)
            d = r.read()

            print 'code --- ' + str(d)

            if (d == '1'):
                self.getResult(oo, fileID, d)

        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return False

        return True


    # 打开下载页面
    def openDownPage(self, oo, fileID, code):
        try:
            formData = {"file_key": fileID, "p": code}
            data_encoded = urllib.urlencode(formData)
            r = oo.open('http://www.dufile.com/dd.php?file_key=' + fileID + '&p=' + code, data_encoded, timeout=10)

            d = r.read()

            with open('./result.html', 'wb') as f:
                f.write(d)

            p = re.compile('<a id="downs" href="(.*?)"', re.S)
            r = re.search(p, d)
            url = r.group(1).strip()
            print url

            self.downLoadFile(oo, url)

        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return False

        return True


    # 下载文件
    def downLoadFile(self, oo, url):
        try:
            p = re.compile('/down/(.*?)\?', re.S)
            r = re.search(p, url)
            file = r.group(1).strip()

            print file

            r = oo.open(url, timeout=10)
            d = r.read()

            with open(file, 'wb') as f:
                f.write(d)


        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return False

        return True


dufile = DUFILE()
dufile.start()
