
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
data = Element('TC(code)-006')
value = ElementValue('TC(code)-006value')
@allure.feature("TC(code)-006 Contact List for Handling Agent")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Contact List for Handling Agent")
    def test1(self, drivers):
        """登录officer用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
            login.is_click(data["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(value['OfficerLoginName'])
            login.input_user_password(value['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        # 跳转到CodeTable->Operator->HandlingInfo页面
        login.get_url(ini.url + "#/CodeTable/Operator/HandlingInfo")
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Contact List for Handling Agent"

        # 判断新增数据是否和已有数据重复
        if len(drivers.find_elements_by_xpath("//div[text()='" + value['HandlingAgent'] +"']")) > 0:
            login.is_click(data['AGTTEST01'])
            login.is_click(data['HandlingAgentDelete'])
        # 新增一条Contact List for Handling Agent信息
        # step 1
        login.is_click(data['AddButton'])
        sleep(1)

        # step 2
        login.input_text(data['HandlingAgent'], value['HandlingAgent'])
        login.input_text(data['CompanyName(English)'], value['CompanyName(English)'])
        login.is_click(data['Type'])
        sleep(1)
        login.is_click(data['Type_Cargo'])
        login.is_click(data['RecordSave'])
        sleep(2)
        # 切换到用户CPATESTER03
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        login.is_click(data['Logout_Yes'])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(value['CPALoginName'])
            login.input_user_password(value['CPAPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # step 3 跳转到Application->Charter Flight>Passenger页面
        login.get_url(ini.url + "#/ApplicationView/CharterFlight/CreateCharterFlight")
        sleep(2)
        login.is_click(data['LocalHandlingAgent'])
        sleep(2)
        drivers.find_element_by_xpath("//li[contains(span, '" + value['HandlingAgent'] + "')]").click()
        sleep(2)
        # 删除测试数据
        # 切换到用户OFFICER1
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(data['Logout_Yes'])
        sleep(2)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(value['OfficerLoginName'])
            login.input_user_password(value['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 40, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))
        # 跳转到CodeTable->Operator->HandlingInfo页面
        login.get_url(ini.url + "#/CodeTable/Operator/HandlingInfo")
        sleep(2)
        login.is_click(data['AGTTEST01'])
        login.is_click(data['HandlingAgentDelete'])
        # 退出当前账号
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(data["Logout_Yes"])
        sleep(2)


if __name__ == '__main__':
    pytest.main(['TestCase/TC_CODE_006/test_code_008.py'])

