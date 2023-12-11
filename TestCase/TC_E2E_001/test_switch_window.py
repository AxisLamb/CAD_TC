#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element

flight = Element('flight')
@allure.feature("TC(ECE)-001 Local Operator Create and Processing Scheduled Passenger Application with error")
class TestMissNoSeatsError:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("switch window")
    def test_001(self, drivers):
        """test1:Miss inputting mandatory No. of Seats field"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
           login.is_click(flight["Logout"])
           login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name("OFFICER1")
            login.input_user_password("12345678a")
            login.click_login_button()

        #跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch_Link'])
        sleep(2)
        login.input_text(flight['ViewMessages_RefNo_Input'], "000000427762")
        login.is_click(flight['ViewMessages_Search_Button'])
        sleep(2)
        login.is_click(flight['ViewMessages_RefNo_Link'])
        sleep(3)

        login.is_click(flight['Messaging'])
        sleep(2)

        #所有窗口计数
        i = 0
        #获得当前主窗口
        nowhandle=drivers.current_window_handle
        #获取所有窗口
        allhandles=drivers.window_handles
        for handle in allhandles:
            i = i+1
        if(i>1):
            #切换到最新打开的窗口
            drivers.switch_to.window(allhandles[-1])
        login.input_text(flight['Email_Message'], "email msg test")
        sleep(2)
        #关闭新窗口
        drivers.close()

        #回到原来主窗口
        drivers.switch_to.window(nowhandle)
        sleep(3)


        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
if __name__ == '__main__':
    pytest.main(['TestCase/test_switch_window.py'])
