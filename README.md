# 写一个爬取~~女神姐姐~~电影的的程序
## 爬取思路
1. 我们需要一个磁力链接，可以搜索关键字的网址，比如说（磁力猪）
2. 根据搜索结果页取出特殊标签所包函的字段
3. 爬出的数据整理成一个种子文件
4. 关闭程序

## 爬取效果
![](/search.png)

## 主要代码，爬取数据
```
def getMianUrl(receiveUrl):
    global findResult
    findResult = False
    browser.get(receiveUrl)
    time.sleep(1.5)

    try:
        zhongZiObj = BeautifulSoup(browser.page_source, 'lxml')
        # print(zhongZiObj)
        torroentDiv = zhongZiObj.find('div', class_='btsowlist')

        if not torroentDiv is None:
            findResult = True
            print("****************", len(torroentDiv))
            allDivs = torroentDiv.find_all("div", class_='row')
            for div in allDivs:
                if not div is None:
                    global result
                    torroentUrl = div.find('a')['href']
                    print('find url ', torroentUrl)
                    torroent = "magnet:?xt=urn:btih:%s" % (torroentUrl[len("http://www.cilizhu2.com/magnet/"):])[:-5]
                    print('find torroent ', torroent)
                    result = result + torroent + "\n"
                    # tkinter.Label(top, text=torroent).pack()
                    # finalTorroent(torroent)
        else:
            print("没有找到相关信息!请重试！！！")
    except:
        print("出现异常")
    finally:
        browser.close()
```
## 主要代码，文件写入

```
def writeDown():
    if findResult == True:
        print('name', str(searchName))
        fileName = str(searchName) + '.js'
        fo = open(fileName, 'a+')
        fo.write(result + '\n')
        fo.close()
```
## 友情提示，需要自己安装依赖库环境
也就两个，BeautifulSoup, webdriver
```
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
```


