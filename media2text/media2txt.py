#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: media2txt.py 
@time: 2021/09/27
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

import speech_recognition as sr


def media2txt():
    file_name = 'test.wav'
    r = sr.Recognizer()

    # open the filewith sr.AudioFile(filename) as source:www.zpedu.com/

    # listen for the data (load audio to memory)

    with sr.AudioFile(file_name) as source:
        audio_data = r.record(source)

        # recognize (convert from speech to text)

        text = r.recognize_google(audio_data)

        print(text)


if __name__ == '__main__':
    media2txt()
