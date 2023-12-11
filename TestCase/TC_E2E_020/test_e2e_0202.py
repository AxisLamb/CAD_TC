#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import os
import string
import pytest
import allure
import logging

from random import randint
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('flight_020')
flightvalue = ElementValue('flightvalue_020')


@allure.feature("TC(ECE)-020 02Create_application_by_Local_Operator")
class TestCreateApplicationByLocalOperator:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Miss inputting mandatory No. of Seats field")
    def test_030(self, drivers):
        """test1: Miss inputting mandatory No. of Seats field"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['OperatorcpaLoginName'])
            login.input_user_password(flightvalue['OperatorcpaPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        # 跳转到Application-Seasonal Schedule-passenger页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule All-Cargo Application"
        now = datetime.now()
        # 获取夏令时开始时间（三月最后一个星期日）
        dst_start = datetime(now.year, 3, 31) - timedelta(days=(datetime(now.year, 3, 31).weekday() + 1) % 7)
        # 获取夏令时结束时间（十月最后一个星期六）
        dst_end = datetime(now.year, 10, 31) - timedelta(days=(datetime(now.year, 10, 31).weekday() + 1) % 7)
        logging.info(dst_start)
        logging.info(dst_end)
        # 夏令时之间
        if (now >= dst_start) and (now < dst_end):
            # 三到十月之间直接1-28号
            if ((now.month > 3) and (now.month < 10)):
                dateFrom = (now + relativedelta(day=1)).strftime("%d/%m/%Y")
                dateTo = (now + relativedelta(day=28)).strftime("%d/%m/%Y")
            # 三月夏令时 （今天--今天加27天）
            elif now.month == 3:
                dateFrom = now.strftime("%d/%m/%Y")
                dateTo = (now + relativedelta(days=27)).strftime("%d/%m/%Y")
            # 十月从1号到夏令时结束(今天-28天  --  今天)
            elif now.month == 10:
                dateFrom = (now - relativedelta(days=27)).strftime("%d/%m/%Y")
                dateTo = now.strftime("%d/%m/%Y")
        else:
            # 冬令时 3或10俩边
            if (now.month < 3) or (now.month > 10):
                dateFrom = (now + relativedelta(day=1)).strftime("%d/%m/%Y")
                dateTo = (now + relativedelta(day=28)).strftime("%d/%m/%Y")
            # 3月冬令时(减27天，今天)
            if now.month == 3:
                dateFrom = (now - relativedelta(days=27)).strftime("%d/%m/%Y")
                dateTo = now.strftime("%d/%m/%Y")
            # 10月冬令时（今天到今天加27天）
            elif now.month == 10:
                dateFrom = now.strftime("%d/%m/%Y")
                dateTo = (now + relativedelta(days=27)).strftime("%d/%m/%Y")
        print(dateFrom, dateTo)
        s = string.ascii_letters
        r = random.choice(s)
        # 航班号用CPA+4位整数和一个随机字母
        Flight_1 = "CPA" + str(randint(1000, 9999)) + r
        Flight_2 = "CPA" + str(randint(1000, 9999)) + r
        print(Flight_1, Flight_2)
        # 填写Flight Schedules表格信息 Start
        # A1行
        login.input_text(flight['FlightNoA1'], Flight_1)
        login.input_text(flight['From_A1'], dateFrom)
        login.input_text(flight['To_A1'], dateTo)
        login.is_click(flight['DOP_1_A1'])
        login.is_click(flight['DOP_3_A1'])
        login.is_click(flight['DOP_5_A1'])
        login.is_click(flight['AircraftType_Select_A1'])
        sleep(1)
        login.input_text(flight['AircraftType_input_A1'], flightvalue['AircraftType_input_A1'])
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_A1'])
        login.input_text(flight['CargoCapacityKg_input_A1'], flightvalue['CargoCapacityKg_input_A1'])
        login.input_text(flight['Route_A1'], flightvalue['Route_A1'])
        login.is_click(flight['LocalTime_STD_A1'])
        login.input_text(flight['LocalTime_STD_A1'], flightvalue['LocalTime_STD_A1'])

        # A2行
        login.input_text(flight['FlightNoA2'], Flight_2)
        login.is_click(flight['AircraftType_Select_A2'])
        sleep(1)
        login.input_text(flight['AircraftType_input_A2'], flightvalue['AircraftType_input_A2'])
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['CargoCapacityKg_input_A2'])
        login.input_text(flight['CargoCapacityKg_input_A2'], flightvalue['CargoCapacityKg_input_A2'])
        login.input_text(flight['Route_A2'], flightvalue['Route_A2'])
        login.is_click(flight['LocalTime_STA_A2'])
        login.input_text(flight['LocalTime_STA_A2'], flightvalue['LocalTime_STA_A2'])
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        # Upload file
        login.is_click(flight['Upload_Related_Documents'])
        sleep(2)
        login.is_click(flight['Doc_Type_Select'])
        sleep(2)
        login.input_text(flight['Doc_Type_Input'], flightvalue['Doc_Type_Input'])
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(1)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestData/In/other_support.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        expiryDate = (datetime.now() + relativedelta(day=datetime.now().day + 1)).strftime("%d/%m/%Y")
        sleep(2)
        login.input_text(flight['ExpiryDate'], expiryDate)
        sleep(2)
        drivers.find_element_by_xpath("/html/body/div[6]/div/div[2]/form/div[5]/div/div/div/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['UploadButton'])
        sleep(2)
        # step 09
        login.is_click(flight['Step09_Click_Condition'])
        sleep(2)
        login.is_click(flight['Step09_Preview_And_Submit'])
        sleep(2)

        # step 10
        login.is_click(flight['Step10_Click_Submit'])
        sleep(5)
        login.is_click(flight['Step10_Click_Lease_No'])
        sleep(2)
        login.is_click(flight['Step10_Click_Lease_No'])
        # step 11
        # login.is_click(flight['Step11_Click_No'])
        sleep(10)
        refNoValue = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[5]/div/div[3]/table/tbody/tr[1]/td[4]/div/a/span/span")
        filename = os.path.dirname(current_path) + '/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        with open(filename, 'w') as f:
            f.write(refNoValue.text)
        # step 12
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/test_e2e_0202.py'])
