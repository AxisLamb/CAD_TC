#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import pytest
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import switch_to

from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

flight = Element('TC(user)-004')
flightvalue = ElementValue('TC(user)-004value')


@allure.feature(
    "TC(user)-004  Maintain User Account (Create, Search, Update) (AS User)")
class TestMaintainUserAccount:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain User Account (Create, Search, Update) (AS User)")
    # 每次测试前需要在flightvalue.yaml文件中更新值，不然会报重复错误
    def test_001(self, drivers):
        """登录OFFICER1用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['OfficerLoginName'])
            login.input_user_password(flightvalue['OfficerPassword'])
            login.click_login_button()
        # 跳转到Admin->User Accounts / Security Setup->Create User Account页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/Admin/UserAccounts/CreateUserAccount")
        drivers.implicitly_wait(30)
        sleep(15)
        # 填写表格信息
        loginUsername = flightvalue['LoginUsername'] + str(random.randint(1000, 9999))
        login.input_text(flight['LoginUsername'], loginUsername)
        login.input_text(flight['Name'], flightvalue['Name'])
        login.input_text(flight['EmailAddress'], flightvalue['EmailAddress'])
        login.is_click(flight['Save'])
        login.is_click(flight['Save_OK'])
        login.is_click(flight['RestPassword'])
        alert = drivers.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/p").text.split(" ")
        restPassword = alert[3]
        login.is_click(flight['Save_OK'])
        login.is_click(flight['Add'])
        sleep(1)
        login.input_text(flight['Search_Name'], flightvalue['Search_Name1'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['CheckBox1'])
        login.is_click(flight['AddSearchResult'])
        login.is_click(flight['Save_OK'])
        login.is_click(flight['Add'])
        login.input_text(flight['Search_Name'], flightvalue['Search_Name2'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['CheckBox1'])
        login.is_click(flight['AddSearchResult'])
        login.is_click(flight['Save_OK'])
        login.is_click(flight['Add'])
        login.input_text(flight['Search_Name'], flightvalue['Search_Name3'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['CheckBox1'])
        login.is_click(flight['AddSearchResult'])
        login.is_click(flight['Save_OK'])
        login.get_url(ini.url + "#/Admin/UserAccounts/SearchUserAccount")
        sleep(6)
        login.input_text(flight['Search_LoginUsername'],loginUsername)
        login.is_click(flight['Search'])
        sleep(3)
        login.get_url(ini.url + "#/View/Messages")
        sleep(3)
        # 从 officer1用户切换到新建用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(loginUsername)
        login.input_user_password(restPassword)
        login.click_login_button()

        sleep(20)
        # 页面加载速度慢，恢复后可删除
        login.is_click(flight['ResePass_Yes'])
        sleep(2)
        login.input_text(flight['OldPassWord'], restPassword)
        login.input_text(flight['NewPassWord'], flightvalue['NewPassWord'])
        login.input_text(flight['ConfirmNewPass'], flightvalue['NewPassWord'])
        login.is_click(flight["Save"])
        login.is_click(flight["Save_OK"])

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/test_create_officer_process_helicopter_approve.py'])
