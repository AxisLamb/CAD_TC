#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
import os
import string
import random
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('flight_010')
flightvalue = ElementValue('flightvalue_010')
flightAccValue = ElementValue('cad_account')

s = string.ascii_letters
r = random.choice(s)
#航班号用CPA+4位整数和一个随机字母
Flight_1 = "CPA"+str(randint(1000, 9999))+r
Flight_2 = "CPA"+str(randint(1000, 9999))+r

@allure.feature("TC(ECE)-010 ")
class TestMissNoSeatsError:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Miss inputting mandatory No. of Seats field")
    def test_030(self, drivers):
        # login AS Officer
        login = LoginPage(drivers)

        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightAccValue['OfficerLoginName'])
            login.input_user_password(flightAccValue['OfficerPassword'])
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
        login.input_text(flight['Step01_Airport_Code'], "HKG")
        login.is_click(flight['Step01_Search'])
        login.is_click(flight['Step01_Click_Port'])
        login.input_text(flight['Step01_Description'], "Hong Kong Intl Airport")
        sleep(2)
        login.is_click(flight['Step01_Save'])
        sleep(2)
        login.is_click(flight['Step01_Sort'])
        sleep(2)
        login.is_click(flight['Step01_Sort'])
        sleep(2)
        login.is_click(flight['Step01_Preview'])
        sleep(5)
        login.is_click(flight['Step01_Preview_Close'])
        sleep(1)

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
        login.is_click(flight['Step02_Preview'])
        sleep(5)
        login.is_click(flight['Step02_Preview_Close'])
        sleep(1)

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
        sleep(2)

        # # step 04
        login.is_click(flight['Step04_RuleSetsId_Sort'])
        login.is_click(flight['Step04_Select'])
        login.is_click(flight['Step04_Configure_Route_Definition'])

        login.is_click(flight['Step04_HomePorts'])
        login.is_click(flight['Step04_HomePorts_Last_Updated_Sort'])
        login.is_click(flight['Step04_HomePorts_Click'])
        login.is_click(flight['Step04_ForeignPorts'])
        # login.is_click(flight['Step04_ForeignPorts_Last_Updated_Sort'])
        sleep(3)
        login.is_click(flight['Step04_ForeignPorts_Click'])
        login.input_text(flight['Step04_Description'], "HKG- > SIN")
        login.input_text(flight['Step04_Remarks'], "HKG- > SIN")
        sleep(2)
        login.is_click(flight['Step04_Save'])
        sleep(2)

        # # step 05
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
        sleep(2)

        # step 06
        '''跳转到#/Misc/MaintainAirTraffic/MaintainAssociations页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainAssociations")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step06_New'])
        login.is_click(flight['Step06_Traffic_Route_Id_Click'])
        login.is_click(flight['Step06_Traffic_Route_Id'])
        login.is_click(flight['Step06_Entitlement_Id_Click'])
        login.is_click(flight['Step06_Entitlement_Id'])
        login.is_click(flight['Step06_Entitlement_Id_Button'])
        login.input_text(flight['Step06_Remarks'], "UAT Testing")
        sleep(2)
        login.is_click(flight['Step06_Save'])
        sleep(2)

        # step 07
        '''跳转到#/Misc/MaintainAirTraffic/RuleLogic页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/RuleLogic")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step07_Rule_Set_ID'])
        login.is_click(flight['Step07_Rule_Set'])
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel01'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel01_Click'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01_Entitlements'])
        sleep(4)
        login.is_click(flight['Step07_RuleLabel01_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel01_True_Response'])
        login.input_text(flight['Step07_RuleLabel01_Edit_Response_Input'], "Route check passed")
        sleep(1)
        login.is_click(flight['Step07_RuleLabel01_Edit_Response_Save'])
        sleep(1)
        login.is_click(flight['Step07_RuleLabel01_False_Response'])
        login.input_text(flight['Step07_RuleLabel01_Edit_Response_Input'], "Route check failed")
        sleep(1)
        login.is_click(flight['Step07_RuleLabel01_Edit_Response_Save'])
        sleep(1)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel02'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel02_Click'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel02_Entitlements'])
        login.is_click(flight['Step07_RuleLabel02_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel02_True_Response'])
        login.input_text(flight['Step07_RuleLabel02_Edit_Response_Input'], "No. Flight check passed")
        sleep(1)
        login.is_click(flight['Step07_RuleLabel02_Edit_Response_Save'])
        login.is_click(flight['Step07_RuleLabel02_False_Response'])
        login.input_text(flight['Step07_RuleLabel02_Edit_Response_Input'], "No. Flight check failed")
        sleep(1)
        login.is_click(flight['Step07_RuleLabel02_Edit_Response_Save'])
        sleep(1)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(3)

        login.is_click(flight['Step07_RuleLabel03'])
        sleep(3)

        login.is_click(flight['Step07_RuleLabel03_Click'])
        sleep(3)

        login.is_click(flight['Step07_RuleLabel03_Entitlements'])
        login.is_click(flight['Step07_RuleLabel03_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel03_True_Response'])
        login.input_text(flight['Step07_RuleLabel03_Edit_Response_Input'], "Check Seats No. passed")
        sleep(1)
        login.is_click(flight['Step07_RuleLabel03_Edit_Response_Save'])
        login.is_click(flight['Step07_RuleLabel03_False_Response'])
        login.input_text(flight['Step07_RuleLabel03_Edit_Response_Input'], "Check Seats No. failed")
        sleep(1)
        login.is_click(flight['Step07_RuleLabel03_Edit_Response_Save'])
        sleep(1)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel04'])
        login.is_click(flight['Step07_RuleLabel04_Click'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel04_Entitlements'])
        login.is_click(flight['Step07_RuleLabel04_Entitlements_Click'])
        login.is_click(flight['Step07_RuleLabel04_True_Response'])
        login.input_text(flight['Step07_RuleLabel04_Edit_Response_Input'], "Check Consumed seats passed")
        sleep(1)
        login.is_click(flight['Step07_RuleLabel04_Edit_Response_Save'])
        login.is_click(flight['Step07_RuleLabel04_False_Response'])
        login.input_text(flight['Step07_RuleLabel04_Edit_Response_Input'], "Check Consumed seats failed")
        sleep(1)
        login.is_click(flight['Step07_RuleLabel04_Edit_Response_Save'])
        sleep(1)
        login.is_click(flight['Step07_True_Response'])
        login.input_text(flight['Step07_True_Response_Input'], "Overall passed")
        sleep(1)
        login.is_click(flight['Step07_True_Response_Save'])
        login.is_click(flight['Step07_False_Response'])
        login.input_text(flight['Step07_False_Response_Input'], "Overall failed")
        sleep(1)
        login.is_click(flight['Step07_False_Response_Save'])
        sleep(1)
        login.is_click(flight['Step07_Save'])
        sleep(2)

        # step 08
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        login.is_click(flight["Logout_Yes"])

        # login Local Operator (CPA)
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightAccValue['CpaOfficerLoginName'])
            login.input_user_password(flightAccValue['CpaOfficerPassword'])
            login.click_login_button()

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        # sleep(20)
        '''跳转到#/ApplicationView/SeasonalSchedule/AddPassengerInfo页面'''
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(5)
        login.input_text(flight['FlightNo'], Flight_1)
        login.input_text(flight['FlightNo_2'], Flight_2)

        login.is_click(flight['Aircraft_Type'])
        login.input_text(flight['Aircraft_Type'], "100")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['No_of_Pax'], "100")
        login.input_text(flight['Route'], "HKG-SIN")
        login.is_click(flight['CPA'])
        login.input_text(flight['STD'], "1030")
        # line2
        # login.input_text(flight['In-out_Flight_Diff'], "0")
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/input").send_keys(
        #     Keys.ENTER)
        login.is_click(flight['Aircraft_Type_2'])
        login.input_text(flight['Aircraft_Type_2'], "100")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['No_of_Pax_2'], "100")
        login.input_text(flight['Route_2'], "SIN-HKG")
        login.is_click(flight['CPA'])
        login.input_text(flight['STA_2'], "1930")

        login.input_text(flight['From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.input_text(flight['To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.is_click(flight['DOP_1'])
        login.is_click(flight['DOP_3'])
        login.is_click(flight['DOP_5'])

        login.input_text(flight['Remarks'], "UAT End2End Testing")
        # Upload file
        login.is_click(flight['Upload_Related_Documents'])
        sleep(2)
        login.is_click(flight['Doc_Type_Select'])
        sleep(1)
        login.input_text(flight['Doc_Type_Select'], "Others")
        sleep(1)
        drivers.find_element_by_xpath(
            "/html/body/div[7]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        # login.is_click(flight['BrowseButton'])
        # sleep(2)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(1)
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

        # step 11
        login.is_click(flight['Step11_Click_No'])
        sleep(2)

        # step 12
        login.is_click(flight['Step12_Click_No'])
        sleep(3)

        # step 13
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()

        login.is_click(flight["Logout_Yes"])

        # login Local Operator (CPA)
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightAccValue['OfficerLoginName'])
            login.input_user_password(flightAccValue['OfficerPassword'])
            login.click_login_button()

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        '''跳转到#/View/Messages页面'''
        login.is_click(flight['Home'])
        sleep(1)
        login.is_click(flight['Message'])
        sleep(1)
        # 搜索最新流程
        login.is_click(flight['AdvancedSearch'])
        sleep(1)
        login.is_click(flight['ScheduledPassenger'])
        sleep(1)
        login.is_click(flight['SearchButton'])
        sleep(1)
        # 选中最新流程
        login.is_click(flight['Subject'])
        sleep(1)
        # 跳转流程页面
        login.is_click(flight['ReferenceNo'])
        sleep(1)

        # step 16
        login.is_click(flight['FlightSchedules'])
        login.is_click(flight['CheckTrafficRights'])
        sleep(10)
        login.is_click(flight['CheckTrafficRightsExport'])
        sleep(5)
        login.is_click(flight['CheckTrafficRightsClose'])
        sleep(5)
        # appp = pywinauto.Desktop()
        # # 选择文件上传的窗口
        # dlgg = appp["另存为"]
        # sleep(2)
        # dlgg["保存(&S)"].click_input()
        # sleep(2)
        # login.is_click(flight['Step15_Select_Record'])
        #
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()

        login.is_click(flight["Logout_Yes"])
        #
        # # missing to input seat no.
        # sleep(999)
        # drivers.implicitly_wait(30)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_010/test_check_traffic_rights.py'])
