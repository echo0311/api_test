# -*- coding: utf-8 -*-
import MySQLdb.cursors
import json

class OperationMysql:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='db_test',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor  # 可以拿到表头
        )
        self.cur = self.conn.cursor()

    def search(self,sql):
        self.cur.execute(sql)
        result =  self.cur.fetchone()
        result = json.dumps(result)
        return result


if __name__ == '__main__':
    oper_mysql = OperationMysql()
    result = oper_mysql.search("select * from tb_user where name = 'echo20110'")
    print(result)