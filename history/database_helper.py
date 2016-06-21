# -*- coding: utf-8 -*-
__author__ = 'jimbray'

import sqlite3


class History():
    def __init__(self, title, target_url, header_img_url):
        create_history_db()
        self.title = title
        self.target_url = target_url
        self.header_img_url = header_img_url
        self.cursor, self.conn = conncet_db()

    def save_to_database(self):

        select_str = 'select * from history where title="%s"' % (self.title)

        cursor = self.conn.execute(select_str)
        if cursor.rowcount > 0:
            #更新
            update_str = 'update history set title="%s",target_url="%s", header_img_url="%s" where title="%s"' % (self.title, self.target_url, self.header_img_url, self.title)
            self.cursor.execute(update_str)
        else:
            insert_str = 'insert into history ("title", "target_url", "header_img_url") values ("%s", "%s", "%s")' % (self.title, self.target_url, self.header_img_url)
            #插入
            self.cursor.execute(insert_str)


        self.conn.commit()
        self.close_database()

    def close_database(self):
        close_db(self.cursor, self.conn)


class Carousel():

    def __init__(self, title, img_url):
        create_carousel_db()
        self.title = title
        self.img_url = img_url
        self.cursor, self.conn = conncet_db()

    def save_to_database(self):
        select_str = 'select * from carousel where title="%s"' % (self.title)

        cursor = self.conn.execute(select_str)
        if cursor.rowcount > 0:
            #更新
            update_str = 'update carousel set title="%s",img_url="%s" where title="%s"' % (self.title, self.img_url, self.title)
            self.cursor.execute(update_str)
        else:
            insert_str = 'insert into carousel ("title", "img_url") values ("%s", "%s")' % (self.title, self.img_url)
            #插入
            self.cursor.execute(insert_str)
        self.conn.commit()
        self.close_database()

    def close_database(self):
        close_db(self.cursor, self.conn)


def create_history_db():
    cursor, conn = conncet_db()
    cursor.execute('CREATE TABLE IF NOT EXISTS history  (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, target_url TEXT, header_img_url TEXT ,content_html TEXT)')
    close_db(cursor, conn)


def create_carousel_db():
    cursor, conn = conncet_db()
    cursor.execute('CREATE TABLE IF NOT EXISTS carousel  (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, img_url TEXT)')
    conn.commit()
    close_db(cursor, conn)


def get_all_history_today():
    cursor, conn = conncet_db()
    select_str = 'select title, target_url, header_img_url, content_html from history'
    cursor.execute(select_str)

    conn.commit()

    result_arr = []

    #处理第一条数据
    first_data = cursor.fetchone()
    dic = {'title': first_data[0], 'target_url': first_data[1], 'header_img_url': first_data[2], 'content_html': first_data[3]}
    result_arr.append(dic)

    if first_data is None:
        close_db(cursor, conn)
        return result_arr
    else:
        for row in cursor.fetchall():
            dic = {'title': row[0], 'target_url': row[1], 'header_img_url': row[2], 'content_html': row[3]}
            result_arr.append(dic)
        close_db(cursor, conn)
        return result_arr


def conncet_db():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    return cursor, conn


def close_db(cursor, conn):
    cursor.close()
    conn.close()




