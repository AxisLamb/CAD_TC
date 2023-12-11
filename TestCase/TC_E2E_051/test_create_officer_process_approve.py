#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import pytest
import allure
from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

flight = Element('flight')
flightvalue = ElementValue('flightvalue')
flightAccValue = ElementValue('cad_account')


@allure.feature(
    "TC(E2E)-051 Local Operator Create and Officer Processing Extra Section All-Cargo Application (Approve)")
class TestCreateOfficerProcessApprove:
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
        logout_elements = drivers.find_elements_by_xpath("//*[@id='testLogout']")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightAccValue['CpaOfficerLoginName'])
            login.input_user_password(flightAccValue['CpaOfficerPassword'])
            login.click_login_button()
        # 跳转到Application-Seasonal Schedule-passenger页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/ApplicationView/ExtraSection/CreateExtraSectionAllCargo")
        drivers.implicitly_wait(30)
        sleep(15)
        # 填写Extra Section All-Cargo Application表格信息
        login.input_text(flight['FlightNo1'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['FlightNo2'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['From1'], flightvalue['From1'])
        login.is_click(flight['FlightNo1'])
        login.input_text(flight['To1'], flightvalue['To1'])
        login.is_click(flight['FlightNo1'])
        login.is_click(flight['DOP1_1'])
        login.is_click(flight['DOP1_3'])
        login.is_click(flight['DOP1_5'])
        login.is_click(flight['AircraftType_Select1_1'])
        login.input_text(flight['AircraftType_input1_1'], flightvalue['AircraftType1_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select1_2'])
        login.input_text(flight['AircraftType_input1_2'], flightvalue['AircraftType1_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity1_1'], flightvalue['CargoCapacity1_1'])
        login.input_text(flight['Route1_1'], flightvalue['Route1_1'])
        login.input_text(flight['CargoCapacity1_2'], flightvalue['CargoCapacity1_2'])
        login.input_text(flight['Route1_2'], flightvalue['Route1_2'])
        login.is_click(flight['STD1_1'])
        login.input_text(flight['STD1_1'], flightvalue['STD1_1'])
        login.input_text(flight['STA1_2'], flightvalue['STA1_2'])
        login.input_text(flight['Remarks1_1'], flightvalue['Remarks1_1'])
        login.input_text(flight['Remarks1_2'], flightvalue['Remarks1_2'])


        login.input_text(flight['FlightNo3'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['FlightNo4'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['From2'], flightvalue['From2'])
        login.is_click(flight['FlightNo3'])
        login.input_text(flight['To2'], flightvalue['To2'])
        login.is_click(flight['FlightNo3'])
        login.is_click(flight['DOP2_1'])
        login.is_click(flight['DOP2_3'])
        login.is_click(flight['DOP2_5'])
        login.is_click(flight['DOP2_7'])
        login.is_click(flight['AircraftType_Select2_1'])
        login.input_text(flight['AircraftType_input2_1'], flightvalue['AircraftType2_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select2_2'])
        login.input_text(flight['AircraftType_input2_2'], flightvalue['AircraftType2_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[4]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity2_1'], flightvalue['CargoCapacity2_1'])
        login.input_text(flight['Route2_1'], flightvalue['Route2_1'])
        login.input_text(flight['CargoCapacity2_2'], flightvalue['CargoCapacity2_2'])
        login.input_text(flight['Route2_2'], flightvalue['Route2_2'])
        login.is_click(flight['STD2_1'])
        login.input_text(flight['STD2_1'], flightvalue['STD2_1'])
        login.input_text(flight['STA2_2'], flightvalue['STA2_2'])
        login.is_click(flight['PCCL2-1'])
        login.is_click(flight['PCCL2-2'])
        login.input_text(flight['Remarks2_1'], flightvalue['Remarks2_1'])
        login.input_text(flight['Remarks2_2'], flightvalue['Remarks2_2'])

        login.input_text(flight['FlightNo5'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['FlightNo6'], "CPA" + str(random.randint(10000, 99999)))
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
        login.input_text(flight['AircraftType_input3_1'], flightvalue['AircraftType3_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select3_2'])
        login.input_text(flight['AircraftType_input3_2'], flightvalue['AircraftType3_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity3_1'], flightvalue['CargoCapacity3_1'])
        login.input_text(flight['Route3_1'], flightvalue['Route3_1'])
        login.input_text(flight['CargoCapacity3_2'], flightvalue['CargoCapacity3_2'])
        login.input_text(flight['Route3_2'], flightvalue['Route3_2'])
        login.is_click(flight['STD3_1'])
        login.input_text(flight['STD3_1'], flightvalue['STD3_1'])
        login.input_text(flight['STA3_2'], flightvalue['STA3_2'])
        login.input_text(flight['Remarks3_1'], flightvalue['Remarks3_1'])
        login.input_text(flight['Remarks3_2'], flightvalue['Remarks3_2'])

        login.input_text(flight['FlightNo7'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['FlightNo8'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['From4'], flightvalue['From4'])
        login.is_click(flight['FlightNo7'])
        login.input_text(flight['To4'], flightvalue['To4'])
        login.is_click(flight['FlightNo7'])
        login.is_click(flight['DOP4_1'])
        login.is_click(flight['DOP4_3'])
        login.is_click(flight['DOP4_5'])
        login.is_click(flight['AircraftType_Select4_1'])
        login.input_text(flight['AircraftType_input4_1'], flightvalue['AircraftType4_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select4_2'])
        login.input_text(flight['AircraftType_input4_2'], flightvalue['AircraftType4_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[8]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity4_1'], flightvalue['CargoCapacity4_1'])
        login.input_text(flight['Route4_1'], flightvalue['Route4_1'])
        login.input_text(flight['CargoCapacity4_2'], flightvalue['CargoCapacity4_2'])
        login.input_text(flight['Route4_2'], flightvalue['Route4_2'])
        login.is_click(flight['STD4_1'])
        login.input_text(flight['STD4_1'], flightvalue['STD4_1'])
        login.input_text(flight['STA4_2'], flightvalue['STA4_2'])
        login.input_text(flight['Remarks4_1'], flightvalue['Remarks4_1'])
        login.input_text(flight['Remarks4_2'], flightvalue['Remarks4_2'])

        login.input_text(flight['FlightNo9'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['From5'], flightvalue['From5'])
        login.is_click(flight['FlightNo9'])
        login.input_text(flight['To5'], flightvalue['To5'])
        login.is_click(flight['FlightNo9'])
        login.is_click(flight['DOP5_2'])
        login.is_click(flight['DOP5_4'])
        login.is_click(flight['AircraftType_Select5_1'])
        login.input_text(flight['AircraftType_input5_1'], flightvalue['AircraftType5_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[9]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity5_1'], flightvalue['CargoCapacity5_1'])
        login.input_text(flight['Route5_1'], flightvalue['Route5_1'])
        login.is_click(flight['STA5_1'])
        login.input_text(flight['STA5_1'], flightvalue['STA5_1'])
        login.input_text(flight['STD5_1'], flightvalue['STD5_1'])
        login.is_click(flight['NextDate_Select5'])
        login.input_text(flight['NextDate_Input5'], flightvalue['NextDate_Input5'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[9]/td[18]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Remarks5_1'], flightvalue['Remarks5_1'])
        login.input_text(flight['Remarks'], flightvalue['Create_Remark'])

        sleep(2)
        login.is_click(flight['SaveAsDraft'])
        sleep(2)
        assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'

        login.is_click(flight['SaveAsTemplate'])
        login.input_text(flight['TemplateName'], "TEST" + str(random.uniform(1, 9999)))
        login.input_text(flight['Description'], "Description")
        sleep(2)
        login.is_click(flight['Template_Save'])
        login.is_click(flight['Confirm'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['BackAndModify1'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['Submit1'])
        sleep(5)
        drivers.find_element_by_class_name("testConfirmButtonClass013").click()
        sleep(2)

        # 从 CPATEST03用户切换到officer1用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightAccValue['OfficerLoginName'])
        login.input_user_password(flightAccValue['OfficerPassword'])
        login.click_login_button()

        # 跳转到View->Messages页面
        sleep(25) # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        login.input_text(flight['ViewMessages_Sender'], flightAccValue['CpaOfficerLoginName'])
        login.is_click(flight['ApplicationType_AllCargo'])
        login.is_click(flight['ViewMessages_Search'])
        sleep(7)
        drivers.find_element_by_id("test0").click()
        sleep(2)
        drivers.find_element_by_id("testApproveExtra").click()
        sleep(2)
        drivers.find_element_by_id("testRecommendate").click()
        sleep(1)
        drivers.find_element_by_id("testConfirm").click()
        sleep(3)
        drivers.find_element_by_class_name("testConfirmButtonClass054").click()
        sleep(1)
        drivers.find_element_by_id("testGenerate01").click()
        sleep(1)
        login.is_click(flight['ViewMessages_GenerateAndEdit1'])
        sleep(2)
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
        login.input_user_name(flightAccValue['CpaOfficerLoginName'])
        login.input_user_password(flightAccValue['CpaOfficerPassword'])
        login.click_login_button()
        # 跳转到View->Messages页面
        sleep(25) # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch_CAP'])
        login.input_text(flight['ViewMessages_SubjectContains_CAP'], "application Approved")
        login.input_text(flight['ViewMessages_Sender_CAP'], flightAccValue['OfficerLoginName'])
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
