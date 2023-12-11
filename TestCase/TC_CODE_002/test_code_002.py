
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
flight = Element('codeflight_002')
flightvalue = ElementValue('codeflightValue_002')
flightAccValue = ElementValue('cad_account')

@allure.feature("TC(code)-002 Maintain Business Party Information")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain Business Party Information")
    def test_144(self, drivers):
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
        login.get_url(ini.url + "#/CodeTable/Business")

        drivers.implicitly_wait(30)
        sleep(5)

        assert drivers.find_element_by_css_selector("h2").text == "Maintain Business Party Information"

        # 新增一条business party信息
        login.is_click(flight['AddButton'])
        sleep(1)
        login.input_text(flight['BusinessPartyName'], flightvalue['BusinessPartyName'])
        login.input_text(flight['EmailAddress'], "test@pccw.com")
        login.input_text(flight['ContractPerson'], flightvalue['ContractPerson'])
        sleep(1)
        login.is_click(flight['AddNewSave'])
        sleep(2)

        '''跳转到message页面'''
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        login.is_click(flight['NewMessage'])
        sleep(2)
        login.is_click(flight['Recipient_select'])
        sleep(1)
        login.input_text(flight['Recipient_input'], flightvalue['BusinessPartyName'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[9]/div/div[2]/form/div[1]/div/div/div[1]/input").send_keys(Keys.ENTER)
        # 点击空白处退出当前多选下拉框
        login.is_click(flight['ClickWrite'])
        login.input_text(flight['Subject'], flightvalue['Subject'])
        login.input_text(flight['Message'], flightvalue['Message'])
        sleep(5)
        login.is_click(flight['sendMessage'])
        sleep(10)
        login.is_click(flight['SendIsOK'])
        sleep(5)
        '''跳转到Business页面'''
        login.get_url(ini.url + "#/CodeTable/Business")
        sleep(5)
        # 通过business party 找到前方的多选框
        drivers.find_element_by_xpath("//div[text()='" + flightvalue['BusinessPartyName'] + "']/../../td[1]/div/label/span/span").click()
        login.is_click(flight["Remove"])
        sleep(2)
        login.is_click(flight["RemoveIsOK"])
        sleep(2)
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(flight["Logout_Yes"])
        sleep(2)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_CODE_002/test_code_002.py'])

