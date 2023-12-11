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
flight = Element('messflight_003')
flightvalue = ElementValue('messflightValue_003')
flightAccValue = ElementValue('cad_account')

@allure.feature("TC(mess)-003 Maintain support document expiry alert")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Alert Parameters for Supporting Documents")
    def test_mess_003(self, drivers):
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
        login.get_url(ini.url + "#/Misc/MaintainAlert")

        drivers.implicitly_wait(30)
        sleep(5)

        assert drivers.find_element_by_css_selector("h2").text == "Alert Parameters for Supporting Documents"

        # add new

        login.is_click(flight['AddButton'])
        sleep(1)
        login.is_click(flight['DocumentType_select'])
        sleep(1)
        login.input_text(flight['DocumentType_input'], flightvalue['AddDocumentType'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[7]/div[3]/div/div[2]/form/div[1]/div/div/div[1]/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight['Operator(ICAO)_select'])
        sleep(1)
        login.input_text(flight['Operator(ICAO)_input'], flightvalue['AddOperator(ICAO)'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[7]/div[3]/div/div[2]/form/div[2]/div/div/div[1]/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight['SubjectOfficer_select'])
        sleep(1)
        login.input_text(flight['SubjectOfficer_input'], flightvalue['AddSubjectOfficer'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[7]/div[3]/div/div[2]/form/div[4]/div/div/div[1]/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight['NoOfDaysBeforeExpiry'], flightvalue['AddNoOfDaysBeforeExpiry'])
        sleep(1)
        login.is_click(flight['Save'])
        sleep(3)
        login.is_click(flight['SaveIsOk'])
        sleep(1)

        #modify
        login.is_click(flight['DocumentType_select_search'])
        sleep(1)
        login.input_text(flight['DocumentType_input_search'], flightvalue['AddDocumentType'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight['Search'])
        sleep(1)
        login.is_click(flight['InboxSelect'])
        login.is_click(flight['Modify'])
        sleep(1)
        login.input_text(flight['NoOfDaysBeforeExpiry'], flightvalue['ModifyNoOfDaysBeforeExpiry'])
        login.is_click(flight['Save'])
        sleep(3)
        login.is_click(flight['ModifyIsOk'])
        sleep(1)

        #remove
        # login.is_click(flight['DocumentType_select_search'])
        # sleep(1)
        # login.input_text(flight['DocumentType_input_search'], flightvalue['AddDocumentType'])
        # sleep(1)
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div/div/div/input").send_keys(Keys.ENTER)
        # sleep(1)
        # login.is_click(flight['Search'])
        # sleep(2)
        login.is_click(flight['InboxSelect'])
        login.is_click(flight['Remove'])
        login.is_click(flight['Removecomfirm'])
        login.is_click(flight['RemoveIsOk'])

        # logout
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(flight["Logout_Yes"])
        sleep(2)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_MESS_003/test_mess_003.py'])





