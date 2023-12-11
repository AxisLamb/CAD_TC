#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pytest
import random
import allure
from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from utils.logger import log

flight = Element('flight')
flightvalue = ElementValue('flightvalue')
account = ElementValue('cad_account')


@allure.feature(
    "TC(E2E)-152 Local Operator Create and Officer Processing Helicopter (thru Extra Section All-Cargo) Application with new code(Approve)")
class TestCreateOfficerHelicopterProcessApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create and Officer Processing Extra Section All-Cargo Application")
    # 每次测试前需要在flightvalue.yaml文件中更新值，不然会报重复错误
    def test_001(self, drivers):
        """登录CPATEST03用户"""
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
        # 跳转到Application-Seasonal Schedule-passenger页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/ApplicationView/ExtraSection/CreateExtraSectionAllCargo")
        drivers.implicitly_wait(30)
        sleep(15)
        # 填写Extra Section All-Cargo Application表格信息
        login.is_click(flight['Helicopter_Application'])
        login.input_text(flight['FlightNo1'], "CPA" + str(random.randint(1000, 9999))+"G")
        login.input_text(flight['FlightNo2'], "CPA" + str(random.randint(1000, 9999))+"G")
        login.input_text(flight['From1'], flightvalue['From1'])
        login.is_click(flight['FlightNo1'])
        login.input_text(flight['To1'], flightvalue['To1'])
        login.is_click(flight['FlightNo1'])
        login.is_click(flight['DOP1_1'])
        login.is_click(flight['DOP1_3'])
        login.is_click(flight['DOP1_5'])
        login.is_click(flight['AircraftType_Select1_1'])
        login.input_text(flight['AircraftType_input1_1'], flightvalue['Helicopter_AircraftType1_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select1_2'])
        login.input_text(flight['AircraftType_input1_2'], flightvalue['Helicopter_AircraftType1_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity1_1'], flightvalue['CargoCapacity1_1'])
        login.input_text(flight['Route1_1'], flightvalue['Helicopter_Route1_1'])
        login.input_text(flight['CargoCapacity1_2'], flightvalue['CargoCapacity1_2'])
        login.input_text(flight['Route1_2'], flightvalue['Helicopter_Route1_2'])
        login.is_click(flight['STD1_1'])
        login.input_text(flight['STA1_1'], flightvalue['Helicopter_STA1_1'])
        login.input_text(flight['STD1_1'], flightvalue['Helicopter_STD1_1'])
        login.input_text(flight['STA1_2'], flightvalue['Helicopter_STA1_2'])
        login.input_text(flight['STD1_2'], flightvalue['Helicopter_STD1_2'])

        login.input_text(flight['FlightNo3'], "CPA" + str(random.randint(1000, 9999))+"G")
        login.input_text(flight['FlightNo4'], "CPA" + str(random.randint(1000, 9999))+"G")
        login.input_text(flight['From2'], flightvalue['From2'])
        login.is_click(flight['FlightNo3'])
        login.input_text(flight['To2'], flightvalue['To2'])
        login.is_click(flight['FlightNo3'])
        login.is_click(flight['DOP2_1'])
        login.is_click(flight['DOP2_3'])
        login.is_click(flight['DOP2_5'])
        login.is_click(flight['DOP2_7'])
        login.is_click(flight['AircraftType_Select2_1'])
        login.input_text(flight['AircraftType_input2_1'], flightvalue['Helicopter_AircraftType2_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select2_2'])
        login.input_text(flight['AircraftType_input2_2'], flightvalue['Helicopter_AircraftType2_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[4]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity2_1'], flightvalue['CargoCapacity2_1'])
        login.input_text(flight['Route2_1'], flightvalue['Helicopter_Route2_1'])
        login.input_text(flight['CargoCapacity2_2'], flightvalue['CargoCapacity2_2'])
        login.input_text(flight['Route2_2'], flightvalue['Helicopter_Route2_2'])
        login.is_click(flight['STD2_1'])
        login.input_text(flight['STA2_1'], flightvalue['Helicopter_STA2_1'])
        login.input_text(flight['STD2_1'], flightvalue['Helicopter_STD2_1'])
        login.input_text(flight['STA2_2'], flightvalue['Helicopter_STA2_2'])
        login.input_text(flight['STD2_2'], flightvalue['Helicopter_STD2_2'])
        login.is_click(flight['PCCL2-1'])
        login.is_click(flight['PCCL2-2'])

        login.input_text(flight['FlightNo5'], "CPA" + str(random.randint(1000, 9999))+"G")
        login.input_text(flight['FlightNo6'], "CPA" + str(random.randint(1000, 9999))+"G")
        login.is_click(flight['InOutFlightDiffSelect3_2'])
        login.input_text(flight['InOutFlightDiffInput3_2'], flightvalue['InOutFlightDiffInput3_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['From3'], flightvalue['From3'])
        login.is_click(flight['FlightNo5'])
        login.input_text(flight['To3'], flightvalue['To3'])
        login.is_click(flight['FlightNo5'])
        login.is_click(flight['DOP3_2'])
        login.is_click(flight['DOP3_4'])
        login.is_click(flight['DOP3_6'])
        login.is_click(flight['AircraftType_Select3_1'])
        login.input_text(flight['AircraftType_input3_1'], flightvalue['Helicopter_AircraftType3_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select3_2'])
        login.input_text(flight['AircraftType_input3_2'], flightvalue['Helicopter_AircraftType3_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity3_1'], flightvalue['CargoCapacity3_1'])
        login.input_text(flight['Route3_1'], flightvalue['Helicopter_Route3_1'])
        login.input_text(flight['CargoCapacity3_2'], flightvalue['CargoCapacity3_2'])
        login.input_text(flight['Route3_2'], flightvalue['Helicopter_Route3_2'])
        login.is_click(flight['STD3_1'])
        login.input_text(flight['STA3_1'], flightvalue['Helicopter_STA3_1'])
        login.input_text(flight['STD3_1'], flightvalue['Helicopter_STD3_1'])
        login.input_text(flight['STA3_2'], flightvalue['Helicopter_STA3_2'])
        login.input_text(flight['STD3_2'], flightvalue['Helicopter_STD3_2'])


        login.input_text(flight['FlightNo7'], "CPA" + str(random.randint(1000, 9999))+"G")
        login.input_text(flight['FlightNo8'], "CPA" + str(random.randint(1000, 9999))+"G")
        login.input_text(flight['From4'], flightvalue['From4'])
        login.is_click(flight['FlightNo7'])
        login.input_text(flight['To4'], flightvalue['To4'])
        login.is_click(flight['FlightNo7'])
        login.is_click(flight['DOP4_1'])
        login.is_click(flight['DOP4_3'])
        login.is_click(flight['DOP4_5'])
        login.is_click(flight['AircraftType_Select4_1'])
        login.input_text(flight['AircraftType_input4_1'], flightvalue['Helicopter_AircraftType4_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select4_2'])
        login.input_text(flight['AircraftType_input4_2'], flightvalue['Helicopter_AircraftType4_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[8]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity4_1'], flightvalue['CargoCapacity4_1'])
        login.input_text(flight['Route4_1'], flightvalue['Helicopter_Route4_1'])
        login.input_text(flight['CargoCapacity4_2'], flightvalue['CargoCapacity4_2'])
        login.input_text(flight['Route4_2'], flightvalue['Helicopter_Route4_2'])
        login.is_click(flight['STD4_1'])
        login.input_text(flight['STA4_1'], flightvalue['Helicopter_STA4_1'])
        login.input_text(flight['STD4_1'], flightvalue['Helicopter_STD4_1'])
        login.input_text(flight['STA4_2'], flightvalue['Helicopter_STA4_2'])
        login.input_text(flight['STD4_2'], flightvalue['Helicopter_STD4_2'])
        login.input_text(flight['Remarks'], flightvalue['Create_Remark'])
        sleep(2)
        login.is_click(flight['SaveAsDraft'])
        sleep(2)
        assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'
        login.is_click(flight['SaveAsTemplate'])
        sleep(3)
        login.input_text(flight['TemplateName'], "Temp" + str(random.uniform(1, 9999)))
        sleep(2)
        login.input_text(flight['Description'], "Description")
        sleep(3)
        login.is_click(flight['Template_Save'])
        sleep(3)
        login.is_click(flight['Confirm'])
        sleep(3)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['BackAndModify1'])
        sleep(3)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(5)
        login.is_click(flight['Submit1'])
        sleep(20)
        drivers.find_element_by_class_name("testConfirmButtonClass013").click()
        # login.is_click("xpath==//button[contains(@class, 'testConfirmButtonClass013')]")
        sleep(8)

        # 从 CPATEST03用户切换到officer1用户
        login.is_click(flight["Logout"])
        sleep(3)
        login.is_click(flight["Logout_Yes"])
        sleep(2)
        login.input_user_name(account['OfficerLoginName'])
        sleep(2)
        login.input_user_password(account['OfficerPassword'])
        sleep(2)
        login.click_login_button()

        # 跳转到View->Messages页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        login.input_text(flight['ViewMessages_Sender'], account['CpaOfficerLoginName'])
        login.is_click(flight['ApplicationType_AllCargo'])
        login.is_click(flight['ViewMessages_Search'])
        sleep(2)
        drivers.find_element_by_id("test0").click()
        sleep(3)
        drivers.find_element_by_id("testApproveExtra").click()
        sleep(2)
        drivers.find_element_by_id("testRecommendate").click()
        sleep(3)
        drivers.find_element_by_id("testConfirm").click()
        sleep(3)
        drivers.find_element_by_class_name("testConfirmButtonClass054").click()
        sleep(3)
        drivers.find_element_by_id("testGenerate01").click()
        sleep(3)
        drivers.find_element_by_id("testGenerateAndEdit01").click()
        sleep(3)
        drivers.find_element_by_id("testOfficePhoneNo").send_keys(flightvalue['AllCargo_OfficePhoneNo'])
        drivers.find_element_by_id("testOfficeFaxNo").send_keys(flightvalue['AllCargo_OfficeFaxNo'])
        drivers.find_element_by_id("testUserName").send_keys(flightvalue['AllCargo_UserName'])
        drivers.find_element_by_id("testPost").send_keys(flightvalue['AllCargo_Post'])
        drivers.find_element_by_id("testCompanyName").send_keys(flightvalue['AllCargo_CompanyName'])
        drivers.find_element_by_id("testSubjectOfficerName").send_keys(flightvalue['AllCargo_OfficerName'])
        drivers.find_element_by_id("testAddress01").send_keys(flightvalue['AllCargo_Address1'])
        drivers.find_element_by_id("testAddress02").send_keys(flightvalue['AllCargo_Address2'])
        drivers.find_element_by_id("testAddress03").send_keys(flightvalue['AllCargo_Address3'])
        drivers.find_element_by_id("testSignedArea").send_keys(flightvalue['AllCargo_SignedArea'])

        login.is_click(flight['AllCargo_RefreshPreview'])
        login.is_click(flight['AllCargo_DownloadAsWord'])
        login.is_click(flight['AllCargo_GeneratePDF'])
        sleep(10)
        login.is_click(flight['AllCargo_Send'])
        sleep(5)
        drivers.find_element_by_class_name("testConfirmButtonClass02").click()
        sleep(2)

        # 从 Officer1用户切换到CPATEST03用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(account['CpaOfficerLoginName'])
        login.input_user_password(account['CpaOfficerPassword'])
        login.click_login_button()
        # 跳转到View->Messages页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch_CAP'])
        login.input_text(flight['ViewMessages_SubjectContains_CAP'], "application Approved")
        login.input_text(flight['ViewMessages_Sender_CAP'], account['OfficerLoginName'])
        login.is_click(flight['ViewMessages_ApprovedMessage_AllCargo'])
        login.is_click(flight['ViewMessages_Search_CAP'])
        sleep(3)
        drivers.find_element_by_id("test0").click()
        sleep(5)
        # assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[1]/div/div/form/div[1]/div[2]/div/div/span").text == 'Approved'
        assert login.element_text(flight['ApprovedStatus']) == 'Approved'

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])



if __name__ == '__main__':
    pytest.main(['TestCase/test_create_officer_process_helicopter_approve.py'])
