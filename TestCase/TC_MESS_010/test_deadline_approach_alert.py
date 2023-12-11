#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pytest
import random
import allure
import datetime
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
    "TC(mess)-010 Deadline approach alert")
class TestDeadlineApproachAlert:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)
    @allure.story("Deadline approach alert")
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
            login.input_user_name(flightvalue['OfficerLoginName'])
            login.input_user_password(flightvalue['OfficerPassword'])
            login.click_login_button()
        # 跳转到Application->Seasonal Application->Passenger页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(15)
        # 填写Create Seasonal Schedule Passenger Application表格信息
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[2]/div[1]/div/div/div/div/input").send_keys("CPA")
        login.input_text(flight['FlightNo1'], "CPA" + str(random.randint(1000, 9999))+"I")
        login.input_text(flight['FlightNo2'], "CPA" + str(random.randint(1000, 9999))+"I")
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
        login.input_text(flight['Remarks1_1'], flightvalue['Remarks1_1'])
        login.input_text(flight['Remarks1_2'], flightvalue['Remarks1_2'])
        sleep(2)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['Submit1'])
        sleep(5)
        drivers.find_element_by_class_name("testCancelButtonClass016").click()
        sleep(2)

        # 跳转到View->Application页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Application")
        login.is_click(flight['RequestFollowUp'])
        sleep(1)
        current_date = datetime.date.today()
        next_date = current_date + datetime.timedelta(days=1)
        login.input_text(flight['CADUser'], flightvalue['CADUser'])
        login.input_text(flight['Deadline'], flightvalue[next_date])
        login.input_text(flight['Message'], flightvalue['Message'])

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
        login.input_user_name(flightvalue['CpaOfficerLoginName'])
        login.input_user_password(flightvalue['CpaOfficerPassword'])
        login.click_login_button()
        # 跳转到View->Messages页面
        sleep(25)  # 页面加载速度慢，恢复后可删除
        login.get_url(ini.url + "#/View/Messages")
        login.is_click(flight['ViewMessages_AdvancedSearch_CAP'])
        login.input_text(flight['ViewMessages_SubjectContains_CAP'], "application Approved")
        login.input_text(flight['ViewMessages_Sender_CAP'], "Officer1")
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
    pytest.main(['TestCase/test_deadline_approach_alert.py'])
