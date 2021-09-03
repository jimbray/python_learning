# 一些注意事项
    # 模块功能：提交数据给 Notion 添加记录……介绍帖已经写了，都差不多
    # 没安装过 requests 模块可以在 Python 终端输入 pip install requests 安装

    # idea 来源链接 https://sspai.com/post/66658

    # 可以尝试 json 在线解析网站，把输出内容复制进去即可（如下）
    # https://www.bejson.com/explore/index_new/

    # 注：开代理可能会因网络问题导致运行失败

    # 如果有问题可以简单询问作者，为什么要简单询问不能困难询问，因为作者也是半吊子
    # 少数派@飘扬：https://sspai.com/u/czyfcdwn/updates
    # QQ：1811753618

# 使用教程
    # 和 GET 那部分的代码一样，据情况修改前 4 项内容
    # 但是 POST 需要编写消息体，需要往下滑到 body 部分
    # 这里已经给出了示例，可以直接运行，运行成功后尝试复现慢慢熟悉即可

# 导入模块，不要碰，其中 re 是用于筛选 ID 的正则表达式模块
import requests; import re

# 父级链接（两端添加引号）
URL = 'bbae1170-539f-40fe-a03d-0d07eb5a8b60'

# 选择操作类型
    # 0 = 查询数据库
    # 1 = 创建数据库
    # 2 = 创建页面
    # 3 = 添加块（Block）
TypeList = 2

# 选择父页面类型
    # 0 = 数据库
    # 1 = 页面
PartentList = 0

# 机器人令牌, 复制对应的机器人令牌粘贴过来就好，注意要带引号
Token = "secret_UhwMkAjlKp5ystNAqMJrjPqvVgnx5zO1w7Rvk53j0ya"

# 使用正则表达式从父级链接中筛选第一个页面 ID
    # 匹配逻辑如下
        # 如果是链接
            # https://www.notion.so/555-5-4-5-d922318b3c1069pb910a09864c927087
            # 删除字符
            # https:d922318b3c1069pb910a09864c927087
            # 匹配
            # d922318b3c1069pb910a09864c927087
        # 如果是有连字符的 ID
            # 0e7f0915-b979-423f-8762-29e4r450324f
            # 删除连字符
            # 0e7f0915b979423f876229e4r450324f
ID = (re.search('([0-9a-zA-Z]{32})', re.sub(r'-', '', re.sub(r'\/.*-', '', format(URL))))).group(1)

# 测试类型组，不用碰
TypeAPI_URL = ["databases/" + ID + '/query', 'databases', "pages", 'blocks/' + ID + '/children']
TypeParent = ["database_id", "page_id"]

# 制作消息体
body = {
    "parent": {
        "type": TypeParent[PartentList], 
        TypeParent[PartentList]: ID
        },
    "properties": {
        "数量":{
            "select":{
                "name":"1"
            }},
        "类别":{
            "select":{
                "name":"咖啡因片"
            }},
        "单份含量":{
            "select":{
                "name":"200mg"
            }},
        "服药日期":{
            "date":{
                "start":"2021-08-03T05:32:00.000+08:00"
            }},
        # 可以在这里留下你的 ID 哦
        "测试员":{
            "rich_text":[{
                    "text":{
                        "content":"默认测试人",
            },}]}}
    }

# 待使用的 API 链接
API_URL = 'https://api.notion.com/v1/' + TypeAPI_URL[TypeList]

# 访问数值
NotionData = requests.request(
    "POST",
    # API 链接
    API_URL,
    # 读取消息体
    json = body,
    headers={
        # 设置机器人令牌
        "Authorization": Token, 
        # 设置 Notion 版本
        "Notion-Version": "2021-05-13"
        },
    )

# 先行定义函数，避免后期拉取数据转化为字典时报错
false = False
true = True
null = None

# 将返回内容转换为字典
NotionDict = eval(NotionData.text)

# 数据类型对照表
messageList = {
    "database": "数据库", 
    "page": "页面", 
    "database_id": "数据库", 
    "page_id": "页面", 
    # 感觉 block 模块没用，封存
    #"block": "块", 
}

# 报错消息对照表
errorMessageList = {
    404: "未找到页面，请检查链接或测试类型是否正确", 
    401: "机器人令牌错误", 
    400: "未提供标题 (Title) 或父页面类型选择错误或消息体编辑错误",
    # 如果有新的报错代码可以发给作者让他更新
    # 少数派@飘扬：https://sspai.com/u/czyfcdwn/updates
    # QQ：1811753618
}

# 输出全部拉取内容
print('\n\n' + NotionData.text + "\n\n完整数据如上，运行状态如下\n")

# 输出读取到的数据类型及父级界面ID
if NotionDict['object'] == 'page':
    print(
        "运行结果：操作成功, 已成功添加新页面\n" + \
        "直达链接：" + NotionDict.get("url") + '\n'
    )
# 输出已知报错
elif NotionDict['status'] in list(errorMessageList):
    print(
        '错误代码：' + str(NotionDict['status']) + '\n'\
        '操作失败：' + errorMessageList[NotionDict['status']] + '\n'\
        '报错原文：' + NotionDict['message'] + '\n'
    )
# 输出未知报错
else:
    print(
        '错误代码：' + str(NotionDict['status']) + '\n'\
        '未知错误：' + NotionDict['message']
    )
















































# 结尾另：
# 实现这样的 Python 内容真的不难
# 在写这两份代码之前，作者唯一的 Python 成就是零基础通过 7h 的学习过了国二，拿了个良好
# 里面除正则表达式有基础外，request 模块甚至 if 语句都是百度来的
# 非常推荐各位学学 Python 和正则表达式，尤其是正则表达式，确实相当方便~
# 我在这里透底不会有人看到吧 233333
# 如果你看到了，就在测试页面添加一条服药年份为 2333 年的记录吧 hhhhhhh