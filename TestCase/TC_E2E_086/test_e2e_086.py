import random
import string
from random import randint
import os

import pytest
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep, WebPage
from common.readelement import Element
from utils.logger import log


temp = str(randint(10, 99))+random.choice(string.ascii_letters)
data = Element('TC(E2E)-086')
value = ElementValue('TC(E2E)-086value')
codeshare_account=ElementValue('cad_account')
@allure.feature(" TC(ECE)-086 Local Operator Create and Officer Processing Private Non-Revenue Application (Approve)")
class TestFlight:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("TC(ECE)-086 Local Operator Create and Officer Processing Private Non-Revenue Application (Approve)")
    def test_001(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
            login.is_click(data["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(codeshare_account['CpaOfficerLoginName'])
            login.input_user_password(codeshare_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 60, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))
        sleep(2)
        #跳转到Application-PrivateNonRevenue页面
        #login.get_url(value['Url_PrivateNonRevenue'])
        login.get_url(ini.url + "#/ApplicationView/PrivateNonRevenue")
        # step 1
        login.is_click(data['LocalHandlingAgent'])
        login.is_click(data['LocalHandlingAgent_CPA'])
        login.input_text(data['RegistrationMark'],value['RegistrationMark'])
        login.is_click(data['AircraftType'])
        login.is_click(data['AircraftType_100'])
        login.is_click(data['NoiseStandard'])
        sleep(3)
        login.input_text(data['PurposeOfFlight'],value['PurposeOfFlight'])
        sleep(3)
        login.input_text(data['NoOfCrew'],value['NoOfCrew'])
        sleep(3)
        login.is_click(data['AircraftFittedWithTCAS'])
        sleep(3)
        login.is_click(data['ServiceType1'])
        sleep(3)
        login.is_click(data['ServiceType1_Ferry'])
        Flight_1 = "CPA01"+temp;
        #login.input_text(data['FlightNo1'], "CPA01"+temp)
        login.input_text(data['FlightNo1'], Flight_1)
        sleep(3)
        login.input_text(data['OperationDate1'], value['OperationDate1'])
        sleep(3)
        login.is_click(data['NoOfPax1'])
        sleep(3)
        login.input_text(data['NoOfPax1'], value['NoOfPax1'])
        sleep(3)
        login.input_text(data['PortFrom1'], value['PortFrom1'])
        sleep(3)
        login.input_text(data['PortTo1'], value['PortTo1'])
        login.input_text(data['LocalTimeSTD1'], value['LocalTimeSTD1'])
        login.input_text(data['FlightScheduleRemarks1'], value['FlightScheduleRemarks1'])

        login.is_click(data['ServiceType2'])
        login.is_click(data['ServiceType2_Ferry'])
        login.input_text(data['FlightNo2'], "CPA02"+temp)
        login.input_text(data['NoOfPax2'], value['NoOfPax2'])
        sleep(1)
        login.input_text(data['PortFrom2'], value['PortFrom2'])
        sleep(1)
        login.input_text(data['PortTo2'], value['PortTo2'])
        sleep(1)
        login.input_text(data['LocalTimeSTA2'], value['LocalTimeSTA2'])
        sleep(1)
        login.input_text(data['FlightScheduleRemarks2'], value['FlightScheduleRemarks2'])
        sleep(2)
        login.is_click(data['ServiceType3'])
        sleep(2)
        login.is_click(data['ServiceType3_GA'])
        sleep(1)
        login.input_text(data['FlightNo3'], "CPA03"+temp)
        sleep(1)
        login.input_text(data['OperationDate3'], value['OperationDate3'])
        sleep(1)
        login.is_click(data['NoOfPax3'])
        login.input_text(data['NoOfPax3'], value['NoOfPax3'])
        login.input_text(data['PortFrom3'], value['PortFrom3'])
        login.input_text(data['PortTo3'], value['PortTo3'])
        login.input_text(data['LocalTimeSTD3'], value['LocalTimeSTD3'])
        login.input_text(data['FlightScheduleRemarks3'], value['FlightScheduleRemarks3'])

        login.is_click(data['ServiceType4'])
        login.is_click(data['ServiceType4_GA'])
        login.input_text(data['FlightNo4'], "CPA04"+temp)
        login.input_text(data['NoOfPax4'], value['NoOfPax4'])
        login.input_text(data['PortFrom4'], value['PortFrom4'])
        login.input_text(data['PortTo4'], value['PortTo4'])
        login.input_text(data['LocalTimeSTA4'], value['LocalTimeSTA4'])
        login.input_text(data['FlightScheduleRemarks4'], value['FlightScheduleRemarks4'])

        login.is_click(data['ServiceType5'])
        login.is_click(data['ServiceType5_TechStop'])
        login.input_text(data['FlightNo5'], "CPA05"+temp)
        login.input_text(data['OperationDate5'], value['OperationDate5'])
        login.is_click(data['NoOfPax5'])
        login.input_text(data['NoOfPax5'], value['NoOfPax5'])
        login.input_text(data['PortFrom5'], value['PortFrom5'])
        login.input_text(data['PortTo5'], value['PortTo5'])
        login.input_text(data['LocalTimeSTA5'], value['LocalTimeSTA5'])
        login.input_text(data['FlightScheduleRemarks5'], value['FlightScheduleRemarks5'])

        login.is_click(data['ServiceType6'])
        login.is_click(data['ServiceType6_TechStop'])
        login.input_text(data['FlightNo6'], "CPA06"+temp)
        login.input_text(data['NoOfPax6'], value['NoOfPax6'])
        login.input_text(data['PortFrom6'], value['PortFrom6'])
        login.input_text(data['PortTo6'], value['PortTo6'])
        login.input_text(data['LocalTimeSTD6'], value['LocalTimeSTD6'])
        login.input_text(data['FlightScheduleRemarks6'], value['FlightScheduleRemarks6'])

        login.is_click(data['ServiceType7'])
        login.is_click(data['ServiceType7_TestFlight'])
        login.input_text(data['FlightNo7'], "CPA07"+temp)
        login.input_text(data['OperationDate7'], value['OperationDate7'])
        login.is_click(data['NoOfPax7'])
        login.input_text(data['NoOfPax7'], value['NoOfPax7'])
        login.input_text(data['PortFrom7'], value['PortFrom7'])
        login.input_text(data['PortTo7'], value['PortTo7'])
        login.input_text(data['LocalTimeSTD7'], value['LocalTimeSTD7'])
        login.input_text(data['FlightScheduleRemarks7'], value['FlightScheduleRemarks7'])

        login.is_click(data['ServiceType8'])
        login.is_click(data['ServiceType8_TestFlight'])
        login.input_text(data['FlightNo8'], "CPA08"+temp)
        login.input_text(data['NoOfPax8'], value['NoOfPax8'])
        login.input_text(data['PortFrom8'], value['PortFrom8'])
        login.input_text(data['PortTo8'], value['PortTo8'])
        login.input_text(data['LocalTimeSTA8'], value['LocalTimeSTA8'])
        login.input_text(data['FlightScheduleRemarks8'], value['FlightScheduleRemarks8'])

        login.is_click(data['ServiceType9'])
        login.is_click(data['ServiceType9_Training'])
        login.input_text(data['FlightNo9'], "CPA09"+temp)
        login.input_text(data['OperationDate9'], value['OperationDate9'])
        login.is_click(data['NoOfPax9'])
        login.input_text(data['NoOfPax9'], value['NoOfPax9'])
        login.input_text(data['PortFrom9'], value['PortFrom9'])
        login.input_text(data['PortTo9'], value['PortTo9'])
        login.input_text(data['LocalTimeSTA9'], value['LocalTimeSTA9'])
        login.input_text(data['FlightScheduleRemarks9'], value['FlightScheduleRemarks9'])

        login.is_click(data['ServiceType10'])
        login.is_click(data['ServiceType10_Training'])
        login.input_text(data['FlightNo10'], "CPA10"+temp)
        login.input_text(data['NoOfPax10'], value['NoOfPax10'])
        login.input_text(data['PortFrom10'], value['PortFrom10'])
        login.input_text(data['PortTo10'], value['PortTo10'])
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
        login.input_text(data['TemplateName'], "template" + str(random.uniform(1, 9999)))
        login.is_click(data['Template_Save'])
        sleep(5)

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
        sleep(3)
        login.is_click(data['PreviewAndSubmit'])
        sleep(3)
        # step 7
        login.is_click(data['Submit'])
        sleep(8)
        try:
            login.is_click(data['Proceed'])
            sleep(3)
        except:
            print("Proceed button not exist")
        login.is_click(data['Submit_OK'])

        sleep(30)
        # assert drivers.find_element_by_css_selector("h2").text == "Search Application"
        # refNoValue = drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/div[5]/div/div[3]/table/tbody/tr[1]/td[4]/div/a/span/span")
        # 保存refNo
        # current_path = os.path.abspath(__file__)
        # filename = os.path.dirname(current_path) + '/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        # with open(filename, 'w') as f:
          #  f.write(refNoValue.text)

        # 将用户切换到Officer
        login.is_click(data['Logout'])
        login.is_click(data['Logout_Yes'])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(codeshare_account['OfficerLoginName'])
            login.input_user_password(codeshare_account['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        sleep(5)
        # step 8&9 跳转到view-messages页面
        #login.get_url(value['Url_ViewMessages'])
        login.get_url(ini.url + "#/View/Messages")
        # 搜索记录
        login.is_click(data['AdvancedSearch'])
        login.input_text(data['Sender'],codeshare_account['CpaOfficerLoginName'])

        login.is_click(data['ApplicationType_PrivateNonRevenue'])
        login.is_click(data['SearchButton'])
        # step 10
        #login.is_click(data['ReferenceNo_Officer'])
        #sleep(2)

        sleep(3)
        drivers.find_element_by_id("test0").click()

        sleep(10)

        # step 21
        #login.get_url(value['Url_viewApplication'])
        login.get_url(ini.url + "index.html#/View/Application")
        login.is_click(data['ApplicationType_PrivateNonRevenue1'])
        #login.is_click(data['AircraftCategory_Helicopter'])
        login.is_click(data['SearchButton1'])
        sleep(3)

        login.is_click(data['ReferenceNo_Officer1'])
        sleep(5)

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
        sleep(5)
        login.is_click(data['Approve'])
        sleep(10)
        # step 34
        login.is_click(data['Generate'])
        sleep(8)
        # step 35
        login.is_click(data['GenerateAndEdit'])
        sleep(2)
        login.input_text(data['TemplateGenerate_OfficePhoneNo'], value['TemplateGenerate_OfficePhoneNo'])
        sleep(1)
        login.input_text(data['TemplateGenerate_FaxNo'], value['TemplateGenerate_FaxNo'])
        sleep(1)
        login.input_text(data['TemplateGenerate_UserName'], value['TemplateGenerate_UserName'])
        sleep(1)
        login.input_text(data['TemplateGenerate_Post'], value['TemplateGenerate_Post'])
        login.input_text(data['TemplateGenerate_CompanyName'], value['TemplateGenerate_CompanyName'])
        login.input_text(data['TemplateGenerate_SubjectOfficerName'], value['TemplateGenerate_SubjectOfficerName'])
        login.input_text(data['TemplateGenerate_Address1'], value['TemplateGenerate_Address1'])
        login.input_text(data['TemplateGenerate_RegMark'], value['TemplateGenerate_RegMark'])
        login.input_text(data['TemplateGenerate_Address2'], value['TemplateGenerate_Address2'])
        login.input_text(data['TemplateGenerate_Address3'], value['TemplateGenerate_Address3'])
        login.input_text(data['TemplateGenerate_SignedArea'], value['TemplateGenerate_SignedArea'])
        sleep(2)
        login.is_click(data['TemplateGenerate_RefreshPreview'])
        sleep(2)
        login.is_click(data['TemplateGenerate_DownloadAsWord'])
        sleep(2)
        login.is_click(data['TemplateGenerate_GeneratePDF'])
        sleep(15)
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

        sleep(20)
        login.is_click(data['Send_OK'])
        sleep(5)

        # step 1
        # 将用户切换到CPATEST03
        login.is_click(data['Logout'])
        login.is_click(data['Logout_Yes'])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(codeshare_account['CpaOfficerLoginName'])
            login.input_user_password(codeshare_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))
        sleep(5)
        #跳转到Application->Schedule Change->Flight Schedule页面
        #login.get_url(value['Flight_Schedule'])
        login.get_url(ini.url + "#/ApplicationView/ScheduleChange/FlightSchedule")
        login.input_text(data['Operation_Period_StartDate'], value['Operation_Period_StartDate_Value'])

        login.input_text(data['Flight_No'], Flight_1)


        #login.is_click(data['Application_Type_PNR'])
        login.is_click(data['Schedule_Change_Search'])
        sleep(25)

        # step 2
        login.is_click(data['Flight_Schedules_Checked'])
        drivers.find_element_by_id("testRevise01").click()

        login.input_text(data['No_Of_Pax1'], value['No_Of_Pax1_Value'])
        login.input_text(data['No_Of_Pax2'], value['No_Of_Pax2_Value'])
        login.input_text(data['Local_Time_STA'], value['Local_Time_STA_Value'])

        drivers.find_element_by_id("testChangeSave01").click()
        sleep(30)
        login.is_click(data['Save_As_Draft_Btn'])
        sleep(10)
        login.is_click(data['Preview_And_Submit_Btn'])
        sleep(10)
        drivers.find_element_by_id("testChangeSubmit01").click()

        sleep(30)
        login.is_click(data['Ok_Btn'])
        sleep(5)

        # step 9
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
        # step 8&9 跳转到view-messages页面
        #login.get_url(value['Url_ViewMessages'])
        login.get_url(ini.url + "#/View/Messages")

        drivers.implicitly_wait(30)
        sleep(5)
        #assert drivers.find_element_by_css_selector("h2").text == "Messages"
        # current_path = os.path.abspath(__file__)
        # filename = os.path.dirname(current_path) + '/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， r以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
        # with open(filename, 'r') as f:
            # refno = f.read()
        # # 打开查询页
        login.is_click(data['ViewMessages_AdvancedSearch'])
        #login.input_text(data['ViewMessages_Search_ReferenceNo'], refno)
        login.input_text(data['ViewMessages_Sender'], codeshare_account['CpaOfficerLoginName'])
        login.is_click(data['Schedule_Charge_Type'])

        login.is_click(data['ViewMessages_Search'])
        sleep(10)
        # 检查查询结果
        # assert drivers.find_element_by_xpath("//*[@id='test0']").text == str(refno)
        # 进入详情页
        login.is_click(data['ViewMessages_ReferenceNo'])
        sleep(5)

        # step25
        drivers.find_element_by_id("testApproveChange").click()

        sleep(5)
        #drivers.find_element_by_id("testConfirm").click()
        #sleep(2)
        #drivers.find_element_by_id("testGenerate01").click()

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
        #login.input_text(data['TemplateGenerate_RegMark'], value['TemplateGenerate_RegMark'])
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
        #sleep(2)
        login.is_click(data['Send'])

        sleep(15)
        login.is_click(data['Send_OK'])



       # step29 将用户切换到CPATEST03
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
        # login.is_click(data['Attachment'])
        # login.is_click(data['Attachment_Close'])
        # step 40
        # login.is_click(data['ReferenceNo_CPATEST03'])

        # login.is_click(data['Inbox_Details_Close_Btn'])
        # sleep(1)
        sleep(5)
        login.input_text(data['SubjectContains_CPATEST03'], value['SubjectContains_CPATEST03'])
        drivers.find_element_by_id("test0").click()
        # login.is_click(data['Reference_No'])
        # login.is_click(data['CPA_Message_Ref_No'])
        sleep(5)

        # step 41
        #login.get_url(value['Url_ViewFightSchedule'])
        # login.get_url(ini.url + "index.html#/View/FlightSchedule")
        # sleep(10)
        # login.is_click(data['Fighth_Schedules_Aircraft_Category'])
        # login.input_text(data['Effective_Period_Start'], value['Effective_Period_StartDate'])
        #
        # login.is_click(data['Fighth_Schedules_Search_Type_GA'])
        # login.is_click(data['Fighth_Schedules_Search_Type_Ferry'])
        # login.is_click(data['Fighth_Schedules_Search_Type_Tech_Stop'])
        # login.is_click(data['Fighth_Schedules_Search_Type_Test_Flight'])
        # login.is_click(data['Fighth_Schedules_Search_Type_Training'])
        #
        # # step 42
        # login.is_click(data['Fighth_Schedules_Search_Search_Btn'])
        #
        # sleep(10)


if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_061/test_e2e_086.py'])

