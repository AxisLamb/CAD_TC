#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('TC(adm)_014')
flightvalue = ElementValue('TC(adm)_014value')

@allure.feature("TC(ADM)-014 ")
class TestMissNoSeatsError:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Miss inputting mandatory No. of Seats field")
    def test_030(self, drivers):
        # login Local Operator (CPA)
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

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        # step 01
        '''跳转到#/Misc/MaintainApproval页面'''
        login.get_url(ini.url + "#/Misc/MaintainApproval")
        drivers.implicitly_wait(30)
        sleep(5)

        login.is_click(flight["OrderByDesc"])
        sleep(2)
        login.is_click(flight["CheckBox"])
        sleep(1)
        login.is_click(flight["Modify"])

        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/Scheduled Passenger with OP Approval.doc"
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div[5]/div/div/span/div[2]/div/div/input").send_keys(file_path)
        sleep(1)
        login.is_click(flight["Save"])
        sleep(3)
        login.is_click(flight["SaveOk"])
        sleep(3)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_ADM_014/test_adm_014.py'])
