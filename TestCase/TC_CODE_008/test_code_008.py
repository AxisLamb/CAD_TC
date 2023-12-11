import logging

import pytest
import allure

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log
flight = Element('codeflight_008')
flightvalue = ElementValue('codeflightValue_008')
@allure.feature("TC(code)-008 Maintain Aircraft information with regmark")
class TestMaintainAircraftinformationWithRegmark:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain Aircraft information with regmark")
    def test1(self, drivers):
        """登录officer用户"""
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
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        # 跳转到CodeTable->Operator->HandlingInfo页面
        login.get_url(ini.url + "?#/CodeTable/Aircraft/Regmark")
        sleep(3)
        login.input_text(flight['Search_Registration_Mark'], flightvalue['Search_Registration_Mark'])
        login.is_click(flight['Search_BTU'])
        # 判断新增数据是否和已有数据重复
        searchResult = drivers.find_elements_by_xpath("//*[@id='app']/div/div/section/div/div[2]/div[1]/div[3]/table/tbody/tr/td[1]")
        if len(searchResult) > 0:
            drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[2]/div[1]/div[3]/table/tbody/tr/td[1]").click()
            login.is_click(flight['delete_BTU'])
            sleep(1)
            login.is_click(flight['delete_BTU_Y'])
            sleep(1)
            login.is_click(flight['OK_BTU'])
        sleep(2)
        # 新增一条信息
        # step 1
        login.is_click(flight['add_BTU'])
        sleep(2)
        login.input_text(flight['Create_Registration_Mark'], flightvalue['Create_Registration_Mark'])
        login.input_text(flight['Create_Operator_ICAO'], flightvalue['Create_Operator_ICAO'])
        login.input_text(flight['Create_Aircrarft_Type_IATA'], flightvalue['Create_Aircrarft_Type_IATA'])
        sleep(1)
        login.is_click(flight['Save_BTU'])
        sleep(3)
        login.is_click(flight['OK_BTU'])
        sleep(1)
        login.input_text(flight['Search_Registration_Mark'], flightvalue['Search_Registration_Mark'])
        login.is_click(flight['Search_BTU'])
        # 判断新增数据是否和已有数据重复
        searchResult = drivers.find_elements_by_xpath("//*[@id='app']/div/div/section/div/div[2]/div[1]/div[3]/table/tbody/tr/td[1]")
        if len(searchResult) > 0:
            drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[2]/div[1]/div[3]/table/tbody/tr/td[1]").click()
            login.is_click(flight['delete_BTU'])
            sleep(1)
            login.is_click(flight['delete_BTU_Y'])
            sleep(1)
            login.is_click(flight['OK_BTU'])
        else:
            logging.info("插入失败")
        sleep(1)
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_CODE_008/test_code_008.py'])

