#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import random
import string
from random import randint

import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.readconfig import ini
from common.readelement import Element
from common.readvalue import ElementValue
from page.webpage import sleep
from page_object.LoginPage import LoginPage

'''
    每次执行前需修改temp的值以免Flight no.重复而报错
'''
s = string.ascii_letters
r = random.choice(s)
temp = str(randint(1000,9999))+r
data = Element('TC(E2E)-120')
value = ElementValue('TC(E2E)-120value')
codeshare_account=ElementValue('cad_account')
@allure.feature(" TC(ECE)-061 Local Operator Create and Officer Processing Private Non-Revenue Application (Approve)")
class TestFlight:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("TC(ECE)-120 Local Operator Create and Officer Processing Private Non-Revenue Application (Approve)")
    def test_001(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(codeshare_account['CpaOfficerLoginName'])
            login.input_user_password(codeshare_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        sleep(2)
        # login.is_click(data['Application'])
        # login.is_click(data['PrivateNonRevenueFlight'])
        #跳转到Application-PrivateNonRevenue页面
        #login.get_url(value['Url_PrivateNonRevenue'])
        login.get_url(ini.url + "#/ApplicationView/PrivateNonRevenue")
       # step 1
        sleep(3)
        login.is_click(data['HelicopterApplication'])
        sleep(3)
        login.is_click(data['LocalHandlingAgent'])
        sleep(1)
        login.is_click(data['LocalHandlingAgent_CPA'])
        sleep(1)
        login.input_text(data['RegistrationMark'], value['RegistrationMark'])
        sleep(1)
        login.is_click(data['LocalHandlingAgent'])
        sleep(1)
        login.is_click(data['AircraftType'])
        sleep(1)
        login.is_click(data['AircraftType_9A1'])
        sleep(1)
        login.is_click(data['NoiseStandard'])
        sleep(1)
        login.input_text(data['PurposeOfFlight'], value['PurposeOfFlight'])
        sleep(1)
        login.input_text(data['NoOfCrew'], value['NoOfCrew'])
        sleep(1)
        login.is_click(data['AircraftFittedWithTCAS'])

        login.is_click(data['ServiceType1'])
        sleep(1)
        login.is_click(data['ServiceType1_Ferry'])
        sleep(1)
        login.input_text(data['FlightNo1'], "CPA01"+temp)
        sleep(1)
        login.is_click(data['In-outFlightDiff1'])
        sleep(1)
        login.is_click(data['In-outFlightDiff1_NA'])
        sleep(1)
        login.input_text(data['OperationDate1'], value['OperationDate1'])
        login.is_click(data['NoOfPax1'])
        login.input_text(data['NoOfPax1'], value['NoOfPax1'])
        login.input_text(data['PortFrom1'], value['PortFrom1'])
        login.input_text(data['PortTo1'], value['PortTo1'])
        login.input_text(data['LocalTimeSTA1'], value['LocalTimeSTA1'])
        login.input_text(data['LocalTimeSTD1'], value['LocalTimeSTD1'])
        login.input_text(data['FlightScheduleRemarks1'], value['FlightScheduleRemarks1'])

        sleep(1)
        login.is_click(data['ServiceType2'])
        sleep(1)
        login.is_click(data['ServiceType2_Ferry'])
        sleep(1)
        login.input_text(data['FlightNo2'], "CPA02"+temp)
        login.is_click(data['In-outFlightDiff2'])
        login.is_click(data['In-outFlightDiff2_NA'])


        login.input_text(data['NoOfPax2'], value['NoOfPax2'])
        login.input_text(data['PortFrom2'], value['PortFrom2'])
        login.input_text(data['PortTo2'], value['PortTo2'])
        login.input_text(data['LocalTimeSTA2'], value['LocalTimeSTA2'])
        login.input_text(data['LocalTimeSTD2'], value['LocalTimeSTD2'])
        login.input_text(data['FlightScheduleRemarks2'], value['FlightScheduleRemarks2'])

        login.is_click(data['ServiceType3'])
        sleep(1)
        login.is_click(data['ServiceType3_GA'])
        sleep(1)
        login.input_text(data['FlightNo3'], "CPA03"+temp)
        login.is_click(data['In-outFlightDiff3'])
        login.is_click(data['In-outFlightDiff3_NA'])
        login.input_text(data['OperationDate3'], value['OperationDate3'])

        login.input_text(data['NoOfPax3'], value['NoOfPax3'])
        login.input_text(data['PortFrom3'], value['PortFrom3'])
        login.input_text(data['PortTo3'], value['PortTo3'])
        login.input_text(data['LocalTimeSTA3'], value['LocalTimeSTA3'])
        login.input_text(data['LocalTimeSTD3'], value['LocalTimeSTD3'])
        login.input_text(data['FlightScheduleRemarks3'], value['FlightScheduleRemarks3'])

        login.is_click(data['ServiceType4'])
        sleep(1)
        login.is_click(data['ServiceType4_GA'])
        sleep(1)
        login.input_text(data['FlightNo4'], "CPA04"+temp)
        login.is_click(data['In-outFlightDiff4'])
        login.is_click(data['In-outFlightDiff4_NA'])

        login.is_click(data['NoOfPax1'])
        login.input_text(data['NoOfPax4'], value['NoOfPax4'])
        login.input_text(data['PortFrom4'], value['PortFrom4'])
        login.input_text(data['PortTo4'], value['PortTo4'])
        login.input_text(data['LocalTimeSTA4'], value['LocalTimeSTA4'])
        login.input_text(data['LocalTimeSTD4'], value['LocalTimeSTD4'])
        login.input_text(data['FlightScheduleRemarks4'], value['FlightScheduleRemarks4'])

        login.is_click(data['ServiceType5'])
        sleep(1)
        login.is_click(data['ServiceType5_TechStop'])
        sleep(1)
        login.input_text(data['FlightNo5'], "CPA05"+temp)
        login.is_click(data['In-outFlightDiff5'])
        login.is_click(data['In-outFlightDiff5_NA'])
        login.input_text(data['OperationDate5'], value['OperationDate5'])

        login.input_text(data['NoOfPax5'], value['NoOfPax5'])
        login.input_text(data['PortFrom5'], value['PortFrom5'])
        login.input_text(data['PortTo5'], value['PortTo5'])
        login.input_text(data['LocalTimeSTA5'], value['LocalTimeSTA5'])
        login.input_text(data['LocalTimeSTD5'], value['LocalTimeSTD5'])
        login.input_text(data['FlightScheduleRemarks5'], value['FlightScheduleRemarks5'])

        login.is_click(data['ServiceType6'])
        sleep(1)
        login.is_click(data['ServiceType6_TechStop'])
        sleep(1)
        login.input_text(data['FlightNo6'], "CPA06"+temp)
        login.is_click(data['In-outFlightDiff6'])
        login.is_click(data['In-outFlightDiff6_NA'])


        login.input_text(data['NoOfPax6'], value['NoOfPax6'])
        login.input_text(data['PortFrom6'], value['PortFrom6'])
        login.input_text(data['PortTo6'], value['PortTo6'])
        login.input_text(data['LocalTimeSTA6'], value['LocalTimeSTA6'])
        login.input_text(data['LocalTimeSTD6'], value['LocalTimeSTD6'])
        login.input_text(data['FlightScheduleRemarks6'], value['FlightScheduleRemarks6'])

        login.is_click(data['ServiceType7'])
        sleep(1)
        login.is_click(data['ServiceType7_TestFlight'])
        sleep(1)
        login.input_text(data['FlightNo7'], "CPA07"+temp)
        login.is_click(data['In-outFlightDiff7'])
        login.is_click(data['In-outFlightDiff7_NA'])
        login.input_text(data['OperationDate7'], value['OperationDate7'])
        login.input_text(data['NoOfPax7'], value['NoOfPax7'])
        login.input_text(data['PortFrom7'], value['PortFrom7'])
        login.input_text(data['PortTo7'], value['PortTo7'])
        login.input_text(data['LocalTimeSTA7'], value['LocalTimeSTA7'])
        login.input_text(data['LocalTimeSTD7'], value['LocalTimeSTD7'])
        login.input_text(data['FlightScheduleRemarks7'], value['FlightScheduleRemarks7'])

        login.is_click(data['ServiceType8'])
        sleep(1)
        login.is_click(data['ServiceType8_TestFlight'])
        sleep(1)
        login.input_text(data['FlightNo8'], "CPA08"+temp)
        login.is_click(data['In-outFlightDiff8'])
        login.is_click(data['In-outFlightDiff8_NA'])
        login.input_text(data['NoOfPax8'], value['NoOfPax8'])
        login.input_text(data['PortFrom8'], value['PortFrom8'])
        login.input_text(data['PortTo8'], value['PortTo8'])
        login.input_text(data['LocalTimeSTA8'], value['LocalTimeSTA8'])
        login.input_text(data['LocalTimeSTD8'], value['LocalTimeSTD8'])
        login.input_text(data['FlightScheduleRemarks8'], value['FlightScheduleRemarks8'])

        login.is_click(data['ServiceType9'])
        sleep(1)
        login.is_click(data['ServiceType9_Training'])
        sleep(1)
        login.input_text(data['FlightNo9'], "CPA09"+temp)
        login.is_click(data['In-outFlightDiff9'])
        login.is_click(data['In-outFlightDiff9_NA'])
        login.input_text(data['OperationDate9'], value['OperationDate9'])
        sleep(2)
        login.input_text(data['NoOfPax9'], value['NoOfPax9'])
        login.input_text(data['PortFrom9'], value['PortFrom9'])
        login.input_text(data['PortTo9'], value['PortTo9'])
        login.input_text(data['LocalTimeSTA9'], value['LocalTimeSTA9'])
        login.input_text(data['LocalTimeSTD9'], value['LocalTimeSTD9'])
        login.input_text(data['FlightScheduleRemarks9'], value['FlightScheduleRemarks9'])

        login.is_click(data['ServiceType10'])
        sleep(1)
        login.is_click(data['ServiceType10_Training'])
        sleep(1)
        login.input_text(data['FlightNo10'], "CPA10"+temp)
        login.is_click(data['In-outFlightDiff10'])
        login.is_click(data['In-outFlightDiff10_NA'])
        login.input_text(data['NoOfPax10'], value['NoOfPax10'])
        login.input_text(data['PortFrom10'], value['PortFrom10'])
        login.input_text(data['PortTo10'], value['PortTo10'])
        login.input_text(data['LocalTimeSTA10'], value['LocalTimeSTA10'])
        login.input_text(data['LocalTimeSTD10'], value['LocalTimeSTD10'])
        login.input_text(data['FlightScheduleRemarks10'], value['FlightScheduleRemarks10'])

        login.input_text(data['Remarks'], value['Remarks'])
        login.is_click(data['UploadApplicationRelatedDocument1'])
        login.is_click(data['DocumentType'])
        login.is_click(data['DocumentType_Others'])
        sleep(2)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        login.input_text(data['ExpiryDate'], value['ExpiryDate'])
        sleep(2)
        login.is_click(data['UploadButton'])
        sleep(2)

        # step 2
        login.is_click(data['SaveAsDraft'])

        # step 3
        login.is_click(data['SaveAsTemplate'])
        login.input_text(data['TemplateName'], "Template" + str(random.uniform(1, 1000)))
        login.is_click(data['Template_Save'])

        login.is_click(data['ConfirmConditions'])
        # step 4
        login.is_click(data['PreviewAndSubmit'])
        # step 5 打印
        # 点击打印按钮,等待10秒后关闭窗口
        # login.is_click(data['Print'])
        # sleep(10)
        # pyautogui.press('esc')

        # step 6
        login.is_click(data['BackAndModify'])
        login.is_click(data['PreviewAndSubmit'])
        # step 7
        login.is_click(data['Submit'])
        # new code port description
        #login.input_text(data['PortDescription'],value['FlightScheduleRemarks1'])
        #login.is_click(data['SavaAsportDescription'])
        sleep(2)
        login.is_click(data['Submit_OK'])
        # step 8 new code暂时不管

        # 将用户切换到Officer
        login.is_click(data['Logout'])
        login.is_click(data['Logout_Yes'])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
          login.input_user_name(codeshare_account['OfficerLoginName'])
          login.input_user_password(codeshare_account['OfficerPassword'])
          login.click_login_button()
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        sleep(5)
        # step 9&10 跳转到View->Messages页面
        #login.get_url(value['Url_ViewMessages'])

        # login.get_url(ini.url + "#/View/Messages")
        # 搜索记录
        # login.is_click(data['AdvancedSearch'])
        # login.input_text(data['Sender'], value['Sender'])
        # login.is_click(data['ApplicationType_PrivateNonRevenue'])
        # login.is_click(data['SearchButton'])
        # sleep(5)
        # # drivers.find_element_by_id("test0").click()
        # # step 11
        # login.is_click(data['ReferenceNo_Officer'])
        #
        # sleep(5)

        # step 12-20 TS Officer不用管

        # step 21
        #login.get_url(value['Url_viewApplication'])
        login.get_url(ini.url + "index.html#/View/Application")

        login.is_click(data['ApplicationType_PrivateNonRevenue1'])
        login.is_click(data['AircraftCategory_Helicopter'])
        login.is_click(data['SearchButton1'])
        sleep(3)

        login.is_click(data['ReferenceNo_Officer1'])
        sleep(2)

        # step 21&22
        '''
        login.is_click(data['ModifyBasicInformation'])
        login.input_text(data['ModifyBasicInformation_RegistrationMark'], value['ModifyBasicInformation_RegistrationMark'])
        login.is_click(data['ModifyBasicInformation_AircraftType'])
        login.is_click(data['ModifyBasicInformation_AircraftType_A139'])
        login.input_text(data['ModifyBasicInformation_PurposeOfFlight'], value['ModifyBasicInformation_PurposeOfFlight'])
        login.input_text(data['ModifyBasicInformation_NoOfCrew'], value['ModifyBasicInformation_NoOfCrew'])
        '''

        # step 23
        '''
        login.is_click(data['SelectModifyRecord'])
        login.is_click(data['ModifyFlightSchedule'])

        login.is_click(data['ModifyFlightSchedule_ServiceType1'])

        login.is_click(data['ModifyFlightSchedule_ServiceType1_GA'])
        login.input_text(data['ModifyFlightSchedule_FlightNo1'], "CPA11"+temp)
        login.is_click(data['ModifyIn-outFlightDiff1'])
        login.is_click(data['ModifyIn-outFlightDiff1_NA'])
        login.input_text(data['ModifyFlightSchedule_OperationDate1'], value['ModifyFlightSchedule_OperationDate1'])
        drivers.find_element_by_xpath("//tr[1]/td[4]//input").send_keys(Keys.ENTER)
        login.input_text(data['ModifyFlightSchedule_NoOfPax1'], value['ModifyFlightSchedule_NoOfPax1'])
        login.input_text(data['ModifyFlightSchedule_PortFrom1'], value['ModifyFlightSchedule_PortFrom1'])
        login.input_text(data['ModifyFlightSchedule_PortTo1'], value['ModifyFlightSchedule_PortTo1'])
        login.input_text(data['ModifyFlightSchedule_LoaclTimeSTA1'], value['ModifyFlightSchedule_LoaclTimeSTA1'])
        login.input_text(data['ModifyFlightSchedule_LoaclTimeSTD1'], value['ModifyFlightSchedule_LoaclTimeSTD1'])
        login.input_text(data['ModifyFlightSchedule_Remarks1'], value['ModifyFlightSchedule_Remarks1'])
        login.is_click(data['ModifyFlightSchedule_ServiceType2'])
        login.is_click(data['ModifyFlightSchedule_ServiceType2_GA'])
        login.input_text(data['ModifyFlightSchedule_FlightNo2'], "CPA12"+temp)
        login.is_click(data['ModifyIn-outFlightDiff2'])
        login.is_click(data['ModifyIn-outFlightDiff2_NA'])
        #  login.input_text(data['ModifyFlightSchedule_OperationDate2'], value['ModifyFlightSchedule_OperationDate2'])
      #  drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[3]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(data['ModifyFlightSchedule_NoOfPax2'], value['ModifyFlightSchedule_NoOfPax2'])
        login.input_text(data['ModifyFlightSchedule_PortFrom2'], value['ModifyFlightSchedule_PortFrom2'])
        login.input_text(data['ModifyFlightSchedule_PortTo2'], value['ModifyFlightSchedule_PortTo2'])
        login.input_text(data['ModifyFlightSchedule_LoaclTimeSTA2'], value['ModifyFlightSchedule_LoaclTimeSTA2'])
        login.input_text(data['ModifyFlightSchedule_LoaclTimeSTD2'], value['ModifyFlightSchedule_LoaclTimeSTD2'])
        login.input_text(data['ModifyFlightSchedule_Remarks2'], value['ModifyFlightSchedule_Remarks2'])
        login.is_click(data['ModifyFlightSchedule_Save'])
        login.is_click(data['Modify_Save'])
        login.is_click(data['Modify_Save_OK'])
        '''
        # step 24


        # step 25
        '''
        login.is_click(data['SelectFromDocumentLibrary'])
        login.is_click(data['DocumentLibraryConfirm'])
        '''
        # step 26
        '''
        login.is_click(data['UploadApplicationRelatedDocument2'])
        login.is_click(data['DocumentType2'])
        login.is_click(data['DocumentType2_Others'])

        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//div[11]//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(data['ExpiryDate2'], value['ExpiryDate'])
        sleep(2)
        login.is_click(data['UploadButton2'])
        sleep(2)
        '''

        # step 27
        '''
        login.is_click(data['ViewUploadedDocuments'])
        login.is_click(data['ViewUploadedDocuments_Close'])
        '''

        # step 28
        '''
        login.is_click(data['Massaging'])
        handles = drivers.window_handles
        # 切换到新窗口 massing
        drivers.switch_to.window(handles[-1])
        login.input_text(data['Massaging_Input'], value['Massaging_Input'])
        sleep(2)
        login.is_click(data['Massaging_Send'])
        sleep(10)
        drivers.close()
        # 切换到原窗口
        drivers.switch_to.window(handles[0])
        '''

        # step 29
        '''
        login.input_text(data['Remarks2'], value['Remarks2'])
        '''
        # step 30
        '''
        login.is_click(data['CADRemarks'])
        login.input_text(data['CADRemarks_Input'], value['CADRemarks_Input'])
        '''
        # step 31
        '''
        login.is_click(data['AutoCountingFrequency'])
        login.is_click(data['AutoCountingFrequency_Close'])
        '''

        # step 32 打印
        # login.is_click(data['PrintApplication'])

        # step 33
        login.is_click(data['Approve'])

        # step 34
        login.is_click(data['Generate'])
        # step 35
        login.is_click(data['GenerateAndEdit'])
        login.input_text(data['TemplateGenerate_OfficePhoneNo'], value['TemplateGenerate_OfficePhoneNo'])
        login.input_text(data['TemplateGenerate_FaxNo'], value['TemplateGenerate_FaxNo'])
        login.input_text(data['TemplateGenerate_UserName'], value['TemplateGenerate_UserName'])
        login.input_text(data['TemplateGenerate_Post'], value['TemplateGenerate_Post'])
        login.input_text(data['TemplateGenerate_CompanyName'], value['TemplateGenerate_CompanyName'])
        login.input_text(data['TemplateGenerate_SubjectOfficerName'], value['TemplateGenerate_SubjectOfficerName'])
        login.input_text(data['TemplateGenerate_Address1'], value['TemplateGenerate_Address1'])
        login.input_text(data['TemplateGenerate_RegMark'], value['TemplateGenerate_RegMark'])
        login.input_text(data['TemplateGenerate_Address2'], value['TemplateGenerate_Address2'])
        login.input_text(data['TemplateGenerate_Address3'], value['TemplateGenerate_Address3'])
        login.input_text(data['TemplateGenerate_SignedArea'], value['TemplateGenerate_SignedArea'])
        login.is_click(data['TemplateGenerate_RefreshPreview'])
        login.is_click(data['TemplateGenerate_DownloadAsWord'])
        login.is_click(data['TemplateGenerate_GeneratePDF'])
        sleep(10)
        # step 36
        # login.is_click(data['AddAttachments'])
        #
        # # 使用pywinauto来选择文件
        # app = pywinauto.Desktop()
        # # 选择文件上传的窗口
        # dlg = app["打开"]
        # # 计算路径
        # current_path = os.path.abspath(__file__)
        # file_path = os.path.dirname(current_path) + "\TestFile\TestAttachment.pdf"
        # # 输入上传文件的路径
        # dlg.Edit.set_text(file_path)
        # sleep(3)
        # # 点击打开
        # dlg["打开(&O)"].click_input()
        sleep(2)
        login.is_click(data['Send'])

        sleep(2)
        login.is_click(data['Send_OK'])
        # step 37
        # 将用户切换到CPATEST03
        login.is_click(data['Logout'])
        login.is_click(data['Logout_Yes'])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(codeshare_account['CpaOfficerLoginName'])
            login.input_user_password(codeshare_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        sleep(2)
        #跳转到view-messages页面
        #login.get_url(value['Url_ViewMessages'])
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(data['AdvancedSearch_CPATEST03'])
        login.input_text(data['SubjectContains_CPATEST03'], value['SubjectContains_CPATEST03'])
        login.input_text(data['Sender_CPATEST03'], codeshare_account['OfficerLoginName'])
        # login.is_click(data['ApplicationType_PrivateNonRevenue_CPATEST03'])
        # sleep(1)
        login.is_click(data['SearchButton_CPATEST03'])
        # step 38
        # login.is_click(data['Message_CPATEST03'])
        # sleep(1)
        # step 39
        #login.is_click(data['Attachment'])
        #login.is_click(data['Attachment_Close'])
        # step 40
        # login.is_click(data['ReferenceNo_CPATEST03'])

        # login.is_click(data['Inbox_Details_Close_Btn'])
        # sleep(1)
        sleep(5)
        login.input_text(data['SubjectContains_CPATEST03'], value['SubjectContains_CPATEST03'])
        drivers.find_element_by_id("test0").click()
        #login.is_click(data['Reference_No'])
       # login.is_click(data['CPA_Message_Ref_No'])
        sleep(5)

        # step 41
        #login.get_url(value['Url_ViewFightSchedule'])
        login.get_url(ini.url + "index.html#/View/FlightSchedule")
        sleep(10)
        login.is_click(data['Fighth_Schedules_Aircraft_Category'])
        login.input_text(data['Effective_Period_Start'], value['Effective_Period_StartDate'])

        login.is_click(data['Fighth_Schedules_Search_Type_GA'])
        login.is_click(data['Fighth_Schedules_Search_Type_Ferry'])
        login.is_click(data['Fighth_Schedules_Search_Type_Tech_Stop'])
        login.is_click(data['Fighth_Schedules_Search_Type_Test_Flight'])
        login.is_click(data['Fighth_Schedules_Search_Type_Training'])

        # step 42
        login.is_click(data['Fighth_Schedules_Search_Search_Btn'])

        sleep(10)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_120/test_E2E_120.py'])

