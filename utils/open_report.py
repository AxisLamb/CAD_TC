#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import webbrowser

import zmail
from config.conf import cm
from utils.logger import log


def open_report(path):
    """打开报告"""
    try:
        # 列出目录的下所有文件和文件夹保存到lists
        lists = os.listdir(path)
        lists.sort(key=lambda fn: os.path.getmtime(path + "\\" + fn))  # 按时间排序
        # # 获取最新的文件保存到file
        file_report = os.path.join(path, lists[-1])
        log.info(file_report)
        # 注册谷歌浏览器，使用谷歌，如果本地没有谷歌，去掉代码，只用默认浏览器
        webbrowser.open(file_report)
        # chrome_path = "C:\\Program Files\Google\Chrome\Application\chrome.exe"
        # webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
        # webbrowser.get("chrome").open(file_report)
        print("报告打开成功！")
    except Exception as e:
        print("Error: 无法打开报告，{}！", format(e))


if __name__ == "__main__":
    open_report()
