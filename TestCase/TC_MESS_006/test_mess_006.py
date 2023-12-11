#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pytest
import allure
import random
import string
from random import randint
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('mess_006')
flightValue = ElementValue('messValue_006')


@allure.feature("[TC(mess)-006]BU Alert")
class TestBUAlert:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("BU Alert")
    def test_mess_006(self, drivers):
        login = LoginPage(drivers)
        # logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        # if len(logout_elements) > 0:
        #     login.is_click(flight["Logout"])
        #     login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightValue['Officer_LoginName'])
            login.input_user_password(flightValue['Officer_Password'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到List of System Parameters页面
        login.get_url(ini.url + "#/Admin/SystemParameters")
        drivers.implicitly_wait(30)
        sleep(2)
        assert drivers.find_element_by_css_selector("h2").text == "List of System Parameters"
        login.input_text(flight['Description'], '0000-2359')
        sleep(1)
        login.is_click(flight['Search'])
        login.is_click(flight['Result'])
        login.is_click(flight['Save'])
        login.is_click(flight['Save_OK'])

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        # Create application by Local Operator(CPA)
        login.input_user_name(flightValue['CpaOfficerLoginName'])
        login.input_user_password(flightValue['CpaOfficerPassword'])
        login.click_login_button()

        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"
        r = random.choice(string.ascii_letters)
        FlightNo1 = "CPA" + str(randint(1000, 9999)) + r
        FlightNo2 = "CPA" + str(randint(1000, 9999)) + r

        # step1 填写flight Schedules表格信息
        # FlightNo1
        login.input_text(flight['FlightNo1'], FlightNo1)
        login.input_text(flight['From1'], "01/11/2023")
        login.input_text(flight['To1'], "30/11/2023")
        sleep(2)
        login.is_click(flight['DOP1_1'])
        login.is_click(flight['DOP1_3'])
        login.is_click(flight['DOP1_5'])
        sleep(2)
        login.is_click(flight['AircraftType_Select1'])
        login.input_text(flight['AircraftType_input1'], "100")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats1'], "100")
        login.input_text(flight['Route1'], "HKG-LAX")
        sleep(2)
        login.is_click(flight['LocalTime_STD1'])
        login.input_text(flight['LocalTime_STD1'], "1030")
        login.input_text(flight['Remarks1'], "UAT End2End Testing 1")
        sleep(2)
        # FlightNo1_2
        login.input_text(flight['FlightNo1_2'], FlightNo2)
        login.is_click(flight['AircraftType_Select1_2'])
        login.input_text(flight['AircraftType_input1_2'], "100")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['NoofSeats1_2'], "100")
        login.input_text(flight['Route1_2'], "LAX-HKG")
        sleep(2)
        login.is_click(flight['LocalTime_STA1_2'])
        login.input_text(flight['LocalTime_STA1_2'], "1930")
        login.input_text(flight['Remarks1_2'], "UAT End2End Testing 2")
        sleep(2)
        login.input_text(flight['Remarks'], "UAT End2End Testing")

        # Upload Document Start
        login.is_click(flight['Upload_Application_Related_Documents'])
        sleep(2)
        login.is_click(flight['Upload_Application_Related_Documents_Type_input'])
        sleep(1)
        login.input_text(flight['Upload_Application_Related_Documents_Type_input'], "Others")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # 选择文件
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
        login.is_click(flight['PreviewAndSubmit'])
        sleep(1)
        login.is_click(flight['Submit'])
        sleep(1)
        login.is_click(flight['Submit_No'])
        sleep(1)
        login.is_click(flight['Submit_Special_Operation_No'])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_MESS_005/test_mess_006.py'])
