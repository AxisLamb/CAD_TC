#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re
import os
import pytest
import allure
import pywinauto
from selenium.webdriver.common.keys import Keys
import string
import random
from random import randint
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('flight_060')
flightvalue = ElementValue('flightvalue_060')


@allure.feature("TC(ECE)-060 ")
class TestMissNoSeatsError:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Miss inputting mandatory No. of Seats field")
    def test_060(self, drivers):
        """test1: Miss inputting mandatory No. of Seats field"""
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
        sleep(1)

        # step 01
        '''跳转到#/Misc/MaintainAirTraffic/MaintainPort页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainPort")
        sleep(1)
        login.is_click(flight['Step01_New'])
        login.is_click(flight['Step01_Ports'])
        sleep(1)
        login.is_click(flight['Step01_Advanced'])
        login.input_text(flight['Step01_Airport_Code'], "HKG")
        login.is_click(flight['Step01_Search'])
        login.is_click(flight['Step01_Click_Port'])
        login.input_text(flight['Step01_Description'], "Hong Kong Intl Airport")
        sleep(1)
        login.is_click(flight['Step01_Save'])
        sleep(1)
        login.is_click(flight['Step01_Sort'])
        sleep(1)
        login.is_click(flight['Step01_Sort'])
        sleep(1)
        login.is_click(flight['Step01_Preview'])
        sleep(1)
        login.is_click(flight['Step01_Preview_Close'])
        sleep(1)
        # step 02
        login.is_click(flight['Step02_New'])
        login.is_click(flight['Step02_Countries'])
        sleep(1)
        login.is_click(flight['Step02_Advanced'])
        login.input_text(flight['Step02_English_Description'], "Singapore")
        login.is_click(flight['Step02_Search'])
        login.is_click(flight['Step02_Click_Country'])
        login.input_text(flight['Step02_Description'], "All Singapore ports")
        sleep(1)
        login.is_click(flight['Step02_Save'])
        sleep(1)
        login.is_click(flight['Step02_Sort'])
        sleep(1)
        login.is_click(flight['Step02_Sort'])
        sleep(1)
        login.is_click(flight['Step02_Preview'])
        sleep(1)
        login.is_click(flight['Step02_Preview_Close'])

        # step 03
        '''跳转到#/Misc/MaintainAirTraffic/MaintainRuleSets页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainRuleSets")
        drivers.implicitly_wait(30)
        sleep(1)
        login.is_click(flight['Step03_New'])
        login.is_click(flight['Step03_Country_Select'])
        login.input_text(flight['Step03_Country_Input'], "Hong Kong (SAR, China)")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[2]/div/div/div/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step03_Type_Select'])
        login.input_text(flight['Step03_Type_Input'], "All-Cargo")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[4]/div/div/div/div/input").send_keys(
            Keys.ENTER)

        login.input_text(flight['Step03_Remarks'], "Rule for Hong Kong")
        login.is_click(flight['Step03_Save'])

        # step 04
        login.is_click(flight['Step04_Select'])
        login.is_click(flight['Step04_Configure_Route_Definition'])

        login.is_click(flight['Step04_HomePorts'])
        # login.is_click(flight['Step04_HomePorts_Last_Updated_Sort'])
        login.is_click(flight['Step04_HomePorts_Click'])
        login.is_click(flight['Step04_ForeignPorts'])
        # login.is_click(flight['Step04_ForeignPorts_Last_Updated_Sort'])
        login.is_click(flight['Step04_ForeignPorts_Click'])
        login.input_text(flight['Step04_Description'], "HKG- >SIN")
        login.input_text(flight['Step04_Remarks'], "HKG- >SIN")
        sleep(1)
        login.is_click(flight['Step04_Save'])

        # step 05
        '''跳转到#/Misc/MaintainAirTraffic/MaintainEntitlement页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainEntitlement")
        drivers.implicitly_wait(30)
        sleep(1)
        login.is_click(flight['Step05_New'])
        login.is_click(flight['Step05_Frequency_Click'])
        login.input_text(flight['Step05_Frequency'], "5")
        login.is_click(flight['Step05_Cargo_Limit_Click'])
        login.input_text(flight['Step05_Cargo_Limit'], "50000")
        login.is_click(flight['Step05_Per_Flight_Cargo_Limit_Click'])
        login.input_text(flight['Step05_Per_Flight_Cargo_Limit'], "10000")
        login.input_text(flight['Step05_Load_Factor'], "50")
        login.input_text(flight['Step05_Description'], "W:5 Cargo:  PL:50000 PP: 10000")
        login.input_text(flight['Step05_Remarks'], "UAT Testing")
        sleep(2)
        login.is_click(flight['Step05_Save'])

        # step 06
        '''跳转到#/Misc/MaintainAirTraffic/MaintainAssociations页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainAssociations")
        drivers.implicitly_wait(30)
        sleep(1)
        login.is_click(flight['Step06_New'])
        login.is_click(flight['Step06_Traffic_Route_Id_Click'])
        login.is_click(flight['Step06_Traffic_Route_Id'])
        login.is_click(flight['Step06_Entitlement_Id_Click'])
        login.is_click(flight['Step06_Entitlement_Id'])
        login.is_click(flight['Step06_Entitlement_Id_Button'])
        login.input_text(flight['Step06_Remarks'], "UAT Testing")
        sleep(1)
        login.is_click(flight['Step06_Save'])

        # step 07
        '''跳转到#/Misc/MaintainAirTraffic/RuleLogic页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/RuleLogic")
        drivers.implicitly_wait(30)
        sleep(1)
        login.is_click(flight['Step07_Rule_Set_ID'])
        login.is_click(flight['Step07_Rule_Set'])
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        login.is_click(flight['Step07_RuleLabel01'])
        login.is_click(flight['Step07_RuleLabel01_Click'])
        login.is_click(flight['Step07_RuleLabel01_Entitlements'])
        login.is_click(flight['Step07_RuleLabel01_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel01_True_Mag'])
        login.input_text(flight['Step07_RuleLabel01_True_Res'], 'Route check passed')
        sleep(1)
        login.is_click(flight['Step07_RuleLabel01_True_Save'])
        login.is_click(flight['Step07_RuleLabel01_False_Mag'])
        login.input_text(flight['Step07_RuleLabel01_False_Res'], 'Route check failed')
        sleep(1)
        login.is_click(flight['Step07_RuleLabel01_False_Save'])
        sleep(1)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
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

        # step 07 填数据集
        login.is_click(flight["Logout_Yes"])
        login.input_user_name("CPATEST03")
        login.input_user_password("12345678a")
        login.click_login_button()
        sleep(1)
        '''跳转到#/ApplicationView/ExtraSection/CreateExtraSectionAllCargo页面'''
        login.get_url(ini.url + "#/ApplicationView/ExtraSection/CreateExtraSectionAllCargo")
        drivers.implicitly_wait(30)
        sleep(1)

        s = string.ascii_letters
        r = random.choice(s)
        # 航班号用CPA+4位整数和一个随机字母
        Flight_1 = "CPA" + str(randint(1000, 9999)) + r
        Flight_2 = "CPA" + str(randint(1000, 9999)) + r

        # 填第1个飞行数据
        login.input_text(flight['FlightNo_1'], Flight_1)
        login.input_text(flight['From_1'], "01/11/2023")
        login.input_text(flight['To_1'], "31/11/2023")
        login.is_click(flight['DOP_2'])
        login.is_click(flight['DOP_4'])
        login.is_click(flight['DOP_6'])
        login.is_click(flight['Service_Type_input_1'])
        login.input_text(flight['Service_Type_input_1'], "100")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['CargoAmount_1'], "6000")
        login.input_text(flight['Route_1'], "HKG-SIN")
        login.input_text(flight['Table_Remarks'], "test for upload")
        # drivers.find_element_by_xpath(
        #      "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[15]/div/span/div/input").send_keys(
        #     Keys.ENTER)
        # sleep(2)
        login.input_text(flight['LocalTime_STD_1'], "1630")

        # 填第2个飞行数据
        login.input_text(flight['FlightNo_2'], Flight_2)

        login.is_click(flight['Service_Type_input_2'])
        login.input_text(flight['Service_Type_input_2'], "100")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['CargoAmount_2'], "6000")
        login.input_text(flight['Route_2'], "SIN-HKG")
        login.input_text(flight['Table_Remarks'], "test for upload")
        login.input_text(flight['LocalTime_STA_2'], "1930")
        # Remark
        login.input_text(flight['Remarks'], "UAT End2End Testing")
        # Upload file
        login.is_click(flight['Upload_Related_Documents'])
        login.is_click(flight['DOC_Type'])
        login.input_text(flight['DOC_Type'], "Aerodrome Operating Minima")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']").send_keys(
            Keys.ENTER)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        drivers.find_element_by_xpath("//*[@id='testUploadButton']/span/span").click()
        # step 09
        login.is_click(flight['SaveAsTemplate'])
        sleep(1)
        login.input_text(flight['TemplateName'], "TEST" + str(random.randint(1000, 9999)))
        login.input_text(flight['Description'], "Description")
        login.is_click(flight['Template_Save'])
        login.is_click(flight['Confirm'])
        login.is_click(flight['PreviewAndSubmit'])
        login.is_click(flight['BackAndModify1'])
        login.is_click(flight['PreviewAndSubmit'])
        login.is_click(flight['Submit1'])
        drivers.find_element_by_class_name("testConfirmButtonClass013").click()

        # step 12
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name("OFFICER1")
        login.input_user_password("12345678a")
        login.click_login_button()
        sleep(1)
        '''跳转到#/View/Messages页面'''
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        login.is_click(flight['Step12_Advanced_Search'])
        login.is_click(flight['Step12_Charter_Extra'])
        login.is_click(flight['Step12_Search'])

        # step 14
        login.is_click(flight['Step14_Message_Ref_No'])

        # step 15
        login.is_click(flight['Step15_Select_Record'])
        login.is_click(flight['Step15_Check_Traffic_Rights'])
        sleep(8)
        login.is_click(flight['Step15_Check_Traffic_Rights_Yes'])
        sleep(8)
        login.is_click(flight['Step15_Check_Traffic_Rights_Out'])
        # step 16
        login.is_click(flight['Step15_Export'])

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/test_hy60.py'])
