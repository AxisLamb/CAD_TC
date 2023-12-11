#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import datetime
import random
import string

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue
from utils.logger import log

flight = Element('user_005')
flightValue = ElementValue('userValue_005')
accountValue = ElementValue('cad_account')

@allure.feature("[TC(user)-005]Maintain User Account (Create, Search, Update) (Senior Officer)")
class TestSeniorOfficerAccount:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain User Account (Create, Search, Update) (Senior Officer)")
    def test_user_005(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(accountValue['OfficerLoginName'])
            login.input_user_password(accountValue['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到Create User Account页面
        login.get_url(ini.url + "#/Admin/UserAccounts/CreateUserAccount")
        drivers.implicitly_wait(30)
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Create User Account"
        # 用户名
        r = '1' + ''.join(random.sample(string.ascii_uppercase, 9))
        log.info("----------------------------username: " + r)
        login.input_text(flight['Login_Username'], r)
        login.input_text(flight['Name'], r)
        login.input_text(flight['Email_Address'], flightValue['Email_Address'])
        login.is_click(flight['Save'])
        sleep(1)
        login.is_click(flight['Save_OK'])
        sleep(1)
        login.is_click(flight['Reset_Password'])
        sleep(1)
        # 密码
        password = drivers.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/p").text
        password = password.replace(" ", "").split(":")[-1]
        log.info("----------------------------password: " + password)
        login.is_click(flight['Reset_OK'])
        sleep(1)

        login.is_click(flight['Add'])
        sleep(1)
        login.input_text(flight['Name2'], flightValue['Name'])
        login.input_text(flight['Description'], flightValue['Description'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['Result_Check'])
        sleep(1)
        login.is_click(flight['Add2'])
        sleep(1)
        login.is_click(flight['Add2_OK'])
        sleep(2)
        login.is_click(flight['Add'])
        sleep(1)
        login.input_text(flight['Name2'], flightValue['Name2'])
        login.input_text(flight['Description'], flightValue['Description2'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['Result_Check'])
        sleep(1)
        login.is_click(flight['Add2'])
        sleep(1)
        login.is_click(flight['Add2_OK'])
        sleep(2)
        login.is_click(flight['Add'])
        sleep(1)
        login.input_text(flight['Name2'], flightValue['Name3'])
        login.input_text(flight['Description'], flightValue['Description3'])
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['Result_Check'])
        sleep(1)
        login.is_click(flight['Add2'])
        sleep(1)
        login.is_click(flight['Add2_OK'])
        sleep(2)

        # 跳转到Search User Account页面
        login.get_url(ini.url + "#/Admin/UserAccounts/SearchUserAccount")
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Search User Account"
        login.is_click(flight['Internal2'])
        login.input_text(flight['Login_Username2'], r)
        login.is_click(flight['Search2'])
        sleep(3)

        # 从OFFICER1用户到新用户切换
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(r)
        login.input_user_password(password)
        login.click_login_button()
        sleep(5)
        login.is_click(flight["Change_Yes"])
        sleep(1)
        login.input_text(flight['Old_Password'], password)
        login.input_text(flight['New_Password'], flightValue['New_Password'])
        login.input_text(flight['Confirm_New_Password'], flightValue['New_Password'])
        login.is_click(flight["Save2"])
        sleep(2)
        login.is_click(flight["Save2_OK"])
        sleep(2)

        # 跳转到Search Supporting Documents (Own Aircraft)页面
        login.get_url(ini.url + "#/View/SupportingDocumentsOwn")
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Search Supporting Documents (Own Aircraft)"
        login.is_click(flight["New"])
        login.is_click(flight['Operator_ICAO2'])
        login.input_text(flight['Operator_ICAO2'], flightValue['Operator_ICAO2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['Document_Type'])
        login.input_text(flight['Document_Type'], flightValue['Document_Type'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[2]/div/div/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # 获取明天的日期
        expiry_date = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        log.info("----------------------------tomorrow date: " + expiry_date)
        login.input_text(flight['Expiry_Date'], expiry_date)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Enclosure_Reference'], flightValue['Enclosure_Reference'])
        login.input_text(flight['Remarks'], flightValue['Enclosure_Reference'])
        login.is_click(flight["Upload"])
        sleep(1)
        login.is_click(flight["Upload_OK"])
        sleep(2)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_USER_005/test_user_005.py'])
