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


@allure.feature(
    "TC(view)-006 Officer Search/view message and to-do-list")
class TestCreateOfficerHelicopterProcessApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Officer Search/view message and to-do-list")
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
            login.input_user_name(flightvalue['CpaOfficerLoginName'])
            login.input_user_password(flightvalue['CpaOfficerPassword'])
            login.click_login_button()
        # 跳转到Application-Seasonal Schedule-passenger页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(15)
        # 填写Extra Section All-Cargo Application表格信息
        FlightNo1 = "CPA" + str(random.randint(1000, 9999)) + "J"
        login.input_text(flight['FlightNo1'], FlightNo1)
        login.input_text(flight['FlightNo2'], "CPA" + str(random.randint(1000, 9999)) + "J")
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
        sleep(2)
        login.input_text(flight['Remarks'], flightvalue['Create_Remark'])
        login.is_click(flight['Confirm'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['Seasonal_Submit'])
        sleep(5)
        drivers.find_element_by_class_name("testCancelButtonClass016").click()
        sleep(2)
        drivers.find_element_by_class_name("testCancelButtonClass071").click()
        sleep(5)

        # 从 CPATEST03用户切换到officer1用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['OfficerLoginName'])
        login.input_user_password(flightvalue['OfficerPassword'])
        login.click_login_button()
        # 跳转到View->Messages页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        # login.input_text(flight['Subject_Contains'], "submitted")
        login.is_click(flight['ApplicationType_Passenger'])
        login.is_click(flight['ViewMessages_Search'])
        sleep(1)
        drivers.find_element_by_id("test0").click()
        sleep(2)
        login.is_click(flight['ReferenceNo_AllCargo'])
        sleep(3)
        drivers.find_element_by_id("testApproveSchedule").click()
        sleep(1)
        drivers.find_element_by_id("testRecommendate").click()
        sleep(1)
        drivers.find_element_by_id("testConfirm").click()
        sleep(3)
        drivers.find_element_by_class_name("testConfirmButtonClass054").click()
        sleep(2)
        drivers.find_element_by_id("testDiscard01").click()
        sleep(2)
        drivers.find_element_by_class_name("testConfirmButtonClass081").click()
        sleep(2)
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        login.is_click(flight['Applications_Awaiting_Processing'])
        sleep(5)
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        login.is_click(flight['Applications_Awaiting_Action'])
        sleep(5)

        # 从 Officer1用户切换到CPATEST03用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['CpaOfficerLoginName'])
        login.input_user_password(flightvalue['CpaOfficerPassword'])
        login.click_login_button()
        # 跳转到View->Messages页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/ApplicationView/ScheduleChange/FlightSchedule")
        login.input_text(flight['Search_FlightNo'], FlightNo1)
        login.is_click(flight['Search_Application_Type'])
        login.is_click(flight['DisplayBy'])
        login.input_text(flight['Effective_Period_From'], flightvalue['From1'])
        sleep(2)
        login.input_text(flight['Effective_Period_To'], flightvalue['To1'])
        sleep(2)
        login.is_click(flight['Flight_Search'])
        sleep(2)
        login.is_click(flight['ChooseCheckbox1'])
        sleep(3)
        drivers.find_element_by_id("testRevise01").click()
        sleep(3)
        login.input_text(flight['ModifySTD1'], flightvalue['ModifySTD1'])
        drivers.find_element_by_id("testChangeSave01").click()
        sleep(2)
        login.is_click(flight['SaveAsDraft1'])
        sleep(5)
        # login.is_click(flight['FlightConfirm'])
        login.is_click(flight['FlightPreviewAndSubmit'])
        sleep(2)
        drivers.find_element_by_id("testChangeSubmit01").click()
        sleep(2)
        drivers.find_element_by_class_name("testConfirmButtonClass091").click()
        sleep(2)
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)


        # 从 CPATEST03用户切换到officer1用户
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['OfficerLoginName'])
        login.input_user_password(flightvalue['OfficerPassword'])
        login.click_login_button()
        # 跳转到View->Messages页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        login.is_click(flight['Applications_Minor_Processing'])


if __name__ == '__main__':
    pytest.main(['TestCase/test_create_officer_process_helicopter_approve.py'])
