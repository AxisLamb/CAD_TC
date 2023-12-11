import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.readelement import Element
import os
codeshare=Element('flight_087')
codesharevalue=ElementValue('flightvalue_087')
cad_account=ElementValue('cad_account')

@allure.feature("TC(ECE)-087 Local Operator Create and Officer Processing Code Sharing Application (Approve)")
class TestSchedulePassengerApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_codeshare(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create Code Sharing Application and Approve")
    # 每次测试前需要在flightvalue.yaml文件中更新FlightNo和TemplateName值，不然会报重复航班号和模板名错误
    def test_087(self, drivers):
        """登录CPATESTCODE03用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//*[@id='testLogout']")
        if len(logout_elements) > 0:
          login.is_click(codeshare["Logout"])
          login.is_click(codeshare["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
           login.input_user_name(cad_account['CpaOfficerLoginName_87'])
           login.input_user_password(cad_account['CpaOfficerPassword_87'])
           login.click_login_button()
        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        #跳转到Application-Seasonal Schedule-passenger页面
        login.get_url(ini.url + "#/ApplicationView/CodeSharing")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Code Sharing Application"

        """创建"""
        login.is_click(codeshare['PratnerOperator_Select'])
        sleep(2)
        login.input_text(codeshare['PratnerOperator_Input'],codesharevalue['PratnerOperator_Select_Value'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)

        login.is_click(codeshare['Operating_Operator_select0'])
        login.input_text(codeshare['Operating_Operator_input0'], codesharevalue['OpeartingOperator0'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['CodeShareRoute_Input0'],codesharevalue['CodeShareRoute0'])
        login.input_text(codeshare['EffectiveDate0'],codesharevalue['EffectiveDate0'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['TicketSaleDate0'],codesharevalue['TicketSaleDate0'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['Remarks0'],codesharevalue['Remarks0'])

        login.is_click(codeshare['Operating_Operator_select1'])
        login.input_text(codeshare['Operating_Operator_input1'], codesharevalue['OpeartingOperator1'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['CodeShareRoute_Input1'], codesharevalue['CodeShareRoute1'])
        login.input_text(codeshare['EffectiveDate1'], codesharevalue['EffectiveDate1'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['TicketSaleDate1'], codesharevalue['TicketSaleDate1'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['Remarks1'], codesharevalue['Remarks1'])

        login.is_click(codeshare['Operating_Operator_select2'])
        login.input_text(codeshare['Operating_Operator_input2'], codesharevalue['OpeartingOperator2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['CodeShareRoute_Input2'], codesharevalue['CodeShareRoute2'])
        login.input_text(codeshare['EffectiveDate2'], codesharevalue['EffectiveDate2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['TicketSaleDate2'], codesharevalue['TicketSaleDate2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['Remarks2'], codesharevalue['Remarks2'])

        login.is_click(codeshare['Operating_Operator_select3'])
        login.input_text(codeshare['Operating_Operator_input3'], codesharevalue['OpeartingOperator3'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['CodeShareRoute_Input3'], codesharevalue['CodeShareRoute3'])
        login.input_text(codeshare['EffectiveDate3'], codesharevalue['EffectiveDate3'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['TicketSaleDate3'], codesharevalue['TicketSaleDate3'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['Remarks3'], codesharevalue['Remarks3'])

        login.is_click(codeshare['Operating_Operator_select4'])
        login.input_text(codeshare['Operating_Operator_input4'], codesharevalue['OpeartingOperator4'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[5]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['CodeShareRoute_Input4'], codesharevalue['CodeShareRoute4'])
        login.input_text(codeshare['EffectiveDate4'], codesharevalue['EffectiveDate4'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[5]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(codeshare['TicketSaleDate4'], codesharevalue['TicketSaleDate4'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[5]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(codeshare['Remarks4'], codesharevalue['Remarks4'])
        login.input_text(codeshare['Remarks'], codesharevalue['Remarks'])
        login.is_click(codeshare['UploadRelativeDocument'])
        sleep(5)
        login.is_click(codeshare['UploadDocumentType_Select'])
        login.input_text(codeshare['UploadDocumentType_Input'], codesharevalue['UploadDocumentType_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//form/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input").send_keys(Keys.ENTER)

        sleep(2)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/sample_file.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(1)


        login.is_click(codeshare['UploadButton'])
        sleep(2)
        login.is_click(codeshare['SaveAsDraft'])
        sleep(1)
        login.is_click(codeshare['SaveAsTemplate'])
        sleep(1)
        login.input_text(codeshare['TeplateName'], codesharevalue['TeplateName'])
        login.input_text(codeshare['TemplateDescrption'], codesharevalue['TemplateDescrption'])
        login.is_click(codeshare['TemplateSave'])
        sleep(1)
        print(login.element_text(codeshare['TemplateElementText']))
        # 已存在template时取消
        if login.element_text(codeshare['TemplateElementText']) == "The template name already exists":
            login.is_click(codeshare['SaveTemplateCancel'])
        sleep(2)
        login.is_click(codeshare['ConfirmButton'])
        login.is_click(codeshare['ExportButton'])
        sleep(2)
        login.is_click(codeshare['PreviewAndSubmit'])
        login.is_click(codeshare['SubmitButton'])
        login.is_click(codeshare['SubmitSuccessButton'])

        """切换到sia"""
        login.is_click(codeshare["Logout"])
        login.is_click(codeshare["Logout_Yes"])
        login.input_user_name(cad_account['SiaOfficerLoginName'])
        login.input_user_password(cad_account['SiaOfficerPassword'])
        login.click_login_button()
        sleep(20)
        # 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        #选择第一条记录
        login.is_click(codeshare["ApplicationSubject"])
        sleep(5)
        login.is_click(codeshare["ApplicationAttachment"])
        sleep(2)
        login.is_click(codeshare["ApplicationReferenceNo"])
        sleep(2)
        login.is_click(codeshare["ApplicationUploadRelate"])
        sleep(2)
        # login.is_click(codeshare["ApplicationUploadBrowse"])
        # sleep(2)

        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/sample_file.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(1)

        login.is_click(codeshare["ApplicationUploadButton"])
        sleep(3)
        login.is_click(codeshare["ApplicationUploadSuccessClose"])
        sleep(3)
        login.is_click(codeshare["ApplicationUploadClose"])
        sleep(3)
        login.is_click(codeshare["ApplicationUploadDetailClose"])
        sleep(3)

        """切换到offer"""
        login.is_click(codeshare["Logout"])
        login.is_click(codeshare["Logout_Yes"])
        login.input_user_name(cad_account['OfficerLoginName'])
        login.input_user_password(cad_account['OfficerPassword'])
        login.click_login_button()
        sleep(20)
        # 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        sleep(40)
        login.is_click(codeshare['ApproveApplicationSubject'])
        sleep(12)
        login.is_click(codeshare['ApproveApplicationReferance'])
        sleep(10)
        login.is_click(codeshare['ApproveApplication_Approve'])
        sleep(10)
        # approve_yes_elements = drivers.find_elements_by_xpath("//button[contains(span, 'Yes')]")
        # if len(approve_yes_elements) > 0:
        #     login.is_click(codeshare["Approve_Yes_Btn"])
        login.is_click(codeshare['ApproveAirlineCheckbox'])
        sleep(5)
        login.is_click(codeshare['ApproveAirlineGenerate'])
        sleep(5)
        login.is_click(codeshare['ApproveAirlinePartnerCheckbox'])
        sleep(5)
        login.is_click(codeshare['ApproveAirlinePartnerGenerate'])
        sleep(5)
        login.is_click(codeshare['ApproveAirlineGenerateAndEdit'])
        sleep(2)
        login.input_text(codeshare['ApproveAirlinePhoneNumberInput'], codesharevalue['ApproveAirlinePhoneNumberInput'])
        login.input_text(codeshare['ApproveAirlineSignedAreaInput'], codesharevalue['ApproveAirlineSignedAreaInput'])
        login.is_click(codeshare['ApproveAirlineRefreshPreview'])
        sleep(2)
        login.is_click(codeshare['ApproveAirlineDownloadAsWord'])
        sleep(2)
        login.is_click(codeshare['ApproveAirlineGeneratePdf'])
        sleep(2)
        login.is_click(codeshare['ApproveAirlinePartnerGenerateAndEdit'])
        sleep(2)
        login.input_text(codeshare['ApproveAirlinePartnerPhoneNumberInput'], codesharevalue['ApproveAirlinePhoneNumberInput'])
        login.input_text(codeshare['ApproveAirlinePartnerSignedAreaInput'], codesharevalue['ApproveAirlineSignedAreaInput'])
        login.is_click(codeshare['ApproveAirlinePartnerRefreshPreview'])
        sleep(2)
        login.is_click(codeshare['ApproveAirlinePartnerDownloadAsWord'])
        sleep(3)
        login.is_click(codeshare['ApproveAirlinePartnerGeneratePdf'])
        sleep(3)
        login.is_click(codeshare['ApproveApplicationSend'])
        drivers.implicitly_wait(30)
        login.is_click(codeshare['ApproveAPplicationSendSuccess'])

        '''切换到cpa'''
        login.is_click(codeshare["Logout"])
        login.is_click(codeshare["Logout_Yes"])
        login.input_user_name(cad_account['CpaOfficerLoginName_87'])
        login.input_user_password(cad_account['CpaOfficerPassword_87'])
        login.click_login_button()
        sleep(20)
        # 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        sleep(5)
        login.is_click(codeshare["ApproveApplicationCheckSubject"])
        sleep(2)
        login.is_click(codeshare["ApproveApplicationCheckReference"])
        sleep(10)
        login.is_click(codeshare["Logout"])
        login.is_click(codeshare["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_087/test_e2e_087.py'])