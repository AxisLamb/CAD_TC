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
flight = Element('codeflight_009')
flightvalue = ElementValue('codeflightValue_009')
flightAccValue = ElementValue('cad_account')

@allure.feature("TC(code)-009 Maintain Airline Operator")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Operator")
    def test_code_009(self, drivers):
        """登录officer用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightAccValue['OfficerLoginName'])
            login.input_user_password(flightAccValue['OfficerPassword'])
            login.click_login_button()

        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到Business页面'''
        login.get_url(ini.url + "#/CodeTable/Operator/Operator")

        drivers.implicitly_wait(30)
        sleep(5)

        assert drivers.find_element_by_css_selector("h2").text == "Operator"

        # 新增一条business party信息
        login.is_click(flight['AddButton'])
        sleep(1)
        login.input_text(flight['OperatorCode(ICAO)'], flightvalue['OperatorCode(ICAO)'])
        login.input_text(flight['OperatorCode(IATA)'], flightvalue['OperatorCode(IATA)'])
        login.input_text(flight['OperatorName'], flightvalue['OperatorName'])
        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        sleep(1)
        login.is_click(flight['SaveAirline'])
        sleep(5)

        '''跳转到AddPassengerInfo页面'''
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        sleep(2)
        login.is_click(flight['Operator(ICAO)_select'])
        sleep(2)
        login.input_text(flight['Operator(ICAO)_input'], flightvalue['OperatorCode(ICAO)'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[2]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)

        '''跳转到Business页面进行删除新增的airline'''
        login.get_url(ini.url + "#/CodeTable/Operator/Operator")
        # 未完成的application离开时会弹框提醒是否退出
        sleep(3)
        login.is_click(flight['LeaveApplication'])
        login.is_click(flight['AdvancedSearch'])
        login.is_click(flight['Operator(IATA)_search_select'])
        sleep(1)
        login.input_text(flight['Operator(IATA)_search_input'], flightvalue['OperatorCode(IATA)'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div[1]/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        # 点击空白处退出当前多选下拉框
        login.is_click(flight['OnclickWrite'])
        login.is_click(flight['Search'])
        sleep(5)
        login.is_click(flight['AirlineOperatorView'])
        sleep(2)
        login.is_click(flight['DeleteAirline'])
        sleep(5)
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(flight["Logout_Yes"])
        sleep(2)
if __name__ == '__main__':
    pytest.main(['TestCase/TC_CODE_009/test_code_009.py'])
