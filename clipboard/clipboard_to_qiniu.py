#-*- coding: utf-8 -*-
__author__ = 'jimbray'


from PIL import ImageGrab, Image, ImageFile
import time
import qiniu
from qiniu import put_file
ImageFile.LOAD_TRUNCATED_IMAGES = True
import os

AK = '_HOWZNE1rkwMOq8wugUL4v4377bFmWIZ3qDxXogy'
SK = 'ba9S06bXl00DOtyS7AgYIGzgMqkzu8Fu8ztuqjDE'
bucket_name = "pic-bag"
buckey_url = {
    'pic-bag': 'http://7xv11f.com1.z0.glb.clouddn.com/',
}

def save_clipboard_image():
    im = ImageGrab.grabclipboard()
    if im is None:
        print('Error: No image data in clipboard')
        return None

    if isinstance(im, Image.Image):
        print im.format, im.size, im.mode
        width, height = im.size
        saved_path = "img_" + str(time.time()) + ".jpg"
        # im.resize((30, 30), Image.ANTIALIAS).load()
        im.save(saved_path)

        print saved_path
        return saved_path
    else:
        print 'the object in clipboard is not a image.'
        return None

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

def deleteLocalImage(path):
    if(os.path.isfile(path)):#文件存在
        os.remove(path)

if __name__ == '__main__':
    saved_path = save_clipboard_image()
    if saved_path == None:
        pass
    else:
        q = Qiniu(AK, SK)
        q.upload_file(bucket_name, saved_path, saved_path)
        deleteLocalImage(saved_path)