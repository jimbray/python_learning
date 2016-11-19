# coding=utf-8
# -*- coding = utf-8 -*-

__author__ = 'jimbray'

from bs4 import BeautifulSoup
import sys, os,urllib2
reload(sys)
sys.setdefaultencoding('utf-8')

test_question_url = 'https://www.zhihu.com/question/26390056'


def get_content_html_soup(url):
        rep = urllib2.Request(url)
        content = urllib2.urlopen(rep).read()
        soup = BeautifulSoup(content, 'html.parser')
        return soup

def start_get_answer(url):
    soup = get_content_html_soup(url)
    title = soup.find('h2', class_='zm-item-title')
    print('start get question answers -> ' + title.span.text)
    answer_info_list = soup.find_all('div', class_='zm-item-answer')
    for answer in answer_info_list:
        author_link_tag = answer.find('a', class_='author-link')
        if author_link_tag is not None:
            author_name = author_link_tag.text
            if author_name is not None:
                author_name = u'匿名用户'
            print('正在 获取 用户 %s 的答案 ' % author_name)
            start_get_answer_content(answer.find('div', class_='zm-editable-content'), title.span.text + '\\' + author_name)


def start_get_answer_content(answer_content, folder_path):
    waiting_download_img_list = []
    if answer_content is not None:
        img_list = answer_content.find_all('img', class_='origin_image')
        if len(img_list) > 0:
            x = 0
            for img in img_list:
                if img is not None:
                    img_url = img['src']
                    if str(img_url).startswith('http'):
                        print(img_url)
                        dir = sys.path[0] + '\\' + folder_path
                        if not os.path.exists(dir):
                            os.makedirs(dir)
                        waiting_download_img_list.append(img_url)
                        fileName = os.path.join(dir, str(x)+'.jpg')
                        download_img(img_url, fileName)
                        x = x + 1

        else:
            print('This Answer Has no Pics. Ignore it.')


def download_img(img_url, dir_path):
    data = urllib2.urlopen(img_url).read()
    with open(dir_path, 'wb') as f:
        f.write(data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('params is not ready. Getting test url')
        start_get_answer(test_question_url)
    else:
        params = sys.argv[1]
        print('starting...url-> ' + params)
        if str(params).startswith('http'):
            start_get_answer(params)
        else:
            print('not working now')
            pass