#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter.messagebox
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

option = Options()
option.add_argument("--headless")
option.add_argument("--disable-gpu")
browser = webdriver.Chrome(chrome_options=option)

def getMianUrl(receiveUrl):
    global findResult
    findResult = False
    browser.get(receiveUrl)
    time.sleep(1.5)
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
                torroent = "magnet:?xt=urn:btih:%s"%(torroentUrl[len("http://www.cilizhu2.com/magnet/"):])[:-5]
                print('find torroent ', torroent)
                result = result + torroent + "\n"
                # tkinter.Label(top, text=torroent).pack()
            # finalTorroent(torroent)
    else:print("没有找到相关信息!请重试！！！")

def writeDown():
    if findResult == True:
        print('name', str(searchName))
        fileName = str(searchName) + '.js'
        fo = open(fileName, 'a+')
        fo.write(result + '\n')
        fo.close()

searchName = str(input("请输入要搜索的番号或作品名或演员："))
result = ""
searchUrl = "http://www.cilizhu2.com/torrent/%s.html"%(searchName)
findResult = False

getMianUrl(searchUrl)
writeDown()
browser.close()
