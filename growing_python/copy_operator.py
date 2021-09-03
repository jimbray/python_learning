#!/usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author:jimbray 
@file: copy_operator.py 
@time: 2019/03/09
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

person = ["name", ["saving", 100]]
hubby = person[:]
print(hubby)

wifey = list(person)
print(wifey)

for x in person, hubby, wifey:
    print(id(x))

hubby[0] = 'Joe'
wifey[0] = 'Jane'
print(hubby + wifey)
# hubby[]