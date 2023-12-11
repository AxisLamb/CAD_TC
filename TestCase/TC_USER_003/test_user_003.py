import os
import pytest
import allure
import random

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

flight = Element('user_003')
flightvalue = ElementValue('userValue_003')

@allure.feature("TC(user)-003 Maintain User Account (Create, Search, Update) (Agent)")
class TestUser003:

    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面,登出已登陆的账号"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])

        login.get_url(ini.url)

    @allure.story("Maintain User Account (Create, Search, Update) (Agent)")
    def test_005(self, drivers):
        """登录CPATEST用户"""
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['Officer_LoginName'])
            login.input_user_password(flightvalue['Officer_Password'])
            login.click_login_button()

        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''Admin -> UserAccounts -> CreateUserAccount'''
        login.get_url(ini.url + "#/Admin/UserAccounts/CreateUserAccount")
        drivers.implicitly_wait(30)
        sleep(2)
        assert drivers.find_element_by_css_selector("h2").text == "Create User Account"

        # 新增一条User Account信息
        login.is_click(flight['UserType'])
        sleep(1)
        login.is_click(flight['UploadButton'])
        sleep(1)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div[1]/div/div/div[2]/div/div/input").send_keys(file_path)
        sleep(1)
        login.is_click(flight['UploadSaveButton'])
        sleep(1)
        login.is_click(flight['Operator'])
        login.input_text(flight['Operator'], flightvalue['Operator'])
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div[2]/div/div[2]/div/div/div/div/input").send_keys(
            Keys.ENTER)
        sleep(1)

        loginUserName = flightvalue['LoginUsername'] + str(random.randint(100000, 999999))
        login.input_text(flight['LoginUsername'], loginUserName)
        sleep(1)
        login.input_text(flight['Name'], flightvalue['Name'])
        sleep(1)
        login.input_text(flight['EmailAddress'], flightvalue['EmailAddress'])
        sleep(1)
        login.is_click(flight['AgentAccount'])
        sleep(1)
        login.is_click(flight['AirlineProfile'])
        sleep(1)
        login.is_click(flight['ConfirmButton'])
        sleep(1)
        login.is_click(flight['ApplicationType'])
        login.input_text(flight['ApplicationType'], flightvalue['ApplicationType'])
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[1]/div[2]/div/div[6]/div/div/div/div[2]/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.is_click(flight['SaveButton'])
        sleep(1)
        login.is_click(flight['OKButton'])
        sleep(1)

        login.is_click(flight['ResetPassword'])
        sleep(1)
        newPasswordMessageElement = drivers.find_element_by_xpath("//div[contains(@class,'el-message-box__message')]/p")
        newPasswordMessage = newPasswordMessageElement.text
        newPassword = newPasswordMessage[17:]
        login.is_click(flight['OKButton'])
        sleep(1)

        #搜索新增的user account
        '''跳转到Admin -> UserAccounts -> SearchUserAccount页面'''
        login.get_url(ini.url + "#/Admin/UserAccounts/SearchUserAccount")
        sleep(2)
        login.is_click(flight['SearchUserType'])
        sleep(1)
        login.input_text(flight['LoginUserName'], loginUserName)
        sleep(1)
        login.is_click(flight['SearchUserButton'])
        sleep(1)
        drivers.find_element_by_xpath("//span[text()='" + loginUserName + "']").click()
        sleep(1)
        login.is_click(flight['AddButton'])
        sleep(1)
        login.input_text(flight['FunctionGroup'], flightvalue['FunctionGroup'])
        sleep(1)
        login.is_click(flight['SearchButton'])
        sleep(1)
        login.is_click(flight['ResultCheckBox'])
        sleep(1)
        login.is_click(flight['GroupAddButton'])
        sleep(1)
        login.is_click(flight['OKButton'])
        sleep(1)

        # 从 OFFICER1 用户到 新用户切换
        login.is_click(flight["Logout"])
        login.is_click(flight["YesButton"])
        login.input_user_name(loginUserName)
        login.input_user_password(newPassword)
        login.click_login_button()

        sleep(10)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        #修改初始密码
        login.is_click(flight['YesButton'])
        sleep(1)
        login.input_text(flight['OldPassword'], newPassword)
        sleep(1)
        login.input_text(flight['NewPassword'], flightvalue['NewPassword'])
        sleep(1)
        login.input_text(flight['ConfirmNewPassword'], flightvalue['NewPassword'])
        sleep(1)
        login.is_click(flight['SaveButton2'])
        sleep(1)
        login.is_click(flight['OKButton'])
        sleep(4)

    if __name__ == '__main__':
        pytest.main(['TestCase/TC_CODE_018/test_usr_003.py'])