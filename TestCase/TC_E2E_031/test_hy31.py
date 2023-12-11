#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import random
import string
from random import randint

import allure
import pytest
from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from common.readelement import Element
from common.readvalue import ElementValue
from page.webpage import sleep
from page_object.LoginPage import LoginPage

flight = Element('flight_031')
flightvalue = ElementValue('flightvalue_031')
cad_account=ElementValue('cad_account')

@allure.feature("TC(ECE)-001 Local Operator Create and Processing Scheduled Passenger Application (Approve)")
class TestSchedulePassengerApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create Seasonal Schedule All-Cargo Application")
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
            login.input_user_name(cad_account['CpaOfficerLoginName'])
            login.input_user_password(cad_account['CpaOfficerPassword'])
            login.click_login_button()
        sleep(20)
        # 跳转到Application-Seasonal Schedule-passenger页面
        login.get_url(ini.url + "#/ApplicationView/CharterFlight/CreateCharterFlightCargo")
        drivers.implicitly_wait(20)
        sleep(1)
        assert drivers.find_element_by_css_selector("h2").text == "Create Charter All-Cargo Application"
        # 填标题的东西
        login.input_text(flight['Registration_Mark'], "HK2023")

        login.is_click(flight['Aircraft_Type'])
        login.input_text(flight['Aircraft_Type'], "70F")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div/div[5]/div[1]/div/div/div/div/input").send_keys(
            Keys.ENTER)

        login.is_click(flight['Aircraft_Nationality'])
        login.input_text(flight['Aircraft_Nationality'], "Hong Kong (SAR, China)")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div/div[5]/div[2]/div/div/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Name_of_Charterer'], "Air Charter Service")
        login.input_text(flight['Address_of_Charterer'], "33 Cameron Road Tsim Sha Tsui, Kowloon Hong Kong")

        login.is_click(flight['Local_Handling_Agent'])
        login.input_text(flight['Local_Handling_Agent'], "AHK")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div/div[8]/div/div/div[1]/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Purpose_of_Service'], "Urgent shipment")
        login.input_text(flight['Points_of_landing_enRoute'], "none")
        login.is_click(flight['Lease_Aircraft'])

        s = string.ascii_letters
        r = random.choice(s)
        Flight_1 = "CPA" + str(randint(1, 999)) + r
        Flight_2 = "CPA" + str(randint(1, 999)) + r
        # 这是第1个
        login.is_click(flight['ServiceType_1'])
        login.input_text(flight['ServiceType_1'], "Charter Cargo")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[2]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['FlightNo_1'], Flight_1)

        login.input_text(flight['From_1'], "01/07/2023")
        login.input_text(flight['To_1'], "31/07/2023")
        login.is_click(flight['DOP_1_1'])
        login.is_click(flight['DOP_1_3'])
        login.is_click(flight['DOP_1_5'])

        login.input_text(flight['CargoAmount_1'], "5000")

        login.input_text(flight['PortFrom_1'], "HKG")
        login.input_text(flight['PortTo_1'], "LAX")
        # login.input_text(flight['LocalTime_STA_1'], "1030")
        login.input_text(flight['LocalTime_STD_1'], "1030")

        login.input_text(flight['Consignor_1'], "Test1")
        login.input_text(flight['Consignee_1'], "Test2")
        login.input_text(flight['Description_1'], "Test3")

        login.is_click(flight['Belly_1'])
        login.is_click(flight['Carriage_1'])
        # login.is_click(flight['PCCL_1'])

        login.input_text(flight['Remarks_1'], "UAT End2End Testing")

        # 这是第2个
        login.is_click(flight['ServiceType_2'])
        login.input_text(flight['ServiceType_2'], "Charter Cargo")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[2]/td[1]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['FlightNo_2'], Flight_2)

        login.input_text(flight['From_2'], "01/07/2023")
        login.input_text(flight['To_2'], "31/07/2023")

        login.input_text(flight['CargoAmount_2'], "5000")

        login.input_text(flight['PortFrom_2'], "LAX")
        login.input_text(flight['PortTo_2'], "HKG")

        login.input_text(flight['LocalTime_STA_2'], "1930")
        # login.input_text(flight['LocalTime_STD_1'], "1030")

        login.input_text(flight['Consignor_2'], "RTest1")
        login.input_text(flight['Consignee_2'], "RTest2")
        login.input_text(flight['Description_2'], "RTest3")

        # login.is_click(flight['Belly_2'])
        login.is_click(flight['Carriage_2'])
        login.is_click(flight['PCCL_2'])

        login.input_text(flight['Remarks_2'], "UAT End2End Testing")
        # 这是第3个
        # login.is_click(flight['ServiceType_3'])
        # login.input_text(flight['ServiceType_3'], "Charter Cargo")
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[3]/td[2]/div/span/div/div/input").send_keys(
        #     Keys.ENTER)
        # login.input_text(flight['FlightNo_3'], "CPA01036")
        #
        # login.input_text(flight['From_3'], "01/07/2023")
        # login.input_text(flight['To_3'], "31/07/2023")
        # login.is_click(flight['DOP_3_1'])
        # login.is_click(flight['DOP_3_3'])
        # login.is_click(flight['DOP_3_5'])
        # login.is_click(flight['DOP_3_7'])
        # login.input_text(flight['CargoAmount_3'], "6000")
        #
        # login.input_text(flight['PortFrom_3'], "HKG")
        # login.input_text(flight['PortTo_3'], "TPE")
        #
        # # login.input_text(flight['LocalTime_STA_1'], "1030")
        # login.input_text(flight['LocalTime_STD_3'], "1030")
        #
        # login.input_text(flight['Consignor_3'], "Test4")
        # login.input_text(flight['Consignee_3'], "Test5")
        # login.input_text(flight['Description_3'], "Test6")
        #
        # # login.is_click(flight['Belly_3'])
        # # login.is_click(flight['Carriage_3'])
        # # login.is_click(flight['PCCL_3'])
        #
        # login.input_text(flight['Remarks_3'], "UAT Testing3")
        #
        # # 这是第4个
        # login.is_click(flight['ServiceType_4'])
        # login.input_text(flight['ServiceType_4'], "Charter Cargo")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[4]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_4'], "CPA01046")
        #
        # login.input_text(flight['From_4'], "01/07/2023")
        # login.input_text(flight['To_4'], "31/07/2023")
        #
        # login.input_text(flight['CargoAmount_4'], "6000")
        #
        # login.input_text(flight['PortFrom_4'], "TPE")
        # login.input_text(flight['PortTo_4'], "HKG")
        # login.input_text(flight['LocalTime_STA_4'], "1600")
        # #login.input_text(flight['LocalTime_STD_1'], "1030")
        #
        # login.input_text(flight['Consignor_4'], "RTest4")
        # login.input_text(flight['Consignee_4'], "RTest5")
        # login.input_text(flight['Description_4'], "RTest6")
        #
        # # login.is_click(flight['Belly_4'])
        # # login.is_click(flight['Carriage_4'])
        # # login.is_click(flight['PCCL_4'])
        #
        # login.input_text(flight['Remarks_4'], "UAT Testing4")
        #
        # # 这是第5个
        # login.is_click(flight['ServiceType_5'])
        # login.input_text(flight['ServiceType_5'], "Charter Cargo")
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[5]/td[2]/div/span/div/div/input").send_keys(
        #     Keys.ENTER)
        # login.input_text(flight['FlightNo_5'], "CPA01056")
        #
        # login.input_text(flight['From_5'], "01/07/2023")
        # login.input_text(flight['To_5'], "31/07/2023")
        # login.is_click(flight['DOP_5_2'])
        # login.is_click(flight['DOP_5_4'])
        #
        # login.input_text(flight['CargoAmount_5'], "10000")
        #
        # login.input_text(flight['PortFrom_5'], "CDG")
        # login.input_text(flight['PortTo_5'], "HKG")
        #
        # login.input_text(flight['LocalTime_STA_5'], "1230")
        # # login.input_text(flight['LocalTime_STD_1'], "1030")
        #
        # login.input_text(flight['Consignor_5'], "Test7")
        # login.input_text(flight['Consignee_5'], "Test8")
        # login.input_text(flight['Description_5'], "Test9")
        #
        # login.is_click(flight['Belly_5'])
        # # login.is_click(flight['Carriage_3'])
        # # login.is_click(flight['PCCL_3'])
        #
        # login.input_text(flight['Remarks_5'], "UAT Testing5")
        #
        # # 这是第6个
        # login.is_click(flight['ServiceType_6'])
        # login.input_text(flight['ServiceType_6'], "Charter Cargo")
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[6]/td[1]/div/span/div/div/input").send_keys(
        #     Keys.ENTER)
        # login.input_text(flight['FlightNo_6'], "CPA01066")
        #
        # login.input_text(flight['From_6'], "01/07/2023")
        # login.input_text(flight['To_6'], "31/07/2023")
        #
        # login.input_text(flight['CargoAmount_6'], "10000")
        #
        # login.input_text(flight['PortFrom_6'], "HKG")
        # login.input_text(flight['PortTo_6'], "CDG")
        #
        # #login.input_text(flight['LocalTime_STA_6'], "1600")
        # login.input_text(flight['LocalTime_STD_6'], "1800")
        #
        # login.input_text(flight['Consignor_6'], "RTest7")
        # login.input_text(flight['Consignee_6'], "RTest8")
        # login.input_text(flight['Description_6'], "RTest9")
        #
        # login.is_click(flight['Belly_6'])
        # # login.is_click(flight['Carriage_6'])
        # # login.is_click(flight['PCCL_6'])
        #
        # login.input_text(flight['Remarks_6'], "UAT Testing6")
        #
        # # 这是第7个
        # login.is_click(flight['ServiceType_7'])
        # login.input_text(flight['ServiceType_7'], "Ferry")
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[7]/td[2]/div/span/div/div/input").send_keys(
        #     Keys.ENTER)
        # login.input_text(flight['FlightNo_7'], "CPA01076")
        #
        # login.input_text(flight['From_7'], "01/07/2023")
        # login.input_text(flight['To_7'], "31/07/2023")
        # login.is_click(flight['DOP_7_1'])
        # login.is_click(flight['DOP_7_3'])
        # login.is_click(flight['DOP_7_5'])
        #
        # login.input_text(flight['CargoAmount_7'], "10000")
        #
        # login.input_text(flight['PortFrom_7'], "HKG")
        # login.input_text(flight['PortTo_7'], "LHR")
        # # login.input_text(flight['LocalTime_STA_6'], "1600")
        # login.input_text(flight['LocalTime_STD_7'], "1030")
        #
        # login.input_text(flight['Consignor_7'], "Test10")
        # login.input_text(flight['Consignee_7'], "Test11")
        # login.input_text(flight['Description_7'], "Test12")
        #
        # # login.is_click(flight['Belly_7'])
        # login.is_click(flight['Carriage_7'])
        # # login.is_click(flight['PCCL_7'])
        #
        # login.input_text(flight['Remarks_7'], "UAT Testing7")
        #
        # # 这是第8个
        # login.is_click(flight['ServiceType_8'])
        # login.input_text(flight['ServiceType_8'], "Ferry")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[8]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_8'], "CPA01086")
        #
        # login.input_text(flight['From_8'], "01/07/2023")
        # login.input_text(flight['To_8'], "31/07/2023")
        #
        # login.input_text(flight['CargoAmount_8'], "10000")
        #
        # login.input_text(flight['PortFrom_8'], "LHR")
        # login.input_text(flight['PortTo_8'], "HKG")
        # login.input_text(flight['LocalTime_STA_8'], "1630")
        # #login.input_text(flight['LocalTime_STD_8'], "1030")
        #
        # login.input_text(flight['Consignor_8'], "RTest10")
        # login.input_text(flight['Consignee_8'], "RTest11")
        # login.input_text(flight['Description_8'], "RTest12")
        #
        # # login.is_click(flight['Belly_8'])
        # login.is_click(flight['Carriage_8'])
        # # login.is_click(flight['PCCL_8'])
        #
        # login.input_text(flight['Remarks_8'], "UAT Testing8")
        #
        # # 这是第9个
        # login.is_click(flight['ServiceType_9'])
        # login.input_text(flight['ServiceType_9'], "Ferry")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[9]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_9'], "CPA01096")
        #
        # login.input_text(flight['From_9'], "01/07/2023")
        # login.input_text(flight['To_9'], "31/07/2023")
        # login.is_click(flight['DOP_9_2'])
        # login.is_click(flight['DOP_9_4'])
        #
        # login.input_text(flight['CargoAmount_9'], "5000")
        #
        # login.input_text(flight['PortFrom_9'], "SIN")
        # login.input_text(flight['PortTo_9'], "HKG")
        # login.input_text(flight['LocalTime_STA_9'], "1030")
        # # login.input_text(flight['LocalTime_STD_9'], "1030")
        #
        # login.input_text(flight['Consignor_9'], "Test13")
        # login.input_text(flight['Consignee_9'], "Test14")
        # login.input_text(flight['Description_9'], "Test15")
        #
        # # login.is_click(flight['Belly_9'])
        # login.is_click(flight['Carriage_9'])
        # login.is_click(flight['PCCL_9'])
        #
        # login.input_text(flight['Remarks_9'], "UAT Testing9")
        #
        # # 这是第10个
        # login.is_click(flight['ServiceType_10'])
        # login.input_text(flight['ServiceType_10'], "Ferry")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[10]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        # login.input_text(flight['FlightNo_10'], "CPA01106")
        #
        # login.input_text(flight['From_10'], "01/07/2023")
        # login.input_text(flight['To_10'], "31/07/2023")
        #
        # login.input_text(flight['CargoAmount_10'], "5000")
        #
        # login.input_text(flight['PortFrom_10'], "HKG")
        # login.input_text(flight['PortTo_10'], "SIN")
        # #login.input_text(flight['LocalTime_STA_8'], "1030")
        # login.input_text(flight['LocalTime_STD_10'], "1630")
        #
        # login.input_text(flight['Consignor_10'], "RTest13")
        # login.input_text(flight['Consignee_10'], "RTest14")
        # login.input_text(flight['Description_10'], "RTest15")
        #
        # # login.is_click(flight['Belly_10'])
        # login.is_click(flight['Carriage_10'])
        # login.is_click(flight['PCCL_10'])
        #
        # login.input_text(flight['Remarks_10'], "UAT Testing10")
        # sleep(2)
        # #结束所有数据集的操作
        sleep(3)
        login.input_text(flight['Remarks'], "UAT End2End Testing")
        sleep(3)
        login.is_click(flight['UploadDoc'])
        sleep(3)
        login.is_click(flight['DOC_Type'])
        sleep(3)
        login.input_text(flight['DOC_Type'], "Aerodrome Operating Minima")
        sleep(3)
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']").send_keys(
            Keys.ENTER)

        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        login.is_click(flight['Doc_Up'])

        login.is_click(flight['SaveAsDraft'])
        sleep(2)
        assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'

        login.is_click(flight['SaveAsTemplate'])
        b = flightvalue['TemplateName'] + str(random.uniform(1, 1000))
        login.input_text(flight['TemplateName'], b)
        login.input_text(flight['Description'], "Description")
        sleep(2)
        login.is_click(flight['Template_Save'])
        # login.is_click(flight['Template_Cancel'])
        login.is_click(flight['Confirm_x'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['BackAndModify'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['Submit'])
        sleep(3)
        login.is_click(flight['Submit_Yes'])
        # 填表格
        sleep(2)
        login.is_click(flight['LessorOperatorName'])
        login.input_text(flight['LessorOperatorName'], "HDA")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['EffectivePeriod1'], "01/07/2023")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['EffectivePeriod2'], "31/12/2023")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input").send_keys(Keys.ENTER)

        login.is_click(flight['Lessor_Doc'])
        login.is_click(flight['Lessor_Doc_Type'])
        login.input_text(flight['Lessor_Doc_Type'], "Aerodrome Operating Minima")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[1]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(
            Keys.ENTER)

        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        login.is_click(flight['Lessor_Doc_Upload'])

        login.is_click(flight["Lessor_Summit"])
        login.is_click(flight["Lessor_Yes"])
        sleep(1)
        login.is_click(flight["Lessor_Ok"])

        # 从 CPATEST03用户切换到officer1用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(cad_account['OfficerLoginName'])
        login.input_user_password(cad_account['OfficerPassword'])
        login.click_login_button()
        sleep(20)
        # 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        login.input_text(flight['ViewMessages_Sender'], cad_account['CpaOfficerLoginName'])
        login.is_click(flight['ViewMessages_ApplicationType'])
        login.is_click(flight['ViewMessages_Search'])
        sleep(3)
        login.is_click(flight['ViewMessages_ReferenceNo'])
        # 13-26管理员的按钮测试
        login.is_click(flight['Modify_1'])
        sleep(3)
        login.is_click(flight['List_1'])
        sleep(2)
        login.is_click(flight['Modify_2'])
        sleep(2)
        login.is_click(flight['Day7'])
        sleep(2)
        login.is_click(flight['Save_Modify'])
        sleep(2)
        login.is_click(flight['Save_All'])
        sleep(2)
        login.is_click(flight['OK_All'])
        sleep(2)
        # 许可证和飞行权
        login.is_click(flight['List_1'])
        sleep(2)
        # login.is_click(flight['Check_Licence'])
        # login.is_click(flight['Check_Traffic_Rights'])
        # login.is_click(flight['Close_Check_Traffic_Rights'])
        # 选择文件
        # login.is_click(flight['Select_from_Document_Library'])
        # sleep(6)
        # login.is_click(flight['Enter_null'])
        # sleep(6)
        # login.input_text(flight['Enter_null'], "")
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/div[1]/form/div/div[11]/div[2]/div/div[3]/div/div[2]/form/div[1]/div[2]/div/div/div/div[1]/input").send_keys(
        #     Keys.ENTER)
        # login.is_click(flight['Search_null'])
        # login.is_click(flight['List_null'])
        # login.is_click(flight['Summit_null'])
        # 上传文件
        drivers.find_element_by_class_name("el-icon-document-add").click()
        login.is_click(flight['Doc_Type_Minima_Input'])
        sleep(2)
        login.input_text(flight['Doc_Type_Minima_Input'], "Aerodrome Operating Minima")
        sleep(2)
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)

        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        login.is_click(flight['Doc_Up'])

        # Messaging
        # login.is_click(flight['Messaging'])
        # Remark
        # login.input_text(flight['Remark_Input'],
        #                  "UAT End2End Testing")

        # Cad Remark
        # login.is_click(flight['Cad_Remark'])
        # login.input_text(flight['Cad_Remark_Input'],
        #                  "UAT End2End Testing")

        # 自动计算
        # login.is_click(flight['Auto_Counting'])
        # login.is_click(flight['Close_Auto_Counting'])
        # 保存全部
        # sleep(3)
        login.is_click(flight['Save_All'])
        sleep(3)
        login.is_click(flight['OK_All2'])
        sleep(3)
        # 管理员同意下一步
        login.is_click(flight['ViewMessages_Approve'])
        login.is_click(flight['process'])

        login.is_click(flight['ViewMessages_Generate'])
        sleep(2)
        login.is_click(flight['ViewMessages_GenerateAndEdit'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_OfficePhoneNo'], "2345671")
        login.input_text(flight['TemplateGenerate_OfficeFaxNo'], "12345678")
        login.input_text(flight['TemplateGenerate_UserName'], "UAT Tester")
        login.input_text(flight['TemplateGenerate_Post'], "Tester")
        # login.input_text(flight['TemplateGenerate_SeasonInTitle'], "Summer 2023")
        login.input_text(flight['TemplateGenerate_CompanyName'], "UAT Testing company")
        login.input_text(flight['TemplateGenerate_Address1'], "Testing address 1")
        login.input_text(flight['TemplateGenerate_SubjectOfficerName'], "Summer 2023")
        login.input_text(flight['TemplateGenerate_Address2'], "Testing address 2")
        # login.input_text(flight['TemplateGenerate_SubjectOfficerName'], "AS Officer")
        login.input_text(flight['TemplateGenerate_Address3'], "Testing address 3")
        login.input_text(flight['TemplateGenerate_Ferry'], "Testing address 3")
        # login.input_text(flight['TemplateGenerate_PermitNo'], "123")
        login.input_text(flight['TemplateGenerate_SignedArea'], "Testing test")
        login.is_click(flight['TemplateGenerate_RefreshPreview'])
        login.is_click(flight['TemplateGenerate_DownloadAsWord'])
        login.is_click(flight['TemplateGenerate_GeneratePDF'])
        sleep(2)
        login.is_click(flight['Send'])
        sleep(30)
        drivers.find_element_by_class_name("testConfirmButtonClass02").click()
        sleep(1)
        # 从 Officer1用户切换到CPATEST03用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(cad_account['CpaOfficerLoginName'])
        login.input_user_password(cad_account['CpaOfficerPassword'])
        login.click_login_button()
        sleep(20)
        # 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        login.is_click(flight['ViewMessages_AdvancedSearch_CAP'])
        sleep(2)
        login.input_text(flight['ViewMessages_SubjectContains_CAP'], "application Approved")
        sleep(2)
        login.input_text(flight['ViewMessages_Sender_CAP'], cad_account['OfficerLoginName'])
        sleep(2)
        login.is_click(flight['ViewMessages_ApplicationType2'])
        sleep(2)
        login.is_click(flight['ViewMessages_Search_CAP'])
        sleep(2)
        price_element = drivers.find_element_by_xpath(
            "//*[@id='test0']/a/span/span[1]")
        refNo = price_element.text
        sleep(3)
        print(refNo)
        login.is_click(flight['ReferenceNo'])
        sleep(3)

        # "Cargo Manifest" page displayed
        login.get_url(ini.url + "#/View/Manifest")
        sleep(2)
        login.input_text(flight['Cargo_Manifest_Reference_No'], refNo)
        sleep(2)
        login.is_click(flight['date_1'])
        sleep(2)
        login.input_text(flight['date_1'], "")
        sleep(2)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[5]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['Cargo_Manifest_Search'])
        sleep(2)
        login.is_click(flight['Cargo_Manifest_Select'])
        sleep(2)
        login.is_click(flight['Cargo_Manifest_Upload_Cargo_Manifest'])
        sleep(2)
        login.input_text(flight['Cargo_Manifest_Date'], "01/10/2023")
        sleep(2)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/form/div[5]/div/div/div/input").send_keys(
            Keys.ENTER)
        sleep(2)
        login.input_text(flight['Cargo_Manifest_Cargo_tonnage'], "111")

        sleep(2)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        login.is_click(flight['Cargo_Manifest_Upload'])
        # 从 CPATEST03用户切换到officer1用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(cad_account['OfficerLoginName'])
        login.input_user_password(cad_account['OfficerPassword'])
        login.click_login_button()
        sleep(20)
        # 选择接受
        login.get_url(ini.url + "#/View/Manifest")
        login.input_text(flight['Cargo_Manifest_Reference_No'], refNo)
        login.is_click(flight['date_1'])
        login.input_text(flight['date_1'], "")

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/test_hy31.py'])
