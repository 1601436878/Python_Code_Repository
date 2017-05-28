# -*- coding: utf-8 -*-
import MySQLdb
import datetime


class Db:
    def Insert(self, type, row, column, isWin):
        conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="11111111", db="five_db", charset="utf8")
        cursor = conn.cursor()
        sql = "insert into operation(`type`,row,`column`,is_win,created) values(%s,%s,%s,%s,%s)"
        # 获得当前时间
        now = datetime.datetime.now()
        # 转换为指定的格式:
        created = now.strftime("%Y-%m-%d %H:%M:%S")
        param = (type, row, column, isWin, created)
        cursor.execute(sql, param)
        cursor.close()
