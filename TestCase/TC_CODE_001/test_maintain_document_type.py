#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pytest
import allure

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('codeTable_001')
flightvalue = ElementValue('flightvalue_104')
accountValue = ElementValue('cad_account')

@allure.feature("[TC(code)-001]Maintain Document Type Information")
class TestMaintainDocumentType:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("add document type information and check")
    def test_code_001(self, drivers):
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
            sleep(20)

        # 跳转到Document Type Information页面
        login.get_url(ini.url + "#/CodeTable/Document")
        drivers.implicitly_wait(30)
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Document Type Information"
        login.is_click(flight['Add'])
        sleep(1)
        login.input_text(flight['Document_Type'], flightvalue['Code_Document_Type_Add'])
        sleep(2)
        login.is_click(flight['Save'])
        sleep(2)
        login.is_click(flight['Save_OK'])
        sleep(2)

        # 跳转到Predefined Documents of Application Type页面
        login.get_url(ini.url + "#/CodeTable/Predefined")
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Predefined Documents of Application Type"
        # //div[text()='Scheduled Passenger']/../../td[1]/div/label/span
        drivers.find_element_by_xpath("//div[text()='Scheduled Passenger']/../../td[1]/div/label/span").click()
        sleep(2)
        login.is_click(flight['Modify'])
        sleep(2)
        # //span[text()=' Document type Test 01 ']/../span[1]
        drivers.find_element_by_xpath("//span[text()=' " + flightvalue['Code_Document_Type_Add'] + " ']/../span[1]").click()
        sleep(2)
        login.is_click(flight['Save2'])
        sleep(2)
        login.is_click(flight['Save2_OK'])
        sleep(2)

        # 从 Officer1 用户到 CPATEST03 用户切换
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(accountValue['CpaOfficerLoginName'])
        login.input_user_password(accountValue['CpaOfficerPassword'])
        login.click_login_button()
        sleep(20)

        # 跳转到Create Seasonal Schedule Passenger Application页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"
        # //div[text()=' Document type Test 01 ']
        drivers.find_element_by_xpath("//div[text()=' " + flightvalue['Code_Document_Type_Add'] + " ']").click()
        sleep(5)
        # 删除
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(accountValue['OfficerLoginName'])
        login.input_user_password(accountValue['OfficerPassword'])
        login.click_login_button()
        sleep(20)
        login.get_url(ini.url + "#/CodeTable/Predefined")
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Predefined Documents of Application Type"
        # //div[text()='Scheduled Passenger']/../../td[1]/div/label/span
        drivers.find_element_by_xpath("//div[text()='Scheduled Passenger']/../../td[1]/div/label/span").click()
        sleep(2)
        login.is_click(flight['Modify'])
        sleep(2)
        # //span[text()=' Document type Test 01 ']/../span[1]
        drivers.find_element_by_xpath("//span[text()=' " + flightvalue['Code_Document_Type_Add'] + " ']/../span[1]").click()
        sleep(2)
        login.is_click(flight['Save2'])
        sleep(2)
        login.is_click(flight['Save2_OK'])
        sleep(2)
        login.get_url(ini.url + "#/CodeTable/Document")
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Document Type Information"
        login.input_text(flight['Search_Document_Type'], flightvalue['Code_Document_Type_Add'])
        login.is_click(flight['Search'])
        sleep(1)
        # //div[text()='Document type Test 01']
        drivers.find_element_by_xpath("//div[text()='" + flightvalue['Code_Document_Type_Add'] + "']").click()
        sleep(1)
        login.is_click(flight['Delete'])
        sleep(1)
        login.is_click(flight['Delete_Yes'])
        sleep(2)
        login.is_click(flight['Delete_OK'])
        sleep(2)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_CODE_001/test_maintain_document_type.py'])
