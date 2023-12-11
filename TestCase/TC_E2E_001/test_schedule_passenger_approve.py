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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.readconfig import ini
from common.readelement import Element
from common.readvalue import ElementValue
from page.webpage import sleep
from page_object.LoginPage import LoginPage

flight = Element('flight')
flightvalue = ElementValue('flightvalue')
@allure.feature("TC(ECE)-001 Local Operator Create and Processing Scheduled Passenger Application (Approve)")
class TestSchedulePassengerApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create Seasonal Schedule Passenger Application and approve")
    # 每次测试前需要在flightvalue.yaml文件中更新FlightNo和TemplateName值，不然会报重复航班号和模板名错误
    def test_001(self, drivers):
        """登录CPATEST03用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
           login.is_click(flight["Logout"])
           login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
           login.input_user_name(flightvalue['CpaOfficerLoginName'])
           login.input_user_password(flightvalue['CpaOfficerPassword'])
           login.click_login_button()

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        #跳转到Application-Seasonal Schedule-passenger页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"

        # login.is_click(flight['Operator_select'])
        # sleep(5)
        # login.input_text(flight['Operator(ICAO)'], "CPA")
        # sleep(2)
        # drivers.find_element_by_xpath("//label[contains(text(),'ICAO')]//following-sibling::div//input").send_keys(Keys.ENTER)
        #填写Flight Schedules表格信息
        # Random flight number
        s = string.ascii_letters
        r = random.choice(s)
        FlightNoA1="CPA"+str(randint(1000, 9999))+r
        login.input_text(flight['FlightNo'], FlightNoA1)
        login.input_text(flight['From'], "22/09/2023")
        login.input_text(flight['To'], "30/09/2023")
        login.is_click(flight['DOP_1'])

        login.is_click(flight['AircraftType_Select'])
        login.input_text(flight['AircraftType_input'], "100")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)

        login.input_text(flight['NoofSeats'], "200")
        login.input_text(flight['Route'], "SIN-HKG")

        login.is_click(flight['LocalTime_STA'])
        login.input_text(flight['LocalTime_STA'], "1000")
        login.input_text(flight['Remarks'], "1002")
        sleep(2)
        login.is_click(flight['SaveAsDraft'])
        sleep(2)
        assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'

        login.is_click(flight['SaveAsTemplate'])
        templateName = "TestByHW"+str(random.uniform(1, 1000))
        login.input_text(flight['TemplateName'],templateName)
        login.input_text(flight['Description'], "Description")
        sleep(2)
        login.is_click(flight['Template_Save'])
        #login.is_click(flight['Template_Cancel'])
        sleep(3)
        login.is_click(flight['Confirm'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        # login.is_click(flight['BackAndModify'])
        # login.is_click(flight['PreviewAndSubmit'])
        # sleep(2)
        login.is_click(flight['Submit'])
        sleep(2)
        login.is_click(flight['Submit_Yes'])
        # login.is_click(flight['Submit_No'])
        # login.is_click(flight['Submit_Close'])
        sleep(2)
        login.is_click(flight['LessorOperatorName_Select'])
        sleep(2)
        login.input_text(flight['LessorOperatorName_input'], "HDA")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        #login.input_text(flight['LessorOperatorName'], "LessorOperatorName")
        login.input_text(flight['EffectivePeriod1'], "21/09/2023")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['EffectivePeriod2'], "01/10/2023")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input").send_keys(Keys.ENTER)

        login.input_text(flight['RegistrationMark'], "HK2023")
        # sleep(5)
        login.is_click(flight['AircraftType_input2'])
        # sleep(2)
        login.input_text(flight['AircraftType_input2'], "100")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[8]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        # login.is_click(flight['AircraftType_100_2'])
        sleep(2)
        login.is_click(flight['AircraftType_Add_Document'])
        sleep(2)
        login.is_click(flight['AircraftType_Upload_Document_Select'])
        sleep(2)
        login.input_text(flight['AircraftType_Upload_Document_input'], "Operation Specification (Lessor)")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/Operation Specification (Lessor) Sample.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight['AircraftType_Upload_Document_Remarks'], "UAT End2End Testing")
        sleep(1)
        login.is_click(flight['AircraftType_Upload_Document_Upload'])
        sleep(1)
        login.is_click(flight['LeaseAircraftOperation_Submit'])
        login.is_click(flight['LeaseAircraftSubmit'])
        login.is_click(flight['LeaseAircraftOK'])


        #从 CPATEST03用户切换到officer1用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['OfficerLoginName'])
        login.input_user_password(flightvalue['OfficerPassword'])
        login.click_login_button()
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        #跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        login.input_text(flight['ViewMessages_Sender'], "CPATEST03")
        login.is_click(flight['ViewMessages_ApplicationType'])
        login.is_click(flight['ViewMessages_Search'])
        sleep(1)
        login.is_click(flight['ViewMessages_ReferenceNo'])

        login.is_click(flight['ViewMessages_Approve'])
        sleep(2)
        login.is_click(flight['ViewMessages_Recommendation'])
        sleep(2)
        #to update
        login.is_click(flight['ViewMessages_Confirm'])
        sleep(2)

        login.is_click(flight['Confirm_OK'])
        #login.is_click(flight['Confirm_Yes'])
        #need to update
        sleep(2)
        login.is_click(flight['ViewMessages_Generate'])
        login.is_click(flight['ViewMessages_GenerateAndEdit'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_OfficePhoneNo'], "2345671")
        login.input_text(flight['TemplateGenerate_OfficeFaxNo'], "12345678")
        login.input_text(flight['TemplateGenerate_UserName'], "UAT Tester")
        # login.input_text(flight['TemplateGenerate_ApplicationType'], "Scheduled Passenger")
        login.input_text(flight['TemplateGenerate_Post'], "Tester")
        login.input_text(flight['TemplateGenerate_SeasonInTitle'], "Summer 2023")
        login.input_text(flight['TemplateGenerate_CompanyName'], "UAT Testing company")
        login.input_text(flight['TemplateGenerate_Address1'], "Testing address 1")
        login.input_text(flight['TemplateGenerate_SeasonInContent'], "Summer 2023")
        login.input_text(flight['TemplateGenerate_Address2'], "Testing address 2")
        login.input_text(flight['TemplateGenerate_SubjectOfficerName'], "AS Officer")
        login.input_text(flight['TemplateGenerate_Address3'], "Testing address 3")
        login.input_text(flight['TemplateGenerate_PermitNo'], "123")
        login.input_text(flight['TemplateGenerate_SignedArea'], "Testing test")
        login.is_click(flight['TemplateGenerate_RefreshPreview'])
        login.is_click(flight['TemplateGenerate_DownloadAsWord'])
        login.is_click(flight['TemplateGenerate_GeneratePDF'])
        sleep(10)
        login.is_click(flight['Send'])
        sleep(2)
        login.is_click(flight['SendOK'])

        #从 Officer1用户切换到用户CPATEST03
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['CpaOfficerLoginName'])
        login.input_user_password(flightvalue['CpaOfficerPassword'])
        login.click_login_button()
        #跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch_CAP'])
        login.input_text(flight['ViewMessages_SubjectContains_CAP'], "application Approved")
        login.input_text(flight['ViewMessages_Sender_CAP'], "Officer1")
        login.is_click(flight['ViewMessages_Search_CAP'])
        login.is_click(flight['ViewMessages_ApprovedMessage_CAP'])
        login.is_click(flight['ApprovedAttachment_CAP'])
        sleep(3)
        login.is_click(flight['ApprovedReferenceNo_CAP'])
        sleep(5)
        #assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[1]/div/div/form/div[1]/div[2]/div/div/span").text == 'Approved'
        assert login.element_text(flight['ApprovedStatus']) == 'Approved'

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/test_schedule_passenger_approve.py'])

