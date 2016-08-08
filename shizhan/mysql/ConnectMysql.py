#! /usr/bin/python
# -*- coding:utf-8 -*-

import MySQLdb

class SQLDB:

    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'hszc2014'
        self.db = 'py_test'
        self.port = 3306
        self.charset = 'utf8'

    # 连接数据库
    def connectDB(self):

        try:
            self.conn = MySQLdb.connect(host=self.host, user=self.user, passwd=self.password,
                                   db=self.db, port=self.port, charset=self.charset)

            self.cursor = self.conn.cursor()

        except MySQLdb.Error, e:
            print 'mysql connect error!'
            print e


    # 查询数据库
    def selectDB(self, sql):
        try:

            self.cursor.execute(sql);
            results = self.cursor.fetchall()

            for row in results:
                print row[0]

        except MySQLdb.Error, e:
            print 'mysql select error!'
            print e


    # 插入数据库
    def insertDB(self, sql):
        try:

            self.cursor.execute(sql)
            #提交
            self.conn.commit()

        except MySQLdb.Error, e:
            print 'mysql insert error!'
            print e
            #回滚
            self.conn.rollback()


    # 修改数据
    def updateDB(self, sql):
        try:
            self.cursor.execute(sql)
            # 提交
            self.conn.commit()

        except MySQLdb.Error, e:
            print 'mysql insert error!'
            print e
            # 回滚
            self.conn.rollback()


    # 关闭数据库
    def closeDB(self):
        self.cursor.close()
        self.conn.close()



# ddb = SQLDB()
# ddb.connectDB()
# ddb.selectDB('select * from info')
# ddb.insertDB("insert into `info` (`id`, `name`, `desc`, `sex`, `address`) values (9, 'naa', 'deeee', '2', 'iii');")
# ddb.updateDB("update `info` set `name` = 'rrr' where `id` = 1;")
# ddb.closeDB()