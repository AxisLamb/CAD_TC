import os
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
from selenium.webdriver.common.keys import Keys

flight = Element('mess_011')
flightvalue = ElementValue('messValue_011')

@allure.feature("TC(mess)-011 Flight Schedule And Slot Inconsistency Alert")
class TestMess011:

    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面,登出已登陆的账号"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])

        login.get_url(ini.url)

    @allure.story("Flight Schedule And Slot Inconsistency Alert")
    def test_011(self, drivers):
        """登录CPATEST用户"""
        login = LoginPage(drivers)
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['Cpa_LoginName'])
            login.input_user_password(flightvalue['Cpa_Password'])
            login.click_login_button()

        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到Application -> Seasonal Schedule -> Passenger'''
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"

        # 新增一条Schedule Passenger信息
        login.is_click(flight['Season'])
        login.input_text(flight['Season'], flightvalue['Season'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[1]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight['FlightNo1'], flightvalue['FlightNo1'])
        sleep(1)
        login.input_text(flight['FlightNo2'], flightvalue['FlightNo2'])
        sleep(1)
        login.is_click(flight['FlightDiff'])
        login.input_text(flight['FlightDiff'], flightvalue['FlightDiff'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight['OperationPeriodFrom'], flightvalue['OperationPeriodFrom'])
        sleep(1)
        login.input_text(flight['OperationPeriodTo'], flightvalue['OperationPeriodTo'])
        sleep(1)
        login.is_click(flight['DOP1'])
        sleep(1)
        login.is_click(flight['DOP3'])
        sleep(1)
        login.is_click(flight['DOP5'])
        sleep(1)
        login.is_click(flight['AircraftType1'])
        login.input_text(flight['AircraftType1'], flightvalue['AircraftType1'])
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.is_click(flight['AircraftType2'])
        login.input_text(flight['AircraftType2'], flightvalue['AircraftType2'])
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.input_text(flight['SeatsNo1'], flightvalue['SeatsNo1'])
        sleep(1)
        login.input_text(flight['SeatsNo2'], flightvalue['SeatsNo2'])
        sleep(1)
        login.input_text(flight['Route1'], flightvalue['Route1'])
        sleep(1)
        login.input_text(flight['Route2'], flightvalue['Route2'])
        sleep(1)
        login.input_text(flight['STD'], flightvalue['STD'])
        sleep(1)
        login.input_text(flight['STA'], flightvalue['STA'])
        sleep(1)
        login.input_text(flight['Remarks1'], flightvalue['Remarks1'])
        sleep(1)
        login.input_text(flight['Remarks2'], flightvalue['Remarks2'])
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        sleep(1)

        # Upload file
        login.is_click(flight['UploadRelatedDocuments'])
        sleep(1)
        login.is_click(flight['DocTypeInput'])
        login.input_text(flight['DocTypeInput'], flightvalue['DocTypeInput'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(1)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(1)
        login.is_click(flight['Indefinite'])
        sleep(1)
        login.is_click(flight['UploadButton'])
        sleep(1)

        login.is_click(flight['ConfirmCheckBox'])
        sleep(1)
        login.is_click(flight['PreviewButton'])
        sleep(2)
        login.is_click(flight['SubmitButton'])
        sleep(1)
        login.is_click(flight['NoButton1'])
        sleep(1)
        login.is_click(flight['NoButton2'])
        sleep(2)

        # 从 CPATEST03 用户到 Officer1 用户切换
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(flightvalue['Officer_LoginName'])
        login.input_user_password(flightvalue['Officer_Password'])
        login.click_login_button()

        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到View -> Application页面'''
        login.get_url(ini.url + "#/View/Application")
        login.is_click(flight['ScheduledPassenger'])
        sleep(1)
        login.is_click(flight['Operator(ICAO)'])
        login.input_text(flight['Operator(ICAO)'], flightvalue['Operator(ICAO)'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div[1]/div/div/div/div[2]/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight['SearchButton'])
        sleep(2)
        login.is_click(flight['ReferenceNo'])
        sleep(2)
        login.is_click(flight['checkData'])
        sleep(1)
        login.is_click(flight['CheckApprovedSlotButton'])
        sleep(2)


    if __name__ == '__main__':
        pytest.main(['TestCase/TC_MESS_011/test_mess_011.py'])