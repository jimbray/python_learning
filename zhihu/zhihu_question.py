# -*- coding=utf-8 -*-
__author__ = 'jimbray'

from bs4 import BeautifulSoup
import sys, urllib2

test_url = 'https://www.zhihu.com/question/25339255'

def get_html(url):
    req = urllib2.Request(url)
    soup = BeautifulSoup(urllib2.urlopen(req), 'html.parser')
    return soup


if __name__ == '__main__':
    html_soup = get_html(test_url)
    title = html_soup.find('h2', class_='zm-item-title').span.string
    print(u'开始查看问题' + title)
    answer_num = html_soup.find('h3', id='zh-question-answer-num').string
    print(answer_num)
    answer_div_list_tag = html_soup.select('div .zm-item-answer')
    if answer_div_list_tag is not None:
        print(u'能看到的回答有 ' + str(len(answer_div_list_tag)) + u'个')
        answer_count = 0;
        for answer_div_tag in answer_div_list_tag:
            answer_count+=1
            print(u'正在获取第' + str(answer_count) + u'个用户的回答')
            author_link_tag = answer_div_tag.find('a', class_='author-link')
            if author_link_tag is not None:
                print(u'这个用户名字叫做 -> ' + author_link_tag.string)
            else:
                niming_tag = answer_div_tag.find('div', class_='zm-item-answer-author-info')
                if niming_tag is not None:
                    print(u'这个用户名字叫做 -> ' + niming_tag.find('span', class_='name').string)
                else:
                    print(u'这个用户没名字？！')
