#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from page.webpage import WebPage, sleep
from common.readelement import Element
from utils.logger import log

menu = Element('menu')


class MenuPage(WebPage):

    def click_1_menu(self, text):
        """顶部菜单"""
        locator = menu['顶部菜单']
        new_locator = list(locator)
        new_locator[1] = new_locator[1].replace('$', text)
        locator = tuple(new_locator)
        print(locator)
        self.is_click(locator)
        sleep()

    def click_2_menu(self, text):
        """二级菜单"""
        locator = menu['二级菜单']
        new_locator = list(locator)
        new_locator[1] = new_locator[1].replace('$', text)
        locator = tuple(new_locator)
        print(locator)
        self.is_click(locator)
        sleep()

    def click_3_menu(self, text):
        """三级菜单"""
        locator = menu['三级菜单']
        new_locator = list(locator)
        new_locator[1] = new_locator[1].replace('$', text)
        locator = tuple(new_locator)
        print(locator)
        self.is_click(locator)
        sleep()


if __name__ == '__main__':
    pass
