
import pytest
import allure

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log
flight = Element('codeflight_007')
flightvalue = ElementValue('codeflightValue_007')
@allure.feature("TC(code)-007 Maintain Aircraft Type")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain Aircraft Type")
    def test1(self, drivers):
        # login TS Officer
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

        # 跳转到Code Table -> Aircraft->Aircraft Type页面
        login.get_url(ini.url + "#/CodeTable/Aircraft/AircraftType")
        sleep(3)
        assert drivers.find_element_by_css_selector("h2").text == "General Aircraft Information"

        # 先删除测试数据
        login.is_click(flight['AdvancedSearch'])
        sleep(1)
        login.input_text(flight["SearchAircraftDescription"], "UAT Testing Description Test 01")
        sleep(1)
        login.is_click(flight['Search'])
        sleep(1)
        menu_table = drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[3]/table")
        rows = menu_table.find_elements_by_tag_name('tr')
        before_add_numbers = len(rows)
        print("before_add_numbers: ",before_add_numbers)
        if before_add_numbers > 0:
            login.is_click(flight['0A1'])
            sleep(1)
            login.is_click(flight['Delete'])
            login.is_click(flight['DeleteYes'])
            login.is_click(flight['DeleteOk'])
            sleep(2)

        # step 1
        login.is_click(flight["Add"])
        sleep(2)

        # step 2
        login.input_text(flight["AircraftType(IATA)"], "0A1")
        login.input_text(flight["AircraftDescription"], "UAT Testing Description Test 01")
        login.input_text(flight["AircraftGroup(IATA)"], "0A1")
        login.input_text(flight["AircraftType(ICAO)"], "0A1")

        login.is_click(flight["CarriageType"])
        login.is_click(flight["CarriageTypeSelect"])
        login.is_click(flight["Category(IATA)"])
        login.is_click(flight["Category(IATA)Select"])
        login.is_click(flight["WakeTurbulence(ICAO)"])
        login.is_click(flight["WakeTurbulence(ICAO)Select"])
        login.is_click(flight["Narrow/WideBody"])
        login.is_click(flight["Narrow/WideBodySelect"])
        login.input_text(flight["AerodromeReferenceCode(ICAO)"], "C")
        login.input_text(flight["NoOfEngines"], "2")

        login.input_text(flight["SeatCapacity"], "109")
        login.input_text(flight["CargoCapacity"], "2687")
        login.input_text(flight["Weight"], "45910")
        login.input_text(flight["Remarks"], "UAT Description Test 01")

        login.is_click(flight["Save"])
        sleep(3)

        # step 3
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

        # 跳转到#/View/Application页面
        login.get_url(ini.url + "#/View/Application")
        sleep(2)
        assert drivers.find_element_by_css_selector("h2").text == "Search Application"

        login.is_click(flight["AircraftType"])
        login.input_text(flight["AircraftTypeInput"], "0A1")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[9]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # login.is_click(flight['AircraftTypeClick'])
        sleep(10)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_CODE_007/test_code_007.py'])

