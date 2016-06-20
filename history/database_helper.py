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
        self.cursor.execute('insert into history (title, target_url, header_img_url) values (self.title, self.target_url, self.header_img_url)')
        close_db()


    def close_database(self):
        close_db(self.cursor, self.conn)

def create_history_db():
    cursor, conn = conncet_db()
    cursor.execute('CREATE TABLE history IF NOT EXISTS (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, target_url TEXT, header_img_url TEXT ,content_html TEXT)')
    close_db(cursor, conn)


def conncet_db():
    conn = sqlite3.connect('history.db')
    cursor = conn.cursor()
    return cursor, conn


def close_db(cursor, conn):
    cursor.close()
    conn.commit()
    conn.close()




