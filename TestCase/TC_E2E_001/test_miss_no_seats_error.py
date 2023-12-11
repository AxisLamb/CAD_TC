#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

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

    @allure.story("Miss inputting mandatory No. of Seats field")
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

        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        '''跳转到Application-Seasonal Schedule-passenger页面'''
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")

        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"
        login.is_click(flight['Operator_select'])
        login.input_text(flight['Operator(ICAO)'], "CPA")
        sleep(5)

        #drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div/div[1]/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        drivers.find_element_by_xpath("//label[contains(text(),'ICAO')]//following-sibling::div//input").send_keys(Keys.ENTER)

        #填写Flight Schedules表格信息
        login.input_text(flight['FlightNo'], "CPA1001")
        login.input_text(flight['From'], "15/09/2023")
        login.input_text(flight['To'], "22/09/2023")
        login.is_click(flight['DOP_1'])

        login.is_click(flight['AircraftType_Select'])
        login.input_text(flight['AircraftType_input'], "100")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)

        # login.input_text(flight['NoofSeats'], "200")


        login.input_text(flight['Route'], "SIN-HKG")

        login.is_click(flight['LocalTime_STA'])
        login.input_text(flight['LocalTime_STA'], "0900")
        sleep(2)

        # missing to input seat no.
        login.is_click(flight['SaveAsDraft'])
        drivers.implicitly_wait(30)
        sleep(5)
        # assert drivers.find_element_by_xpath("//ul[@class='error']//li").text == 'No. of Seats is a mandatory field.(CPA1002/Record 1)'
        assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/ul/li").text == 'No. of Seats is a mandatory field.(CPA1001/Record 1)'

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
if __name__ == '__main__':
    pytest.main(['TestCase/test_miss_no_seats_error.py'])
