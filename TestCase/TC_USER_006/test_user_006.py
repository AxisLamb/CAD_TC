#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import random
import string

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue
from utils.logger import log

flight = Element('user_006')
flightValue = ElementValue('userValue_006')


@allure.feature("[TC(user)-006]Maintain User Account (Create, Search, Update) (STAT user)")
class TestUserAccount:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain User Account (Create, Search, Update) (STAT user)")
    def test_user_006(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightValue['Officer_LoginName'])
            login.input_user_password(flightValue['Officer_Password'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到Create User Account页面
        login.get_url(ini.url + "#/Admin/UserAccounts/CreateUserAccount")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create User Account"
        r = '1' + ''.join(random.sample(string.ascii_uppercase, 9))
        log.info("----------------------------username:  " + r)
        login.input_text(flight['Login_Username'], r)
        login.input_text(flight['Name'], r)
        login.input_text(flight['Email_Address'], flightValue['Email_Address'])

        login.is_click(flight['Save'])
        sleep(1)
        login.is_click(flight['Save_OK'])
        sleep(1)
        login.is_click(flight['Reset_Password'])
        sleep(1)
        # 记录账号和密码
        password = drivers.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/p").text
        log.info("----------------------------" + password)
        te = r + ":" + password.replace(" ", "").split(":")[-1]
        log.info("----------------------------username and password:   " + te)
        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path)+'/TestFile/memo.txt'
        # 'w'表示覆盖写
        with open(filename, 'w') as f:
            f.write(te)
        login.is_click(flight['Reset_OK'])
        sleep(1)
        login.is_click(flight['Add'])
        sleep(1)
        login.input_text(flight['Name2'], flightValue['TA_ADMIN_Name'])
        login.input_text(flight['Description'], flightValue['TA_ADMIN_Description'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['Search_Result_Item'])
        login.is_click(flight['Add2'])
        sleep(1)
        login.is_click(flight['Add2_OK'])
        sleep(1)

        login.is_click(flight['Add'])
        sleep(1)
        login.input_text(flight['Name2'], flightValue['TA_USER_Name'])
        login.input_text(flight['Description'], flightValue['TA_USER_Description'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['Search_Result_Item'])
        login.is_click(flight['Add2'])
        sleep(1)
        login.is_click(flight['Add2_OK'])
        sleep(1)

        login.is_click(flight['Add'])
        sleep(1)
        login.input_text(flight['Name2'], flightValue['TA_RUSER_Name'])
        login.input_text(flight['Description'], flightValue['TA_RUSER_Description'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['Search_Result_Item'])
        login.is_click(flight['Add2'])
        sleep(1)
        login.is_click(flight['Add2_OK'])
        sleep(1)

        login.is_click(flight['Add'])
        sleep(1)
        login.input_text(flight['Name2'], flightValue['TA_ASRPT_Name'])
        login.input_text(flight['Description'], flightValue['TA_ASRPT_Description'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['Search_Result_Item'])
        login.is_click(flight['Add2'])
        sleep(1)
        login.is_click(flight['Add2_OK'])
        sleep(2)

        # 跳转到Search User Account页面
        login.get_url(ini.url + "#/Admin/UserAccounts/SearchUserAccount")
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Search User Account"
        login.input_text(flight['Login_Username2'], r)
        login.is_click(flight['Search2'])
        sleep(3)
        login.is_click(flight['Total_Pages'])
        sleep(2)

        # 从OFFICER1用户到新用户切换
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        with open(filename, "r") as f:
            data = f.readline()
            log.info("----------------------------" + data)
        pWord = data.split(':')[-1]
        login.input_user_name(data.split(':')[0])
        login.input_user_password(pWord)
        login.click_login_button()
        sleep(20)
        drivers.implicitly_wait(30)
        login.is_click(flight["Change_Yes"])
        sleep(3)
        login.input_text(flight['Old_Password'], pWord)
        login.input_text(flight['New_Password'], flightValue['New_Password'])
        login.input_text(flight['Confirm_New_Password'], flightValue['New_Password'])
        login.is_click(flight["Save2"])
        sleep(3)
        login.is_click(flight["Save2_OK"])
        sleep(2)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_USER_006/test_user_006.py'])
