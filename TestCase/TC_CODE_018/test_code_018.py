
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

flight = Element('codeflight_018')
flightvalue = ElementValue('codeflightValue_018')

@allure.feature("TC(code)-018 Maintain Service Type")
class TestCode018:

    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面,登出已登陆的账号"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])

        login.get_url(ini.url)

    @allure.story("Maintain Service Type")
    def test_018(self, drivers):
        """登录officer用户"""
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['OfficerLoginName'])
            login.input_user_password(flightvalue['OfficerPassword'])
            login.click_login_button()

        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到Code Table -> Service Type'''
        login.get_url(ini.url + "#/CodeTable/ServiceType")
        drivers.implicitly_wait(30)
        sleep(2)
        assert drivers.find_element_by_css_selector("h2").text == "Service Type Information(IATA)"

        # 新增一条Service Type信息
        login.is_click(flight['AddButton'])
        sleep(2)
        login.input_text(flight['ServiceType'], flightvalue['ServiceType'])
        sleep(1)
        login.input_text(flight['EnglishDescription'], flightvalue['EnglishDescription'])
        sleep(1)
        login.input_text(flight['CustomizedServiceTypeDescription'], flightvalue['CustomizedServiceTypeDescription'])
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        sleep(1)
        login.is_click(flight['SaveButton'])
        sleep(2)

        # 删除添加的测试数据
        drivers.find_element_by_xpath("//div[text()='" + flightvalue['EnglishDescription'] + "']").click()
        sleep(1)
        login.is_click(flight['DeleteButton'])
        sleep(1)
        login.is_click(flight['DeleteYesButton'])
        sleep(2)

    if __name__ == '__main__':
        pytest.main(['TestCase/TC_CODE_018/test_code_018.py'])