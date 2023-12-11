#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import random
import string

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('view_004')
flightValue = ElementValue('viewValue_004')
accountValue = ElementValue('cad_account')

@allure.feature("[TC(view)-004]Officer Search the flights from master schedule database and seasonal schedule database")
class TestFlightsByOfficer:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create and upload application by Officer")
    def test_view_004(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(accountValue['OfficerLoginName'])
            login.input_user_password(accountValue['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到Create Seasonal Schedule Passenger Application页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"
        login.is_click(flight['Season'])
        login.input_text(flight['Season'], flightValue['Season'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[1]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['Operator_ICAO'])
        login.input_text(flight['Operator_ICAO'], flightValue['Operator_ICAO'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)

        # 填写Flight Schedules表格信息
        rl = random.choice(string.ascii_letters)
        # line 1 and line2
        login.input_text(flight['Flight_No'], "CPA" + str(random.randint(1000, 9999)) + rl)
        login.input_text(flight['From'], flightValue['Operation_Period_From'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To'], flightValue['Operation_Period_To'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1'])
        login.is_click(flight['DOP_3'])
        login.is_click(flight['DOP_5'])
        login.is_click(flight['Aircraft_Type'])
        login.input_text(flight['Aircraft_Type'], flightValue['Aircraft_Type'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_of_Seats'], flightValue['No_of_Seats'])
        login.input_text(flight['Route'], flightValue['Route'])
        login.is_click(flight['STD'])
        login.input_text(flight['STD'], flightValue['STD'])
        login.input_text(flight['Remarks'], flightValue['Remarks'] + "1")
        sleep(2)
        login.input_text(flight['Flight_No2'], "CPA" + str(random.randint(1000, 9999)) + rl)
        login.is_click(flight['Aircraft_Type2'])
        login.input_text(flight['Aircraft_Type2'], flightValue['Aircraft_Type'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_of_Seats2'], flightValue['No_of_Seats'])
        login.input_text(flight['Route2'], flightValue['Route2'])
        login.is_click(flight['STA'])
        login.input_text(flight['STA'], flightValue['STA'])
        login.input_text(flight['Remarks'], flightValue['Remarks'] + "2")
        login.input_text(flight['Remarks2'], flightValue['Remarks'])
        sleep(2)

        # Upload file
        login.is_click(flight['Upload_application_related_document'])
        sleep(2)
        login.is_click(flight['Document_Type'])
        login.input_text(flight['Document_Type'], flightValue['Document_Type_Others'])
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.is_click(flight['Indefinite'])
        sleep(2)
        login.is_click(flight['Upload'])
        sleep(2)
        login.is_click(flight['Click_Condition'])
        sleep(2)
        login.is_click(flight['Preview_and_Submit'])
        sleep(2)
        login.is_click(flight['Upload_and_Approve'])
        sleep(2)
        login.is_click(flight['Recommendation'])
        sleep(2)
        login.is_click(flight['Confirm'])
        sleep(2)
        login.is_click(flight['Confirm_OK'])
        sleep(3)
        login.is_click(flight['Application_Type'])
        sleep(2)
        login.is_click(flight['Search'])
        sleep(2)
        login.is_click(flight['Reference_No'])
        sleep(6)

        # 跳转到Enquire Flight Information页面
        login.get_url(ini.url + "#/View/Flightinformation")
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Enquire Flight Information"
        login.input_text(flight['Period_From'], flightValue['Operation_Period_From'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['Period_To'], flightValue['Operation_Period_To'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[2]/div/div/div/div[2]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['Operator_ICAO2'])
        login.input_text(flight['Operator_ICAO2'], flightValue['Operator_ICAO'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['Service_Type'])
        sleep(2)
        login.is_click(flight['Display_By'])
        sleep(2)
        login.is_click(flight['Search2'])
        sleep(6)
        # login.is_click(flight['Total_Pages'])
        # sleep(2)
        login.is_click(flight['Source_of_Data_Seasonal'])
        sleep(2)
        login.is_click(flight['Search2'])
        sleep(6)
        # login.is_click(flight['Total_Pages'])
        # sleep(2)


        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_VIEW_004/test_view_004.py'])
