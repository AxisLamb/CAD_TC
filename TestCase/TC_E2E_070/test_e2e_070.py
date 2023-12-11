#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import random
import string
from random import randint

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.readconfig import ini
from common.readelement import Element
from common.readvalue import ElementValue
from page.webpage import sleep
from page_object.LoginPage import LoginPage

flight = Element('flight_070')
flightvalue = ElementValue('flightvalue_070')
@allure.feature("TC(ECE)-070 ")
class TestTrafficRightsInPNR:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Officer Create traffic rights rules and check traffic rights in Private Non-Revenue Application")
    def test_070(self, drivers):
        # Random flight number
        s = string.ascii_letters
        r = random.choice(s)
        # 航班号用CPA+4位整数和一个随机字母
        FlightNoA1 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoA2 = "CPA" + str(randint(1000, 9999)) + r

        # TemplateName 随机生成数
        TemplateName = "Test" + str(random.uniform(1, 1000))
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
        waits = WebDriverWait(drivers, 100, 0.8)
        wait20s = WebDriverWait(drivers, 20, 0.8)
        wait20s.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        #step 01:Create port sets by Officer
        '''跳转到#/Misc/MaintainAirTraffic/MaintainPort页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainPort")
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Maintain Port Sets']")))
        sleep(2)
        login.is_click(flight['Step01_New'])
        login.is_click(flight['Step01_Ports'])
        sleep(3)
        login.is_click(flight['Step01_Advanced'])
        sleep(10)
        login.input_text(flight['Step01_English_Name'], "Hong Kong/Hong Kong Intl")
        sleep(10)
        # login.input_text(flight['Step01_Airport_Code'], "HKG")
        login.is_click(flight['Step01_Search'])
        waits.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/div[5]/div/div[3]/table/tbody/tr")))
        sleep(2)
        login.is_click(flight['Step01_Click_Port'])
        login.input_text(flight['Step01_Description'], "Hong Kong Intl Airport")
        sleep(3)
        login.is_click(flight['Step01_Save'])
        sleep(2)
        login.is_click(flight['Step01_Sort'])
        sleep(3)
        login.is_click(flight['Step01_Sort'])
        sleep(3)
        login.is_click(flight['Step01_Preview'])
        sleep(3)
        login.is_click(flight['Step01_Preview_Close'])
        sleep(3)
        # step 02
        login.is_click(flight['Step02_New'])
        login.is_click(flight['Step02_Countries'])
        sleep(3)
        login.is_click(flight['Step02_Advanced'])
        login.input_text(flight['Step02_Country_Code'], "JP")
        login.is_click(flight['Step02_Search'])
        login.is_click(flight['Step02_Click_Country'])
        login.input_text(flight['Step02_Description'], "All Japan ports")
        sleep(3)
        login.is_click(flight['Step02_Save'])
        sleep(3)
        login.is_click(flight['Step02_Sort'])
        sleep(3)
        login.is_click(flight['Step02_Sort'])
        sleep(3)
        login.is_click(flight['Step02_Preview'])
        sleep(3)
        login.is_click(flight['Step02_Preview_Close'])

        # step 03
        '''跳转到#/Misc/MaintainAirTraffic/MaintainRuleSets页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainRuleSets")
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Maintain Traffic Rights Rule Sets']")))
        sleep(2)
        login.is_click(flight['Step03_New'])
        login.is_click(flight['Step03_Country_Select'])
        login.input_text(flight['Step03_Country_Input'], "Hong Kong (SAR, China)")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['Step03_Type_Select'])
        login.input_text(flight['Step03_Type_Input'], "Passegner")
        # login.input_text(flight['Step03_Type_Input'], "Passenger")
        sleep(3)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[4]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Step03_Remarks'], "Rule for Hong Kong")
        login.is_click(flight['Step03_Save'])
        sleep(3)

        # step 04
        login.is_click(flight['Step04_Select'])
        login.is_click(flight['Step04_Configure_Route_Definition'])
        login.is_click(flight['Step04_HomePorts'])
        sleep(2)
        login.is_click(flight['Step04_HomePorts_Last_Updated_Sort'])
        sleep(2)
        login.is_click(flight['Step04_HomePorts_Click'])
        login.is_click(flight['Step04_ForeignPorts'])
        sleep(2)
        login.is_click(flight['Step04_ForeignPorts_Last_Updated_Sort'])
        sleep(2)
        login.is_click(flight['Step04_ForeignPorts_Click'])
        login.input_text(flight['Step04_Description'], "HKG- > JP")
        login.input_text(flight['Step04_Remarks'], "HKG- > JP")
        sleep(3)
        login.is_click(flight['Step04_Save'])

        # step 05
        '''跳转到#/Misc/MaintainAirTraffic/MaintainEntitlement页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainEntitlement")
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Maintain Route Entitlements']")))
        sleep(2)
        login.is_click(flight['Step05_New'])
        sleep(5)
        login.is_click(flight['Step05_Frequency_Click'])
        sleep(3)
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
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Maintain Route Entitlements Associations']")))
        sleep(2)
        login.is_click(flight['Step06_New'])
        login.is_click(flight['Step06_Traffic_Route_Id_Click'])
        sleep(2)
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
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Create Rules Logic']")))
        sleep(2)
        login.is_click(flight['Step07_Rule_Set_ID'])
        login.is_click(flight['Step07_Rule_Set'])
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(10)
        login.is_click(flight['Step07_RuleLabel01'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01_Click'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01_Entitlements'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel01_Entitlements_Click'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel01_True_Mag'])
        login.input_text(flight['Step07_RuleLabel01_True_Res'], 'Route check passed')
        sleep(3)
        login.is_click(flight['Step07_RuleLabel01_True_Save'])
        login.is_click(flight['Step07_RuleLabel01_False_Mag'])
        login.input_text(flight['Step07_RuleLabel01_False_Res'], 'Route check failed')
        sleep(3)
        login.is_click(flight['Step07_RuleLabel01_False_Save'])
        sleep(2)

        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(5)
        login.is_click(flight['Step07_RuleLabel02'])
        login.is_click(flight['Step07_RuleLabel02_Click'])
        login.is_click(flight['Step07_RuleLabel02_Entitlements'])
        login.is_click(flight['Step07_RuleLabel02_Entitlements_Click'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel02_True_Mag'])
        login.input_text(flight['Step07_RuleLabel02_True_Res'], 'No. Flight check passed')
        sleep(3)
        login.is_click(flight['Step07_RuleLabel02_True_Save'])
        login.is_click(flight['Step07_RuleLabel02_False_Mag'])
        login.input_text(flight['Step07_RuleLabel02_False_Res'], 'No. Flight check failed')
        sleep(3)
        login.is_click(flight['Step07_RuleLabel02_False_Save'])

        sleep(2)
        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(5)
        login.is_click(flight['Step07_RuleLabel03'])
        login.is_click(flight['Step07_RuleLabel03_Click'])
        login.is_click(flight['Step07_RuleLabel03_Entitlements'])
        login.is_click(flight['Step07_RuleLabel03_Entitlements_Click'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel03_True_Mag'])
        login.input_text(flight['Step07_RuleLabel03_True_Res'], 'Check Seats No. passed')
        sleep(3)
        login.is_click(flight['Step07_RuleLabel03_True_Save'])
        login.is_click(flight['Step07_RuleLabel03_False_Mag'])
        login.input_text(flight['Step07_RuleLabel03_False_Res'], 'Check Seats No. failed')
        sleep(3)
        login.is_click(flight['Step07_RuleLabel03_False_Save'])
        sleep(2)

        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(5)
        login.is_click(flight['Step07_RuleLabel04'])
        login.is_click(flight['Step07_RuleLabel04_Click'])
        login.is_click(flight['Step07_RuleLabel04_Entitlements'])
        login.is_click(flight['Step07_RuleLabel04_Entitlements_Click'])
        sleep(3)
        login.is_click(flight['Step07_RuleLabel04_True_Mag'])
        login.input_text(flight['Step07_RuleLabel04_True_Res'], 'Check Consumed seats passed')
        sleep(3)
        login.is_click(flight['Step07_RuleLabel04_True_Save'])
        login.is_click(flight['Step07_RuleLabel04_False_Mag'])
        login.input_text(flight['Step07_RuleLabel04_False_Res'], 'Check Consumed seats failed')
        sleep(3)
        login.is_click(flight['Step07_RuleLabel04_False_Save'])
        sleep(2)

        login.is_click(flight['Step07_True_Res'])
        sleep(3)
        login.input_text(flight['Step07_True_msg'], 'Overall passed')
        sleep(3)
        login.is_click(flight['Step07_True_Save'])
        sleep(3)
        login.is_click(flight['Step07_False_Res'])
        sleep(3)
        login.input_text(flight['Step07_False_msg'], 'Overall failed')
        sleep(3)
        login.is_click(flight['Step07_False_Save'])
        sleep(3)
        login.is_click(flight['Step07_Save'])



        # step 08
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name("CPATEST03")
        login.input_user_password("12345678a")
        login.click_login_button()
        wait20s.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到#/ApplicationView/PrivateNonRevenue'''
        login.get_url(ini.url + "#/ApplicationView/PrivateNonRevenue")
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Create Private Non-Revenue Application']")))
        sleep(2)
        login.is_click(flight['Local_Handling_Agent_Select'])
        login.input_text(flight['Local_Handling_Agent_input'], 'CPA')
        drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div/div[1]/div[3]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Registration_mark'], 'HK2023')
        login.is_click(flight['Aircraft_type_select'])
        login.input_text(flight['Aircraft_type_input'], "100")
        drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div/div[1]/div[4]/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['Noise_Standard'])
        login.input_text(flight['Purpose_of_Flight'], "Training")
        login.input_text(flight['No_of_Crew'], '10')
        login.is_click(flight['Aircraft_Fitted_with_TCAS'])
        sleep(2)
        # line 1
        login.is_click(flight['Service_Type_select'])
        login.input_text(flight['Service_Type_input'], "Ferry")
        drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div/div[3]/div/div[3]/table/tbody/tr[1]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo'] ,FlightNoA1)
        login.input_text(flight['Operation_Date'], "31/07/2023")
        drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div/div[3]/div/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_Of_Pax'], "100")
        login.input_text(flight['Port_IATA_From'], 'HKG')
        login.input_text(flight['Port_IATA_To'], 'NRT')
        login.input_text(flight['LocalTime_STD'], "1030")
        login.input_text(flight['Table_Remarks'], "AT End2End Testing")
        # line2
        login.is_click(flight['Service_Type_select_2'])
        login.input_text(flight['Service_Type_input_2'], "Ferry")
        drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div/div[3]/div/div[3]/table/tbody/tr[2]/td[1]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_2'] ,FlightNoA2)
        sleep(2)
        login.is_click(flight['InOut_Flight_Diff_Select_2'])
        login.input_text(flight['InOut_Flight_Diff_2'], '1')
        drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div/div[3]/div/div[3]/table/tbody/tr[2]/td[3]/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(3)
        login.input_text(flight['No_of_Pax_2'], '50')
        login.input_text(flight['Port_From_2'], 'NRT')
        login.input_text(flight['Port_To_2'], 'HKG')
        login.input_text(flight['LocalTime_STA_2'], "1930")
        login.input_text(flight['Table_Remarks_2'], "AT End2End Testing")
        login.input_text(flight['Remarks'], "UAT End2End Testing")
        sleep(2)
        # Upload file
        login.is_click(flight['Upload_Related_Documents'])
        sleep(2)
        login.is_click(flight['Doc_Type_Input'])
        sleep(2)
        login.input_text(flight['Doc_Type_Input'], "Aerodrome Operating Minima")
        sleep(3)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # 使用pywinauto来选择文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("/html/body/div[9]/div/div[2]/form/div[1]/div/div/div/span/div[2]/div/div/input").send_keys(file_path)
        sleep(2)
        login.is_click(flight['UploadButton'])
        sleep(2)

        # step 09
        login.is_click(flight['Step09_Click_Confirm'])
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
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name("OFFICER1")
        login.input_user_password("12345678a")
        login.click_login_button()
        wait20s.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到#/View/Messages页面'''
        login.get_url(ini.url + "#/View/Messages")
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Messages']")))
        login.is_click(flight['Step12_Advanced_Search'])
        login.input_text(flight['Step12_ViewMessages_Sender'], "CPATEST03")
        login.is_click(flight['Step12_PNR'])
        login.is_click(flight['Step12_Search'])
        sleep(2)

        # step 14
        login.is_click(flight['Step14_Message_Ref_No'])

        # step 15
        login.is_click(flight['Step15_Select_Record'])
        login.is_click(flight['Step15_Check_Traffic_Rights'])
        sleep(5)
        drivers.implicitly_wait(10)
        login.is_click(flight['Step15_Check_Traffic_Rights_Export'])
        sleep(5)
        login.is_click(flight['Step15_Check_Traffic_Rights_Discard'])
        sleep(5)
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_070/test_e2e_070.py'])
