#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('flight_097')
flightvalue = ElementValue('flightvalue_097')
accountValue = ElementValue('cad_account')

def uploadFile(drivers, login, addDocuments, documentsType, remarks, filePath):
    sleep(1)
    login.is_click(addDocuments)
    sleep(1)
    login.is_click(flight['DocumentsType'])
    login.input_text(flight['DocumentsType'], documentsType)
    sleep(1)
    drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
    sleep(1)
    # login.is_click(flight['uploadBrowse'])
    sleep(1)
    # 计算路径
    current_path = os.path.abspath(__file__)
    file_path = os.path.dirname(current_path) + "/TestFile/" + filePath
    sleep(1)
    drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
    sleep(1)
    login.is_click(flight['UploadRemarks'])
    login.input_text(flight['UploadRemarks'], remarks)
    sleep(1)
    login.is_click(flight['UploadButton'])
    sleep(1)

@allure.feature("TC(ECE)-097 Local Operator Create and Officer Processing Lease Aircraft Application(Approve)")
class TestMissNoSeatsError:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Miss inputting mandatory No. of Seats field")
    def test_097(self, drivers):
        # login Local Operator (CPA)
        login = LoginPage(drivers)

        logout_elements = drivers.find_elements_by_xpath("//*[@id='testLogout']")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(accountValue['CpaOfficerLoginName'])
            login.input_user_password(accountValue['CpaOfficerPassword'])
            login.click_login_button()

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        '''跳转到Apply for Lease Aircraft Operation页面'''
        login.get_url(ini.url + "#/ApplicationView/LeaseAircraft")
        sleep(3)

        drivers.implicitly_wait(30)
        sleep(1)
        assert drivers.find_element_by_css_selector("h2").text == "Apply for Lease Aircraft Operation"
        # Operator
        # login.is_click(flight['Operator_select'])
        # login.input_text(flight['Operator(ICAO)'], "CPA")
        # sleep(1)
        #
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)

        # LeaseOperator
        login.is_click(flight['LeaseOperator_select'])
        login.input_text(flight['LeaseOperator(ICAO)'], "SIA")
        sleep(1)

        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[2]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)

        # EffectivePeriod
        login.is_click(flight['EffectivePeriodPrefix'])
        login.input_text(flight['EffectivePeriodPrefix'], "01/08/2023")
        sleep(1)

        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[1]/input").send_keys(Keys.ENTER)

        login.is_click(flight['EffectivePeriodSuffix'])
        login.input_text(flight['EffectivePeriodSuffix'], "31/12/2023")
        sleep(1)

        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input").send_keys(Keys.ENTER)

        # Supporting Documents
        # Upload file
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Aerodrome Operating Minima", "Remarks 1", "sample_file.pdf")
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Air Operator Certificate (Lessor)", "Remarks 2", "other_supports.pdf")
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Air Operator Certificate (Lessee)", "Remarks 3", "sample_file.pdf")
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Aircraft Lease Agreement", "Remarks 4", "other_supports.pdf")
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Government Approval (Lessor)", "Remarks 5", "sample_file.pdf")
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Government Approval (Lessee)", "Remarks 6", "other_supports.pdf")
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Insurance Certificate (Lessor)", "Remarks 7", "sample_file.pdf")
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Insurance Certificate (Lessee)", "Remarks 8", "other_supports.pdf")
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Operation Specification (Lessor)", "Remarks 9", "sample_file.pdf")
        uploadFile(drivers, login, flight['SupportingAddDocuments'], "Operation Specification (Lessee)", "Remarks 10", "other_supports.pdf")

        # RegistrationMark
        login.is_click(flight['RegistrationMark'])
        login.input_text(flight['RegistrationMark'], "HK2001")
        sleep(1)
        # AircraftType
        login.is_click(flight['AircraftType'])
        login.input_text(flight['AircraftType'], "141")
        sleep(1)

        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[8]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        # Upload file
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Aerodrome Operating Minima", "Remarks 15", "sample_file.pdf")
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Air Operator Certificate (Lessor)", "Remarks 16", "other_supports.pdf")
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Air Operator Certificate (Lessee)", "Remarks 17", "sample_file.pdf")
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Aircraft Lease Agreement", "Remarks 18", "other_supports.pdf")
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Government Approval (Lessor)", "Remarks 19", "sample_file.pdf")
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Government Approval (Lessee)", "Remarks 20", "other_supports.pdf")
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Insurance Certificate (Lessor)", "Remarks 21", "sample_file.pdf")
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Insurance Certificate (Lessee)", "Remarks 22", "other_supports.pdf")
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Operation Specification (Lessor)", "Remarks 23", "sample_file.pdf")
        uploadFile(drivers, login, flight['AircraftAddDocuments'], "Operation Specification (Lessee)", "Remarks 24", "other_supports.pdf")

        # Remarks
        login.is_click(flight['Remarks'])
        login.input_text(flight['Remarks'], "UAT End2End Testing")
        sleep(1)

        # Submit
        login.is_click(flight['Submit'])
        sleep(2)
        login.is_click(flight['SubmitOk'])
        sleep(2)

        # logout
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        # login AS Officer
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(accountValue['OfficerLoginName'])
            login.input_user_password(accountValue['OfficerPassword'])
            login.click_login_button()

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        # 跳转message页面
        login.is_click(flight['Home'])
        sleep(1)
        login.is_click(flight['Message'])
        sleep(1)
        # 搜索最新流程
        login.is_click(flight['AdvancedSearch'])
        sleep(1)
        login.is_click(flight['LeaseAircraft'])
        sleep(1)
        login.is_click(flight['SearchButton'])
        sleep(6)
        # 选中最新流程
        login.is_click(flight['Subject'])
        sleep(6)
        # 跳转流程页面
        login.is_click(flight['ReferenceNo'])
        sleep(6)
        # Modify
        login.is_click(flight['Modify'])
        sleep(2)
        login.is_click(flight['ModifyLeaseType'])
        sleep(1)
        login.input_text(flight['ModifyRemarks'], "Update Remarks")

        # Officer Remarks
        login.is_click(flight['OfficerRemarks'])
        sleep(1)
        login.input_text(flight['OfficerRemarksInput'], "THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING REMARKS WITH 250 CHARACTERS THIS IS A TESTING RE")

        # CAD Remarks
        login.is_click(flight['CADRemarks'])
        sleep(1)
        login.input_text(flight['CADRemarksInput'], "THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS THIS IS A TESTING CAD REMARKS WITH 250 CHARACTERS!")

        # Modify Save
        login.is_click(flight['Save'])
        sleep(1)
        login.is_click(flight['SaveOk'])
        sleep(1)

        # Supporting Document Upload
        login.is_click(flight['SupportingDocumentUpload'])
        sleep(1)
        login.input_text(flight['SupportingDocumentRegistrationMarkUpload'], "HK2001")
        login.is_click(flight['SupportingDocumentAircraftTypeUpload'])
        sleep(1)
        login.input_text(flight['SupportingDocumentAircraftTypeUpload'], "143")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div[1]/div/div[2]/form/div[8]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['SupportingDocumentExpiryDateUpload'])
        sleep(1)
        login.input_text(flight['SupportingDocumentExpiryDateUpload'], "21/12/2023")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div[1]/div/div[2]/form/div[9]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['SupportingDocumentEnclosureReferenceUpload'], "End2End Test")
        login.input_text(flight['SupportingDocumentRemarksUpload'], "UAT app remarks test")
        login.is_click(flight['SupportingDocumentUploadButton'])
        sleep(1)
        login.is_click(flight['SupportingDocumentUploadButtonOk'])
        sleep(1)

        # List Of Aircraft Related Document Upload
        login.is_click(flight['ListOfAircraftRelatedDocumentUpload'])
        sleep(1)
        login.input_text(flight['ListOfAircraftRelatedDocumentRegistrationMarkUpload'], "HK2001")
        login.is_click(flight['ListOfAircraftRelatedDocumentAircraftTypeUpload'])
        sleep(1)
        login.input_text(flight['ListOfAircraftRelatedDocumentAircraftTypeUpload'], "143")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div[1]/div/div[2]/form/div[8]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['ListOfAircraftRelatedDocumentExpiryDateUpload'])
        sleep(1)
        login.input_text(flight['ListOfAircraftRelatedDocumentExpiryDateUpload'], "21/12/2023")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div[1]/div/div[2]/form/div[9]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['ListOfAircraftRelatedDocumentEnclosureReferenceUpload'], "End2End Test")
        login.input_text(flight['ListOfAircraftRelatedDocumentRemarksUpload'], "UAT app remarks test")
        login.is_click(flight['ListOfAircraftRelatedDocumentUploadButton'])
        sleep(1)
        login.is_click(flight['ListOfAircraftRelatedDocumentUploadButtonOk'])
        sleep(1)

        # Show Documents for Aircrafts Leased from Other Airlines
        login.is_click(flight['ShowDocumentsForAircraftsLeasedFromOtherAirlines'])
        sleep(3)
        login.is_click(flight['CloseDocumentsForAircraftsLeasedFromOtherAirlines'])
        sleep(1)
        # Show Documents for Aircrafts Leased to Other Airlines
        login.is_click(flight['ShowDocumentsForAircraftsLeasedToOtherAirlines'])
        sleep(3)
        login.is_click(flight['CloseDocumentsForAircraftsLeasedToOtherAirlines'])
        sleep(1)

        # Messaging

        # login.is_click(flight['Messaging'])
        # sleep(2)
        #
        # #所有窗口计数
        # i = 0
        # #获得当前主窗口
        # nowhandle=drivers.current_window_handle
        # #获取所有窗口
        # allhandles=drivers.window_handles
        # for handle in allhandles:
        #     i = i+1
        # if(i > 1):
        #     #切换到最新打开的窗口
        #     drivers.switch_to.window(allhandles[-1])
        # login.input_text(flight['MessagingInput'], "email msg test")
        # login.is_click(flight['Send'])
        # sleep(5)
        # #关闭新窗口
        # drivers.close()
        #
        # #回到原来主窗口
        # drivers.switch_to.window(nowhandle)
        # sleep(3)

        # Approve
        login.is_click(flight['Approve'])
        sleep(3)
        # Generate
        login.is_click(flight['Generate'])
        sleep(15)
        # Generate And Edit
        login.is_click(flight['GenerateAndEdit'])
        sleep(3)
        login.input_text(flight['OfficePhoneNo'], "2345671")
        login.input_text(flight['OfficeFaxNo'], "12345678")
        login.input_text(flight['UserName'], "UAT Tester")
        login.input_text(flight['Post'], "Tester")
        login.input_text(flight['CompanyName'], "UAT Testing company")
        login.input_text(flight['Address1'], "Testing address 1")
        login.input_text(flight['Address2'], "Testing address 2")
        login.input_text(flight['Address3'], "Testing address 3")
        login.input_text(flight['FromDate'], "01/07/2023")
        drivers.find_element_by_xpath("/html/body/div[7]/div/div[2]/div/div[1]/form/div[6]/div[2]/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['ToDate'], "31/12/2023")
        drivers.find_element_by_xpath("/html/body/div[7]/div/div[2]/div/div[1]/form/div[7]/div[2]/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['SignedArea'], "Testing test")
        login.input_text(flight['AircraftRegmark'], "HK2024")
        login.input_text(flight['AirlinesName'], "CPA")
        sleep(3)
        login.is_click(flight['RefreshPreview'])
        sleep(2)
        login.is_click(flight['DownloadAsWord'])
        sleep(5)
        login.is_click(flight['GeneratePDF'])
        sleep(5)

        # Send
        login.is_click(flight['Send'])
        sleep(20)
        login.is_click(flight['SendOk'])
        sleep(3)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        # login Local Operator (CPA)
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(accountValue['CpaOfficerLoginName'])
            login.input_user_password(accountValue['CpaOfficerPassword'])
            login.click_login_button()

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))
        sleep(3)
        login.is_click(flight["OfficerSubject"])
        sleep(3)
        login.is_click(flight["OfficerAttachment"])
        sleep(10)
        login.is_click(flight["OfficerReferenceNo"])
        sleep(15)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        sleep(5)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_097/test_local_operator_create.py'])
