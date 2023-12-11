#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pytest
import random
import allure
from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from utils.logger import log

flight = Element('flight')
flightvalue = ElementValue('flightvalue')


@allure.feature(
    "TC(code)-010 Maintain Port Code")
class TestCreateMaintainCode:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain Port Code")
    # 每次测试前需要在flightvalue.yaml文件中更新值，不然会报重复错误
    def test_001(self, drivers):
        """登录officer1用户"""
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
        # 跳转到Code Table ->Location->Airport页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/CodeTable/Location/Airport")
        drivers.implicitly_wait(30)
        sleep(15)
        # 填写AirportCode表格信息
        login.is_click(flight['AirportCode_Add'])
        sleep(2)
        login.input_text(flight['AirportCode_IATA'], flightvalue['AirportCode_IATA'])
        login.input_text(flight['AirportCode_ICAO'], flightvalue['AirportCode_ICAO'])
        login.input_text(flight['AirportCode_CountryCode'], flightvalue['AirportCode_CountryCode'])
        login.input_text(flight['AirportCode_EnglishName'], flightvalue['AirportCode_EnglishName'])
        login.input_text(flight['AirportCode_Remark'], flightvalue['AirportCode_Remark'])
        login.is_click(flight['AirportCode_Save'])
        sleep(5)
        # assert drivers.find_element_by_xpath("//h2[contains(.,'Record saved')]").text == 'Record saved'

        # 从 officer1用户切换到CPATEST03用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['CpaOfficerLoginName'])
        login.input_user_password(flightvalue['CpaOfficerPassword'])
        login.click_login_button()
        # 跳转到Application->Seasonal Schedule->Passenger页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        login.is_click(flight['Open_RouteList'])
        sleep(5)
        login.is_click(flight['Show_RouteList'])
        ele = drivers.find_elements_by_xpath("//li[contains(span," + "'" + flightvalue['AirportCode_IATA'] + "'" + ")]")
        if len(ele) > 0:
            print("该元素存在")
        login.is_click(flight['Close_RouteList'])
        sleep(1)
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        # 删除测试code table ，该块代码仅用作测试
        login.input_user_name(flightvalue['OfficerLoginName'])
        login.input_user_password(flightvalue['OfficerPassword'])
        login.click_login_button()
        # 跳转到View->Messages页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/CodeTable/Location/Airport")
        drivers.implicitly_wait(30)
        sleep(15)
        drivers.find_element_by_id("testAdvancedSearch02").click()
        sleep(2)
        login.input_text(flight['SearchAirportCode_IATA'], flightvalue['AirportCode_IATA'])
        login.input_text(flight['SearchAirportCode_ICAO'], flightvalue['AirportCode_ICAO'])
        login.is_click(flight["SearchAirportCode"])
        sleep(2)
        login.is_click(flight["AirportCode"])
        sleep(2)
        login.is_click(flight["Delete_AirportCode"])
        sleep(1)
        login.is_click(flight["Delete_Yes"])
        sleep(2)
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])



if __name__ == '__main__':
    pytest.main(['TestCase/test_maintain_port_code.py'])
