#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import random

import allure
import pytest
from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from common.readelement import Element
from common.readvalue import ElementValue
from page.webpage import sleep
from page_object.LoginPage import LoginPage

flight = Element('flight_112')
flightvalue = ElementValue('flightvalue_112')
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
        drivers.implicitly_wait(30)
        sleep(1)
        assert drivers.find_element_by_css_selector("h2").text == "Create Charter All-Cargo Application"
        # 填标题的东西
        login.is_click(flight['Helicopter_Application'])
        login.input_text(flight['Registration_Mark'], "HK2023")
        login.is_click(flight['Lease_Aircraft'])
        login.is_click(flight['Aircraft_Type'])
        login.input_text(flight['Aircraft_Type'], "9A1")
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
        login.input_text(flight['Local_Handling_Agent'], "ABW")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div/div[8]/div/div/div[1]/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Purpose_of_Service'], "Urgent shipment")
        login.input_text(flight['Points_of_landing_enRoute'], "none")

        Flight_1 = "CPA" + str(random.uniform(1, 1000))
        Flight_2 = "CPA" + str(random.uniform(1, 1000))
        # 这是第1个
        login.is_click(flight['ServiceType_1'])
        login.input_text(flight['ServiceType_1'], "Charter Cargo")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[2]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['FlightNo_1'], Flight_1)

        login.input_text(flight['From_1'], "01/11/2023")
        login.input_text(flight['To_1'], "30/11/2023")
        login.is_click(flight['DOP_1_1'])
        login.is_click(flight['DOP_1_3'])
        login.is_click(flight['DOP_1_5'])

        login.input_text(flight['CargoAmount_1'], "5000")

        login.input_text(flight['PortFrom_1'], "HKG")
        login.input_text(flight['PortTo_1'], "9P7")
        login.input_text(flight['LocalTime_STA_1'], "1230")
        login.input_text(flight['LocalTime_STD_1'], "1030")

        login.input_text(flight['Consignor_1'], "Test1")
        login.input_text(flight['Consignee_1'], "Test2")
        login.input_text(flight['Description_1'], "Test3")

        login.is_click(flight['Belly_1'])
        login.is_click(flight['Carriage_1'])
        # login.is_click(flight['PCCL_1'])

        login.input_text(flight['Remarks_1'], "UAT Testing1")

        # 这是第2个
        login.is_click(flight['ServiceType_2'])
        login.input_text(flight['ServiceType_2'], "Charter Cargo")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[2]/td[1]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['FlightNo_2'], Flight_2)

        login.input_text(flight['From_2'], "01/11/2023")
        login.input_text(flight['To_2'], "30/11/2023")

        login.input_text(flight['CargoAmount_2'], "5000")

        login.input_text(flight['PortFrom_2'], "9P7")
        login.input_text(flight['PortTo_2'], "HKG")

        login.input_text(flight['LocalTime_STA_2'], "1930")
        login.input_text(flight['LocalTime_STD_2'], "1530")

        login.input_text(flight['Consignor_2'], "RTest1")
        login.input_text(flight['Consignee_2'], "RTest2")
        login.input_text(flight['Description_2'], "RTest3")
        sleep(3)
        # login.is_click(flight['Belly_2'])
        login.is_click(flight['Carriage_2'])
        sleep(3)
        login.is_click(flight['PCCL_2'])
        sleep(3)
        login.input_text(flight['Remarks_2'], "UAT Testing2")

        # #结束所有数据集的操作
        login.input_text(flight['Remarks'], "UAT End2End Testing")
        sleep(6)
        login.is_click(flight['UploadDoc'])
        sleep(6)
        login.is_click(flight['DOC_Type'])
        sleep(6)
        login.input_text(flight['DOC_Type'], "Aerodrome Operating Minima")
        sleep(6)
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']").send_keys(
            Keys.ENTER)
        # 计算路径
        sleep(6)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(6)
        login.is_click(flight['Doc_Up'])
        sleep(6)
        login.is_click(flight['SaveAsDraft'])
        sleep(6)

        login.is_click(flight['SaveAsTemplate'])
        sleep(6)

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
        sleep(2)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['Submit'])
        sleep(15)
        # 免填写表格
        # login.is_click(flight['Close_New_Code'])
        # sleep(1)
        login.is_click(flight['Submit_Yes'])
        # login.is_click(flight['Submit_No'])
        # login.is_click(flight['Submit_Close'])
        # 填表格
        sleep(5)
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

        # login.input_text(flight['Lessor_Mark'], 'HK2023')
        # login.is_click(flight['Lessor_Type'])
        # login.input_text(flight['Lessor_Type'], "A139")
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/form/div[8]/div[2]/div/div/div/div/input").send_keys(
        #     Keys.ENTER)
        # login.input_text(flight['Lessor_Remark'],'Lease aircraft list aircraft remarks')

        login.is_click(flight["Lessor_Summit"])
        login.is_click(flight["Lessor_Yes"])
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
        sleep(5)
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        sleep(5)
        login.input_text(flight['ViewMessages_Sender'], cad_account['CpaOfficerLoginName'])
        sleep(5)
        login.is_click(flight['ViewMessages_ApplicationType'])
        sleep(5)
        login.is_click(flight['ViewMessages_Search'])
        sleep(5)
        price_element = drivers.find_element_by_xpath(
            "//*[@id='test0']/a/span/span[1]")
        refNo = price_element.text
        print(refNo)
        sleep(5)
        login.is_click(flight['ViewMessages_ReferenceNo'])
        # 13-26管理员的按钮测试
        sleep(5)
        login.is_click(flight['Modify_1'])
        sleep(5)
        login.is_click(flight['List_1'])
        sleep(5)
        login.is_click(flight['Modify_2'])
        # login.is_click(flight['Day7'])
        sleep(5)
        login.is_click(flight['Save_Modify'])
        sleep(5)
        login.is_click(flight['Save_All1'])
        sleep(5)
        login.is_click(flight['OK_All'])
        # #许可证和飞行权
        # login.is_click(flight['List_1'])
        # login.is_click(flight['Check_Licence'])
        # login.is_click(flight['Check_Traffic_Rights'])
        # login.is_click(flight['Close_Check_Traffic_Rights'])
        # # 选择文件
        login.is_click(flight['Select_from_Document_Library'])
        # login.is_click(flight['Enter_null'])
        # login.input_text(flight['Enter_null'], "")
        # sleep(2)
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[11]/div[2]/div/div[3]/div/div[2]/form/div[1]/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.is_click(flight['Search_null'])
        # sleep(2)
        login.is_click(flight['List_null'])
        sleep(2)
        login.is_click(flight['Summit_null'])
        # 上传文件
        drivers.find_element_by_class_name("el-icon-document-add").click()
        login.is_click(flight['Doc_Type_Minima_Input'])
        sleep(2)
        login.input_text(flight['Doc_Type_Minima_Input'], "Aerodrome Operating Minima")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(1)

        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        login.is_click(flight['NewUpload'])

        # login.is_click(flight['Messaging'])
        # Remark
        login.input_text(flight['Remark_Input'],
                         "THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING RE")

        # Cad Remark
        login.is_click(flight['Cad_Remark'])
        login.input_text(flight['Cad_Remark_Input'],
                         "THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING RE")

        # #自动计算
        # login.is_click(flight['Auto_Counting'])
        # login.is_click(flight['Close_Auto_Counting'])
        # 保存全部
        login.is_click(flight['Save_All1'])
        login.is_click(flight['OK_All2'])
        # 管理员同意下一步
        login.is_click(flight['ViewMessages_Approve'])
        login.is_click(flight['process'])

        login.is_click(flight['ViewMessages_Generate'])
        sleep(2)
        login.is_click(flight['ViewMessages_GenerateAndEdit'])
        sleep(1)
        login.input_text(flight['TemplateGenerate_OfficePhoneNo'], "2345671")
        login.input_text(flight['TemplateGenerate_OfficeFaxNo'], "12345678")
        # login.input_text(flight['TemplateGenerate_UserName'], "UAT Tester")
        login.input_text(flight['TemplateGenerate_Post'], "Tester")
        # login.input_text(flight['TemplateGenerate_SeasonInTitle'], "Summer 2023")
        # login.input_text(flight['TemplateGenerate_CompanyName'], "UAT Testing company")
        login.input_text(flight['TemplateGenerate_Address1'], "Testing address 1")
        # login.input_text(flight['TemplateGenerate_SeasonInContent'], "Summer 2023")
        login.input_text(flight['TemplateGenerate_Address2'], "Testing address 2")
        # login.input_text(flight['TemplateGenerate_SubjectOfficerName'], "AS Officer")
        login.input_text(flight['TemplateGenerate_Address3'], "Testing address 3")
        # login.input_text(flight['TemplateGenerate_PermitNo'], "123")
        login.input_text(flight['TemplateGenerate_Ferry'], "Ferry")
        login.input_text(flight['TemplateGenerate_SignedArea'], "Testing test")
        login.is_click(flight['TemplateGenerate_RefreshPreview'])
        login.is_click(flight['TemplateGenerate_DownloadAsWord'])
        login.is_click(flight['TemplateGenerate_GeneratePDF'])
        sleep(10)
        login.is_click(flight['Send'])
        sleep(20)
        login.is_click(flight['SendOK'])
        # drivers.find_element_by_class_name("testConfirmButtonClass02").click()
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
        login.is_click(flight['ViewMessages_AdvancedSearch_CAP'])
        login.input_text(flight['ViewMessages_SubjectContains_CAP'], "application Approved")
        login.input_text(flight['ViewMessages_Sender_CAP'], cad_account['OfficerLoginName'])
        login.is_click(flight['ViewMessages_ApplicationType2'])
        login.is_click(flight['ViewMessages_Search_CAP'])

        # login.is_click(flight['ViewMessages_ApprovedMessage_CAP'])
        # sleep(2)
        price_element = drivers.find_element_by_xpath(
            "//*[@id='test0']/a/span/span[1]")
        refNo = price_element.text
        print(refNo)
        login.is_click(flight['ReferenceNo'])
        sleep(2)

        # "Cargo Manifest" page displayed
        # login.input_user_name(cad_account['CpaOfficerLoginName'])
        # login.input_user_password(cad_account['CpaOfficerPassword'])
        # login.click_login_button()
        login.get_url(ini.url + "#/View/Manifest")
        login.input_text(flight['Cargo_Manifest_Reference_No'], refNo)

        login.is_click(flight['date_1'])
        login.input_text(flight['date_1'], "")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[5]/div/div/div/div[1]/input").send_keys(Keys.ENTER)

        login.is_click(flight['Cargo_Manifest_Search'])
        login.is_click(flight['Cargo_Manifest_Select'])
        login.is_click(flight['Cargo_Manifest_Upload_Cargo_Manifest'])
        login.input_text(flight['Cargo_Manifest_Date'], "01/10/2023")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/form/div[5]/div/div/div/input").send_keys(
            Keys.ENTER)
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

        login.is_click(flight['date_2'])
        login.input_text(flight['date_2'], "")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[5]/div/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Cargo_Manifest_Search'])
        # login.is_click(flight['Cargo_Manifest_Select'])
        # login.is_click(flight['Cargo_Manifest_Detail'])
        # login.is_click(flight['Cargo_Manifest_Download'])
        # sleep(2)
        # login.is_click(flight['Cargo_Manifest_Receive'])

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/test_hy112.py'])
