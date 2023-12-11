#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import pytest
import allure

from selenium.webdriver.common.by import By
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('flight_020')
flightvalue = ElementValue('flightvalue_020')
@allure.feature("TC(ECE)-020 01Create_port_sets_by_Officer")
class TestCreatePortSetsByOfficer:
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
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        # # step 01
        '''跳转到#/Misc/MaintainAirTraffic/MaintainPort页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainPort")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step01_New'])
        login.is_click(flight['Step01_Ports'])
        sleep(5)
        login.is_click(flight['Step01_Advanced'])
        sleep(5)
        login.input_text(flight['Step01_Airport_Code'], "HKG")
        sleep(5)
        login.is_click(flight['Step01_Search'])
        login.is_click(flight['Step01_Click_Port'])
        login.input_text(flight['Step01_Description'], "Hong Kong Intl Airport")
        sleep(2)
        login.is_click(flight['Step01_Save'])
        sleep(2)
        login.is_click(flight['Step01_Sort'])
        sleep(2)
        login.is_click(flight['Step01_Sort'])
        login.is_click(flight['Step01_Preview'])
        sleep(5)
        login.is_click(flight['Step01_Preview_Close'])
        portId = drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]").text
        # step 02
        login.is_click(flight['Step02_New'])
        login.is_click(flight['Step02_Countries'])
        sleep(5)
        login.is_click(flight['Step02_Advanced'])
        login.input_text(flight['Step02_English_Description'], "Singapore")
        login.is_click(flight['Step02_Search'])
        login.is_click(flight['Step02_Click_Country'])
        login.input_text(flight['Step02_Description'], "All Singapore ports")
        sleep(2)
        login.is_click(flight['Step02_Save'])
        sleep(2)
        login.is_click(flight['Step02_Sort'])
        sleep(2)
        login.is_click(flight['Step02_Sort'])
        login.is_click(flight['Step02_Preview'])
        sleep(5)
        login.is_click(flight['Step02_Preview_Close'])
        portId2 = drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]").text
        # step 03
        '''跳转到#/Misc/MaintainAirTraffic/MaintainRuleSets页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainRuleSets")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step03_New'])
        login.is_click(flight['Step03_Country_Select'])
        login.input_text(flight['Step03_Country_Input'], "Hong Kong (SAR, China)")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['Step03_Type_Select'])
        login.input_text(flight['Step03_Type_Input'], "All-Cargo")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[4]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['Step03_Remarks'], "Rule for Hong Kong")
        sleep(2)
        login.is_click(flight['Step03_Save'])
        #存ruleSetID
        ruleSetID = drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]").text
        # # step 04
        login.is_click(flight['Step04_Select'])
        login.is_click(flight['Step04_Configure_Route_Definition'])
        sleep(5)
        #取前俩个portid
        login.is_click(flight['Step04_HomePorts'])
        sleep(3)
        # login.is_click(flight['Step04_HomePorts_Last_Updated_Sort'])
        HomePortsPath = "//div[contains(text(),'"+portId+"')]"
        print(HomePortsPath)
        drivers.find_element_by_xpath(HomePortsPath).click()
        sleep(5)
        login.is_click(flight['Step04_ForeignPorts'])
        # login.is_click(flight['Step04_ForeignPorts_Last_Updated_Sort'])
        sleep(3)
        drivers.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div[3]/table/tbody/tr[1]/td[1]/div").click()
        login.input_text(flight['Step04_Description'], "HKG- > SG")
        login.input_text(flight['Step04_Remarks'], "HKG- > SG")
        sleep(2)
        login.is_click(flight['Step04_Save'])

        # # step 05
        '''跳转到#/Misc/MaintainAirTraffic/MaintainEntitlement页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainEntitlement")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step05_New'])
        login.is_click(flight['Step05_Frequency_Click'])
        login.input_text(flight['Step05_Frequency'], "5")
        login.is_click(flight['Step05_Cargo_limit_Click'])
        login.input_text(flight['Step05_Cargo_limit'], "50000")
        login.is_click(flight['Step05_Per_flight_cargo_Click'])
        login.input_text(flight['Step05_Per_flight_cargo'], "10000")
        login.input_text(flight['Step05_Load_Factor'], "50")
        login.input_text(flight['Step05_Description'], "W:5 Cargo:  PL:50000 PP: 10000")
        login.input_text(flight['Step05_Remarks'], "UAT Testing")
        sleep(2)
        login.is_click(flight['Step05_Save'])
        #存EntitlementID
        entitlementID = drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div[1]/div[3]/table/tbody/tr[1]/td[2]").text
        # step 06
        '''跳转到#/Misc/MaintainAirTraffic/MaintainAssociations页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainAssociations")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step06_New'])
        login.is_click(flight['Step06_Traffic_Route_Id_Click'])
        ruleSetPath = "//span[contains(text(),'"+ruleSetID+"')]"
        print(ruleSetPath)
        drivers.find_element_by_xpath(ruleSetPath).click()
        login.is_click(flight['Step06_Entitlement_Id_Click'])
        entitlementPath = "//div[contains(text(),'"+entitlementID+"')]"+"/parent::*//parent::*//preceding-sibling::*//div"
        print(entitlementPath)
        drivers.find_element_by_xpath(entitlementPath).click()
        login.is_click(flight['Step06_Entitlement_Id_Button'])
        login.input_text(flight['Step06_Remarks'], "UAT Testing")
        sleep(2)
        login.is_click(flight['Step06_Save'])


        # step 07
        '''跳转到#/Misc/MaintainAirTraffic/RuleLogic页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/RuleLogic")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step07_Rule_Set_ID'])
        sleep(1)
        # login.is_click(flight['Step07_Rule_Set'])
        ruleSetIDPath = "//div[contains(text(),'"+ruleSetID+"')]"
        print(ruleSetIDPath)
        drivers.find_element_by_xpath(ruleSetIDPath).click()
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(1)
        login.is_click(flight['Step07_RuleLabel01'])
        sleep(1)
        login.is_click(flight['Step07_RuleLabel01_Click'])
        login.is_click(flight['Step07_RuleLabel01_Entitlements'])
        sleep(1)
        login.is_click(flight['Step07_RuleLabel01_Entitlements_Click'])
        login.is_click(flight['True_Response_Message01'])
        sleep(1)
        login.input_text(flight['True_Response_Message01_Input'], "Route check passed")
        login.is_click(flight['Response_Message_Save01'])
        login.is_click(flight['False_Response_Message01'])
        sleep(1)
        login.input_text(flight['False_Response_Message01_Input'], "Route check failed")
        login.is_click(flight['Response_Message_Save01'])
        sleep(2)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(1)
        login.is_click(flight['Step07_RuleLabel02'])
        login.is_click(flight['Step07_RuleLabel02_Click'])
        login.is_click(flight['Step07_RuleLabel02_Entitlements'])
        login.is_click(flight['Step07_RuleLabel02_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel02_True_Mag'])
        login.input_text(flight['Step07_RuleLabel02_True_Res'], 'No. Flight check passed')
        sleep(1)
        login.is_click(flight['Step07_RuleLabel02_True_Save'])
        login.is_click(flight['Step07_RuleLabel02_False_Mag'])
        login.input_text(flight['Step07_RuleLabel02_False_Res'], 'No. Flight check failed')
        sleep(1)
        login.is_click(flight['Step07_RuleLabel02_False_Save'])
        sleep(1)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        login.is_click(flight['Step07_RuleLabel03'])
        login.is_click(flight['Step07_RuleLabel03_Click'])
        login.is_click(flight['Step07_RuleLabel03_Entitlements'])
        login.is_click(flight['Step07_RuleLabel03_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel03_True_Mag'])
        login.input_text(flight['Step07_RuleLabel03_True_Res'], 'Check Seats No. passed')
        sleep(1)
        login.is_click(flight['Step07_RuleLabel03_True_Save'])
        login.is_click(flight['Step07_RuleLabel03_False_Mag'])
        login.input_text(flight['Step07_RuleLabel03_False_Res'], 'Check Seats No. failed')
        sleep(1)
        login.is_click(flight['Step07_RuleLabel03_False_Save'])
        sleep(1)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        login.is_click(flight['Step07_RuleLabel04'])
        login.is_click(flight['Step07_RuleLabel04_Click'])
        login.is_click(flight['Step07_RuleLabel04_Entitlements'])
        login.is_click(flight['Step07_RuleLabel04_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel04_True_Mag'])
        login.input_text(flight['Step07_RuleLabel04_True_Res'], 'Check Consumed seats passed')
        sleep(1)
        login.is_click(flight['Step07_RuleLabel04_True_Save'])
        login.is_click(flight['Step07_RuleLabel04_False_Mag'])
        login.input_text(flight['Step07_RuleLabel04_False_Res'], 'Check Consumed seats failed')
        sleep(1)
        login.is_click(flight['Step07_RuleLabel04_False_Save'])
        sleep(1)
        login.is_click(flight['Step07_True_Res'])
        sleep(1)
        login.input_text(flight['Step07_True_msg'], 'Overall passed')
        sleep(1)
        login.is_click(flight['Step07_True_Save'])
        sleep(1)
        login.is_click(flight['Step07_False_Res'])
        sleep(1)
        login.input_text(flight['Step07_False_msg'], 'Overall failed')
        sleep(1)
        login.is_click(flight['Step07_False_Save'])
        login.is_click(flight['Step07_Save'])
        sleep(1)
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()

        # step 08
        # login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/test_e2e_0201.py'])
