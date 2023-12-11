#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging
import os
import string
import random
from random import randint
import pytest
import allure
from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from utils.logger import log

flight = Element('adm_007')
flightValue = ElementValue('admValue_007')


@allure.feature("[TC(adm)-007]Manage template")
class TestSchedulePassengerApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create Scheduled All-Cargo Application and approve")
    # 每次测试前需要在flightvalue.yaml文件中更新FlightNo和TemplateName值，不然会报重复航班号和模板名错误
    def test_001(self, drivers):
        # Random flight number
        s = string.ascii_letters
        r = random.choice(s)
        # 航班号用CPA+4位整数和一个随机字母
        FlightNoA1 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoA2 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoB1 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoB2 = "CPA" + str(randint(1000, 9999)) + r
        # TemplateName 随机生成数
        TemplateName = "Test" + str(random.uniform(1, 1000))

        """登录"""
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
        sleep(30)
        # 跳转到Create Seasonal Schedule Passenger Application页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"

        # step1 填写flight Schedules表格信息
        # FlightNo1
        login.input_text(flight['FlightNo1'], FlightNoA1)
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
        login.input_text(flight['FlightNo1_2'], FlightNoA2)
        login.is_click(flight['AircraftType_Select1_2'])
        login.input_text(flight['AircraftType_input1_2'], "100")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['NoofSeats1_2'], "100")
        login.input_text(flight['Route1_2'], "LAX-HKG")
        sleep(2)
        login.is_click(flight['LocalTime_STA1_2'])
        login.input_text(flight['LocalTime_STA1_2'], "1230")
        login.input_text(flight['Remarks1_2'], "UAT End2End Testing 2")
        sleep(2)

        login.input_text(flight['Remarks'], "UAT End2End Testing")

        # step3
        login.is_click(flight['SaveAsTemplate'])
        login.input_text(flight['TemplateName'], TemplateName)
        login.input_text(flight['Description'], "UAT Testing")
        sleep(1)
        login.is_click(flight['Template_Save'])
        sleep(3)

        # 跳转到View->Template页面
        login.get_url(ini.url + "#/View/Template")
        sleep(3)
        login.is_click(flight['Scheduled_Passenger_Check'])
        login.input_text(flight['Template_Name_Input'], TemplateName)
        sleep(1)
        login.is_click(flight['Search'])
        sleep(3)
        login.is_click(flight['Template_Edit'])
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Update Seasonal Schedule Passenger Template — " + TemplateName

        # Update FlightNo1
        login.input_text(flight['FlightNo1'], FlightNoB1)
        login.input_text(flight['From1'], "01/12/2023")
        login.input_text(flight['To1'], "31/12/2023")
        sleep(2)
        login.is_click(flight['DOP1_1'])
        login.is_click(flight['DOP1_2'])
        login.is_click(flight['DOP1_3'])
        login.is_click(flight['DOP1_7'])
        sleep(2)
        login.is_click(flight['AircraftType_Select1'])
        login.is_click(flight['AircraftType_Select1'])
        login.input_text(flight['AircraftType_input1'], "141")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats1'], "200")
        login.input_text(flight['Route1'], "HKG-MFM")
        sleep(2)
        login.is_click(flight['LocalTime_STD1'])
        login.input_text(flight['LocalTime_STD1'], "1030")
        login.input_text(flight['Remarks1'], "UAT End2End Update 1")
        sleep(2)

        # Update FlightNo1_2
        login.input_text(flight['FlightNo1_2'], FlightNoB2)
        login.is_click(flight['AircraftType_Select1_2'])
        login.is_click(flight['AircraftType_Select1_2'])
        login.input_text(flight['AircraftType_input1_2'], "141")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['NoofSeats1_2'], "200")
        login.input_text(flight['Route1_2'], "MFM-HKG")
        sleep(2)
        login.is_click(flight['LocalTime_STA1_2'])
        login.input_text(flight['LocalTime_STA1_2'], "1230")
        login.input_text(flight['Remarks1_2'], "UAT End2End Update 2")
        sleep(2)



        login.is_click(flight['Update_Template_Btn'])
        sleep(2)
        login.is_click(flight['Template_Save'])
        sleep(2)
        login.is_click(flight['Discard_Btn'])
        sleep(2)

        login.is_click(flight['Scheduled_Passenger_Check'])
        login.input_text(flight['Template_Name_Input'], TemplateName)
        sleep(1)
        login.is_click(flight['Search'])
        sleep(3)
        login.is_click(flight['Template_Item_CheckBox'])
        sleep(1)
        login.is_click(flight['Copy_To_New_Application'])
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/TC_ADM_007/test_adm_007.py'])

