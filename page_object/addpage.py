#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from utils.logger import log

add = Element('add')


class AddPage(WebPage):

    def click_add_button(self):
        """点击搜索"""
        self.is_click(add['新增'])
        sleep()

    def click_modify_button(self):
        """点击重置"""
        self.is_click(add['修改'])
        sleep()

    def click_cancel_button(self):
        """点击重置"""
        self.is_mouse_click(add['取消'])
        sleep()

if __name__ == '__main__':
    pass
