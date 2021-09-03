# 一些注意事项
    # 模块功能：自动筛选 ID，可轻松切换查询数据类型，直接输出拉取内容与父级界面ID，通俗易懂的报错提示
    # 没安装过 requests 模块可以在 Python 终端输入 pip install requests 安装

    # idea 来源链接 https://sspai.com/post/66658

    # 可以尝试 json 在线解析网站，把输出内容复制进去即可（如下）
    # https://www.bejson.com/explore/index_new/

    # 注：开代理可能会因网络问题导致运行失败

    # 如果有问题可以简单询问作者，为什么要简单询问不能困难询问，因为作者也是半吊子
    # 少数派@飘扬：https://sspai.com/u/czyfcdwn/updates
    # QQ：1811753618

# 使用教程
    # 把待检测页面链接复制过来
    # 选择类型
    # 注册机器人并把机器人邀请到你的 notion 页面里
    # 填写机器人令牌
    # 运行~
    # 查看 or 复制输出结果

# 导入模块，不要碰，其中 re 是用于筛选 ID 的正则表达式模块
import requests; import re

# 待检测链接（两端要添加单引号/双引号）
URL = 'https://www.notion.so/4ec8487f82694f2da3daa8a95bf4f2bf'

# 选择待测试链接类型（0 = 数据库，1 = 页面, 2 = 块对象(块对象已封存需自行解锁), 用户对象没写）
TypeList = 1

# 机器人令牌, 复制对应的机器人令牌粘贴过来就好，注意要带引号
Token = "secret_UhwMkAjlKp5ystNAqMJrjPqvVgnx5zO1w7Rvk53j0ya"

###########################################################
# 以下代码一般不需要进行自定义或修改
###########################################################

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

# 调试输出
# print('匹配到的 ID 为：' + ID)

# 类型数组，不用碰，用于拼接在 API 链接后面
Type = [
    # 0 = 数据库类型
    "databases/" + ID, 
    # 1 = 页面类型    
    "pages/" + ID, 
    # 2 = 块类型
    # 感觉 block 模块没用，封存
    # "blocks/" + ID + "/children"
    ]

# 待查询的 API 链接
API_URL = 'https://api.notion.com/v1/' + Type[TypeList]

# 调试输出
# print('\n\n待搜链接为\n\n', API_URL, '\n\n')

# 通过 Notion API 拉取数据
NotionData = requests.request(
    "GET",
    API_URL,
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
    # "block": "块", 
    # "list": "列表（内容一般是块 block）",
}

# 报错消息对照表
errorMessageList = {
    404: "未找到该页面，请检查链接或测试类型是否正确", 
    401: "机器人令牌错误", 
    400: "验证失败，请检查所选类型或待测 ID 是否正确"
    # 如果有新的报错代码可以发给作者让他更新
    # 少数派@飘扬：https://sspai.com/u/czyfcdwn/updates
    # QQ：1811753618
}

# 输出全部拉取内容
print('\n\n' + NotionData.text + "\n\n完整数据如上，其余数据如下\n")

# 输出读取到的数据类型及父级界面ID
if NotionDict['object'] in ['database', 'page', 'list']:
    # 专为 block 类型弄得消息提示……但是发现它没有父级页面信息……聊胜于无吧
    if NotionDict['object'] == 'list':
        print("链接类型：" + messageList[NotionDict['object']] + "\n")
    else:
        print(
            "链接类型：" + messageList[NotionDict['object']] + "\n" \
            "父级类型：" + messageList[NotionDict['parent']['type']] + "\n" \
            "父级界面ID：" + NotionDict['parent'][NotionDict['parent']['type']] + "\n" \
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
        '未知错误：' + NotionDict['message'] + '\n'
    )