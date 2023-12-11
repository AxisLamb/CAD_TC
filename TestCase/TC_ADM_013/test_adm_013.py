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

flight = Element('admflight_013')
flightvalue = ElementValue('admflightValue_013')
flightAccValue = ElementValue('cad_account')

@allure.feature("TC(adm)-013 Maintain Flight Application Preference")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("List of Flight Application Preference")
    def test_adm_013(self, drivers):
        """登录CPATEST03用户"""
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

        '''跳转到MaintainFlight页面'''
        login.get_url(ini.url + "#/Misc/MaintainFlight")

        drivers.implicitly_wait(30)
        sleep(5)

        login.is_click(flight['AddMiscData'])
        sleep(3)
        login.is_click(flight['MiscApplicationType'])

        login.is_click(flight['MiscOperatorNationality_select'])
        sleep(1)
        login.input_text(flight['MiscOperatorNationality_input'], "Hong Kong (SAR, China)")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div/div[2]/form/div[2]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['MiscOperatorNationality_select'])

        login.is_click(flight['MiscOperator_select'])
        sleep(1)
        login.input_text(flight['MiscOperator_input'], "CPA")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div/div[2]/form/div[3]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['MiscOperator_select'])

        login.is_click(flight['MiscAirCraftType_select'])
        sleep(1)
        login.input_text(flight['MiscAirCraftType_input'], "100")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div/div[2]/form/div[4]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['MiscAirCraftType_select'])

        login.is_click(flight['MiscCountry_select'])
        sleep(1)
        login.input_text(flight['MiscCountry_input'], "Chinese Taipei")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div/div[2]/form/div[5]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['MiscCountry_select'])

        login.input_text(flight['MiscPort'], "TPE")
        login.input_text(flight['MiscFromDate'], "01/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div/div[2]/form/div[7]/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['MiscToDate'], "30/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div/div[2]/form/div[7]/div/div[2]/input").send_keys(Keys.ENTER)
        login.is_click(flight['MiscRecipient_select'])
        sleep(1)
        login.input_text(flight['MiscRecipient_input'], "Officer1")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[4]/div/div/div[2]/form/div[9]/div/div[1]/div[1]/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['MiscSave'])
        sleep(5)
        # 切换officer用户
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(flight["Logout_Yes"])
        sleep(2)
        elementsOfficer = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elementsOfficer) > 0:
            login.input_user_name(flightAccValue['CpaOfficerLoginName'])
            login.input_user_password(flightAccValue['CpaOfficerPassword'])
            login.click_login_button()
        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(5)

        # 填写Flight Schedules表格信息 Start
        # basic
        #航班号用CPA+4位整数和一位随机字母组成
        s=string.ascii_letters
        r=random.choice(s)
        FlightNoA1="CPA"+str(randint(1000, 9999))+r
        FlightNoA2="CPA"+str(randint(1000, 9999))+r


        # flight information
        login.input_text(flight['FlightNoA1'], FlightNoA1)
        login.input_text(flight['From'], "01/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To'], "30/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1'])
        login.is_click(flight['DOP_3'])
        login.is_click(flight['DOP_5'])

        login.is_click(flight['AircraftType_A1_select'])
        sleep(1)
        login.input_text(flight['AircraftType_A1_input'], "100")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['RouteA1'], "HKG-LAX")
        login.input_text(flight['No_of_SeatA1'], "100")

        sleep(1)
        login.input_text(flight['STD_A1'], "1030")

        login.input_text(flight['FlightNoA2'], FlightNoA2)
        login.is_click(flight['FlightDiff_select'])
        sleep(1)
        login.input_text(flight['FlightDiff_input'], "+0")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_A2_select'])
        sleep(1)
        login.input_text(flight['AircraftType_A2_input'], "100")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['RouteA2'], "LAX-HKG")
        login.input_text(flight['No_of_SeatA2'], "100")

        sleep(1)
        login.input_text(flight['STA_A2'], "1930")

        login.input_text(flight['Remarks'], "UAT End2End Testing")


        # upload
        login.is_click(flight['Upload_Application_Related_Documents'])
        sleep(2)
        login.is_click(flight['Upload_Application_Related_Documents_Type_Select'])
        sleep(1)
        login.input_text(flight['Upload_Application_Related_Documents_Type_input'], "Others")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        # sleep(1)
        # login.is_click(flight['Upload_Application_Related_Documents_Browse'])
        sleep(2)

        # # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_support.pdf"
        # # 输入上传文件的路径
        # dlg.Edit.set_text(file_path)
        # sleep(3)
        # # 点击打开
        # dlg["打开(&O)"].click_input()
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        expiryDate = (datetime.today().date() + timedelta(days=1)).strftime("%d/%m/%Y")
        login.input_text(flight['Upload_Application_Related_Documents_Expiry_Date'], expiryDate)
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)

        sleep(2)
        login.is_click(flight['Upload_Application_Related_Documents_Btn'])
        sleep(2)
        # submit
        login.is_click(flight['Confirm'])
        sleep(1)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(1)
        login.is_click(flight['Submit'])
        sleep(4)
        # drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small testCancelButtonClass016']").click()
        drivers.find_element_by_class_name("testCancelButtonClass016").click()
        sleep(1)
        # drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small testCancelButtonClass071']").click()
        drivers.find_element_by_class_name("testCancelButtonClass071").click()
        sleep(4)
        # 切换officer用户
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(flight["Logout_Yes"])
        sleep(2)
        elementsOfficer = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elementsOfficer) > 0:
            login.input_user_name(flightAccValue['OfficerLoginName'])
            login.input_user_password(flightAccValue['OfficerPassword'])
            login.click_login_button()
        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到页面
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight["AdvanceSearch"])

        login.is_click(flight["ScheduledBox"])
        sleep(1)
        login.is_click(flight["Search"])
        sleep(2)
        login.is_click(flight["Message"])
        login.is_click(flight["Discard"])
        sleep(2)
        '''跳转到MaintainFlight页面'''
        login.get_url(ini.url + "#/Misc/MaintainFlight")

        drivers.implicitly_wait(30)
        sleep(5)
        drivers.find_element_by_xpath("//div[text()='Scheduled Passenger']/../../td[1]/div/label/span/span").click()
        login.is_click(flight["Remove"])
        sleep(1)
        login.is_click(flight["RemoveIsOK"])


        # logout
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(flight["Logout_Yes"])
        sleep(2)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_ADM_013/test_adm_013.py'])