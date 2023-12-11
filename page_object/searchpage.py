#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from selenium.webdriver import ActionChains

from page.webpage import WebPage, sleep
from common.readelement import Element
from utils.logger import log

search = Element('search')


class SearchPage(WebPage):
    """搜索类"""

    def input_search(self, content):
        """输入搜索"""
        self.input_text(search['搜索框'], txt=content)
        sleep()

    @property
    def imagine(self):
        """搜索联想"""
        return [x.text for x in self.find_elements(search['候选'])]

    def click_search(self):
        """点击搜索"""
        self.is_click(search['搜索按钮'])

    def input_search_text(self, content):
        """输入搜索"""
        self.input_text(search['查询输入框'], txt=content)
        sleep()

    def input_search_text_ex(self, text, content):
        """输入搜索"""
        locator = search['查询框']
        new_locator = list(locator)
        new_locator[1] = new_locator[1].replace('$', text)
        locator = tuple(new_locator)
        self.input_text(locator, txt=content)
        sleep()

    def textarea_search_text_ex(self, text, content):
        """输入搜索"""
        locator = search['文本域查询框']
        new_locator = list(locator)
        new_locator[1] = new_locator[1].replace('$', text)
        locator = tuple(new_locator)
        self.input_text(locator, txt=content)
        sleep()

    def input_search_text_by_name(self, locator_name, content):
        """输入搜索"""
        self.input_text(search[locator_name], content)
        sleep()

    def click_item_by_name(self, name, txt):
        """输入搜索"""
        self.ass_data_click(name, txt)
        sleep()

    def click_button_by_text(self, text):
        """输入搜索"""
        self.ass_data_click('按钮', text)
        sleep()

    def click_link_by_text(self, text):
        """点击搜索"""
        self.ass_data_click('链接', text)
        sleep()

    def click_search_button(self):
        """点击搜索"""
        self.is_click(search['查询按钮'])
        sleep()

    def click_reset_button(self):
        """点击重置"""
        self.is_click(search['重置按钮'])
        sleep()

    def move_to_element(self, name, text):
        element = self.ass_data(name, text)
        ActionChains(self.driver).move_to_element(element).perform()
        sleep(1)

    def ass_data_click(self, name, text):
        element = self.ass_data(name, text)
        element.click()

    def ass_data(self, name, text):
        locator = search[name]
        new_locator = list(locator)
        new_locator[1] = new_locator[1].replace('$', text)
        locator = tuple(new_locator)
        element = self.find_element(locator)
        # 滚动到指定元素
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center', inline: "
                                   "'nearest' });", element)
        sleep(1)
        return element


if __name__ == '__main__':
    pass
