#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import pytest
import allure
import logging

from selenium.webdriver.common.by import By
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('flight_020')
flightvalue = ElementValue('flightvalue_020')


@allure.feature("TC(ECE)-020 03Check_Traffic_Rights_by_Officer")
class TestCheckTrafficRightsByOfficer:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Miss inputting mandatory No. of Seats field")
    def test_030(self, drivers):
        """test1: Miss inputting mandatory No. of Seats field"""
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
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        '''跳转到#/View/Messages页面'''
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path) + '/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， r以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
        with open(filename, 'r') as f:
            refno = f.read()
        login.is_click(flight['Step12_Advanced_Search'])
        login.input_text(flight['OptSearch_ReferenceNo'], refno)
        login.input_text(flight['OptSearch_Sender'], flightvalue['OperatorcpaLoginName'])
        login.is_click(flight['Step12_Search'])
        sleep(2)

        # step 13
        # login.is_click(flight['Step13_Open_Message'])
        # sleep(2)

        # step 14
        login.is_click(flight['Step14_Message_Ref_No'])

        # step 15
        login.is_click(flight['Step15_Select_Record'])
        login.is_click(flight['Step15_Check_Traffic_Rights'])
        sleep(8)
        # login.is_click(flight['Step15_Check_Traffic_Rights_Yes'])
        # sleep(8)
        # login.is_click(flight['Step15_Check_Traffic_Rights_Out'])

        # step 16
        login.is_click(flight['Step15_Export'])
        sleep(8)
        login.is_click(flight['Step15_Cancel'])
        sleep(2)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        current_path = os.path.abspath(__file__)
        # 清空文件内容
        # '该文件夹下所有的文件（包括文件夹）'
        file_path = os.path.dirname(current_path) + '/TestData/Out'
        FileList = os.listdir(file_path)
        logging.info(FileList)
        # '遍历所有文件'
        for files in FileList:
            files = os.path.join(file_path, files)
            logging.info(files)
            # 清空文件内容
            with open(files, 'a+') as f:
                f.truncate(0)


if __name__ == '__main__':
    pytest.main(['TestCase/test_e2e_0203.py'])
