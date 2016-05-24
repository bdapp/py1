# -*- coding:utf-8 -*-

# 百度贴吧
import urllib
import urllib2
import re

class Tool:
        #去除img标签
        removeImg = re.compile('<img.*?>')
        #删除超链接
        removeHref = re.compile('<a.*?>|</a>')
        #把换行符换成\n
        removeBR = re.compile('<br>|<br />|<tr.*?>|</tr>|<div .*?>|</div>')
        #制表符TD换成\t
        removeTD = re.compile('<td.*?>|</td>')
        #段落开头替换p
        removeP = re.compile('<p.*?>|</p>')
        #删除其它标签
        removeOther = re.compile('<.*?>')

        def replace(self, x):
                #x = re.sub(self.removeImg, "", x)
                x = re.sub(self.removeHref, "", x)
                x = re.sub(self.removeBR, "\n", x)
                x = re.sub(self.removeTD, "\t", x)
                x = re.sub(self.removeP, "\n  ", x)
                x = re.sub(self.removeP, "", x)
                return x.strip()

class BDTB:
        #初始化 BDTB类
        def __init__(self, baseUrl, seeLZ):
            self.baseUrl = baseUrl
            self.seeLZ = '?see_lz=' + str(seeLZ)
            self.tool = Tool()

        # 根据页码获取内容
        def getPage(self, pageNum):
            try:
                url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)
                return response.read()
            except urllib2.HTTPError, e:
                print e.code
                print e.reason

        # 获取标题
        def getTitle(self):
                pattern = re.compile('<h1 class="core_title_txt  ".*?>(.*?)</h1>', re.S)
                result = re.search(pattern, allContent)
                if result:
                    return result.group(1).strip()
                else:
                    return None

        # 获取正文
        def getContent(self):
            pattern = re.compile('class="d_post_content j_d_post_content  clearfix">(.*?)</div>', re.S)
            result = re.findall(pattern, allContent)
            for x in result:
                print "=================\n" + self.tool.replace(x)

        # <ul class="p_tail"><li><span>5楼</span></li><li><span>2016-05-08 18:59</span></li></ul>
        # 获取楼层
        def getFloor(self):
            pattern = re.compile('&quot;date&quot;:&quot;(.*?)&quot;.*?<a data-field.*?>(.*?)</a>', re.S)
            #pattern = re.compile('', re.S)
            items = re.findall(pattern, allContent)
            f = 1
            for x in items:
                print str(f) + '楼 \t' + x[0] + '\t' + x[1]
                f += 1



baseUrl = "http://tieba.baidu.com/p/4534108543"
bdtb = BDTB(baseUrl, 0)
allContent = bdtb.getPage(1)
#bdtb.getTitle()
#bdtb.getContent()
bdtb.getFloor()

