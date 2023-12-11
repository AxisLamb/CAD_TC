#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import traceback

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from page.webpage import WebPage, sleep
from common.readelement import Element
from utils.logger import log

login = Element('login')


class LoginPage(WebPage):

    def input_user_name(self, txt):
        """输入账号"""
        self.input_text(login['账号'], txt)
        sleep()

    def input_user_password(self, txt):
        """输入密码"""
        self.input_text(login['密码'], txt)
        sleep()

    def click_login_button(self):
        """点击登录"""
        self.is_click(login['登录'])
        sleep()

    def click_login_out_button(self):
        try:
            """点击登出"""
            self.is_click(login['登出头像'])
            sleep()
            self.is_click(login['注销登录'])
            sleep()
            self.is_click(login['注销确定'])
            # # 打印元素
            # print("element", element)
            # # 判断input、select等元素是否可编辑
            # print("is_enabled", element.is_enabled())
            # # 判断该元素是否在页面上（不是能否看到，而是判断html代码是否存在）
            # print("is_displayed", element.is_displayed())
            # # 判断该元素是否已选中
            # print("is_selected", element.is_selected())
            # move.click()
            # print(move)
            # move.click()
            # ActionChains(self.driver).move_to_element(move).perform()
            sleep()
        except NoSuchElementException as e:
            # 打印异常堆栈信息
            print(traceback.print_exc())


if __name__ == '__main__':
    pass
