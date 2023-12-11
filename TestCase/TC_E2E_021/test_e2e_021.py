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

flight = Element('flight_021')
flightvalue = ElementValue('flightvalue_021')
account = ElementValue('cad_account')
@allure.feature("TC(ECE)-021 ")
class TestMissNoSeatsError:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Miss inputting mandatory No. of Seats field")
    def test_021(self, drivers):
        """test1: Miss inputting mandatory No. of Seats field"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(account['CpaOfficerLoginName'])
            login.input_user_password(account['CpaOfficerPassword'])
            login.click_login_button()
        sleep(20)

        '''跳转到CreateCharterFlight页面'''
        login.get_url(ini.url + "#/ApplicationView/CharterFlight/CreateCharterFlight")

        drivers.implicitly_wait(30)
        sleep(5)

        # 填写Flight 基础信息
        assert drivers.find_element_by_css_selector("h2").text == "Create Charter Passenger Application"
        # login.is_click(flight['Operator(ICAO)_select'])
        # login.input_text(flight['Operator(ICAO)_input'], "CPA")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)

        login.input_text(flight['Registration_mark'], 'HK2023')

        login.is_click(flight['Aircraft_type_select'])
        login.input_text(flight['Aircraft_type_input'], "100")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[5]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)

        login.is_click(flight['Aircraft_nationality_select'])
        login.input_text(flight['Aircraft_nationality_input'], "Hong Kong (SAR, China)")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[5]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)

        login.input_text(flight['Name_of_charterer'], 'Air Charter Service')
        login.input_text(flight['Address_of_charterer'], '33 Cameron Road Tsim Sha Tsui, Kowloon Hong Kong')

        login.is_click(flight['Local_handling_agent_select'])
        login.input_text(flight['Local_handling_agent_input'], "HKE")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[8]/div/div/div[1]/div/input").send_keys(Keys.ENTER)

        login.input_text(flight['Purpose_of_service'], 'Urgent flight')
        login.input_text(flight['Points_of_landing'], 'none')
        sleep(2)


        #填写Flight Schedules表格信息
        #line 1
        login.is_click(flight['Service_Type_select'])
        login.input_text(flight['Service_Type_input'], "Charter Pax")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        login.input_text(flight['From'], "01/07/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To'], "31/07/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1'])
        login.is_click(flight['DOP_3'])
        login.is_click(flight['DOP_5'])
        login.input_text(flight['No_of_Pax'], '100')
        login.input_text(flight['Port_From'], 'HKG')
        login.input_text(flight['Port_To'], 'LAX')
        login.input_text(flight['LocalTime_STD'], "1030")
        login.input_text(flight['Table_Remarks'], "UAT Testing1")
        # line2
        login.is_click(flight['Service_Type_select_2'])
        login.input_text(flight['Service_Type_input_2'], "Charter Pax")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[2]/td[1]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_2'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        login.input_text(flight['No_of_Pax_2'], '50')
        login.input_text(flight['Port_From_2'], 'LAX')
        login.input_text(flight['Port_To_2'], 'HKG')
        login.input_text(flight['LocalTime_STA_2'], "1930")
        login.input_text(flight['Table_Remarks_2'], "UAT Testing2")


        #line 3
        login.is_click(flight['Service_Type_select_3'])
        login.input_text(flight['Service_Type_input_3'], "Ferry")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[3]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_3'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        login.input_text(flight['From_3'], "01/07/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[3]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To_3'], "31/07/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[3]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1_3'])
        login.is_click(flight['DOP_3_3'])
        login.is_click(flight['DOP_5_3'])
        login.is_click(flight['DOP_7_3'])
        login.input_text(flight['No_of_Pax_3'], '100')
        login.input_text(flight['Port_From_3'], 'HKG')
        login.input_text(flight['Port_To_3'], 'TPE')
        login.input_text(flight['LocalTime_STD_3'], "1030")
        login.input_text(flight['Table_Remarks_3'], "UAT Testing3")
        # line4
        login.is_click(flight['Service_Type_select_4'])
        login.input_text(flight['Service_Type_input_4'], "Ferry")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[4]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_4'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        login.input_text(flight['No_of_Pax_4'], '50')
        login.input_text(flight['Port_From_4'], 'TPE')
        login.input_text(flight['Port_To_4'], 'HKG')
        login.input_text(flight['LocalTime_STA_4'], "1600")
        login.input_text(flight['Table_Remarks_4'], "UAT Testing4")

        # #line 5
        # login.is_click(flight['Service_Type_select_5'])
        # login.input_text(flight['Service_Type_input_5'], "Medical")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[5]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_5'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        # login.input_text(flight['From_5'], "01/07/2023")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[5]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['To_5'], "31/07/2023")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[5]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        # login.is_click(flight['DOP_2_5'])
        # login.is_click(flight['DOP_4_5'])
        # login.is_click(flight['DOP_6_5'])
        # login.input_text(flight['No_of_Pax_5'], '250')
        # login.input_text(flight['Port_From_5'], 'CDG')
        # login.input_text(flight['Port_To_5'], 'HKG')
        # login.input_text(flight['LocalTime_STA_5'], "1230")
        # login.input_text(flight['Table_Remarks_5'], "UAT Testing5")
        # # line6
        # login.is_click(flight['Service_Type_select_6'])
        # login.input_text(flight['Service_Type_input_6'], "Medical")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[6]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_6'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        # login.is_click(flight['In_Out_Diff_select_6'])
        # login.input_text(flight['In_Out_Diff_input_6'], "+1")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[6]/td[3]/div/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['No_of_Pax_6'], '100')
        # login.input_text(flight['Port_From_6'], 'HKG')
        # login.input_text(flight['Port_To_6'], 'CDG')
        # login.input_text(flight['LocalTime_STD_6'], "1800")
        # login.input_text(flight['Table_Remarks_6'], "UAT Testing6")
        #
        # #line 7
        # login.is_click(flight['Service_Type_select_7'])
        # login.input_text(flight['Service_Type_input_7'], "Charter Pax")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[7]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_7'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        # login.input_text(flight['From_7'], "01/07/2023")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[7]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['To_7'], "31/07/2023")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[7]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        # login.is_click(flight['DOP_1_7'])
        # login.is_click(flight['DOP_3_7'])
        # login.is_click(flight['DOP_5_7'])
        # login.input_text(flight['No_of_Pax_7'], '300')
        # login.input_text(flight['Port_From_7'], 'HKG')
        # login.input_text(flight['Port_To_7'], 'LHR')
        # login.input_text(flight['LocalTime_STD_7'], "1030")
        # login.input_text(flight['Table_Remarks_7'], "UAT Testing7")
        # # line8
        # login.is_click(flight['Service_Type_select_8'])
        # login.input_text(flight['Service_Type_input_8'], "Ferry")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[8]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_8'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        # login.input_text(flight['No_of_Pax_8'], '250')
        # login.input_text(flight['Port_From_8'], 'LHR')
        # login.input_text(flight['Port_To_8'], 'HKG')
        # login.input_text(flight['LocalTime_STA_8'], "1630")
        # login.input_text(flight['Table_Remarks_8'], "UAT Testing8")
        #
        # #line 9
        # login.is_click(flight['Service_Type_select_9'])
        # login.input_text(flight['Service_Type_input_9'], "Charter Pax")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[9]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_9'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        # login.input_text(flight['From_9'], "01/07/2023")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[9]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['To_9'], "31/07/2023")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[9]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        # login.is_click(flight['DOP_2_9'])
        # login.is_click(flight['DOP_4_9'])
        # login.input_text(flight['No_of_Pax_9'], '600')
        # login.input_text(flight['Port_From_9'], 'SIN')
        # login.input_text(flight['Port_To_9'], 'HKG')
        # login.input_text(flight['LocalTime_STA_9'], "1030")
        # login.input_text(flight['Table_Remarks_9'], "UAT Testing9")
        # # line10
        # login.is_click(flight['Service_Type_select_10'])
        # login.input_text(flight['Service_Type_input_10'], "Medical")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[10]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_10'], flightvalue['Flight_CPA'] + str(randint(1000, 9999))+r)
        # login.input_text(flight['No_of_Pax_10'], '500')
        # login.input_text(flight['Port_From_10'], 'HKG')
        # login.input_text(flight['Port_To_10'], 'SIN')
        # login.input_text(flight['LocalTime_STD_10'], "1630")
        # login.input_text(flight['Table_Remarks_10'], "UAT Testing10")

        login.input_text(flight['Remarks'], "UAT End2End Testing")
        # Upload file
        login.is_click(flight['Upload_Related_Documents'])
        sleep(2)
        login.is_click(flight['Doc_Type_Select'])
        sleep(2)
        login.input_text(flight['Doc_Type_Input'], "Aerodrome Operating Minima")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # login.is_click(flight['BrowseButton'])
        # sleep(2)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/sample_file.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.is_click(flight['UploadButton'])
        sleep(2)

        login.is_click(flight['Click_Condition'])
        # step 02 Click "Save as Draft"
        login.is_click(flight['Save_AS_Draft'])
        sleep(2)
        # step 03
        login.is_click(flight['Save_AS_Template'])
        login.input_text(flight['Template_Name'], 'Charter Template'+ str(randint(1000, 9999))+r)
        login.input_text(flight['Template_Description'], 'Charter Template Description')
        login.is_click(flight['Template_Save'])
        # sleep(2)
        # step 04
        login.is_click(flight['Preview_And_Submit'])
        sleep(2)
        # step 05 Print
        # step 06
        login.is_click(flight['Back_And_Modify'])
        sleep(2)
        login.is_click(flight['Preview_And_Submit'])
        sleep(2)
        # step 07
        login.is_click(flight['Click_Submit'])
        # step 08
        sleep(10)
        # login.is_click(flight['Click_YES_01'])
        # sleep(2)
        login.is_click(flight['Click_YES_01'])


        # 从CPATEST03用户到 Officer1用户切换
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(account['OfficerLoginName'])
            login.input_user_password(account['OfficerPassword'])
            login.click_login_button()
        sleep(20)

        # step 10 '''Message'''
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        # step 11
        login.is_click(flight['Advanced_Search'])
        # login.input_text(flight['Sender'], "OFFICER2")
        login.is_click(flight['Charter_Passenger'])
        login.is_click(flight['Search'])
        sleep(3)
        login.is_click(flight['Open_Message'])
        sleep(5)
        # step 12
        login.is_click(flight['Message_Ref_No'])
        sleep(2)
        # step 15
        login.is_click(flight['Modify_Button'])
        sleep(2)
        login.input_text(flight['Modify_Registration_Mark'], "HK1997")
        login.input_text(flight['Modify_Name_Of_Charterer'], "Air Charter Service LTD")
        login.input_text(flight['Modify_Address_Of_Charterer'], "34 Cameron Road Tsim Sha Tsui, Kowloon Hong Kong")
        # 有问题，错误信息是ValueError: not enough values to unpack (expected 2, got 1)
        # login.is_click(flight['Modify_Local_Handing_Agent_Select'])
        # login.input_text(flight['Modify_Local_Handing_Agent_Input'], "KQA")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[1]/div/div/form/div/div[8]/div/div/div[1]/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Modify_Purpose_Of_Service'], "Urgent  shipment ")
        login.is_click(flight['Save_Button'])
        sleep(2)
        login.is_click(flight['Record_Save'])
        sleep(2)
        # step 16
        login.is_click(flight['Check_Licence_Select_Record'])
        login.is_click(flight['Check_Licence_Button'])
        sleep(2)
        # step 17
        # login.is_click(flight['Check_Traffic_Right_Button'])
        # sleep(2)
        # login.is_click(flight['Check_Traffic_Right_Close'])
        # sleep(2)
        # step 18 没有该按钮
        # step 19
        login.is_click(flight['Upload_Button'])
        sleep(2)
        login.is_click(flight['Lease_Aircraft_Button'])
        sleep(2)
        login.is_click(flight['Upload_Document_Lessor_Operator_Select'])
        login.input_text(flight['Upload_Document_Lessor_Operator_Input'], flightvalue['Lessor_Operator_ICAO'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[6]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # login.is_click(flight['Upload_Document_Type_Select'])
        # login.input_text(flight['Upload_Document_Type_Input'], flightvalue['Document_Type'])
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[7]/div/div/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['Upload_Document_Registration_Mark'], flightvalue['Registration_Mark2'])
        # login.is_click(flight['Upload_Document_Aircraft_Type_Select'])
        # login.input_text(flight['Upload_Document_Aircraft_Type_Input'], flightvalue['Aircraft_Type2'])
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[8]/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # login.input_text(flight['Upload_Document_Expiry_Date_Input'], flightvalue['Expiry_Date'])
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[9]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Upload_Document_Enclosure'], flightvalue['Enclosure_Reference'])
        login.input_text(flight['Upload_Document_Remarks'], flightvalue['Remarks2'])
        login.is_click(flight['Upload_Click'])
        sleep(2)
        login.is_click(flight['Upload_Click_OK'])
        sleep(2)
        # step 20
        # login.is_click(flight['Select_From_Document_Library_Button'])
        # login.is_click(flight['Select_From_Document_Library_Confirm'])
        # step 21
        ''' todo 文件上传 '''
        login.is_click(flight['Upload_Application_related_Document_Button'])
        sleep(2)
        login.is_click(flight['New_Doc_Type_Select'])
        sleep(2)
        login.input_text(flight['New_Doc_Type_Input'], "Others")
        sleep(2)
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # login.is_click(flight['New_BrowseButton'])
        # sleep(2)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("/html/body/div[4]/div/div[2]/form/div[1]/div/div/div/span/div[2]/div/div/input").send_keys(file_path)
        # 输入上传文件的路径
        sleep(2)
        login.is_click(flight['New_Indefinite'])
        sleep(2)
        login.is_click(flight['Upload_Application_related_Document_Upload'])
        sleep(2)
        # login.is_click(flight['Upload_Application_related_Document_Close'])
        # step 22
        login.is_click(flight['View_Uploaded_Documents'])
        sleep(5)
        login.is_click(flight['View_Uploaded_Documents_Close'])
        # step 23
        # login.is_click(flight['Messaging'])
        # login.input_text(flight['Messaging_Text'], "test")
        # login.is_click(flight['Messaging_Send'])
        # sleep(10)
        # step 24
        login.input_text(flight['Remarks_Text'],
                         "THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250  ")
        # step 25
        login.is_click(flight['CAD_Remarks'])
        login.input_text(flight['CAD_Remarks_Text'],
                         "THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESS!")
        # step 26
        login.is_click(flight['Auto_Counting_Frequency'])
        sleep(2)
        login.is_click(flight['Auto_Counting_Frequency_Close'])
        sleep(2)
        # step 27
        # login.is_click(flight['Print_Application'])
        # step 28
        login.is_click(flight['Approve'])
        login.is_click(flight['Approve_Proceed'])
        # step 29
        login.is_click(flight['Generate'])
        sleep(2)
        # step 30
        login.is_click(flight['Generate_And_Edit'])
        sleep(2)
        login.input_text(flight['Template_Office_Phone_No'], flightvalue['Office_Phone_No'])
        login.input_text(flight['Template_Fax_No'], flightvalue['Office_Fax_No'])
        login.input_text(flight['Template_User_Name'], flightvalue['User_Name'])
        login.input_text(flight['Template_Post'], flightvalue['Post'])
        login.input_text(flight['Template_Address1'], flightvalue['Address1'])
        login.input_text(flight['Template_Address2'], flightvalue['Address2'])
        login.input_text(flight['Template_Address3'], flightvalue['Address3'])
        login.input_text(flight['Template_Signed_Area'], flightvalue['Signed_Area'])
        login.input_text(flight['Template_Ferry'], flightvalue['Ferry'])
        login.is_click(flight['Template_RefreshPreview'])
        sleep(3)
        login.is_click(flight['Template_Download_As_Word'])
        sleep(3)
        login.is_click(flight['Template_Generate_PDF'])
        sleep(6)
        # step 31
        login.is_click(flight['Send_Letter'])
        sleep(10)
        resultText = login.element_text(flight['Send_letter_failed_Text'])
        if resultText == 'Failed to send an external email. Procedure.':
            # send 失败
            login.is_click(flight['Send_Letter_failed_ok'])
            login.is_click(flight['Discard'])
            login.is_click(flight['Yes_After_Discard'])
            sleep(3)
        else:
            # send 成功   'Email has been sent.'
            login.is_click(flight['Send_letter_Close'])
            sleep(3)


        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(account['CpaOfficerLoginName'])
            login.input_user_password(account['CpaOfficerPassword'])
            login.click_login_button()
        sleep(20)
        # step 32 '''Message'''
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        # step 33
        # login.is_click(flight['CPA_Advanced_Search'])
        # login.is_click(flight['CPA_Charter_Passenger'])
        # login.is_click(flight['CPA_Search'])
        # sleep(2)
        # login.is_click(flight['CPA_Open_Message'])
        # sleep(2)
        # step 34
        # step 35
        login.is_click(flight['CPA_Message_Ref_No'])
        sleep(10)
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_021/test_e2e_021.py'])
