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
flight = Element('TC(code)-011')
flightvalue  = ElementValue('TC(code)-011value')
@allure.feature("TC(code)-011 Maintain City Code")
class TestMaintainCountryCode:

    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面,登出已登陆的账号"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])

        login.get_url(ini.url)

    @allure.story("Maintain Country Code")
    def test_11(self, drivers):
        """登录officer用户"""
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['OfficerLoginName'])
            login.input_user_password(flightvalue['OfficerPassword'])
            login.click_login_button()


        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到Code Table -> Location -> Country页面'''
        login.get_url(ini.url + "#/CodeTable/Location/Country")
        drivers.implicitly_wait(30)
        sleep(2)
       # assert drivers.find_element_by_css_selector("h2").text == "City Information"

        # 新增一条Country信息
        login.is_click(flight['AddButton'])
        sleep(2)
        login.input_text(flight['CountryCode'], flightvalue['CountryCode'])
        sleep(1)
        login.is_click(flight['RegionCode'])
        login.is_click(flight['RegionCode_AF'])
        sleep(1)
        login.input_text(flight['EnglishDescription'], flightvalue['EnglishDescription'])
        sleep(1)
        login.input_text(flight['ChineseDescription'], flightvalue['ChineseDescription'])
        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        sleep(1)

        login.is_click(flight['SaveButton'])
        sleep(1)

        '''跳转到 View -> Application 页面'''
        login.get_url(ini.url + "#/View/Application")
        sleep(2)
        #搜索输入的city
        login.is_click(flight['RouteBy'])
        sleep(1)
        login.input_text(flight['RouteBy'], flightvalue['RouteBy'])
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[4]/div[1]/div/div/div[1]/div/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.input_text(flight['ApplicationEnglishDescription'], flightvalue['EnglishDescription'])
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[4]/div[1]/div/div/div[2]/div[1]/input").send_keys(
            Keys.ENTER)
        sleep(5)

        '''跳转到Code Table -> Location -> City页面'''
        login.get_url(ini.url + "#/CodeTable/Location/City")
        sleep(2)
        # 搜索并删除添加的测试数据
        login.input_text(flight['SearchCityCode'], flightvalue['CityCode'])
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight['SearchButton'])
        sleep(1)
        drivers.find_element_by_xpath("//div[text()='" + flightvalue['CityCode'] + "']").click()
        sleep(1)
        login.is_click(flight['DeleteButton'])
        sleep(1)
        login.is_click(flight['DeleteYesButton'])
        sleep(1)

    if __name__ == '__main__':
        pytest.main(['TestCase/TC_CODE_011/test_code_011.py'])
