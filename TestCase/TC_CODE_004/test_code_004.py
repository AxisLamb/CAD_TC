
import pytest
import allure

from selenium.webdriver.common.keys import Keys

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
flight = Element('codeflight_004')
account = ElementValue('cad_account')
@allure.feature("TC(code)-004 Maintain Service Type Code")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain Service Type Code")
    def test_144(self, drivers):
        """登录officer用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(account['OfficerLoginName'])
            login.input_user_password(account['OfficerPassword'])
            login.click_login_button()
        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到Business页面'''
        login.get_url(ini.url + "#/CodeTable/ServiceType")

        drivers.implicitly_wait(30)
        sleep(5)

        login.is_click(flight["Add"])
        login.input_text(flight["Service_Type"], "Z")
        login.input_text(flight["English_Description"], "UAT Service Type Test 01")
        login.input_text(flight["Custom_Description"], "Test 01")
        login.input_text(flight["Remarks"], "UAT Remarks Test 01")
        sleep(2)
        login.is_click(flight["Save"])
        sleep(2)
        login.is_click(flight["SaveOk"])
        sleep(2)

        login.is_click(flight["Sort"])
        login.is_click(flight["Select_Record"])
        login.is_click(flight["Delete"])
        sleep(2)
        login.is_click(flight["Click_Yes"])
        sleep(2)


        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        sleep(2)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_CODE_004/test_code_004.py'])

