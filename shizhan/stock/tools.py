#-*- coding:utf-8 -*-
import re

class Tool:
        #去除img标签
        removeImg = re.compile('<img.*?>')
        #删除超链接
        removeHref = re.compile('<a.*?>|</a>')
        #把换行符换成\n
        # removeBR = re.compile('<br>|<br/>|<br />|<tr.*?>|</tr>|<div .*?>|</div>')
        #制表符TD换成\t
        removeTD = re.compile('<td.*?>|</td>')
        #段落开头替换p
        removeP = re.compile('<p.*?>|</p>')
        #删除其它标签
        removeOther = re.compile('<.*?>')
        #删除多余空格
        removeBlank = re.compile('   ')
        #替换H字体
        removeH = re.compile('<h.*?>|<H.*?>')
        # 替换"号
        removeY = re.compile('"')
        #替换html代码
        removeHtml = re.compile('')


        def replace(self, x):
                x = re.sub(self.removeImg, "", x)
                x = re.sub(self.removeHref, "", x)
                # x = re.sub(self.removeBR, "", x)
                x = re.sub(self.removeTD, "", x)
                x = re.sub(self.removeP, "", x)
                x = re.sub(self.removeOther, "", x)
                x = re.sub(self.removeBlank, "", x)
                x = re.sub(self.removeH, "", x)
                x = re.sub(self.removeY, "", x)
                return x.strip()