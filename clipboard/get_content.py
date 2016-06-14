# -*- coding:utf-8 -*-
__author__ = 'jimbray'

from PIL import ImageGrab
import time
from qiniu import Auth, put_file, etag
import  qiniu.config
import os

AK = '_HOWZNE1rkwMOq8wugUL4v4377bFmWIZ3qDxXogy'
SK = 'ba9S06bXl00DOtyS7AgYIGzgMqkzu8Fu8ztuqjDE'
bucket_name = "pic-bag"
buckey_url = {
    'pic-bag': 'http://7xv11f.com1.z0.glb.clouddn.com/',
}

def save_clipboard_image():
    pic = ImageGrab.grab()
    saved_path = "img_" + str(time.time()) + ".jpg";
    pic.save(saved_path)
    return saved_path

class Qiniu():
    def __init__(self, ak, sk):
        self.access_key = ak
        self.secret_key = sk
        self._q = qiniu.Auth(self.access_key, self.secret_key)

    def upload_file(self, bucket_name, key, file_path):
        #生成上传 Token，可以指定过期时间等
        token = self._q.upload_token(bucket_name, key, 3600)
        ret, info = put_file(token, key, file_path)
        print(info)
        pic_url = self.get_pic_url(bucket_name, file_path)
        add_to_clipboard(pic_url, file_path)

    def get_pic_url(self, bucket_name, file_path):
        result = buckey_url[bucket_name] + file_path
        return result


def add_to_clipboard(pic_url, file_name):
    txt = '![' + file_name +']('+ pic_url +')'
    print(txt)
    command = 'echo ' + txt.strip() + '| clip'
    os.system(command)

if __name__ == '__main__':
    saved_path = save_clipboard_image()
    q = Qiniu(AK, SK)
    q.upload_file(bucket_name, saved_path, saved_path)
