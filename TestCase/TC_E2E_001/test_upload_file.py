#!/usr/bin/env python3
import os

import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element

flight = Element('flight')


@allure.feature("TC(ECE)-001 Local Operator Create and Processing Scheduled Passenger Application with error")
class TestUploadFile:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Upload file")
    def test_001(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
          login.is_click(flight["Logout"])
          login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name("OFFICER1")
            login.input_user_password("12345678a")
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))

        '''跳转到Application-Seasonal Schedule-passenger页面'''
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")

        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"

        # Upload file
        login.is_click(flight['Upload_Related_Documents'])
        sleep(2)
        login.is_click(flight['Doc_Type_Minima_Select'])
        sleep(2)
        login.input_text(flight['Doc_Type_Minima_Input'], "Minima")
        sleep(1)
        drivers.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/sample_file.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        login.is_click(flight['UploadButton'])
        sleep(2)
        assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[2]/div").text == "sample_file.pdf"

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/test_upload_file.py'])
