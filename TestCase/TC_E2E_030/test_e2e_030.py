#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import os
import pytest
import allure
from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

import string
import random
from random import randint

s = string.ascii_letters
r = random.choice(s)

flight = Element('flight_030')
flightvalue = ElementValue('flightvalue_030')
account = ElementValue('cad_account')
@allure.feature("TC(ECE)-030 ")
class TestMissNoSeatsError:
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
            login.input_user_name(account['OfficerLoginName'])
            login.input_user_password(account['OfficerPassword'])
            login.click_login_button()
        sleep(25)

        # step 01
        '''跳转到#/Misc/MaintainAirTraffic/MaintainPort页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainPort")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step01_New'])
        login.is_click(flight['Step01_Ports'])
        sleep(10)
        login.is_click(flight['Step01_Advanced'])
        sleep(2)
        login.input_text(flight['Step01_Airport_Code'], "HKG")
        sleep(2)
        login.is_click(flight['Step01_Search'])
        login.is_click(flight['Step01_Click_Port'])
        login.input_text(flight['Step01_Description'], "Hong Kong Intl Airport")
        sleep(2)
        login.is_click(flight['Step01_Save'])
        sleep(2)
        # login.is_click(flight['Step01_Sort'])
        sleep(2)
        # login.is_click(flight['Step01_Sort'])
        login.is_click(flight['Step01_Preview'])
        sleep(5)
        login.is_click(flight['Step01_Preview_Close'])


        # step 02
        login.is_click(flight['Step02_New'])
        login.is_click(flight['Step02_Countries'])
        sleep(10)
        login.is_click(flight['Step02_Advanced'])
        login.input_text(flight['Step02_English_Description'], "India")
        login.is_click(flight['Step02_Search'])
        login.is_click(flight['Step02_Click_Country'])
        login.input_text(flight['Step02_Description'], "All India ports")
        sleep(2)
        login.is_click(flight['Step02_Save'])
        sleep(2)
        # login.is_click(flight['Step02_Sort'])
        sleep(2)
        # login.is_click(flight['Step02_Sort'])
        login.is_click(flight['Step02_Preview'])
        sleep(5)
        login.is_click(flight['Step02_Preview_Close'])
        sleep(2)

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
        login.input_text(flight['Step03_Type_Input'], "Pass")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[4]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['Step03_Remarks'], "Rule for Hong Kong")
        sleep(2)
        login.is_click(flight['Step03_Save'])

        # step 04
        sleep(4)
        login.is_click(flight['Step04_Select'])
        login.is_click(flight['Step04_Configure_Route_Definition'])

        login.is_click(flight['Step04_HomePorts'])
        # login.is_click(flight['Step04_HomePorts_Last_Updated_Sort'])
        login.is_click(flight['Step04_HomePorts_Click'])
        login.is_click(flight['Step04_ForeignPorts'])
        # login.is_click(flight['Step04_ForeignPorts_Last_Updated_Sort'])
        login.is_click(flight['Step04_ForeignPorts_Click'])
        login.input_text(flight['Step04_Description'], "HKG- > IN")
        login.input_text(flight['Step04_Remarks'], "HKG- > IN")
        sleep(2)
        login.is_click(flight['Step04_Save'])

        # step 05
        '''跳转到#/Misc/MaintainAirTraffic/MaintainEntitlement页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainEntitlement")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step05_New'])
        login.is_click(flight['Step05_Frequency_Click'])
        login.input_text(flight['Step05_Frequency'], "5")
        login.is_click(flight['Step05_Passenger_Limit_Click'])
        login.input_text(flight['Step05_Passenger_Limit'], "500")
        login.is_click(flight['Step05_Per_Flight_Passenger_Limit_Click'])
        login.input_text(flight['Step05_Per_Flight_Passenger_Limit'], "100")
        login.input_text(flight['Step05_Load_Factor'], "50")
        login.input_text(flight['Step05_Description'], "W:5 PAX:  PL:500 PP: 100")
        login.input_text(flight['Step05_Remarks'], "UAT Testing")
        sleep(2)
        login.is_click(flight['Step05_Save'])


        # step 06
        '''跳转到#/Misc/MaintainAirTraffic/MaintainAssociations页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainAssociations")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step06_New'])
        sleep(2)
        login.is_click(flight['Step06_Traffic_Route_Id_Click'])
        login.is_click(flight['Step06_Traffic_Route_Id'])
        login.is_click(flight['Step06_Entitlement_Id_Click'])
        login.is_click(flight['Step06_Entitlement_Id'])
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
        login.is_click(flight['Step07_Rule_Set'])
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01'])
        login.is_click(flight['Step07_RuleLabel01_Click'])
        login.is_click(flight['Step07_RuleLabel01_Entitlements'])
        login.is_click(flight['Step07_RuleLabel01_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel01_True_Mag'])
        login.input_text(flight['Step07_RuleLabel01_True_Res'], 'Route check passed')
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01_True_Save'])
        login.is_click(flight['Step07_RuleLabel01_False_Mag'])
        login.input_text(flight['Step07_RuleLabel01_False_Res'], 'Route check failed')
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01_False_Save'])
        sleep(2)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel02'])
        login.is_click(flight['Step07_RuleLabel02_Click'])
        login.is_click(flight['Step07_RuleLabel02_Entitlements'])
        login.is_click(flight['Step07_RuleLabel02_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel02_True_Mag'])
        login.input_text(flight['Step07_RuleLabel02_True_Res'], 'No. Flight check passed')
        sleep(2)
        login.is_click(flight['Step07_RuleLabel02_True_Save'])
        login.is_click(flight['Step07_RuleLabel02_False_Mag'])
        login.input_text(flight['Step07_RuleLabel02_False_Res'], 'No. Flight check failed')
        sleep(2)
        login.is_click(flight['Step07_RuleLabel02_False_Save'])
        sleep(2)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel03'])
        login.is_click(flight['Step07_RuleLabel03_Click'])
        login.is_click(flight['Step07_RuleLabel03_Entitlements'])
        login.is_click(flight['Step07_RuleLabel03_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel03_True_Mag'])
        login.input_text(flight['Step07_RuleLabel03_True_Res'], 'Check Seats No. passed')
        sleep(2)
        login.is_click(flight['Step07_RuleLabel03_True_Save'])
        login.is_click(flight['Step07_RuleLabel03_False_Mag'])
        login.input_text(flight['Step07_RuleLabel03_False_Res'], 'Check Seats No. failed')
        sleep(2)
        login.is_click(flight['Step07_RuleLabel03_False_Save'])
        sleep(2)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel04'])
        login.is_click(flight['Step07_RuleLabel04_Click'])
        login.is_click(flight['Step07_RuleLabel04_Entitlements'])
        login.is_click(flight['Step07_RuleLabel04_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel04_True_Mag'])
        login.input_text(flight['Step07_RuleLabel04_True_Res'], 'Check Consumed seats passed')
        sleep(2)
        login.is_click(flight['Step07_RuleLabel04_True_Save'])
        login.is_click(flight['Step07_RuleLabel04_False_Mag'])
        login.input_text(flight['Step07_RuleLabel04_False_Res'], 'Check Consumed seats failed')
        sleep(2)
        login.is_click(flight['Step07_RuleLabel04_False_Save'])
        sleep(2)
        login.is_click(flight['Step07_True_Res'])
        sleep(2)
        login.is_click(flight['Step07_True_select'])
        sleep(2)
        login.input_text(flight['Step07_True_msg'], 'Overall passed')
        sleep(2)
        login.is_click(flight['Step07_True_Save'])
        sleep(2)
        login.is_click(flight['Step07_False_Res'])
        sleep(2)
        login.is_click(flight['Step07_True_select'])
        sleep(2)
        login.input_text(flight['Step07_False_msg'], 'Overall failed')
        sleep(2)
        login.is_click(flight['Step07_False_Save'])
        login.is_click(flight['Step07_Save'])
        sleep(2)
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        login.is_click(flight["Logout_Yes"])

        # step 08
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(account['CpaOfficerLoginName'])
            login.input_user_password(account['CpaOfficerPassword'])
            login.click_login_button()
        sleep(20)
        '''跳转到#/ApplicationView/CharterFlight/CreateCharterFlight页面'''
        login.get_url(ini.url + "#/ApplicationView/CharterFlight/CreateCharterFlight")
        drivers.implicitly_wait(30)
        sleep(5)
        login.input_text(flight['Registration_mark'], 'HK2023')
        login.is_click(flight['Aircraft_type_select'])
        login.input_text(flight['Aircraft_type_input'], "100")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[5]/div[1]/div/div/div/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Aircraft_nationality_select'])
        login.input_text(flight['Aircraft_nationality_input'], "Hong Kong (SAR, China)")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[5]/div[2]/div/div/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Name_of_charterer'], 'Air Charter Service')
        login.input_text(flight['Address_of_charterer'], '33 Cameron Road Tsim Sha Tsui, Kowloon Hong Kong')
        login.is_click(flight['Local_handling_agent_select'])
        login.input_text(flight['Local_handling_agent_input'], "HKE")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[8]/div/div/div[1]/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Purpose_of_service'], 'Test Traffic Rights')
        login.input_text(flight['Points_of_landing'], 'none')
        sleep(2)
        # line 1
        login.is_click(flight['Service_Type_select'])
        login.input_text(flight['Service_Type_input'], "Charter Pax")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[2]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['FlightNo'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        login.input_text(flight['From'], "01/07/2023")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['To'], "31/07/2023")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['DOP_1'])
        login.is_click(flight['DOP_3'])
        login.is_click(flight['DOP_5'])
        login.input_text(flight['No_of_Pax'], '100')
        login.input_text(flight['Port_From'], 'HKG')
        login.input_text(flight['Port_To'], 'BOM')
        login.input_text(flight['LocalTime_STD'], "1030")
        login.input_text(flight['Table_Remarks'], "UAT Testing1")
        # line2
        login.is_click(flight['Service_Type_select_2'])
        login.input_text(flight['Service_Type_input_2'], "Charter Pax")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[2]/td[1]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['FlightNo_2'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        login.input_text(flight['No_of_Pax_2'], '50')
        login.input_text(flight['Port_From_2'], 'BOM')
        login.input_text(flight['Port_To_2'], 'HKG')
        login.input_text(flight['LocalTime_STA_2'], "1930")
        login.input_text(flight['Table_Remarks_2'], "UAT Testing2")
        login.input_text(flight['Remarks'], "UAT End2End Testing")
        # Upload file
        login.is_click(flight['Upload_Related_Documents'])
        sleep(2)
        login.is_click(flight['Doc_Type_Select'])
        sleep(2)
        login.input_text(flight['Doc_Type_Input'], "Others")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(1)
        # login.is_click(flight['BrowseButton'])
        # sleep(2)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        login.is_click(flight['New_Indefinite'])
        sleep(2)
        login.is_click(flight['UploadButton'])
        sleep(2)


        # step 09
        login.is_click(flight['Step09_Click_Condition'])
        sleep(2)
        login.is_click(flight['Step09_Preview_And_Submit'])
        sleep(2)

        # step 10
        login.is_click(flight['Step10_Click_Submit'])
        sleep(5)
        login.is_click(flight['Step10_Click_Submit_Yes'])
        sleep(2)

        # step 11
        # login.is_click(flight['Step11_Click_No'])
        sleep(2)

        # step 12
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(account['OfficerLoginName'])
            login.input_user_password(account['OfficerPassword'])
            login.click_login_button()
        sleep(20)
        '''跳转到#/View/Messages页面'''
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step12_Advanced_Search'])
        login.is_click(flight['Step12_Charter_Passenger'])
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
        sleep(5)
        login.is_click(flight['Step15_Check_Traffic_Rights_Yes'])

        # step 16
        # login.is_click(flight['Step15_Export'])
        # appp = pywinauto.Desktop()
        # # 选择文件上传的窗口
        # dlgg = appp["另存为"]
        # sleep(2)
        # dlgg["保存(&S)"].click_input()
        # sleep(2)
        # login.is_click(flight['Step15_Select_Record'])

        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_030/test_e2e_030.py'])
