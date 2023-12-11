import os
import allure
import pytest
from selenium.webdriver.common.keys import Keys
from page_object.LoginPage import LoginPage
from common.readconfig import ini
from page.webpage import sleep
from common.readvalue import ElementValue
from common.readelement import Element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

flight = Element('flight_083')
flightvalue = ElementValue('flightvalue_083')
cad_account = ElementValue('cad_account')
@allure.feature("TC(ECE)-083 Local Operator Create and Officer Processing Schedule Change Application (Approve) for Charter Cargo application")
class TestTrafficRightsRulesApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Process application by Officer")
    def test_083(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight['Logout_Yes'])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['OfficerLoginName'])
            login.input_user_password(cad_account['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        sleep(5)
        # 跳转到/View/Messages页面
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)

        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path) + '/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， r以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
        with open(filename, 'r') as f:
            refno = f.read()

        # step21
        login.is_click(flight['AdvancedSearch'])
        sleep(3)
        login.input_text(flight['Sender'], cad_account['CpaOfficerLoginName'])
        sleep(5)
        login.input_text(flight['ReferenceNo'], refno)
        sleep(5)
        login.is_click(flight['ScheduleChange'])
        sleep(5)

        # step22
        login.is_click(flight['Search_msg'])
        sleep(5)

        # step23
        login.is_click(flight['msg'])
        sleep(5)

        # step24 Step 26~36 are optional, can skip to step #37 for direct processing

        # step25
        login.is_click(flight['ClickFirstFlight'])
        sleep(3)
        login.is_click(flight['Modify'])
        sleep(3)
        login.is_click(flight['ModifyServiceType1'])
        sleep(3)
        login.input_text(flight['ModifyServiceType1'], flightvalue['ModifyServiceType'])
        sleep(3)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(3)
        login.is_click(flight['ModifyServiceType2'])
        sleep(2)
        login.input_text(flight['ModifyServiceType2'], flightvalue['ModifyServiceType'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['ModifyDop1'])
        sleep(2)
        login.is_click(flight['ModifyDop2'])
        sleep(2)
        login.is_click(flight['ModifyDop3'])
        sleep(3)
        login.is_click(flight['ModifyDop4'])
        sleep(3)
        login.is_click(flight['ModifyDop5'])
        sleep(3)
        login.is_click(flight['ModifyDop6'])
        sleep(3)
        login.input_text(flight['ModifyCargoAmount1'], flightvalue['ModifyCargoAmount1'])
        sleep(3)
        login.input_text(flight['ModifyCargoAmount2'], flightvalue['ModifyCargoAmount2'])
        sleep(3)
        login.input_text(flight['ModifyRemarks1'], flightvalue['ModifyRemarks1'])
        sleep(3)
        login.input_text(flight['ModifyRemarks2'], flightvalue['ModifyRemarks2'])
        sleep(3)
        login.is_click(flight['ModifySave'])
        sleep(5)

        # step26
        login.is_click(flight['ClickFirstFlight'])
        sleep(2)
        login.is_click(flight['CheckLicence'])
        sleep(2)

        # step27
        # login.is_click(flight['CheckTrafficRights'])
        # sleep(2)
        # login.is_click(flight['CheckTrafficRightsClose'])
        # sleep(2)

        # step28
        login.is_click(flight['CheckApprovedSlot'])
        sleep(2)

        # step29
        login.is_click(flight['ClickUpload'])
        sleep(2)
        login.is_click(flight['ClickLeaseAircraft'])
        sleep(2)
        login.is_click(flight['LessorOperator(ICAO)'])
        sleep(2)
        login.input_text(flight['LessorOperator(ICAO)'], flightvalue['LessorOperator(ICAO)'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[6]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['DocumentType'])
        sleep(2)
        login.input_text(flight['DocumentType'], flightvalue['DocumentType'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[7]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['RegistrationMark'], flightvalue['RegistrationMark'])
        sleep(2)
        login.is_click(flight['AircraftType'])
        sleep(2)
        login.input_text(flight['AircraftType'], flightvalue['AircraftType'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[8]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['ExpiryDate'])
        sleep(2)
        login.input_text(flight['ExpiryDate'], flightvalue['ExpiryDate'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[9]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['EnclosureReference'], flightvalue['EnclosureReference'])
        sleep(2)
        login.input_text(flight['UploadRemarks'], flightvalue['UploadRemarks'])
        sleep(2)
        login.is_click(flight['UploadButton'])
        sleep(2)
        login.is_click(flight['Upload_Ok'])
        sleep(2)

        # step30
        login.is_click(flight['ClickSelectDoc'])
        sleep(2)
        login.is_click(flight['SelectDoc1'])
        sleep(2)
        login.is_click(flight['SelectDoc1Confirm'])
        sleep(2)

        # step31
        login.is_click(flight['ClickUploadDoc'])
        sleep(2)
        login.is_click(flight['ClickDocType'])
        sleep(2)
        login.input_text(flight['ClickDocType'], flightvalue['DocType'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestData/In/other_supports.pdf"
        drivers.find_element_by_xpath("//*[@id='testBrowse']/following::input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight['ClickDate'], flightvalue['ClickDate'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['ClickUploadButton'])
        sleep(2)

        # step32
        # login.is_click(flight['ViewUploadedDocuments'])
        # sleep(2)
        # login.is_click(flight['ViewUploadedDocumentsClose'])
        # sleep(2)

        # step33
        login.is_click(flight['Messaging'])
        sleep(2)
        # 所有窗口计数
        i = 0
        # 获得当前主窗口
        nowhandle = drivers.current_window_handle
        # 获取所有窗口
        allhandles = drivers.window_handles
        for handle in allhandles:
            i = i + 1
        if (i > 1):
            # 切换到最新打开的窗口
            drivers.switch_to.window(allhandles[-1])
        sleep(2)
        # 关闭新窗口
        drivers.close()
        # 回到原来主窗口
        drivers.switch_to.window(nowhandle)
        sleep(3)

        # step34
        login.input_text(flight['RemarksText'], flightvalue['RemarksText'])
        sleep(2)

        # step35
        login.is_click(flight['CADRemarks'])
        sleep(2)
        login.input_text(flight['CADRemarksText'], flightvalue['CADRemarksText'])
        sleep(2)

        # step36
        # login.is_click(flight['PrintApplication'])

        # step37
        login.is_click(flight['ClickApprove'])
        sleep(2)

        # step38
        login.is_click(flight['ClickGenerate'])
        sleep(2)

        # step39
        login.is_click(flight['ClickGenerateAndEdit'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_OfficePhoneNo'], flightvalue['TemplateGenerate_OfficePhoneNo'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_OfficeFaxNo'], flightvalue['TemplateGenerate_OfficeFaxNo'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_UserName'], flightvalue['TemplateGenerate_UserName'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_Post'], flightvalue['TemplateGenerate_Post'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_CompanyName'], flightvalue['TemplateGenerate_CompanyName'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_SubjectOfficerName'], flightvalue['TemplateGenerate_SubjectOfficerName'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_Address1'], flightvalue['TemplateGenerate_Address1'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_Address2'], flightvalue['TemplateGenerate_Address2'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_Address3'], flightvalue['TemplateGenerate_Address3'])
        sleep(2)
        login.input_text(flight['TemplateGenerate_SignedArea'], flightvalue['TemplateGenerate_SignedArea'])
        sleep(2)
        login.is_click(flight['TemplateGenerate_RefreshPreview'])
        sleep(2)
        login.is_click(flight['TemplateGenerate_DownloadAsWord'])
        sleep(2)
        login.is_click(flight['TemplateGenerate_GeneratePDF'])
        sleep(10)

        # step40
        login.is_click(flight['SendLetter'])
        sleep(15)
        login.is_click(flight['SendLetterOK'])
        sleep(3)

        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight['Logout_Yes'])


if __name__ == '__main__':
    pytest.main(['TestCase/test_tc_e2e_083_3.py'])