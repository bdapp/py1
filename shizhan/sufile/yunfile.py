# -*- coding:utf-8 -*-

# 下载http://www.yunfile.com/
# 网站有IP时间限制

import urllib2
import urllib
import random
import time
import re
from socket import error as SocketError
from cookielib import CookieJar


class YUNFILE:
    def __init__(self):
        # 代理地址
        self.PROXY_IP = '121.204.165.51:8118'
        # 初始页
        self.OPEN_URL = 'http://page2.dfpan.com/fs/7al1ex230801312653fb4/'
        # 验证码页
        self.CODE_URL = 'http://page2.dfpan.com/verifyimg/getPcv.html'
        # 打开下载页
        self.DOWN_URL = 'http://page2.dfpan.com/file/down/'

        self.user_agents = [

            # PC-UA
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',

            # MOB-UA
            'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
            'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
            'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
            'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
            'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
            'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
            'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
            'UCWEB7.0.2.37/28/999',
            'NOKIA5700/ UCWEB7.0.2.37/28/999',
            'Openwave/ UCWEB7.0.2.37/28/999',
            'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999'
        ]

    # 打开初始页获取cookie
    def start(self):
        try:
            # fileID = raw_input('The file id is: ')
            # 配置代理
            proxy = urllib2.ProxyHandler({'http': self.PROXY_IP})
            # 配置Cookie
            cj = CookieJar()
            cookieHandle = urllib2.HTTPCookieProcessor(cj)
            # 走代理和带cookie
            # opener = urllib2.build_opener(proxy, cookieHandle)
            # 只带cookie
            opener = urllib2.build_opener(cookieHandle)
            # 随机获取userAgent
            user_agent = random.choice(self.user_agents)
            print user_agent
            opener.addheaders = [
                ('User-Agent', user_agent),
                ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
                ('Connection', 'keep-alive'),
                ('Referer',  self.OPEN_URL)
            ]

            urllib2.install_opener(opener)

            r = opener.open(self.OPEN_URL, timeout=10)
            d = r.read()

            p = re.compile('<div id="premium_div"  style="display: ;">.*?Membership/\',\'(.*?)\',\'(.*?)\'', re.S)
            id = re.findall(p, d)
            url = ''
            for i in id:
                url = i[0] + i[1]

            if url == '':
                print '失败'
            else:
                self.getVerifyCode(opener, url)


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



    def getVerifyCode(self, opener, id):
        try:
            c = opener.open(self.CODE_URL, timeout=10)
            co = c.read()

            with open('./yunfile_c.jpg', 'wb') as f:
                f.write(co)

            code = raw_input('input code:')

            self.getDownPage(opener, self.DOWN_URL + id + '/' + code + '.html')

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


    def getDownPage(self, opener, url):
        try:
            t = 30
            while t > 0:
                print t
                t=t-1
                time.sleep(1)


            print url
            c = opener.open(url, timeout=10)
            d = c.read()


            # 取POST地址
            r1 = re.compile('var saveCdnUrl = "";.*?"(.*?)"', re.S)
            p1 = re.search(r1, d)
            u1 = p1.group(1).strip()
            u1 = u1 + 'view?action=downfile&fid='

            # 取POST参数
            r2 = re.compile('var vericode = "(.*?)".*?form.fileId.value = "(.*?)".*?name="module" value="(.*?)".*?name="userId" value="(.*?)".*?name="vid1" value="(.*?)".*?name="md5" value="(.*?)"', re.S)
            p2 = re.findall(r2, d)

            formData = ''
            for i in p2:
                formData = {"module": i[2], "userId": i[3], "fileId": i[1], "vid": i[0], "vid1": i[4], "md5": i[5]}
                u1 = u1 + 'view?action=downfile&fid=' + i[3] + i[1] + i[0]

            print u1
            print formData
            data_encoded = urllib.urlencode(formData)
            r = opener.open(u1, data_encoded, timeout=10)
            d = r.read()

            if d.find('<html xmlns="http://www.w3.org/1999/xhtml">') != -1:
                print d
                print '下载文件失败'
            else:
                with open('./a.rar', 'wb') as f:
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

yunFile = YUNFILE()
yunFile.start()