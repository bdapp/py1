# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import os

class TAOBAO:
    def __init__(self):
        self.baseUrl = 'https://mm.taobao.com/json/request_top_list.htm?page='

    # 请求网页
    def getPage(self, pageIndex):
        url = self.baseUrl + str(pageIndex)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    # 创建目录
    def mkdir(self, path):
        path.strip()
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            return True
        else:
            return False

    # 获取MM的用户ID
    def getMmId(self, person):
        pattern = re.compile('user_id=(.*?)$', re.S)
        result = re.search(pattern, person)
        return result.group(1)

    # 获取相册ID
    def getAlbumId(self, albumUrl):
        pattern = re.compile('&album_id=(.*?)&album', re.S)
        result = re.search(pattern, albumUrl)
        return  result.group(1)

    # 获取相册图片
    def getAlbumContent(self, content, name, num):
        pattern = re.compile('"picUrl":"(.*?)_290', re.S)
        result = re.findall(pattern, content)
        flag = 1
        for x in result:
            #图片地址
            print 'http:' + x
            self.saveImage(name, str(num) + str(flag)+'.jpg', 'http:' + x)
            flag += 1

    # 获取相册集地址
    def getAlbumImg(self, albumUrl, userId, name, num):
        albumId = self.getAlbumId(albumUrl)
        url = 'https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id=' + userId + '&album_id='+ albumId+'&top_pic_id=0&cover=&page=1'
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)

        self.getAlbumContent(response.read(), name, num)


    # 获取相册列表
    def getAlbumList(self, url, userId, name):
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)

        pattern = re.compile('class="mm-fengmian clearfix">.*?class="mm-first" href="(.*?)"', re.S)
        result = re.findall(pattern, response.read())
        num = 0
        for item in result:
            self.getAlbumImg(item, userId, name, num)
            num += 1

    # 保存图片
    def saveMmPic(self, name, person):
        id = self.getMmId(person)
        albumUrl = 'https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20=' + id
        self.getAlbumList(albumUrl, id, name)

    # 保存图片
    def saveImage(self, name, picName, url):
        folder = '/home/ubt/tb/' + name + '/'
        self.mkdir(folder)

        u = urllib.urlopen(url)
        data = u.read()
        f = open(folder + picName, 'wb')
        f.write(data)
        f.close()

    # 保存头像
    def saveHeadIcon(self, name, url):
        folder = '/home/ubt/tb/' + name
        files = folder + '/' + name + '.jpg'
        self.mkdir(folder)
        self.saveImage(files, url)

    # 获取整页内容
    def getContent(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('class="lady-avatar".*?"(.*?)".*?class="lady-name" href="(.*?)".*?target="_blank">(.*?)</a>', re.S)
        items = re.findall(pattern, page)

        for item in items:
            #print item[0] + item[1] + item[2]
            imgUrl = 'https:' + item[0]
            personUrl = 'https:' + item[1]
            name = item[2]

            self.saveImage(name, name+'.jpg', imgUrl)
            #self.saveHeadIcon(name, imgUrl)
            self.saveMmPic(name, personUrl)

tb = TAOBAO()
tb.getContent(5)