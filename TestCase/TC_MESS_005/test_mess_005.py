#!/usr/bin/env python3
# -*- coding:utf-8 -*-

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

flight = Element('mess_005')
flightValue = ElementValue('messValue_005')
accountValue = ElementValue('cad_account')

@allure.feature("[TC(mess)-005]Maintain Alert Out of Office/Public holiday Alert")
class TestUpdateHolidayAlert:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain Alert Out of Office/Public holiday Alert")
    def test_mess_005(self, drivers):
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

        # 跳转到List of System Parameters页面
        login.get_url(ini.url + "#/Admin/SystemParameters")
        drivers.implicitly_wait(30)
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "List of System Parameters"
        login.input_text(flight['Description'], flightValue['Description'])
        sleep(1)
        login.is_click(flight['Search'])
        sleep(2)
        # //span[text()='Message for auto alert for non-office hour']
        drivers.find_element_by_xpath("//span[text()='" + flightValue['Description'] + "']").click()
        sleep(2)
        login.input_text(flight['Value'], flightValue['Value'])
        sleep(1)
        login.is_click(flight['Save'])
        sleep(2)
        login.is_click(flight['Save_OK'])
        sleep(2)

        # 跳转到Configure for Holiday页面
        login.get_url(ini.url + "#/Misc/Holiday")
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "Configure for Holiday"
        login.is_click(flight["Add"])
        sleep(2)
        login.input_text(flight['Start_Date'], flightValue['Start_Date'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div/div[2]/form/div[1]/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['End_Date'], flightValue['End_Date'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div/div[2]/form/div[2]/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Description2'], flightValue['Description2'])
        login.input_text(flight['Alert_Message'], flightValue['Alert_Message'])
        sleep(1)
        login.is_click(flight["Create"])
        sleep(2)

        # 删除
        login.input_text(flight['Description3'], flightValue['Description2'])
        login.is_click(flight["Search2"])
        sleep(2)
        # //span[text()='The day following National Day']/../../../td[1]/div/label/span
        drivers.find_element_by_xpath("//span[text()='" + flightValue['Description2'] + "']/../../../td[1]/div/label/span").click()
        sleep(2)
        login.is_click(flight["Remove"])
        sleep(2)
        login.is_click(flight["Remove_Yes"])
        sleep(3)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/TC_MESS_005/test_mess_005.py'])
