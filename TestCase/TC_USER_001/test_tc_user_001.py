import allure
import pytest
import random
import string
from random import randint
from selenium.webdriver.common.keys import Keys
from page_object.LoginPage import LoginPage
from common.readconfig import ini
from page.webpage import sleep
from common.readvalue import ElementValue
from common.readelement import Element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

flight = Element('user_001')
flightvalue = ElementValue('uservalue_001')
cad_account = ElementValue('cad_account')
@allure.feature("TC(USER)-001 Maintain User Account (Create, Search, Update) (Local Operator)")
class TestUser001:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain User Account (Create, Search, Update) (Local Operator)")
    def test_001(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['OfficerLoginName'])
            login.input_user_password(cad_account['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到/Admin/UserAccounts/CreateUserAccount页面
        login.get_url(ini.url + "#/Admin/UserAccounts/CreateUserAccount")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create User Account"

        r = random.choice(string.ascii_letters)
        LoginUsername = "AHKTESTER" + str(randint(1, 999)) + r

        # step1
        login.is_click(flight['UserType_External'])
        sleep(1)
        login.input_text(flight['LoginUsername'], LoginUsername)
        sleep(1)
        login.input_text(flight['Name'], flightvalue['Name'])
        sleep(1)
        login.input_text(flight['EmailAddress'], flightvalue['EmailAddress'])
        sleep(1)
        login.input_text(flight['PhoneNo'], flightvalue['PhoneNo'])
        sleep(1)
        login.input_text(flight['FaxNo'], flightvalue['FaxNo'])
        sleep(1)
        login.input_text(flight['Address1'], flightvalue['Address1'])
        sleep(1)
        login.input_text(flight['Address2'], flightvalue['Address2'])
        sleep(1)
        login.input_text(flight['Address3'], flightvalue['Address3'])
        sleep(1)
        login.is_click(flight['Operator_input'])
        login.input_text(flight['Operator_input'], flightvalue['Operator_input'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div[2]/div/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight['Create_save'])
        sleep(1)
        login.is_click(flight['Create_save_OK'])
        sleep(2)

        # step2
        login.is_click(flight['ResetPassword'])
        sleep(1)
        text = drivers.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/div[2]/p").text
        psw = text[17:]
        login.is_click(flight['ResetPassword_OK'])
        sleep(1)

        # step3
        login.is_click(flight['Add'])
        sleep(2)

        # step4
        login.input_text(flight['Search_Name'], flightvalue['Search_Name'])
        sleep(1)
        login.input_text(flight['Search_Description'], flightvalue['Search_Description'])
        sleep(1)
        login.is_click(flight['Search'])
        sleep(2)

        # step5
        login.is_click(flight['Search_Result'])
        sleep(1)
        login.is_click(flight['Search_Add'])
        sleep(1)
        login.is_click(flight['Search_Add_OK'])
        sleep(2)

        # step6
        # 跳转到/Admin/UserAccounts/SearchUserAccount页面
        login.get_url(ini.url + "#/Admin/UserAccounts/SearchUserAccount")
        drivers.implicitly_wait(30)
        sleep(2)
        assert drivers.find_element_by_css_selector("h2").text == "Search User Account"
        sleep(2)

        login.is_click(flight['Account_External'])
        sleep(1)
        login.input_text(flight['Account_LoginUsername'], LoginUsername)
        sleep(1)
        login.is_click(flight['Account_Search'])
        sleep(2)

        # step7
        login.is_click(flight['Logout'])
        sleep(1)
        login.is_click(flight['Logout_Yes'])
        sleep(2)

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(LoginUsername)
            login.input_user_password(psw)
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # step8
        login.is_click(flight['ChangePsw_YES'])
        sleep(1)
        login.input_text(flight['OldPsw'], psw)
        sleep(1)
        login.input_text(flight['NewPsw'], "1234567a")
        sleep(1)
        login.input_text(flight['NewPsw_confirm'], "1234567a")
        sleep(1)
        login.is_click(flight['NewPsw_save'])
        sleep(1)
        login.is_click(flight['ChangePsw_OK'])
        sleep(2)

        login.is_click(flight["Logout"])
        sleep(1)
        login.is_click(flight["Logout_Yes"])
        sleep(2)


if __name__ == '__main__':
        pytest.main(['TestCase/test_tc_user_001.py'])