# -*- coding: utf-8 -*-

__author__ = 'jimbray'

import os,datetime

def get_release_time():
    today = datetime.datetime.now()
    return today.strftime('%Y-%m-%d-%H-%M-%S')

def copy_apk_to_release_share_folder():
    dir_name = 'C:\\Users\\dell\\.jenkins\\workspace\\Poof-Android\\app\\build\\outputs\\apk\\'
    target_dir_name = 'H:\\Poof_for_Android_Release\\'
    for file in os.listdir(dir_name):
        source_file_full_name = os.path.join(dir_name, file)
        target_file_full_name = os.path.join(target_dir_name, file)
        target_file_full_name = target_file_full_name.replace('Poof-', 'Poof-' + get_release_time() + '-')
        if os.path.isfile(source_file_full_name):
            os.system('copy %s %s' % (source_file_full_name, target_file_full_name))


if __name__ == '__main__':
    copy_apk_to_release_share_folder()