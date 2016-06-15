# -*- coding:utf-8 -*-

# 通过代理刷点击量
import urllib2
import random
import time
from socket import error as SocketError
import getProxyList


class REFRESH:
    def __init__(self):

        self.baseUrl = 'http://www.cashlai.com'

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


    # 打开页面
    def refreshPage(self, ip):
        try:
            print 'ip ------ ' + ip
            user_agent = random.choice(self.user_agents)
            proxy = urllib2.ProxyHandler({'http':''+ ip +''})
            opener = urllib2.build_opener(proxy)
            opener.addheaders = [('User-Agent',user_agent)]
            opener.open(self.baseUrl, timeout=10)

        except urllib2.HTTPError, e:
            print 'HTTPError: ' + str(e.code)
            return False
        except urllib2.URLError, e:
            print 'URLError: ' + str(e.reason)
            return  False
        except SocketError as e:
            print 'SocketError: ' + str(e.errno)
            return  False

        return True

    # 获取proxy的ip地址组
    def getProxyIpList(self):
        proxy = getProxyList.PROXY()
        list = proxy.getProxy()
        print 'ipList length: ' + str(len(list))

        return list

    # 开始循环执行
    def start(self, ipList):
        count  = 1
        for ip in ipList:
            startTime = time.time()
            randomTime = random.uniform(1, 10)

            if self.refreshPage(ip):
                time.sleep(randomTime)
            else:
                randomTime = 0

            costTime = time.time() - startTime - randomTime
            print '第'+ str(count) +'次耗时: ' + str(costTime)

            # 耗时结果写入文件
            if costTime<5 :
                with open('./time.txt', 'ab') as f:
                    localTime = time.asctime(time.localtime(time.time()))
                    f.write(localTime + '\t\t耗时: ' + str(costTime))
                    f.write('\t\tip ------ ' + ip + '\n')

            count += 1



    def open(self):
        ipList = self.getProxyIpList()
        if len(ipList)>0 :
            self.start(ipList)
        else:
            print '找不到代理地址'


refresh = REFRESH()
refresh.open()

