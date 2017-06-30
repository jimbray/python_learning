#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jimbray on 2017/6/30
__author__ = 'jimbray'
import pandas as pd
import math


def convert():
    df = pd.read_excel('final.xlsx', sheetname=3)

    # print(df.dtypes)

    # for android_key in df['Key (Android)']:
    #     if android_key is not None:
    #         if isinstance(android_key, float):
    #             if math.isnan(android_key) is False:
    #                 print(android_key)
    #         elif isinstance(android_key, str):
    #             print(android_key)

    # print(type(df['Key (Android)']))
    print(type(df))
    # print(len(df))
    for index, row in df.iterrows():
        # print(index)
        # print(row.a)
        # Chinese / 'Key (Android)'
        text = row['Chinese']
        if isinstance(text, float):
            if math.isnan(text) is False:
                print(text)
            else:
                print(text)
        elif isinstance(text, str):
            print(text)





if __name__ == '__main__':
    convert()