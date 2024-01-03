#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging
import os
import string
import random
from random import randint
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from utils.logger import log

flight = Element('flight_011')
flightvalue = ElementValue('flightvalue_011')
CadAccountValue= ElementValue('cad_account')
@allure.feature("TC(E2E)-011 Local Operator Create and Officer Processing Scheduled All-Cargo Application (Approve)")
class TestSchedulePassengerApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create Scheduled All-Cargo Application and approve")
    def test_001(self, drivers):
        # Random flight number
        s = string.ascii_letters
        r = random.choice(s)
        # 航班号用CPA+4位整数和一个随机字母
        FlightNoA1 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoA2 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoB1 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoB2 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoC1 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoC2 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoD1 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoD2 = "CPA" + str(randint(1000, 9999)) + r
        FlightNoE1 = "CPA" + str(randint(1000, 9999)) + r

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
            login.input_user_name(CadAccountValue['CpaOfficerLoginName'])
            login.input_user_password(CadAccountValue['CpaOfficerPassword'])
            login.click_login_button()
        waits = WebDriverWait(drivers, 100, 0.8)
        wait20s = WebDriverWait(drivers, 20, 0.8)

        wait20s.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Messages']")))
        #跳转到Application-Seasonal Schedule-passenger页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Create Seasonal Schedule All-Cargo Application']")))
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule All-Cargo Application"

        #填写Flight Schedules表格信息 Start
        # A1行
        login.input_text(flight['FlightNoA1'], FlightNoA1)
        login.input_text(flight['From_A1'], "01/11/2023")
        login.input_text(flight['To_A1'], "30/11/2023")
        login.is_click(flight['DOP_1_A1'])
        login.is_click(flight['DOP_3_A1'])
        login.is_click(flight['DOP_5_A1'])
        login.is_click(flight['AircraftType_Select_A1'])
        sleep(2)
        login.input_text(flight['AircraftType_input_A1'], "77F")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_A1'])
        login.input_text(flight['CargoCapacityKg_input_A1'], "5000")
        login.input_text(flight['Route_A1'], "HKG-LAX")
        login.is_click(flight['LocalTime_STD_A1'])
        login.input_text(flight['LocalTime_STD_A1'], "1030")
        sleep(2)
        login.input_text(flight['Remarks_A1'], "UAT End2End Testing 1")

        # A2行
        login.input_text(flight['FlightNoA2'], FlightNoA2)
        login.is_click(flight['FlightDiff_Select_A2'])
        sleep(2)
        login.input_text(flight['FlightDiff_input_A2'], "0")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select_A2'])
        sleep(2)
        login.input_text(flight['AircraftType_input_A2'], "77F")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_A2'])
        login.input_text(flight['CargoCapacityKg_input_A2'], "5000")
        login.input_text(flight['Route_A2'], "LAX-HKG")
        login.is_click(flight['LocalTime_STA_A2'])
        login.input_text(flight['LocalTime_STA_A2'], "1930")
        login.input_text(flight['Remarks_A2'], "UAT End2End Testing 2")
        sleep(2)

        # B1行
        login.input_text(flight['FlightNoB1'], FlightNoB1)
        login.input_text(flight['From_B1'], "01/11/2023")
        login.input_text(flight['To_B1'], "30/11/2023")
        login.is_click(flight['DOP_1_B1'])
        login.is_click(flight['DOP_3_B1'])
        login.is_click(flight['DOP_5_B1'])
        login.is_click(flight['DOP_7_B1'])
        login.is_click(flight['AircraftType_Select_B1'])
        sleep(2)
        login.input_text(flight['AircraftType_input_B1'], "M1F")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_B1'])
        login.input_text(flight['CargoCapacityKg_input_B1'], "6000")
        login.input_text(flight['Route_B1'], "HKG-TPE")
        login.is_click(flight['LocalTime_STD_B1'])
        login.input_text(flight['LocalTime_STD_B1'], "1050")
        sleep(2)
        login.is_click(flight['PCCL_B1'])
        login.input_text(flight['Remarks_B1'], "UAT End2End Testing 3")
        sleep(2)

        # B2行
        login.input_text(flight['FlightNoB2'], FlightNoB2)
        login.is_click(flight['FlightDiff_Select_B2'])
        sleep(2)
        login.input_text(flight['FlightDiff_input_B2'], "0")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select_B2'])
        sleep(2)
        login.input_text(flight['AircraftType_input_B2'], "M1F")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_B2'])
        login.input_text(flight['CargoCapacityKg_input_B2'], "6000")
        login.input_text(flight['Route_B2'], "TPE-HKG")
        login.is_click(flight['LocalTime_STA_B2'])
        login.input_text(flight['LocalTime_STA_B2'], "1600")
        login.is_click(flight['PCCL_B2'])
        login.input_text(flight['Remarks_B2'], "UAT End2End Testing 4")
        sleep(2)

        # C1行
        login.input_text(flight['FlightNoC1'], FlightNoC1)
        login.input_text(flight['From_C1'], "01/11/2023")
        login.input_text(flight['To_C1'], "30/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[5]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_2_C1'])
        login.is_click(flight['DOP_4_C1'])
        login.is_click(flight['DOP_6_C1'])
        login.is_click(flight['AircraftType_Select_C1'])
        sleep(2)
        login.input_text(flight['AircraftType_input_C1'], "ABY")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[5]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_C1'])
        login.input_text(flight['CargoCapacityKg_input_C1'], "10000")
        login.input_text(flight['Route_C1'], "HKG-CDG")
        login.is_click(flight['LocalTime_STD_C1'])
        login.input_text(flight['LocalTime_STD_C1'], "1230")
        login.input_text(flight['Remarks_C1'], "UAT End2End Testing 5")
        sleep(2)

        # C2行
        login.input_text(flight['FlightNoC2'], FlightNoC2)
        login.is_click(flight['FlightDiff_Select_C2'])
        sleep(2)
        login.input_text(flight['FlightDiff_input_C2'], "1")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select_C2'])
        sleep(2)
        login.input_text(flight['AircraftType_input_C2'], "ABY")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[6]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_C2'])
        login.input_text(flight['CargoCapacityKg_input_C2'], "10000")
        login.input_text(flight['Route_C2'], "CDG-HKG")
        login.is_click(flight['LocalTime_STA_C2'])
        login.input_text(flight['LocalTime_STA_C2'], "1800")
        login.input_text(flight['Remarks_C2'], "UAT End2End Testing 6")
        sleep(2)

        # D1行
        login.input_text(flight['FlightNoD1'], FlightNoD1)
        login.input_text(flight['From_D1'], "01/11/2023")
        login.input_text(flight['To_D1'], "30/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[7]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        sleep(3)
        login.is_click(flight['DOP_1_D1'])
        login.is_click(flight['DOP_3_D1'])
        login.is_click(flight['DOP_5_D1'])
        login.is_click(flight['AircraftType_Select_D1'])
        sleep(2)
        login.input_text(flight['AircraftType_input_D1'], "77F")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[7]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_D1'])
        login.input_text(flight['CargoCapacityKg_input_D1'], "10000")
        login.input_text(flight['Route_D1'], "HKG-LHR")
        login.is_click(flight['LocalTime_STD_D1'])
        login.input_text(flight['LocalTime_STD_D1'], "0930")
        login.input_text(flight['Remarks_D1'], "UAT End2End Testing 7")
        sleep(2)

        # D2行
        login.input_text(flight['FlightNoD2'], FlightNoD2)
        login.is_click(flight['FlightDiff_Select_D2'])
        sleep(2)
        login.input_text(flight['FlightDiff_input_D2'], "0")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[8]/td[2]/div/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select_D2'])
        sleep(2)
        login.input_text(flight['AircraftType_input_D2'], "77F")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[8]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_D2'])
        login.input_text(flight['CargoCapacityKg_input_D2'], "10000")
        login.input_text(flight['Route_D2'], "LHR-HKG")
        login.is_click(flight['LocalTime_STA_D2'])
        login.input_text(flight['LocalTime_STA_D2'], "0500")
        login.input_text(flight['Remarks_D2'], "UAT End2End Testing 8")
        sleep(2)

        # E1行
        login.input_text(flight['FlightNoE1'], FlightNoE1)
        login.input_text(flight['From_E1'], "01/11/2023")
        login.input_text(flight['To_E1'], "30/11/2023")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[9]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_2_E1'])
        login.is_click(flight['DOP_4_E1'])
        login.is_click(flight['AircraftType_Select_E1'])
        sleep(2)
        login.input_text(flight['AircraftType_input_E1'], "76Y")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[9]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_E1'])
        login.input_text(flight['CargoCapacityKg_input_E1'], "5000")
        login.input_text(flight['Route_E1'], "SIN-HKG-LAX")
        login.is_click(flight['LocalTime_STD_E1'])
        login.input_text(flight['LocalTime_STD_E1'], "1230")
        login.is_click(flight['LocalTime_STA_E1'])
        login.input_text(flight['LocalTime_STA_E1'], "1530")
        login.is_click(flight['NextDate_Select_E1'])
        sleep(2)
        login.input_text(flight['NextDate_input_E1'], "1")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[9]/td[18]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Remarks_E1'], "UAT End2End Testing 9")
        sleep(2)
        # 填写Flight Schedules表格信息 End

        login.input_text(flight['Remarks'], "UAT End2End Testing")

        # Upload Document Start
        sleep(2)
        login.is_click(flight['Upload_Application_Related_Documents'])
        sleep(5)
        login.is_click(flight['Upload_Application_Related_Documents_Type_input'])
        sleep(2)
        login.input_text(flight['Upload_Application_Related_Documents_Type_input'], "Others")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # 使用pywinauto来选择文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight['Upload_Application_Related_Documents_Expiry_Date'], "31/12/2023")
        sleep(2)
        login.is_click(flight['Upload_Application_Related_Documents_Btn'])
        sleep(5)
        # Upload Document End

        login.is_click(flight['SaveAsDraft'])
        sleep(3)
        assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'
        login.is_click(flight['SaveAsTemplate'])
        sleep(3)
        login.input_text(flight['TemplateName'], TemplateName)
        login.input_text(flight['Description'], "Description")
        sleep(2)
        login.is_click(flight['Template_Save'])
        sleep(3)
        # assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'

        login.is_click(flight['Confirm'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(5)
        login.is_click(flight['BackAndModify'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(5)
        login.is_click(flight['Submit'])
        try:
            login.is_click(flight['Proceed'])
            sleep(3)
        except:
            print("Proceed button not exist")
        waits.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'testConfirmButtonClass016')]")))
        login.is_click(flight['Submit_Yes'])
        sleep(5)

        login.is_click(flight['LessorOperatorName_Select'])
        sleep(5)
        login.input_text(flight['LessorOperatorName_input'], "HDA")
        sleep(5)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['LessorOperatorName'], "HDA")
        login.input_text(flight['EffectivePeriod1'], "01/11/2023")
        sleep(3)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['EffectivePeriod2'], "31/12/2023")
        sleep(3)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input").send_keys(Keys.ENTER)

        # Add Supporting Documents
        login.is_click(flight['Supporting_Document_Add'])
        sleep(2)
        login.is_click(flight['DocumentType_Input'])
        sleep(2)
        login.input_text(flight['DocumentType_Input'], "Aerodrome Operating Minima")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testDocumentTypeLease']").send_keys(Keys.ENTER)
        sleep(2)
        # 使用pywinauto来选择文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/End to End Lease Aircraft.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight['DocumentType_Remarks'], "End to End lease aircraft")
        sleep(2)
        login.is_click(flight['DocumentType_Upload'])
        sleep(2)

        login.input_text(flight['RegistrationMark'], "HK2023")
        sleep(2)
        login.is_click(flight['AircraftType_input2'])
        sleep(2)
        login.input_text(flight['AircraftType_input2'], "77F")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[8]/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['AircraftType_Add_Document'])
        sleep(2)
        login.is_click(flight['AircraftType_Upload_Document_input'])
        sleep(2)
        login.input_text(flight['AircraftType_Upload_Document_input'], "Operation Specification (Lessor)")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testDocumentTypeLease']").send_keys(Keys.ENTER)
        sleep(5)
        # 使用pywinauto来选择文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/End to End Lease Aircraft_1.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight['AircraftType_Upload_Document_Remarks'], "UAT End2End Testing")
        sleep(3)
        login.is_click(flight['AircraftType_Upload_Document_Upload'])
        sleep(3)

        login.is_click(flight['LeaseAircraftOperation_Submit'])
        sleep(3)
        login.is_click(flight['LeaseAircraftSubmit'])
        sleep(3)
        login.is_click(flight['LeaseAircraftOK'])
        sleep(5)

        # 从CPATEST03用户到 Officer1用户切换
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(CadAccountValue['OfficerLoginName'])
        login.input_user_password(CadAccountValue['OfficerPassword'])
        login.click_login_button()
        wait20s.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        #跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Messages']")))
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        login.input_text(flight['ViewMessages_Sender'], CadAccountValue['CpaOfficerLoginName'])
        login.is_click(flight['ViewMessages_ApplicationType'])
        login.is_click(flight['ViewMessages_Search'])
        sleep(2)
        login.is_click(flight['ViewMessages_ReferenceNo'])
        sleep(2)

        #viewMessage页面相关按钮操作
        login.is_click(flight['ViewMessages_Basic_Modify'])
        sleep(2)
        login.is_click(flight['ViewMessages_Basic_Save'])
        sleep(2)
        login.is_click(flight['ViewMessages_Basic_Save_OK'])

        #Update flight Schedule Start
        login.is_click(flight['ViewMessages_Schedule_Item'])
        sleep(2)
        login.is_click(flight['ViewMessages_Schedule_Modify'])
        sleep(5)
        login.is_click(flight['Update_Schedule_DOP_1'])
        sleep(2)
        login.is_click(flight['Update_Schedule_DOP_2'])
        sleep(2)
        login.is_click(flight['Update_Schedule_DOP_3'])
        sleep(2)
        login.is_click(flight['Update_Schedule_DOP_4'])
        sleep(2)
        login.is_click(flight['Update_Schedule_DOP_5'])
        sleep(2)
        login.is_click(flight['Update_Schedule_DOP_6'])
        sleep(6)
        # 删除原有的AircraftType 77F, 修改为ABY
        # login.is_click(flight['Update_Schedule_AircraftType_Select'])
        # sleep(6)
        # login.is_click(flight['Update_Schedule_AircraftType_Select'])
        login.is_click(flight['Update_Schedule_AircraftType_input'])
        sleep(6)
        login.input_text(flight['Update_Schedule_AircraftType_input'], "ABY")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['Update_Schedule_CargoCapacityKg_input'], "6000")
        sleep(2)
        login.input_text(flight['Update_Schedule_STD_input'], "1630")
        sleep(2)
        login.is_click(flight['Update_Schedule_EB'])
        sleep(2)
        login.is_click(flight['Update_Schedule_PCCL'])
        sleep(3)
        login.input_text(flight['Update_Schedule_Remarks_input'], "Test for update")
        sleep(3)
        login.is_click(flight['Update_Schedule_Save'])
        sleep(5)
        # Update flight Schedule End

        # ViewMessage ViewMessages_Select_from_Document_Library Start
        login.is_click(flight['ViewMessages_Select_from_Document_Library'])
        sleep(3)
        login.is_click(flight['ViewMessages_Select_from_Document_Library_Operator'])
        sleep(3)
        login.is_click(flight['ViewMessages_Select_from_Document_Library_Search'])
        sleep(3)
        login.is_click(flight['ViewMessages_Select_from_Document_Library_Item'])
        sleep(3)
        login.is_click(flight['ViewMessages_Select_from_Document_Library_Confirm'])
        sleep(3)
        # ViewMessage ViewMessages_Select_from_Document_Library End

        # ViewMessage  Click "Upload" in newly submitted documents section Start
        login.is_click(flight['ViewMessages_Upload'])
        sleep(3)
        login.is_click(flight['ViewMessages_Upload_Lease_Aircraft'])
        sleep(3)
        login.is_click(flight['ViewMessages_Upload_Lessor_Operator_Select'])
        sleep(3)
        login.input_text(flight['ViewMessages_Upload_Lessor_Operator_input'], "HDA")
        sleep(3)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[6]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)

        sleep(3)
        login.is_click(flight['ViewMessages_Upload_Document_Type_Select'])
        sleep(3)
        login.is_click(flight['ViewMessages_Upload_Document_Type_Select'])
        sleep(3)
        login.input_text(flight['ViewMessages_Upload_Document_Type_input'], "Government Approval (Lessee)")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[7]/div/div/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['ViewMessages_Upload_Registration_Mark'], "HK2025")

        sleep(2)
        login.is_click(flight['ViewMessages_Upload_Aircraft_Type_Select'])
        sleep(2)
        login.input_text(flight['ViewMessages_Upload_Aircraft_Type_input'], "ABY")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[8]/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['ViewMessages_Upload_Expiry_Date'], "21/12/2023")
        sleep(2)
        login.input_text(flight['ViewMessages_Upload_Enclosure_Reference'], "End2End Test")
        sleep(2)
        login.input_text(flight['ViewMessages_Upload_Remarks'], "")
        sleep(2)
        login.input_text(flight['ViewMessages_Upload_Remarks'], "Testing")
        sleep(2)
        login.is_click(flight['ViewMessages_Upload_Btn'])
        sleep(2)
        login.is_click(flight['ViewMessages_Upload_OK'])
        sleep(2)
        # ViewMessage  Click "Upload" in newly submitted documents section End

        # ViewMessage Upload_application_related_document Start
        login.is_click(flight['ViewMessages_Upload_application_related_document'])
        sleep(2)
        login.is_click(flight['ViewMessages_Upload_application_related_document_type_input'])
        sleep(2)
        login.input_text(flight['ViewMessages_Upload_application_related_document_type_input'], "Aerodrome Operating Minima")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # 使用pywinauto来选择文件
        current_path_message = os.path.abspath(__file__)
        file_path_message = os.path.dirname(current_path_message) + "/TestFile/Copy_other_supports.pdf"
        drivers.find_element_by_xpath("/html/body/div[8]/div/div[2]/form/div[1]/div/div/div/span/div[2]/div/div/input").send_keys(file_path_message)
        sleep(2)
        login.is_click(flight['ViewMessages_Upload_application_related_document_type_Btn'])
        sleep(2)
        # ViewMessage Upload_application_related_document End

        # ViewMessage View Uploaded Documents Start
        login.is_click(flight['View_Uploaded_Documents'])
        sleep(2)
        login.is_click(flight['View_Uploaded_Documents_Close'])
        sleep(2)
        # ViewMessage View Uploaded Documents End


        # ViewMessage Remarks Textarea Start
        sleep(2)
        login.input_text(flight['ViewMessages_Remarks_Textarea'],"THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING RE")
        sleep(2)
        login.is_click(flight['ViewMessages_CAD_Remarks'])
        sleep(2)
        login.input_text(flight['ViewMessages_CAD_Remarks_Textarea'],"THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS!")
        sleep(2)
        # ViewMessage Remarks Textarea End

        # ViewMessage ViewMessages_Auto_Counting_frequency Start
        sleep(2)
        login.is_click(flight['ViewMessages_Auto_Counting_frequency'])
        sleep(2)
        login.is_click(flight['ViewMessages_Auto_Counting_frequency_Discard'])
        sleep(2)
        # ViewMessage ViewMessages_Auto_Counting_frequency End

        # ViewMessage ViewMessages_Approve Start
        sleep(2)
        login.is_click(flight['ViewMessages_Approve'])
        sleep(3)
        login.is_click(flight['ViewMessages_Recommendation'])
        sleep(5)
        login.is_click(flight['ViewMessages_Confirm'])
        waits.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'testConfirmButtonClass054')]")))
        login.is_click(flight['Confirm_OK'])
        sleep(6)
        # ViewMessage ViewMessages_Approve End

        login.is_click(flight['ViewMessages_Generate'])
        login.is_click(flight['ViewMessages_GenerateAndEdit'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_OfficePhoneNo'], "2345671")
        login.input_text(flight['TemplateGenerate_OfficeFaxNo'], "12345678")
        login.input_text(flight['TemplateGenerate_UserName'], "UAT Tester")
        # login.input_text(flight['TemplateGenerate_ApplicationType'], "Scheduled Passenger")
        login.input_text(flight['TemplateGenerate_Post'], "Tester")
        login.input_text(flight['TemplateGenerate_CompanyName'], "UAT Testing company")
        login.input_text(flight['TemplateGenerate_Address1'], "Testing address 1")
        login.input_text(flight['TemplateGenerate_Address2'], "Testing address 2")
        login.input_text(flight['TemplateGenerate_SubjectOfficerName'], "AS Officer")
        login.input_text(flight['TemplateGenerate_Address3'], "Testing address 3")
        login.input_text(flight['TemplateGenerate_PermitNo'], "123")
        login.input_text(flight['TemplateGenerate_SignedArea'], "Testing test")
        login.is_click(flight['TemplateGenerate_RefreshPreview'])
        login.is_click(flight['TemplateGenerate_DownloadAsWord'])
        login.is_click(flight['TemplateGenerate_GeneratePDF'])
        sleep(20)
        login.is_click(flight['Send'])
        waits.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'testConfirmButtonClass02')]")))
        login.is_click(flight['SendOK'])

        # 从 Officer1用户切换到CPATEST03用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(CadAccountValue['CpaOfficerLoginName'])
        login.input_user_password(CadAccountValue['CpaOfficerPassword'])
        login.click_login_button()
        wait20s.until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        # 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        waits.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Messages']")))
        login.is_click(flight['ViewMessages_AdvancedSearch_CAP'])
        login.input_text(flight['ViewMessages_SubjectContains_CAP'], "application Approved")
        login.input_text(flight['ViewMessages_Sender_CAP'], CadAccountValue['OfficerLoginName'])
        sleep(2)
        login.is_click(flight['ViewMessages_Search_CAP'])
        login.is_click(flight['ViewMessages_ApprovedMessage_CAP'])
        login.is_click(flight['ApprovedAttachment_CAP'])
        sleep(3)
        login.is_click(flight['ApprovedReferenceNo_CAP'])
        sleep(5)
        # assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[1]/div/div/form/div[1]/div[2]/div/div/span").text == 'Approved'
        assert login.element_text(flight['ApprovedStatus']) == 'Approved'

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_011/test_e2e_011.py'])

