import os
import pytest
import allure
import string
import random
from selenium.webdriver.common.keys import Keys
from random import randint
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

flight = Element('admflight_002')
flightvalue = ElementValue('admflightValue_002')
flightAccValue = ElementValue('cad_account')

@allure.feature("TC(adm)-002 Manage Airline profile")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create Seasonal Schedule Passenger Application")
    def test_adm_002(self, drivers):
        """登录CPATEST03用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightAccValue['CpaOfficerLoginName'])
            login.input_user_password(flightAccValue['CpaOfficerPassword'])
            login.click_login_button()

        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到AddPassengerInfo页面'''
        login.get_url(ini.url + "#/AirlineInformation/View")

        drivers.implicitly_wait(30)
        sleep(5)

       # assert drivers.find_element_by_css_selector("h2").text == "Airline Information"


        login.input_text(flight['LocalGroundHandingAgent'], flightvalue['LocalGroundHandingAgent'])
        login.input_text(flight['CallSignRadioTelephony'], flightvalue['CallSignRadioTelephony'])
        login.input_text(flight['ContactName'], flightvalue['ContactName'])
        login.input_text(flight['ContactPost'], flightvalue['ContactPost'])
        login.input_text(flight['ContactTel'], flightvalue['ContactTel'])
        login.input_text(flight['ContactFax'], flightvalue['ContactFax'])
        login.input_text(flight['ContactEmail'], flightvalue['ContactEmail'])
        login.input_text(flight['ContactAddress'], flightvalue['ContactAddress'])
        login.input_text(flight['AddresseeName'], flightvalue['AddresseeName'])
        login.input_text(flight['AddresseePost'], flightvalue['AddresseePost'])
        login.input_text(flight['AddresseeTel'], flightvalue['AddresseeTel'])
        login.input_text(flight['AddresseeFax'], flightvalue['AddresseeFax'])
        login.input_text(flight['AddresseeEmail'], flightvalue['AddresseeEmail'])
        login.input_text(flight['AddresseeAddress'], flightvalue['AddresseeAddress'])
        login.input_text(flight['LocalName'], flightvalue['LocalName'])
        login.input_text(flight['LocalPost'], flightvalue['LocalPost'])
        login.input_text(flight['LocalTel'], flightvalue['LocalTel'])
        login.input_text(flight['LocalFax'], flightvalue['LocalFax'])
        login.input_text(flight['LocalEmail'], flightvalue['LocalEmail'])
        login.input_text(flight['LocalAddress'], flightvalue['LocalAddress'])
        login.input_text(flight['EmerContactName'], flightvalue['EmerContactName'])
        login.input_text(flight['EmerContactPost'], flightvalue['EmerContactPost'])
        login.input_text(flight['EmerContactTel'], flightvalue['EmerContactTel'])
        login.input_text(flight['EmerContactFax'], flightvalue['EmerContactFax'])
        login.input_text(flight['EmerContactEmail'], flightvalue['EmerContactEmail'])
        login.input_text(flight['EmerContactAddress'], flightvalue['EmerContactAddress'])
        login.input_text(flight['EmerContactAftn'], flightvalue['EmerContactAftn'])
        login.is_click(flight['AirlineSave'])
        sleep(3)
        login.is_click(flight['AirlineExport'])
        sleep(5)
        login.is_click(flight['AirlineSave'])
        sleep(3)
        login.is_click(flight['FleetButton'])
        login.is_click(flight['AddButton'])
        sleep(1)
        login.is_click(flight['IATAAircraftType_select'])
        sleep(1)
        login.input_text(flight['IATAAircraftType_input'], "100")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div/div[1]/div[3]/div/div[3]/div[3]/div/div[2]/div[1]/div/form[3]/div/div/div/div[1]/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['RegistrationMark'], "CPA1")
        login.input_text(flight['AirlineInternalCode'], "CPA001")
        login.input_text(flight['CargoCapacity'], "10000")
        login.input_text(flight['SeatCapacity'], "200")
        login.input_text(flight['Weight'], "5000")
        login.input_text(flight['Remarks'], "UAT testing fleet and aircraft")
        login.is_click(flight['FleetSave'])
        sleep(2)
        # search
        login.is_click(flight['OperatorCode_Select'])
        sleep(1)
        login.input_text(flight['OperatorCode_Input'], "CPA")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div/div[1]/div[3]/div/div[1]/div[1]/form[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['AircraftType'], "100")
        login.input_text(flight['RegMark'], "CPA1")
        login.is_click(flight['Search'])
        sleep(3)
        login.is_click(flight['Update'])
        sleep(2)
        #先清除当前数据
        login.is_click(flight['IATAAircraftType_select'])

        login.is_click(flight['IATAAircraftType_select'])
        sleep(1)
        login.input_text(flight['IATAAircraftType_input'], "141")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div/div[1]/div[3]/div/div[3]/div[3]/div/div[2]/div[1]/div/form[3]/div/div/div/div[1]/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['RegistrationMark'], "CPA2")
        # login.input_text(flight['AirlineInternalCode'], "CPA001")
        login.input_text(flight['CargoCapacity'], "5000")
        login.input_text(flight['SeatCapacity'], "100")
        login.input_text(flight['Weight'], "2000")
        login.input_text(flight['Remarks'], "UAT testing fleet and aircraft update")
        login.is_click(flight['FleetSave'])
        sleep(2)
        login.input_text(flight['AircraftType'], "141")
        login.input_text(flight['RegMark'], "CPA2")
        login.is_click(flight['Search'])
        sleep(3)
        login.is_click(flight['Remove'])
        sleep(3)
        login.is_click(flight['RemoveIsOk'])
        sleep(3)
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
    pytest.main(['TestCase/TC_ADM_002/test_adm_002.py'])