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
data = Element('TC(E2E)-061')
value = ElementValue('TC(E2E)-061value')
codeshare_account=ElementValue('cad_account')
@allure.feature(" TC(ECE)-061 Local Operator Create and Officer Processing Private Non-Revenue Application (Approve)")
class TestFlight:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("TC(ECE)-061 Local Operator Create and Officer Processing Private Non-Revenue Application (Approve)")
    def test_001(self, drivers):
        """登录"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//*[@id='testLogout']")
        if len(logout_elements) > 0:
            drivers.find_element_by_xpath("//*[@id='testLogout']").click()
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
        sleep(2)
        login.is_click(data['LocalHandlingAgent'])
        sleep(2)
        login.is_click(data['LocalHandlingAgent_CPA'])
        login.input_text(data['RegistrationMark'],value['RegistrationMark'])
        sleep(2)
        login.is_click(data['AircraftType'])
        sleep(2)
        login.is_click(data['AircraftType_100'])
        login.is_click(data['NoiseStandard'])
        sleep(2)
        login.input_text(data['PurposeOfFlight'],value['PurposeOfFlight'])
        sleep(2)
        login.input_text(data['NoOfCrew'],value['NoOfCrew'])
        sleep(2)
        login.is_click(data['AircraftFittedWithTCAS'])

        sleep(2)
        login.is_click(data['ServiceType1'])
        sleep(8)
        login.is_click(data['ServiceType1_Ferry'])
        sleep(6)
        login.input_text(data['FlightNo1'], "CPA01"+temp)
        login.input_text(data['OperationDate1'], value['OperationDate1'])
        sleep(2)
        login.is_click(data['NoOfPax1'])
        sleep(2)
        login.input_text(data['NoOfPax1'], value['NoOfPax1'])
        login.input_text(data['PortFrom1'], value['PortFrom1'])
        login.input_text(data['PortTo1'], value['PortTo1'])
        login.input_text(data['LocalTimeSTD1'], value['LocalTimeSTD1'])
        login.input_text(data['FlightScheduleRemarks1'], value['FlightScheduleRemarks1'])

        login.is_click(data['ServiceType2'])
        sleep(2)
        login.is_click(data['ServiceType2_Ferry'])
        sleep(2)
        login.input_text(data['FlightNo2'], "CPA02"+temp)
        login.input_text(data['NoOfPax2'], value['NoOfPax2'])
        login.input_text(data['PortFrom2'], value['PortFrom2'])
        login.input_text(data['PortTo2'], value['PortTo2'])
        login.input_text(data['LocalTimeSTA2'], value['LocalTimeSTA2'])
        login.input_text(data['FlightScheduleRemarks2'], value['FlightScheduleRemarks2'])

        login.is_click(data['ServiceType3'])
        sleep(2)
        login.is_click(data['ServiceType3_GA'])
        sleep(2)
        login.input_text(data['FlightNo3'], "CPA03"+temp)
        login.input_text(data['OperationDate3'], value['OperationDate3'])
        login.is_click(data['NoOfPax3'])
        sleep(2)
        login.input_text(data['NoOfPax3'], value['NoOfPax3'])
        login.input_text(data['PortFrom3'], value['PortFrom3'])
        login.input_text(data['PortTo3'], value['PortTo3'])
        login.input_text(data['LocalTimeSTD3'], value['LocalTimeSTD3'])
        login.input_text(data['FlightScheduleRemarks3'], value['FlightScheduleRemarks3'])

        login.is_click(data['ServiceType4'])
        sleep(2)
        login.is_click(data['ServiceType4_GA'])
        sleep(2)
        login.input_text(data['FlightNo4'], "CPA04"+temp)
        login.input_text(data['NoOfPax4'], value['NoOfPax4'])
        login.input_text(data['PortFrom4'], value['PortFrom4'])
        login.input_text(data['PortTo4'], value['PortTo4'])
        login.input_text(data['LocalTimeSTA4'], value['LocalTimeSTA4'])
        login.input_text(data['FlightScheduleRemarks4'], value['FlightScheduleRemarks4'])

        login.is_click(data['ServiceType5'])
        sleep(2)
        login.is_click(data['ServiceType5_TechStop'])
        sleep(2)
        login.input_text(data['FlightNo5'], "CPA05"+temp)
        login.input_text(data['OperationDate5'], value['OperationDate5'])
        login.is_click(data['NoOfPax5'])
        sleep(2)
        login.input_text(data['NoOfPax5'], value['NoOfPax5'])
        login.input_text(data['PortFrom5'], value['PortFrom5'])
        login.input_text(data['PortTo5'], value['PortTo5'])
        login.input_text(data['LocalTimeSTA5'], value['LocalTimeSTA5'])
        login.input_text(data['FlightScheduleRemarks5'], value['FlightScheduleRemarks5'])

        login.is_click(data['ServiceType6'])
        sleep(2)
        login.is_click(data['ServiceType6_TechStop'])
        sleep(2)
        login.input_text(data['FlightNo6'], "CPA06"+temp)
        login.input_text(data['NoOfPax6'], value['NoOfPax6'])
        login.input_text(data['PortFrom6'], value['PortFrom6'])
        login.input_text(data['PortTo6'], value['PortTo6'])
        login.input_text(data['LocalTimeSTD6'], value['LocalTimeSTD6'])
        login.input_text(data['FlightScheduleRemarks6'], value['FlightScheduleRemarks6'])

        login.is_click(data['ServiceType7'])
        sleep(2)
        login.is_click(data['ServiceType7_TestFlight'])
        sleep(2)
        login.input_text(data['FlightNo7'], "CPA07"+temp)
        login.input_text(data['OperationDate7'], value['OperationDate7'])
        login.is_click(data['NoOfPax7'])
        sleep(2)
        login.input_text(data['NoOfPax7'], value['NoOfPax7'])
        login.input_text(data['PortFrom7'], value['PortFrom7'])
        login.input_text(data['PortTo7'], value['PortTo7'])
        login.input_text(data['LocalTimeSTD7'], value['LocalTimeSTD7'])
        login.input_text(data['FlightScheduleRemarks7'], value['FlightScheduleRemarks7'])

        login.is_click(data['ServiceType8'])
        sleep(2)
        login.is_click(data['ServiceType8_TestFlight'])
        sleep(2)
        login.input_text(data['FlightNo8'], "CPA08"+temp)
        login.input_text(data['NoOfPax8'], value['NoOfPax8'])
        login.input_text(data['PortFrom8'], value['PortFrom8'])
        login.input_text(data['PortTo8'], value['PortTo8'])
        login.input_text(data['LocalTimeSTA8'], value['LocalTimeSTA8'])
        login.input_text(data['FlightScheduleRemarks8'], value['FlightScheduleRemarks8'])

        login.is_click(data['ServiceType9'])
        sleep(2)
        login.is_click(data['ServiceType9_Training'])
        sleep(2)
        login.input_text(data['FlightNo9'], "CPA09"+temp)
        login.input_text(data['OperationDate9'], value['OperationDate9'])
        login.is_click(data['NoOfPax9'])
        sleep(2)
        login.input_text(data['NoOfPax9'], value['NoOfPax9'])
        login.input_text(data['PortFrom9'], value['PortFrom9'])
        login.input_text(data['PortTo9'], value['PortTo9'])
        login.input_text(data['LocalTimeSTA9'], value['LocalTimeSTA9'])
        login.input_text(data['FlightScheduleRemarks9'], value['FlightScheduleRemarks9'])

        login.is_click(data['ServiceType10'])
        sleep(2)
        login.is_click(data['ServiceType10_Training'])
        sleep(2)
        login.input_text(data['FlightNo10'], "CPA10"+temp)
        login.input_text(data['NoOfPax10'], value['NoOfPax10'])
        login.input_text(data['PortFrom10'], value['PortFrom10'])
        login.input_text(data['PortTo10'], value['PortTo10'])
        login.input_text(data['LocalTimeSTD10'], value['LocalTimeSTD10'])
        login.input_text(data['FlightScheduleRemarks10'], value['FlightScheduleRemarks10'])

        login.input_text(data['Remarks'], value['Remarks'])
        login.is_click(data['UploadApplicationRelatedDocument1'])
        sleep(2)
        login.is_click(data['DocumentType'])
        sleep(2)
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
        sleep(2)

        # step 3
        login.is_click(data['SaveAsTemplate'])
        sleep(2)
        login.input_text(data['TemplateName'], "Template" + str(random.uniform(1, 9999)))
        sleep(2)
        login.is_click(data['Template_Save'])
        sleep(5)

        login.is_click(data['ConfirmConditions'])
        sleep(5)
        # step 4
        login.is_click(data['PreviewAndSubmit'])
        sleep(3)
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
        sleep(15)
        login.is_click(data['Submit_OK'])
        sleep(5)
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
        sleep(2)
        login.is_click(data['SearchButton'])
        sleep(2)
        # step 10
        login.is_click(data['ReferenceNo_Officer'])
        sleep(2)

        # step 11&12
        login.is_click(data['ModifyBasicInformation'])
        sleep(2)
        login.input_text(data['ModifyBasicInformation_RegistrationMark'], value['ModifyBasicInformation_RegistrationMark'])
        sleep(2)
        login.is_click(data['ModifyBasicInformation_AircraftType'])
        sleep(2)
        login.is_click(data['ModifyBasicInformation_AircraftType_773'])
        login.input_text(data['ModifyBasicInformation_PurposeOfFlight'], value['ModifyBasicInformation_PurposeOfFlight'])
        login.input_text(data['ModifyBasicInformation_NoOfCrew'], value['ModifyBasicInformation_NoOfCrew'])

        # step 13
        login.is_click(data['SelectModifyRecord'])
        sleep(2)
        login.is_click(data['ModifyFlightSchedule'])
        sleep(2)
        login.is_click(data['ModifyFlightSchedule_ServiceType1'])
        sleep(2)
        login.is_click(data['ModifyFlightSchedule_ServiceType1_GA'])
        sleep(2)
        login.input_text(data['ModifyFlightSchedule_FlightNo1'], "CPA11"+temp)
        login.input_text(data['ModifyFlightSchedule_OperationDate1'], value['ModifyFlightSchedule_OperationDate1'])
        drivers.find_element_by_xpath("//tr[1]/td[4]//input").send_keys(Keys.ENTER)
        login.input_text(data['ModifyFlightSchedule_NoOfPax1'], value['ModifyFlightSchedule_NoOfPax1'])
        login.input_text(data['ModifyFlightSchedule_PortFrom1'], value['ModifyFlightSchedule_PortFrom1'])
        login.input_text(data['ModifyFlightSchedule_PortTo1'], value['ModifyFlightSchedule_PortTo1'])
        login.input_text(data['ModifyFlightSchedule_LoaclTimeSTD1'], value['ModifyFlightSchedule_LoaclTimeSTD1'])
        login.input_text(data['ModifyFlightSchedule_Remarks1'], value['ModifyFlightSchedule_Remarks1'])
        login.is_click(data['ModifyFlightSchedule_ServiceType2'])
        sleep(2)
        login.is_click(data['ModifyFlightSchedule_ServiceType2_GA'])
        sleep(2)
        login.input_text(data['ModifyFlightSchedule_FlightNo2'], "CPA12"+temp)
        login.input_text(data['ModifyFlightSchedule_NoOfPax2'], value['ModifyFlightSchedule_NoOfPax2'])
        login.input_text(data['ModifyFlightSchedule_PortFrom2'], value['ModifyFlightSchedule_PortFrom2'])
        login.input_text(data['ModifyFlightSchedule_PortTo2'], value['ModifyFlightSchedule_PortTo2'])
        login.input_text(data['ModifyFlightSchedule_LoaclTimeSTA2'], value['ModifyFlightSchedule_LoaclTimeSTA2'])
        login.input_text(data['ModifyFlightSchedule_Remarks2'], value['ModifyFlightSchedule_Remarks2'])
        login.is_click(data['ModifyFlightSchedule_Save'])
        login.is_click(data['Modify_Save'])
        login.is_click(data['Modify_Save_OK'])

        # step 14
        # login.is_click(data['SelectModifyRecord'])
        # sleep(2)
        # login.is_click(data['CheckTrafficRights'])
        # sleep(5)
        # login.is_click(data['CheckTrafficRights_Close'])
        # sleep(5)
        # login.is_click(data['CheckTApprovedSlot'])

        # step 15
        # login.is_click(data['NewlySubmittedDocuments_Upload'])
        # login.is_click(data['LeaseAircraft'])
        # # login.input_text(data['LeaseAircraft_LessorOperator'], value['LeaseAircraft_LessorOperator'])
        # login.is_click(data['LeaseAircraft_LessorOperator'])
        # login.is_click(data['LeaseAircraft_LessorOperator_HDA'])
        # login.is_click(data['LeaseAircraft_DocumentType'])
        # login.is_click(data['LeaseAircraft_DocumentType_GovernmentApproval(Lessee)'])
        # login.input_text(data['LeaseAircraft_RegistrationMark'], value['LeaseAircraft_RegistrationMark'])
        # login.is_click(data['LeaseAircraft_AircraftType'])
        # login.is_click(data['LeaseAircraft_AircraftType_722'])
        # login.input_text(data['LeaseAircraft_ExpiryDate'], value['LeaseAircraft_ExpiryDate'])
        # # drivers.find_element_by_xpath("//div[contains(label,'Expiry Date')]//input[@type='text']").send_keys(Keys.ENTER)
        #
        # login.is_click(data['LeaseAircraft_PNRRelated'])
        # login.is_click(data['LeaseAircraft_PNRRelated_Close'])
        # login.input_text(data['LeaseAircraft_EnclosureReference'], value['LeaseAircraft_EnclosureReference'])
        # login.input_text(data['LeaseAircraft_Remarks'], value['LeaseAircraft_Remarks'])
        # login.is_click(data['LeaseAircraft_Upload'])
        # login.is_click(data['LeaseAircraft_Upload_OK'])

        # step 16
        login.is_click(data['SelectFromDocumentLibrary'])
        sleep(1)
        login.is_click(data['DocumentLibraryConfirm'])
        sleep(1)
        # step 17
        login.is_click(data['UploadApplicationRelatedDocument2'])
        sleep(1)
        login.is_click(data['DocumentType2'])
        sleep(1)
        login.is_click(data['DocumentType2_Others'])
        sleep(1)

        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(data['ExpiryDate2'], value['ExpiryDate'])
        sleep(2)
        login.is_click(data['UploadButton2'])
        sleep(2)

        # step 18
        login.is_click(data['ViewUploadedDocuments'])
        sleep(1)
        login.is_click(data['ViewUploadedDocuments_Close'])
        sleep(1)

        # step 19
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

        # step 20
        login.input_text(data['Remarks2'], value['Remarks2'])

        # step 21
        login.is_click(data['CADRemarks'])
        login.input_text(data['CADRemarks_Input'], value['CADRemarks_Input'])

        # step 22
        login.is_click(data['AutoCountingFrequency'])
        login.is_click(data['AutoCountingFrequency_Close'])

        # step 23 打印
        # login.is_click(data['PrintApplication'])

        # step 24
        login.is_click(data['Approve'])
        sleep(5)
        # step 25
        login.is_click(data['Generate'])
        sleep(10)
        # step 26
        login.is_click(data['GenerateAndEdit'])
        sleep(1)
        login.input_text(data['TemplateGenerate_OfficePhoneNo'], value['TemplateGenerate_OfficePhoneNo'])
        sleep(1)
        login.input_text(data['TemplateGenerate_FaxNo'], value['TemplateGenerate_FaxNo'])
        sleep(1)
        login.input_text(data['TemplateGenerate_UserName'], value['TemplateGenerate_UserName'])
        sleep(1)
        login.input_text(data['TemplateGenerate_Post'], value['TemplateGenerate_Post'])
        sleep(1)
        login.input_text(data['TemplateGenerate_CompanyName'], value['TemplateGenerate_CompanyName'])
        sleep(1)
        login.input_text(data['TemplateGenerate_SubjectOfficerName'], value['TemplateGenerate_SubjectOfficerName'])
        sleep(1)
        login.input_text(data['TemplateGenerate_Address1'], value['TemplateGenerate_Address1'])
        sleep(1)
        login.input_text(data['TemplateGenerate_RegMark'], value['TemplateGenerate_RegMark'])
        sleep(1)
        login.input_text(data['TemplateGenerate_Address2'], value['TemplateGenerate_Address2'])
        sleep(1)
        login.input_text(data['TemplateGenerate_Address3'], value['TemplateGenerate_Address3'])
        sleep(1)
        login.input_text(data['TemplateGenerate_SignedArea'], value['TemplateGenerate_SignedArea'])
        sleep(1)
        login.is_click(data['TemplateGenerate_RefreshPreview'])
        sleep(2)
        login.is_click(data['TemplateGenerate_DownloadAsWord'])
        sleep(2)
        login.is_click(data['TemplateGenerate_GeneratePDF'])
        sleep(6)
        # login.is_click(data['TemplateGenerate_Close'])
        #sleep(2)
        login.is_click(data['Send'])
        sleep(15)
        login.is_click(data['Send_OK'])
        sleep(5)
        # step 28
        # 将用户切换到CPATEST03
        login.is_click(data['Logout'])
        login.is_click(data['Logout_Yes'])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(codeshare_account['CpaOfficerLoginName'])
            login.input_user_password(codeshare_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))
        sleep(2)
        #跳转到view-messages页面
        #login.get_url(value['Url_ViewMessages'])
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(data['AdvancedSearch_CPATEST03'])
        login.input_text(data['SubjectContains_CPATEST03'], value['SubjectContains_CPATEST03'])
        login.input_text(data['Sender_CPATEST03'], codeshare_account['OfficerLoginName'])
        login.is_click(data['ApplicationType_PrivateNonRevenue_CPATEST03'])
        login.is_click(data['SearchButton_CPATEST03'])
        # step 29
        login.is_click(data['Message_CPATEST03'])
        sleep(2)
        # step 30
        login.is_click(data['Attachment'])
        sleep(3)
        # step 31
        login.is_click(data['ReferenceNo_CPATEST03'])
        sleep(3)
        login.is_click(data['Logout'])
        login.is_click(data['Logout_Yes'])
        sleep(3)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_061/test_e2e_061.py'])

