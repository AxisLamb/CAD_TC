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

flight = Element('codeflight_017')
flightvalue = ElementValue('codeflightValue_017')

@allure.feature("TC(code)-017 Maintain Cancel Flight Reason Code")
class TestMaintainCancelFlightReasonCode:

    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面,登出已登陆的账号"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])

        login.get_url(ini.url)

    @allure.story("Maintain Cancel Flight Reason Code")
    def test_144(self, drivers):
        """登录officer用户"""
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['OfficerLoginName'])
            login.input_user_password(flightvalue['OfficerPassword'])
            login.click_login_button()

        sleep(2)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到Code Table ->Helicopter->Flight Cancel Reason'''
        login.get_url(ini.url + "#/CodeTable/Helicopter/Reason")
        drivers.implicitly_wait(30)
        sleep(2)
        assert drivers.find_element_by_css_selector("h2").text == "Cancel Flight Reason Information"

        # 新增一条Cancel Flight Reason信息
        login.is_click(flight['AddButton'])
        sleep(2)
        login.input_text(flight['Cancel_Flight_Reason'], flightvalue['Cancel_Flight_Reason'])
        sleep(3)
        login.input_text(flight['English_Description'], flightvalue['English_Description'])
        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        login.is_click(flight['SaveButton'])
        sleep(2)

        # 查看Cancel Flight Reason数据
        login.get_url(ini.url + "#/Other/Helicopter/Enquire")
        sleep(2)
        drivers.find_elements_by_xpath("//*[@id='CANCEL_REASON.HC1']")
        print("页面选中的值" + flightvalue['Cancel_Flight_Reason'])
        # 删除添加的Cancel Flight Reason 测试数据
        sleep(2)
        login.get_url(ini.url + "#/CodeTable/Helicopter/Reason")
        drivers.find_element_by_xpath("//td[contains(div,'HC1')]").click()
        sleep(3)
        login.is_click(flight['DeleteButton'])
        sleep(3)
        login.is_click(flight['DeleteYesButton'])
        sleep(5)
        login.is_click(flight['DeleteYesOKBtn'])
        sleep(3)
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

    if __name__ == '__main__':
        pytest.main(['TestCase/TC_CODE_017/test_code_017.py'])