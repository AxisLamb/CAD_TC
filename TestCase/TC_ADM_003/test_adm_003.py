#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pytest
import allure
import os
import string
import random
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

flight = Element('TC(adm)_003')
flightvalue = ElementValue('TC(adm)_003value')
s = string.ascii_letters
r = random.choice(s)
#航班号用CPA+4位整数和一个随机字母
Flight_1 = "CPA"+str(randint(1000, 9999))+r
Flight_2 = "CPA"+str(randint(1000, 9999))+r

@allure.feature("TC(ADM)-003 ")
class TestMissNoSeatsError:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Miss inputting mandatory No. of Seats field")
    def test_030(self, drivers):
        # login Local Operator (CPA)
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

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        # step 01
        '''跳转到#/View/DocumentLibrary页面'''
        login.get_url(ini.url + "#/View/DocumentLibrary")
        drivers.implicitly_wait(30)
        sleep(5)

        login.is_click(flight["UploadDocumentButton"])
        sleep(1)
        login.is_click(flight["DocumentType"])
        login.input_text(flight['DocumentType'], "Aerodrome Operating Minima")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[4]/div/div[2]/div/form/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)

        login.input_text(flight['RegistrationMark'], "CPA2")
        login.is_click(flight["AircraftType(IATA)"])
        sleep(1)
        login.input_text(flight['AircraftType(IATA)'], "100")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[4]/div/div[2]/div/form/div[2]/div[2]/div/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight["AircraftType(IATA)Label"])
        login.input_text(flight['Remarks'], "UAT Testing")

        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/sample_file.pdf"
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div[2]/div/div[1]/div[1]/div/div/input").send_keys(file_path)
        sleep(1)
        login.is_click(flight["Attach"])
        sleep(3)
        login.is_click(flight["AttachOk"])
        sleep(3)

        login.is_click(flight["Update"])
        sleep(1)
        login.input_text(flight['UpdateRegistrationMark'], "CPA002")
        login.is_click(flight["UpdateAircraftType(IATA)"])
        sleep(1)
        login.input_text(flight['UpdateAircraftType(IATA)'], "141")
        sleep(1)
        drivers.find_element_by_xpath(
            "/html/body/div[4]/div/div[2]/div[1]/form/div[3]/div/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight["UpdateAircraftType(IATA)Label"])
        login.input_text(flight['UpdateRemarks'], "UAT Testing of update")
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        sleep(1)
        drivers.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[1]/div[1]/div[1]/div/div/input").send_keys(file_path)
        sleep(1)
        login.is_click(flight["UpdateButton"])
        sleep(1)
        login.is_click(flight["UpdateButtonOk"])

        sleep(1)
        login.is_click(flight["CheckBox"])
        sleep(1)
        login.is_click(flight["BatchDownload"])
        sleep(2)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        # login AS Officer
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['OfficerLoginName'])
            login.input_user_password(flightvalue['OfficerPassword'])
            login.click_login_button()

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        # step 01
        '''跳转到#/View/DocumentLibrary页面'''
        login.get_url(ini.url + "#/View/DocumentLibrary")
        drivers.implicitly_wait(30)
        sleep(5)

        login.is_click(flight["DocumentTypeSearch"])
        sleep(1)
        login.input_text(flight['DocumentTypeSearch'], "Aerodrome Operating Minima")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[1]/div[4]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight["DocumentTypeSearchLabel"])

        login.is_click(flight["Operator(ICAO)"])
        sleep(1)
        login.input_text(flight['Operator(ICAO)'], "CPA")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[1]/div[4]/form/div[1]/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight["DocumentTypeSearchLabel"])

        login.input_text(flight['RegistrationMarkSearch'], "CPA002")
        login.input_text(flight['FileName'], "other_supports.pdf")
        login.input_text(flight['RemarksSearch'], "UAT Testing of update")
        login.is_click(flight["CurrentValid"])
        login.is_click(flight["CurrentValidSelect"])
        login.is_click(flight["Status"])
        sleep(1)
        login.input_text(flight['Status'], "All")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[1]/div[4]/form/div[4]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)

        login.is_click(flight["Search"])
        sleep(2)
        login.is_click(flight["CheckBoxSearch"])
        sleep(1)
        login.is_click(flight["MarkReceive"])
        sleep(1)
        login.is_click(flight["MarkReceiveOk"])
        sleep(2)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        # login Local Operator (CPA)
        login = LoginPage(drivers)

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['CpaOfficerLoginName'])
            login.input_user_password(flightvalue['CpaOfficerPassword'])
            login.click_login_button()

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        # 跳转message页面
        login.is_click(flight['Home'])
        sleep(1)
        # login.is_click(flight['Message'])
        # sleep(1)
        # 搜索最新流程
        login.is_click(flight['AdvancedSearch'])
        sleep(1)
        login.input_text(flight['SubjectContains'], 'Supporting Document has been acknowledged.')
        login.is_click(flight['SearchButton'])
        sleep(1)
        # login.is_click(flight['OrderBy'])
        # sleep(1)
        # 选中最新流程
        login.is_click(flight['Subject'])
        sleep(1)
        # 跳转流程页面
        # login.is_click(flight['ReferenceNo'])
        sleep(5)
        login.is_click(flight['Discard'])
        sleep(1)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_ADM_003/test_adn_003.py'])
