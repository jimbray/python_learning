#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:jimbray 
@file: hf_weather.py 
@time: 2022/03/08
@contact: jimbra16@gmail.com
@site: http://jimbray.xyz
@Descriptions: 
"""
import requests


def get_weather():
    base_url = "https://devapi.qweather.com/v7/indices/1d"
    # 深圳ID，通过https://geoapi.qweather.com/v2/city/top?number=10&range=cn&key=c1599639af99455fa82488aac62c087d 获取
    location = "101280601"
    # 天气指数类型：https://dev.qweather.com/docs/resource/indices-info/
    type = "1,2,3,5,8,10,13,14,15,16"

    # get url 操作
    url = base_url + "?location=" + location + "&type=" + type + "&key=c1599639af99455fa82488aac62c087d"
    # print(url)
    # 获取数据
    response = requests.get(url)
    # 获取数据
    data = response.json()
    daily_data = data['daily']
    date = daily_data[0]['date']
    result_str = "日期：" + date + "\n"
    simple_result_str = "日期：" + date + "\n"
    for i in range(0, len(daily_data)):
        result_str = result_str + daily_data[i]['name'] + "：" + str(daily_data[i]['category']) + "\n" + daily_data[i][
            'text'] + "\n"

    for i in range(0, len(daily_data)):
        simple_result_str = simple_result_str + daily_data[i]['name'] + "：" + str(daily_data[i]['category']) + "\n"

    return result_str, simple_result_str


def sendWeather(result, simple_result):
    base_url = "https://cloud-dev-4d6931-1252086379.ap-shanghai.app.tcloudbase.com/push_all"
    result_url = base_url + "?content=" + result
    simple_result_url = base_url + "?content=" + simple_result
    requests.get(result_url)
    requests.get(simple_result_url)


if __name__ == '__main__':
    IHMWLMSEAL-eyJsaWNlbnNlSWQiOiJJSE1XTE1TRUFMIiwibGljZW5zZWVOYW1lIjoidHJlbmRzIHJhYmJpcyIsImFzc2lnbmVlTmFtZSI6IiIsImFzc2lnbmVlRW1haWwiOiIiLCJsaWNlbnNlUmVzdHJpY3Rpb24iOiIiLCJjaGVja0NvbmN1cnJlbnRVc2UiOmZhbHNlLCJwcm9kdWN0cyI6W3siY29kZSI6IlBDIiwiZmFsbGJhY2tEYXRlIjoiMjAyMy0wMi0wOCIsInBhaWRVcFRvIjoiMjAyMy0wMi0wOCIsImV4dGVuZGVkIjpmYWxzZX0seyJjb2RlIjoiUFBDIiwiZmFsbGJhY2tEYXRlIjoiMjAyMy0wMi0wOCIsInBhaWRVcFRvIjoiMjAyMy0wMi0wOCIsImV4dGVuZGVkIjp0cnVlfSx7ImNvZGUiOiJQV1MiLCJmYWxsYmFja0RhdGUiOiIyMDIzLTAyLTA4IiwicGFpZFVwVG8iOiIyMDIzLTAyLTA4IiwiZXh0ZW5kZWQiOnRydWV9LHsiY29kZSI6IlBTSSIsImZhbGxiYWNrRGF0ZSI6IjIwMjMtMDItMDgiLCJwYWlkVXBUbyI6IjIwMjMtMDItMDgiLCJleHRlbmRlZCI6dHJ1ZX0seyJjb2RlIjoiUENXTVAiLCJmYWxsYmFja0RhdGUiOiIyMDIzLTAyLTA4IiwicGFpZFVwVG8iOiIyMDIzLTAyLTA4IiwiZXh0ZW5kZWQiOnRydWV9XSwibWV0YWRhdGEiOiIwMTIwMjIwMjA4UFNBTjAwMDAwNSIsImhhc2giOiJUUklBTDozMzQzMzQ3ODMiLCJncmFjZVBlcmlvZERheXMiOjcsImF1dG9Qcm9sb25nYXRlZCI6ZmFsc2UsImlzQXV0b1Byb2xvbmdhdGVkIjpmYWxzZX0=-TT/mvlYqIE07j8qgnrhSSVpMtD4buKsRuntPuB17Zb8KodU2SUcb8byLpLG1pU+xEIIyG3Scu/ypjXmQ9w4iyvOT+NYGmeeHFMHnknQVEhhUvDZjTMNXPct03KeHcjxJX8jMSsuRkTooePx1beXjHTuxcyiO8qJcNOOl/97pT45kGTqSJohat0Xe7oiwrE6u3JZhfSdmYV9iJxz6XGNeoPMPnXbH17yoP75eXUqQJzUGxqdeHyKVHSUUJTGfO3IHgjN9y2TwYET5oFjRy1qSMRf4vXpPCK7tnfqhCGISQiDCm+ETB133CcmArxlRVlKdbAIM/7W++eOn5AfW/CNvgg==-MIIETDCCAjSgAwIBAgIBDTANBgkqhkiG9w0BAQsFADAYMRYwFAYDVQQDDA1KZXRQcm9maWxlIENBMB4XDTIwMTAxOTA5MDU1M1oXDTIyMTAyMTA5MDU1M1owHzEdMBsGA1UEAwwUcHJvZDJ5LWZyb20tMjAyMDEwMTkwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCUlaUFc1wf+CfY9wzFWEL2euKQ5nswqb57V8QZG7d7RoR6rwYUIXseTOAFq210oMEe++LCjzKDuqwDfsyhgDNTgZBPAaC4vUU2oy+XR+Fq8nBixWIsH668HeOnRK6RRhsr0rJzRB95aZ3EAPzBuQ2qPaNGm17pAX0Rd6MPRgjp75IWwI9eA6aMEdPQEVN7uyOtM5zSsjoj79Lbu1fjShOnQZuJcsV8tqnayeFkNzv2LTOlofU/Tbx502Ro073gGjoeRzNvrynAP03pL486P3KCAyiNPhDs2z8/COMrxRlZW5mfzo0xsK0dQGNH3UoG/9RVwHG4eS8LFpMTR9oetHZBAgMBAAGjgZkwgZYwCQYDVR0TBAIwADAdBgNVHQ4EFgQUJNoRIpb1hUHAk0foMSNM9MCEAv8wSAYDVR0jBEEwP4AUo562SGdCEjZBvW3gubSgUouX8bOhHKQaMBgxFjAUBgNVBAMMDUpldFByb2ZpbGUgQ0GCCQDSbLGDsoN54TATBgNVHSUEDDAKBggrBgEFBQcDATALBgNVHQ8EBAMCBaAwDQYJKoZIhvcNAQELBQADggIBAB2J1ysRudbkqmkUFK8xqhiZaYPd30TlmCmSAaGJ0eBpvkVeqA2jGYhAQRqFiAlFC63JKvWvRZO1iRuWCEfUMkdqQ9VQPXziE/BlsOIgrL6RlJfuFcEZ8TK3syIfIGQZNCxYhLLUuet2HE6LJYPQ5c0jH4kDooRpcVZ4rBxNwddpctUO2te9UU5/FjhioZQsPvd92qOTsV+8Cyl2fvNhNKD1Uu9ff5AkVIQn4JU23ozdB/R5oUlebwaTE6WZNBs+TA/qPj+5/we9NH71WRB0hqUoLI2AKKyiPw++FtN4Su1vsdDlrAzDj9ILjpjJKA1ImuVcG329/WTYIKysZ1CWK3zATg9BeCUPAV1pQy8ToXOq+RSYen6winZ2OO93eyHv2Iw5kbn1dqfBw1BuTE29V2FJKicJSu8iEOpfoafwJISXmz1wnnWL3V/0NxTulfWsXugOoLfv0ZIBP1xH9kmf22jjQ2JiHhQZP7ZDsreRrOeIQ/c4yR8IQvMLfC0WKQqrHu5ZzXTH4NO3CwGWSlTY74kE91zXB5mwWAx1jig+UXYc2w4RkVhy0//lOmVya/PEepuuTTI4+UJwC7qbVlh5zfhj8oTNUXgN0AOc+Q0/WFPl1aw5VV/VrO8FCoB15lFVlpKaQ1Yh+DVU8ke+rt9Th0BCHXe0uZOEmH0nOnH/0onD
