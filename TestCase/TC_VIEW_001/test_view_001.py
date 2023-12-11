#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import string
import random
from random import randint
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

flight = Element('view_001')
flightValue = ElementValue('viewValue_001')


@allure.feature("[TC(view)-001]Officer Search/view Applications and request for withdraw")
class TestRequestForWithdrawByOfficer:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create and upload application by Officer")
    def test_view_001(self, drivers):
        # Random flight number
        s = string.ascii_letters
        r = random.choice(s)
        # 航班号用CPA+4位整数和一个随机字母
        FlightNoA1 = "CPA" + str(randint(1000, 9999)) + r
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightValue['CpaOfficerLoginName'])
            login.input_user_password(flightValue['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 60, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到Create Seasonal Schedule Passenger Application页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"

        # step1 填写flight Schedules表格信息
        # FlightNo1
        login.input_text(flight['FlightNo1'], FlightNoA1)
        login.input_text(flight['From1'], "01/11/2023")
        login.input_text(flight['To1'], "30/11/2023")
        sleep(2)
        login.is_click(flight['DOP1_6'])
        sleep(2)
        login.is_click(flight['AircraftType_Select1'])
        login.input_text(flight['AircraftType_input1'], "100")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats1'], "100")
        login.input_text(flight['Route1'], "HKG-LAX")
        sleep(2)
        login.is_click(flight['LocalTime_STD1'])
        login.input_text(flight['LocalTime_STD1'], "1030")
        login.input_text(flight['Remarks1'], "One way flight")
        sleep(2)

        login.input_text(flight['Remarks'], "UAT End2End Testing")

        # Upload Document Start
        sleep(1)
        login.is_click(flight['Upload_Application_Related_Documents'])
        sleep(2)
        # login.is_click(flight['Upload_Application_Related_Documents_Type_Select'])
        # sleep(1)
        login.is_click(flight['Upload_Application_Related_Documents_Type_input'])
        login.input_text(flight['Upload_Application_Related_Documents_Type_input'], "Others")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # 使用pywinauto来选择文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight['Upload_Application_Related_Documents_Expiry_Date'], "31/12/2023")
        sleep(1)
        login.is_click(flight['Upload_Application_Related_Documents_Btn'])
        sleep(2)
        # Upload Document End

        login.is_click(flight['Confirm'])
        sleep(3)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(5)
        login.is_click(flight['Submit'])
        sleep(20)
        drivers.implicitly_wait(30)
        login.is_click(flight['Submit_No'])
        sleep(10)
        login.is_click(flight['Special_Operation_No'])
        sleep(4)

        login.is_click(flight['Scheduled_Passenger_Check'])
        sleep(3)
        login.is_click(flight['Search'])
        sleep(3)
        login.is_click(flight['Scheduled_Passenger_Item'])
        sleep(3)
        login.is_click(flight['Withdraw'])
        sleep(3)
        login.is_click(flight['Withdraw_Scheduled_Passenger_Item'])
        sleep(2)
        login.is_click(flight['Schedule_For_Withdraw'])
        sleep(2)
        login.is_click(flight['Schedule_For_Withdraw_Yes'])
        sleep(2)
        login.is_click(flight['Schedule_For_Withdraw_Discard'])
        sleep(3)
        login.is_click(flight['Withdraw_Reference_No'])
        sleep(3)
        drivers.find_element_by_xpath("//div[contains(span, 'Withdraw')]")


        # 从CPATEST03 用户切换到Officer1用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightValue['LoginName'])
        login.input_user_password(flightValue['Password'])
        login.click_login_button()
        sleep(20)
        drivers.implicitly_wait(30)
        # 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Application")
        sleep(5)
        login.is_click(flight['Withdraw_Reference_No_Officer1'])
        sleep(3)
        drivers.find_element_by_xpath("//div[contains(span, 'Withdraw')]")
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_VIEW_001/test_view_001.py'])
