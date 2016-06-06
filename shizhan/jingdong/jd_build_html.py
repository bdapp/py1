# -*- coding:utf-8 -*-
'''
根据统计结果生成统计图页面
'''

import json
import webbrowser
import os
import jd_csv_sort


class RESULT:

    def __init__(self):
        self.js = './html/data.js'     # 数据文件
        self.html = './html/index.html'   # 结果展示页
        self.ph = 20                   # 排行榜数量

        self.num = 0   # 品牌数量
        self.type = [] # 品牌名称
        self.pro = []   # 型号+评价
        self.sys = []   # 系统+评价
        self.vers = []  # 系统版本
        self.hots = {}  # 热门型号排行
        self.hsys = {}  # 热门系统排行

        self.allName=[]
        self.allCount=[]
        self.allSys = []

    # 生成data文件
    def write_file(self):
        try:
            with open(self.js, 'ab') as f:
                f.write('var num=' + str(self.num) + '\n')
                f.write('var type=' + json.dumps(self.type) + '\n')
                f.write('var pro=' + json.dumps(self.pro) + '\n')
                f.write('var sys=' + json.dumps(self.sys) + '\n')
                f.write('var vers=' + json.dumps(self.vers) + '\n')
                f.write('var hots=' + json.dumps(self.hots) + '\n')
                f.write('var hsys=' + json.dumps(self.hsys) + '\n')

        except Exception:
            print '写入data.js文件出错'


    # 排出最热门手机型号
    def getHotPros(self):

        hot_count = []
        hot_name = []

        for i in range(self.ph):
            id = self.allCount.index(max(self.allCount))
            #print self.allCount[id]
            #print self.allName[id]
            hot_count.append(self.allCount[id])
            hot_name.append(self.allName[id])
            self.allCount.remove(self.allCount[id])
            self.allName.remove(self.allName[id])

        self.hots['count'] = hot_count
        self.hots['name'] = hot_name


    # 排出热门品牌
    def getAllTips(self):
        allTips = []
        l = os.listdir('./file/')
        for i in l:
            add = jd_csv_sort.ADD('./file/' + i)
            # 获取品牌总评价数据
            all_tips = add.get_all_tips()
            allTips.append((i.replace('.csv', ''), all_tips))

        allTips.sort(lambda x, y: cmp(x[1], y[1]))
        allTips.reverse()

        return allTips


    # 排出热门系统版本
    def getAllSystem(self):

        hot_system = []
        for i in self.allSys:
            num = 0
            for j in self.allSys:
                if j.get('name') == i.get('name'):
                    num += j.get('value')

            hot_system.append((i.get('name'), num))
        #print hot_system

        hot_system.sort(lambda x, y: cmp(x[1], y[1]))
        hot_system.reverse()
        #print hot_system

        hot_result = []
        name = ''
        for i in hot_system:
            if i[0] != name :
                hot_result.append(i)
            name = i[0]

        s_name = []
        s_code = []
        for i in hot_result:
            s_name.append(i[0])
            s_code.append(i[1])
        self.hsys['sys_name'] = s_name
        self.hsys['sys_code'] = s_code






    # 从csv文件获取数据
    def build_html(self, file):

        add = jd_csv_sort.ADD('./file/' + file)
        # 获取热门排行数据
        rs = add.get_hots()

        # 获取系统排行数据
        system_line = add.get_version()


        # 热门数据分别写到两个list
        data = []
        categories = []
        # 系统排行写入两个list
        version = []
        ver_name = []

        try:
            for r in range(0, self.ph):
                #print rs[r][1]
                #print rs[r][0]
                data.append(rs[r][1])
                categories.append(rs[r][0])

                self.allName.append('[' + file.replace('.csv','') + '] ' + rs[r][0])
                self.allCount.append(rs[r][1])

        except Exception as e:
            print e

        try:
            for i in range(0, len(system_line)):
                mdic = {}
                mdic['name'] = system_line[i][0]
                mdic['value'] = system_line[i][1]
                version.append(mdic)
                ver_name.append(system_line[i][0])
                self.allSys.append(mdic)
        except Exception as e:
            print e


        # 写入json
        pro_list = {}
        pro_list["categories"] = categories
        pro_list["data"] = data
        self.pro.append(pro_list)

        self.sys.append(version)
        self.vers.append(ver_name)


    def start(self):

        self.type = self.getAllTips()
        self.num = len(self.type)

        for i in self.type:
            self.build_html(i[0]+'.csv')

        self.getHotPros()

        self.getAllSystem()
        self.write_file()


        # 打开浏览器
        webbrowser.open(self.html)


result = RESULT()
result.start()