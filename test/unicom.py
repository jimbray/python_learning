#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: unicom.py 
@time: 2022/02/25
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""

import requests


def get_data():
    url = 'http://wap.10010.com/mobileService/query/queryRealTimeFeeInfoNew.htm?menuId=000200010001&mobile_c_from=null&Accesstype=null&activiChannel=wap'
    # post 请求 url
    headers = {
        "Cookie": "jsessionid=2jcligmgi6fh; piw=%7B%22login_name%22%3A%22185****8216%22%2C%22nickName%22%3A%22%E8%94%A1%E5%81%A5%E5%BD%AC%22%2C%22rme%22%3A%7B%22ac%22%3A%22%22%2C%22at%22%3A%22%22%2C%22pt%22%3A%2201%22%2C%22u%22%3A%2218503058216%22%7D%2C%22verifyState%22%3A%22%22%7D; userprocode=051; citycode=540; SHOP_PROV_CITY=; mallcity=51|510; mallflag=null; JUT=DaKbHjPXWKhHodTCtmtAEUIMueYtuRIUWij+uDXRXhlUiD74Laj8ng8zzUsoFVCS1hE6RDzlDhGzRww5eFF98+blDuzaB5v8ZwF9ga18dTqglNBvVoWOX6iT/K1qrTUfgKjJ1Phdoc1OWNyNKbY+CBg4+0R+KaEpKDWNS5f6w8XRuBqLcXk4ZHqc4w95r3PJ1TX5P/U5kBoQrFtlR3uMAQJf6MkEKL90ktIP/NLJhKTv7uYxDvr99XrA8bnZ9xbDosXZz4ZcV7qNqwpZLjD0CdgyGISP2wY3vbPlqCmaFKjzp3idxNUvAfcr2MR6N93gAgG+pxiJIzDTNvohVeP7qgq2HEsoTeXmYIEvwZWiTuCSEJ8jk4CiAP/BFA8ybIRCUR/fp77jn94ny1VzMob5PyEzaH3zlst4S6N7B9XhqQh7pNQmak/zfz09rYnDwJJO0ZK1e4Nx5nDjQaDoIs46Y2LPH8jib18BtwO56ccsF5LU5982RL5kZnuLavVWw5eZpvx771tx+mmMZB2Oanpti6BJMx9l84Y1t5P0s50+mic=3GLnxCi2yI/Om7uVhx/pUA==; WT=18503058216; acw_tc=d361481816457759537824139e2b1dac52a1495d1001bedbf7bf051dd6; mobileservice=1645775954.896.423.201991; SHAREJSESSIONID=840AC66F30BE14E59873EFDEC2E00CA1; logHostIP=""; _uop_id=a1a6824856330053361a65c7aea197cb; PROV_ID=051; CITY_ID=540; wapCookiesCityId=city_051; wapCookiesCityName=%E5%B9%BF%E4%B8%9C; _pk_ses.4.4857=1; _pk_id.4.4857=f53ca14e646f9977.1645775976.1.1645775986.1645775976."
    }
    response = requests.get(url, headers=headers)
    print(response.text)


if __name__ == '__main__':
    get_data()
