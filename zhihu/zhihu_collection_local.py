# - * - coding: utf-8 -*-

__author__ = 'jimbray'

import urllib2
from bs4 import BeautifulSoup
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')


website = 'https://www.zhihu.com'
base_url = 'https://www.zhihu.com/collection/69135664?page='


class QuestionInfo():


    def __init__(self, title, link):
        self.title = title
        self.link = website + str(link)


    def get_title(self):
        return self.title


    def get_link(self):
        return self.link


class ZhihuCollectionSpider():

    def __init__(self, pageStart, pageEnd, url):
        self.url = url
        self.pageStart = int(pageStart)
        self.pageEnd = int(pageEnd) + 1

    def start(self):
        for page in range(self.pageStart, self.pageEnd):
            url = self.url + str(page)
            content_soup = self.get_content_html_soup(url)

            questionInfoList = []

            questionList = content_soup.find_all('div', class_='zm-item')
            for question in questionList:
                question_head = question.find('h2', class_='zm-item-title')
                title = question_head.a.string
                link = question_head.a['href']
                questionInfoList.append(QuestionInfo(title, link))

            for question in questionInfoList:
                # print('%s (%s)' % (question.get_title(), question.get_link()))
                print('开始获取问题->' + question.get_title())
                self.start_get_question(question.get_link(), question.get_title())


    def get_content_html_soup(self, url):
        rep = urllib2.Request(url)
        content = urllib2.urlopen(rep).read()
        soup = BeautifulSoup(content, 'html.parser')
        return soup


    def start_get_question(self, url, title):
        answers_soup = self.get_content_html_soup(url)
        answer_info_list = answers_soup.find_all('div', class_='zm-item-answer')
        for answer in answer_info_list:
            author_link_tag = answer.find('a', class_='author-link')
            if author_link_tag is not None:
                author_name = author_link_tag.text
                if author_name is not None:
                    print('正在 获取 用户 %s 的答案 ' % author_name)
                    self.start_get_answer(answer.find('div', class_='zm-editable-content'), title + '\\' + author_name)


    def start_get_answer(self, answer_content, folder_path):
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
                            self.download_img(img_url, fileName)
                            x = x + 1

            else:
                print('This Answer Has no Pics. Ignore it.')


    def download_img(self, img_url, dir_path):
        data = urllib2.urlopen(img_url).read()
        with open(dir_path, 'wb') as f:
            f.write(data)


    def start_downloading_img(self, waiting_download_img_list):
        if waiting_download_img_list is not None:
            pass


if __name__ == '__main__':
    page, limit, paramsNum = 1, 0, len(sys.argv)
    if paramsNum >= 3:
        page, pageEnd = sys.argv[1], sys.argv[2]
    elif paramsNum == 2:
        page = sys.argv[1]
        pageEnd = page
    else:
        page, pageEnd = 1, 1

    spider = ZhihuCollectionSpider(page, pageEnd, base_url)
    spider.start()


