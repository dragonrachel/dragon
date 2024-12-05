# -*- coding: utf-8 -*-

import requests
import re
import time
from bs4 import BeautifulSoup

# 定义函数，用于获取网页内容
def fetch_url_content(url):
    try:
        # 设置请求头
        headers = {

            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
        }
        # 发送HTTP GET请求
        response = requests.get(url,timeout=(30,30),headers=headers)
        # 检查响应状态码
        if response.status_code == 200:
            # 尝试自动检测响应的编码格式
            response.encoding = response.apparent_encoding
            # 返回响应的文本数据
            return response.text
        else:
            return f"请求失败，状态码: {response.status_code}"
    except requests.RequestException as e:
        return f"请求发生异常: {e}"

# 示例网址
next_url = "https://www.taokepeixun.com/xiaoshuo/37494866354/48756340354.html"
title = ""
# 获取网页内容
#content = fetch_url_content(url)
#i=28
# 读取文件内容
#print(content)
for i in range(1,1447):
    #print(i)
    #time.sleep(5)
    if i % 10 == 0 and i!= 0:
        print(f"第{i}次请求,暂停10秒")
        time.sleep(1)
    
    if re.search(r'html',next_url) == None:
        print("没有html后缀")
        exit()

    content = fetch_url_content(next_url)
    print(f"第{i}次请求,网址: {next_url}")
    print(f"第{i}次请求,内容: {content}[:50]")
    content = content.replace(r"<br>","AA")  
    pre_title = title

    # bs4解析网页内容
    soup = BeautifulSoup(content, 'html.parser')
    # 匹配标题
    title = soup.title.string
    print(f"标题: {title}")
    # 匹配下一章链接
    next_url = soup.find('a', text=re.compile(r'下一章'))['href']
    next_url = "https://www.taokepeixun.com" + next_url
    print(f"下一章网址: {next_url}")
    # 匹配文章内容
    content = soup.find('div', id='content').get_text()
    # 去除HTML标签
    #content = re.sub(r'<.*?>', '', content)
    # 去除空白字符
    content = re.sub(r'\s', '', content)

    # 去除广告内容
    #content = re.sub(r'\r', 'AA', content)
    # 去除广告内容
    content = re.sub(r'\(h.*cc', '', content)
    # 换行
    content = re.sub(r'A{2,}','\n', content)
    # 换行
    #content = re.sub(r'\n{1,}','\n', content)
# 换行
    #content = re.sub(r'　','', content)

    #print(f"内容: {content}")
    """ # 正则表达式匹配标题
    pattern = r'<title>(.*?)</title>'
    match = re.search(pattern, content)
    #print(match.group(1))
    match = re.search(r'(.*?)\|', match.group(1))
    if match:
        title = match.group(1)
        print(f"标题: {title}")
    else:
        print("未找到标题") 

    #print(content)
    # 正则表达式匹配下一章网址
    pattern = r'保存书签(.*?)下一章'
    match = re.search(pattern, content)
    if match:
        next_url = match.group(1)
        next_url = re.search(r'\"(.*?)\"', next_url).group(1)
        next_url = "https://www.zkwxw.net" + next_url
        print(f"下一章网址: {next_url}")
    else:
        print("未找到下一章网址") 


    # 正则表达式匹配文章内容
    pattern = r'下一章(.*?)下一章'
    match = re.search(pattern, content)
    if match:
        content = match.group(1)
        #print(f"内容: {content}")
        content = re.search(r'<p>(.*)</p>', content).group(1)
        #print(f"内容: {content}")
        # 去除HTML标签
        content = re.sub(r'</p><p>', r'\n  ', content)
        # 去除空白字符
        #content = re.sub(r'\s', '', content)
        
        #print(f"内容: {content}")
    else:
        print("未找到内容")  """

    #print(title)
    #print(pre_title)

    if title != pre_title:
        text=f"\n{title}\n{content}"
    else:
        text=f"  {content}\n"
    # 将内容写入文件
    with open("web3.txt", "a", encoding="utf-8") as file:
        file.write(text)
    #print(match.group(0))