# import requests
# proxies = {'http': "socks5://127.0.0.1:1080"}
# print requests.get('http://www.google.com', proxies=proxies).text
#
#
#



import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",1080)
socket.socket =socks.socksocket
import urllib2
print urllib2.urlopen('http://page4.dix3.com/file/su2266/a5ba31f3/').read()