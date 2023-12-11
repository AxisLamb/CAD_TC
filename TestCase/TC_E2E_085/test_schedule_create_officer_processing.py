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

flight = Element('TC(E2E)-085')
flightvalue = ElementValue('TC(E2E)-085value')


@allure.feature(
    "TC(E2E)-085 Local Operator Create and Officer Processing Schedule Change Application (Approve) for Schedule Passenger application")
class TestScheduleCreateAndOfficerProcessing:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Local Operator Create and Officer Processing Schedule Change Application (Approve) for Schedule Passenger application")
    # 每次测试前需要在flightvalue.yaml文件中更新值，不然会报重复错误
    def test_001(self, drivers):
        """登录officer1用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['CpaOfficerLoginName'])
            login.input_user_password(flightvalue['CpaOfficerPassword'])
            login.click_login_button()
        # 跳转到Code Table ->Location->Airport页面
        sleep(5)  # 页面加载速度慢，恢复后可删除
        # 创建航班号
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        Search_FlightNo1 = "CPA" + str(random.randint(10000, 99999))
        login.input_text(flight['FlightNo1'], Search_FlightNo1)
        login.input_text(flight['FlightNo2'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['From1'], flightvalue['From1'])
        login.is_click(flight['FlightNo1'])
        login.input_text(flight['To1'], flightvalue['To1'])
        login.is_click(flight['FlightNo1'])
        login.is_click(flight['DOP1_1'])
        login.is_click(flight['DOP1_2'])
        login.is_click(flight['DOP1_3'])
        login.is_click(flight['DOP1_4'])
        login.is_click(flight['DOP1_5'])
        login.is_click(flight['DOP1_6'])
        login.is_click(flight['DOP1_7'])
        login.is_click(flight['AircraftType_Select1_1'])
        login.input_text(flight['AircraftType_input1_1'], flightvalue['AircraftType1_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select1_2'])
        login.input_text(flight['AircraftType_input1_2'], flightvalue['AircraftType1_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity1_1'], flightvalue['CargoCapacity1_1'])
        login.input_text(flight['Route1_1'], flightvalue['Route1_1'])
        login.input_text(flight['CargoCapacity1_2'], flightvalue['CargoCapacity1_2'])
        login.input_text(flight['Route1_2'], flightvalue['Route1_2'])
        login.is_click(flight['STD1_2'])
        login.input_text(flight['STD1_2'], flightvalue['STD1_2'])
        login.input_text(flight['STA1_1'], flightvalue['STA1_1'])

        Search_FlightNo2 = "CPA" + str(random.randint(10000, 99999))
        login.input_text(flight['FlightNo3'], Search_FlightNo2)
        login.input_text(flight['FlightNo4'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['From2'], flightvalue['From2'])
        login.is_click(flight['FlightNo3'])
        login.input_text(flight['To2'], flightvalue['To2'])
        login.is_click(flight['FlightNo3'])
        login.is_click(flight['DOP2_1'])
        login.is_click(flight['DOP2_2'])
        login.is_click(flight['DOP2_3'])
        login.is_click(flight['DOP2_4'])
        login.is_click(flight['DOP2_5'])
        login.is_click(flight['DOP2_6'])
        login.is_click(flight['DOP2_7'])
        login.is_click(flight['AircraftType_Select2_1'])
        login.input_text(flight['AircraftType_input2_1'], flightvalue['AircraftType2_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select2_2'])
        login.input_text(flight['AircraftType_input2_2'], flightvalue['AircraftType2_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity2_1'], flightvalue['CargoCapacity2_1'])
        login.input_text(flight['Route2_1'], flightvalue['Route2_1'])
        login.input_text(flight['CargoCapacity2_2'], flightvalue['CargoCapacity2_2'])
        login.input_text(flight['Route2_2'], flightvalue['Route2_2'])
        login.is_click(flight['STD2_2'])
        login.input_text(flight['STD2_2'], flightvalue['STD2_2'])
        login.input_text(flight['STA2_1'], flightvalue['STA2_1'])

        Search_FlightNo3 = "CPA" + str(random.randint(10000, 99999))
        login.input_text(flight['FlightNo5'], Search_FlightNo3)
        login.input_text(flight['FlightNo6'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['From3'], flightvalue['From3'])
        login.is_click(flight['FlightNo5'])
        login.input_text(flight['To3'], flightvalue['To3'])
        login.is_click(flight['FlightNo5'])
        login.is_click(flight['DOP3_1'])
        login.is_click(flight['DOP3_2'])
        login.is_click(flight['DOP3_3'])
        login.is_click(flight['DOP3_4'])
        login.is_click(flight['DOP3_5'])
        login.is_click(flight['DOP3_6'])
        login.is_click(flight['DOP3_7'])
        login.is_click(flight['AircraftType_Select3_1'])
        login.input_text(flight['AircraftType_input3_1'], flightvalue['AircraftType3_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[5]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select3_2'])
        login.input_text(flight['AircraftType_input3_2'], flightvalue['AircraftType3_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[6]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity3_1'], flightvalue['CargoCapacity3_1'])
        login.input_text(flight['Route3_1'], flightvalue['Route3_1'])
        login.input_text(flight['CargoCapacity3_2'], flightvalue['CargoCapacity3_2'])
        login.input_text(flight['Route3_2'], flightvalue['Route3_2'])
        login.is_click(flight['STD3_2'])
        login.input_text(flight['STD3_2'], flightvalue['STD3_2'])
        login.input_text(flight['STA3_1'], flightvalue['STA3_1'])

        Search_FlightNo4 = "CPA" + str(random.randint(10000, 99999))
        login.input_text(flight['FlightNo7'], Search_FlightNo4)
        login.input_text(flight['FlightNo8'], "CPA" + str(random.randint(10000, 99999)))
        login.input_text(flight['From4'], flightvalue['From4'])
        login.is_click(flight['FlightNo7'])
        login.input_text(flight['To4'], flightvalue['To4'])
        login.is_click(flight['FlightNo7'])
        login.is_click(flight['DOP4_1'])
        login.is_click(flight['DOP4_2'])
        login.is_click(flight['DOP4_3'])
        login.is_click(flight['DOP4_4'])
        login.is_click(flight['DOP4_5'])
        login.is_click(flight['DOP4_6'])
        login.is_click(flight['DOP4_7'])
        login.is_click(flight['AircraftType_Select4_1'])
        login.input_text(flight['AircraftType_input4_1'], flightvalue['AircraftType4_1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[7]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select4_2'])
        login.input_text(flight['AircraftType_input4_2'], flightvalue['AircraftType4_2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[8]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['CargoCapacity4_1'], flightvalue['CargoCapacity4_1'])
        login.input_text(flight['Route4_1'], flightvalue['Route4_1'])
        login.input_text(flight['CargoCapacity4_2'], flightvalue['CargoCapacity4_2'])
        login.input_text(flight['Route4_2'], flightvalue['Route4_2'])
        login.is_click(flight['STD4_2'])
        login.input_text(flight['STD4_2'], flightvalue['STD4_2'])
        login.input_text(flight['STA4_1'], flightvalue['STA4_1'])
        login.input_text(flight['Remarks'], "UAT End2End Testing")
        sleep(1)
        login.is_click(flight['SaveAsDraft1'])
        sleep(1)
        assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'
        login.is_click(flight['SaveAsTemplate'])
        login.input_text(flight['TemplateName'], "TEST" + str(random.uniform(1, 9999)))
        login.input_text(flight['Description'], "Description")
        sleep(1)
        login.is_click(flight['Template_Save'])
        sleep(1)
        login.is_click(flight['Confirm'])
        sleep(1)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(1)
        login.is_click(flight['Submit1'])
        sleep(5)
        drivers.find_element_by_class_name("testConfirmButtonClass016").click()
        sleep(1)
        login.get_url(ini.url + "#/View/Messages")
        sleep(1)

        # 从 CPATEST03用户切换到officer1用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['OfficerLoginName'])
        login.input_user_password(flightvalue['OfficerPassword'])
        login.click_login_button()

        # 跳转到View->Messages页面
        sleep(5)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        sleep(1)
        login.input_text(flight['ViewMessages_Sender'], "CPATEST03")
        sleep(1)
        login.is_click(flight['ApplicationType_AllCargo'])
        sleep(1)
        login.is_click(flight['ViewMessages_Search'])
        sleep(5)
        drivers.find_element_by_id("test0").click()
        sleep(8)
        drivers.find_element_by_id("testApproveSchedule").click()
        sleep(1)
        drivers.find_element_by_id("testRecommendate").click()
        sleep(5)
        drivers.find_element_by_id("testConfirm").click()
        sleep(15)
        drivers.find_element_by_class_name("testConfirmButtonClass054").click()
        sleep(5)
        drivers.find_element_by_id("testDiscard01").click()
        sleep(1)
        drivers.find_element_by_class_name("testConfirmButtonClass081").click()
        sleep(5)

        # 从 Officer1用户切换到CPATEST03用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['CpaOfficerLoginName'])
        login.input_user_password(flightvalue['CpaOfficerPassword'])
        login.click_login_button()
        # 跳转到/ApplicationView/ScheduleChange/FlightSchedule页面

        login.get_url(ini.url + "#/ApplicationView/ScheduleChange/FlightSchedule")
        login.input_text(flight['Search_FlightNo'], Search_FlightNo1)
        login.is_click(flight['Search_Application_Type'])
        login.is_click(flight['DisplayBy'])
        login.input_text(flight['Effective_Period_From'], flightvalue['From1'])
        sleep(1)
        login.input_text(flight['Effective_Period_To'], flightvalue['To1'])
        sleep(1)
        login.is_click(flight['Flight_Search'])
        sleep(1)
        login.is_click(flight['ChooseCheckbox1'])
        sleep(1)
        drivers.find_element_by_id("testRevise01").click()
        sleep(1)
        #点击1234567
        login.is_click(flight['DOP1'])
        # login.is_click(flight['DOP2'])
        login.is_click(flight['DOP3'])
        # login.is_click(flight['DOP4'])
        login.is_click(flight['DOP5'])
        # login.is_click(flight['DOP6'])
        login.is_click(flight['DOP7'])
        drivers.find_element_by_id("testChangeSave01").click()
        sleep(5)
        login.input_text(flight['Search_FlightNo'], Search_FlightNo2)
        sleep(1)
        login.is_click(flight['Flight_Search'])
        sleep(1)
        login.is_click(flight['ChooseCheckbox1'])
        sleep(1)
        drivers.find_element_by_id("testRevise01").click()
        sleep(1)
        # 改日期
        login.is_click(flight['DOP1'])
        login.is_click(flight['DOP2'])
        login.is_click(flight['DOP3'])
        login.is_click(flight['DOP4'])
        login.is_click(flight['DOP5'])
        # login.is_click(flight['DOP6'])
        login.is_click(flight['DOP7'])
        login.input_text(flight['Cargo_1'], '5000')
        login.input_text(flight['Cargo_2'], '5000')
        login.input_text(flight['Std_Time'], '1130')
        login.input_text(flight['Sta_Time'], '1930')
        login.is_click(flight['Date_From_1'])
        login.input_text(flight['Date_From_1'], '08/11/2023')
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Date_To_1'])
        login.input_text(flight['Date_To_1'],'15/11/2023')
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/span/div/input").send_keys(Keys.ENTER)

        drivers.find_element_by_id("testChangeSave01").click()
        sleep(5)
        login.input_text(flight['Search_FlightNo'], Search_FlightNo3)
        sleep(1)
        login.is_click(flight['Flight_Search'])
        sleep(1)
        login.is_click(flight['ChooseCheckbox1'])
        sleep(1)
        drivers.find_element_by_id("testRevise01").click()
        sleep(1)
        login.input_text(flight['ModifySTA1'], flightvalue['ModifySTA1'])
        login.is_click(flight['Date_To_1'])
        login.input_text(flight['Date_To_1'], '15/11/2023')
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Std_Time'], '1130')
        login.input_text(flight['Sta_Time'], '1630')
        login.input_text(flight['Cargo_1'], '6000')
        login.input_text(flight['Cargo_2'], '6000')
        # copy
        login.is_click(flight['List_1'])
        login.is_click(flight['Copy'])
        login.input_text(flight['ModifySTA1'], flightvalue['ModifySTA1'])
        login.is_click(flight['Date_From_2'])
        login.input_text(flight['Date_From_2'], '22/11/2023')
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[6]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Date_To_2'])
        login.input_text(flight['Date_To_2'], '30/11/2023')
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[7]/div/span/div/input").send_keys(
            Keys.ENTER)

        drivers.find_element_by_id("testChangeSave01").click()
        sleep(5)
        login.input_text(flight['Search_FlightNo'], Search_FlightNo4)
        sleep(1)
        login.is_click(flight['Flight_Search'])
        sleep(1)
        login.is_click(flight['ChooseCheckbox1'])
        sleep(1)
        drivers.find_element_by_id("testRevise01").click()
        sleep(1)
        login.input_text(flight['Cargo_1'], '7000')
        login.input_text(flight['Cargo_2'], '7000')
        login.input_text(flight['Std_Time'], '1130')
        login.input_text(flight['Sta_Time'], '1630')
        drivers.find_element_by_id("testChangeSave01").click()
        sleep(1)
        login.is_click(flight['SaveAsDraft1'])
        sleep(5)
        # login.is_click(flight['FlightConfirm'])
        login.is_click(flight['FlightPreviewAndSubmit'])
        sleep(1)
        drivers.find_element_by_id("testChangeSubmit01").click()
        sleep(1)
        drivers.find_element_by_class_name("testConfirmButtonClass091").click()
        sleep(5)

        # 从 CPATEST03用户切换到officer1用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        sleep(5)
        login.input_user_name(flightvalue['OfficerLoginName'])
        login.input_user_password(flightvalue['OfficerPassword'])
        login.click_login_button()
        # 跳转到View->Messages页面
        # sleep(15) # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        sleep(5)
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        sleep(5)
        login.input_text(flight['ViewMessages_Sender'], flightvalue['CpaOfficerLoginName'])
        sleep(5)
        login.is_click(flight['ViewMessages_ApplicationType'])
        sleep(5)
        login.is_click(flight['ViewMessages_Search'])
        drivers.find_element_by_id("test0").click()
        sleep(8)
        drivers.find_element_by_id("testApproveChange").click()
        sleep(10)
        drivers.find_element_by_id("testRecommendate").click()
        sleep(10)
        drivers.find_element_by_id("testConfirm").click()
        sleep(25)
        drivers.find_element_by_class_name("testConfirmButtonClass054").click()
        sleep(10)
        drivers.find_element_by_id("testGenerate01").click()
        sleep(15)
        drivers.find_element_by_id("testGenerateAndEdit01").click()
        sleep(5)
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
        sleep(15)
        login.is_click(flight['AllCargo_Send'])
        sleep(30)
        drivers.find_element_by_class_name("testConfirmButtonClass02").click()
        sleep(5)



        # 从 Officer1用户切换到CPATEST03用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['CpaOfficerLoginName'])
        login.input_user_password(flightvalue['CpaOfficerPassword'])
        login.click_login_button()
        # 跳转到View->Messages页面
        sleep(5) # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        sleep(10)
        drivers.find_element_by_id("test0").click()
        sleep(8)
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/test_schedule_create_officer_processing.py'])