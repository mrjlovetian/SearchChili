#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
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
    browser.get(receiveUrl)
    time.sleep(1.5)
    zhongZiObj = BeautifulSoup(browser.page_source, 'lxml')
    # print(zhongZiObj)
    torroentDiv = zhongZiObj.find('div', class_='btsowlist')
    listBox.delete(0, tkinter.END)
    if not torroentDiv is None:
        print("****************", len(torroentDiv))
        allDivs = torroentDiv.find_all("div", class_='row')
        for div in allDivs:
            if not div is None:
                torroentUrl = div.find('a')['href']
                print('find url ', torroentUrl)
                torroent = "magnet:?xt=urn:btih:%s"%(torroentUrl[len("http://www.cilizhu2.com/magnet/"):])[:-5]
                print('find torroent ', torroent)
                listBox.insert(0, torroent)
                # tkinter.Label(top, text=torroent).pack()
            # finalTorroent(torroent)
    else:tkinter.messagebox.showinfo("fail", "没有找到相关信息!")


def clickBtn():
    var = entry.get()
    print("-----------------", var)
    searchUrl = "http://www.cilizhu2.com/torrent/%s.html"%(var)
    print("searchUrl", searchUrl)
    getMianUrl(searchUrl)

    # if var.startswith("http"):
    #     getMianUrl(var)
    # else:
    #     tkinter.messagebox.askretrycancel("出错了！", "不是有效的URL")



# 界面
top = tkinter.Tk()
top.frame = (0, 0, 50, 50)
top.title("界面化")

entry = tkinter.Entry(top, text="pacher", width=100)

entry.pack()

btn = tkinter.Button(top, text="搜索", command=clickBtn)
btn.pack()

listBox = tkinter.Listbox(top, width=100)
listBox.pack()

# labelHello = tkinter.Label(top, text="欢迎界面", height=40, width=100, fg='red')
#
# labelHello.pack()



top.mainloop()

