#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
import os
import string
import random
from datetime import datetime, timedelta
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('TC(VIEW)-003')
flightvalue = ElementValue('TC(VIEW)-003value')
s = string.ascii_letters
r = random.choice(s)
#航班号用CPA+4位整数和一个随机字母
Flight_1 = "CPA"+str(randint(1000, 9999))+r
Flight_2 = "CPA"+str(randint(1000, 9999))+r

@allure.feature("TC(view)-003")
class TestMissNoSeatsError:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Miss inputting mandatory No. of Seats field")
    def test_030(self, drivers):
        # login AS Officer
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

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        # step 01
        '''跳转到#/ApplicationView/SeasonalSchedule/AddPassengerInfo页面'''
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(5)

        login.is_click(flight['Operator(ICAO)'])
        login.input_text(flight['Operator(ICAO)'], "CPA")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)

        login.input_text(flight['FlightNo'], Flight_1)
        login.input_text(flight['FlightNo_2'], Flight_2)

        login.is_click(flight['Aircraft_Type'])
        login.input_text(flight['Aircraft_Type'], "100")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['No_of_Pax'], "100")
        login.input_text(flight['Route'], "HKG-LAX")
        login.is_click(flight['Service_Type'])
        login.input_text(flight['STD'], "1030")
        # line2
        # login.input_text(flight['In-out_Flight_Diff'], "0")
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/input").send_keys(
        #     Keys.ENTER)
        login.is_click(flight['Aircraft_Type_2'])
        login.input_text(flight['Aircraft_Type_2'], "100")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['No_of_Pax_2'], "100")
        login.input_text(flight['Route_2'], "LAX-HKG")
        login.is_click(flight['Service_Type'])
        login.input_text(flight['STA_2'], "1930")

        login.input_text(flight['From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['DOP_1'])
        login.is_click(flight['DOP_3'])
        login.is_click(flight['DOP_5'])
        login.input_text(flight['Remarks_1'], "UAT End2End Testing 1")
        login.input_text(flight['Remarks_2'], "UAT End2End Testing 2")

        login.input_text(flight['Remarks'], "UAT End2End Testing")
        # Upload file
        login.is_click(flight['Upload_Related_Documents'])
        sleep(2)
        login.is_click(flight['Doc_Type_Select'])
        sleep(1)
        login.input_text(flight['Doc_Type_Select'], "Others")
        sleep(1)
        drivers.find_element_by_xpath(
            "/html/body/div[7]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        # login.is_click(flight['BrowseButton'])
        # sleep(2)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(1)
        login.is_click(flight['New_Indefinite'])
        sleep(2)
        login.is_click(flight['UploadButton'])
        sleep(2)

        # step 02
        login.is_click(flight['Step09_Click_Condition'])
        sleep(2)
        login.is_click(flight['Step09_Preview_And_Submit'])
        sleep(2)

        # step 03
        login.is_click(flight['Step10_Upload_and_Approve'])
        sleep(5)

        # step 04
        login.is_click(flight['Recommendation'])
        sleep(1)
        login.is_click(flight['Confirm'])
        sleep(2)

        # step 05
        login.is_click(flight['Click_Ok'])
        sleep(3)

        # # step 06
        # '''跳转到#/View/Application页面'''
        # login.get_url(ini.url + "#/View/Application")
        # drivers.implicitly_wait(30)
        # sleep(5)
        #
        # login.is_click(flight['Operator(ICAO)_06'])
        # login.input_text(flight['Operator(ICAO)_06'], "CPA")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # login.is_click(flight['Click_06'])
        #
        # login.is_click(flight['ApplicationType_06'])
        # login.is_click(flight['Search_06'])
        # sleep(1)
        #
        # login.is_click(flight['CheckBox_06'])
        # login.is_click(flight['RequestFollowUp_06'])
        # sleep(1)
        #
        # login.is_click(flight['CADUser_07'])
        # login.input_text(flight['CADUser_07'], "Officer1")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[14]/div/div[2]/form/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        #
        # current_date = datetime.now()
        # next_1_date = current_date + timedelta(days=1)
        # next_5_date = current_date + timedelta(days=5)
        # formatted_1_date = next_1_date.strftime('%d/%m/%Y')
        # formatted_5_date = next_5_date.strftime('%d/%m/%Y')
        # # print("Formatted date:", formatted_1_date)
        #
        # login.input_text(flight['Deadline_07'], formatted_1_date)
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[14]/div/div[2]/form/div[3]/div/div/div/input").send_keys(Keys.ENTER)
        #
        # login.input_text(flight['Message_07'], "UAT testing deadline alert")
        #
        # sleep(1)
        # login.is_click(flight['Save'])
        # sleep(1)

        # step 08
        login.is_click(flight['Home'])
        sleep(1)
        login.get_url(ini.url + "#/View/FlightSchedule")
        drivers.implicitly_wait(30)
        sleep(5)

        login.is_click(flight['Operator(ICAO)_06'])
        login.input_text(flight['Operator(ICAO)_06'], "CPA")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['Click_06'])

        login.input_text(flight['FilghtNo'], Flight_1)

        login.input_text(flight['SearchFrom'], '01/11/2023')
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[5]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['SearchTo'], '30/11/2023')
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[5]/div/div/div/div[2]/input").send_keys(Keys.ENTER)
        # login.is_click(flight['Click_06'])

        login.is_click(flight['ServiceType'])

        login.is_click(flight['Search_06'])
        sleep(10)
        # login.is_click(flight['Click_07'])
        # sleep(2)

        login.is_click(flight['FlightByPeriod'])

        login.is_click(flight['Search_06'])
        sleep(10)
        # login.is_click(flight['Click_07'])
        # sleep(2)

        # login.is_click(flight['CheckBox_06'])
        # login.is_click(flight['RequestFollowUp_06'])
        # sleep(1)
        #
        # login.is_click(flight['CADUser_07'])
        # login.input_text(flight['CADUser_07'], "Officer1")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[14]/div/div[2]/form/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        #
        # login.input_text(flight['Deadline_07'], formatted_5_date)
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[14]/div/div[2]/form/div[3]/div/div/div/input").send_keys(Keys.ENTER)
        #
        # login.input_text(flight['Message_07'], "UAT testing deadline alert update")
        #
        # sleep(1)
        # login.is_click(flight['Save'])
        # sleep(10)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        #
        # # missing to input seat no.
        # sleep(999)
        # drivers.implicitly_wait(30)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_VIEW_003/test_view_003.py'])
