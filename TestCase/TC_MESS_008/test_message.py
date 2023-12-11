import os
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

flight = Element('mess_008')
flightvalue = ElementValue('messvalue_008')
cad_account = ElementValue('cad_account')
@allure.feature("TC(MESS)-008 Alert users for application being re-allocated by Senior")
class TestMessage:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Alert users for application being re-allocated by Senior")
    def test_008(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['CpaOfficerLoginName'])
            login.input_user_password(cad_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到/ApplicationView/SeasonalSchedule/AddPassengerInfo页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"

        r = random.choice(string.ascii_letters)
        FlightNo1 = "CPA" + str(randint(1, 9999)) + r
        FlightNo2 = "CPA" + str(randint(1, 9999)) + r

        login.is_click(flight['Season'])
        login.input_text(flight['Season'], "Summer")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[1]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)

        # step1 填写flight Schedules表格信息
        # FlightNo1
        login.input_text(flight['FlightNo1'], FlightNo1)
        login.input_text(flight['From1'], flightvalue['From1'])
        login.input_text(flight['To1'], flightvalue['To1'])
        sleep(2)
        login.is_click(flight['DOP1'])
        login.is_click(flight['DOP3'])
        login.is_click(flight['DOP5'])
        sleep(2)
        login.is_click(flight['AircraftType_Select1'])
        login.input_text(flight['AircraftType_input1'], flightvalue['AircraftType_input1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoOfSeats1'], flightvalue['NoOfSeats1'])
        login.input_text(flight['Route1'], flightvalue['Route1'])
        sleep(2)
        login.is_click(flight['LocalTime_STD1'])
        login.input_text(flight['LocalTime_STD1'], flightvalue['LocalTime_STD1'])
        login.input_text(flight['Remarks1'], flightvalue['Remarks1'])
        sleep(2)
        # FlightNo1_2
        login.input_text(flight['FlightNo2'], FlightNo2)
        login.is_click(flight['AircraftType_Select2'])
        login.input_text(flight['AircraftType_input2'], flightvalue['AircraftType_input2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['NoOfSeats2'], flightvalue['NoOfSeats2'])
        login.input_text(flight['Route2'], flightvalue['Route2'])
        sleep(2)
        login.is_click(flight['LocalTime_STA2'])
        login.input_text(flight['LocalTime_STA2'], flightvalue['LocalTime_STA2'])
        login.input_text(flight['Remarks2'], flightvalue['Remarks2'])
        sleep(2)

        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        sleep(2)

        # 选择文件
        login.is_click(flight['SelectDoc'])
        login.input_text(flight['DocType_input'], flightvalue['DocType_input1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['DocType_input'], flightvalue['DocType_input2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['Doc_search'])
        sleep(1)
        login.is_click(flight['Doc_confirm'])
        sleep(2)

        # 上传文件
        login.is_click(flight['UploadDoc'])
        sleep(2)
        login.is_click(flight['UploadDoc_input_others'])
        sleep(2)
        login.input_text(flight['UploadDoc_input_others'], flightvalue['UploadDoc_input_others'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight['ExpiryDate'], "31/12/2099")
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['UploadButton'])
        sleep(2)
        assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[2]/div").text == "other_supports.pdf"

        # step2 Click "Preview and Submit"
        login.is_click(flight['PreviewAndSubmit_Confirm'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)

        # step3 Click "Submit"
        login.is_click(flight['Submit'])
        sleep(2)

        # step4 Click "No" in lease aircraft dialog
        login.is_click(flight['LeaseAircraft_No'])
        sleep(2)

        # step5 Click "No" in special operation dialog
        login.is_click(flight['SpecialOperation_No'])
        sleep(2)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        # step6
        # 切换到OFFICER1
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['OfficerLoginName'])
            login.input_user_password(cad_account['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到/View/Application
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Messages"
        sleep(1)

        login.is_click(flight['AdvancedSearch'])
        sleep(2)
        login.input_text(flight['Sender'], cad_account['CpaOfficerLoginName'])
        sleep(2)
        login.is_click(flight['ApplicationType'])
        sleep(2)
        login.is_click(flight['Msg_Search'])
        sleep(2)
        login.is_click(flight['Msg_Select'])
        sleep(2)
        login.is_click(flight['ReassignOfficer_Input'])
        login.input_text(flight['ReassignOfficer_Input'], cad_account['Officer2LoginName'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[16]/div[2]/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['ReassignOfficer'])
        sleep(2)
        login.is_click(flight['ReassignOfficer_OK'])
        sleep(2)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        # step7
        # 切换到OFFICER2
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['Officer2LoginName'])
            login.input_user_password(cad_account['Officer2Password'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到/View/Messages
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Messages"
        sleep(1)

        login.is_click(flight['ViewMessages_AdvancedSearch'])
        sleep(1)
        login.input_text(flight['ViewMessages_Sender'], cad_account['OfficerLoginName'])
        sleep(1)
        login.is_click(flight['ViewMessages_ApplicationType'])
        sleep(1)
        login.is_click(flight['ViewMessages_Search'])
        sleep(1)

        # step8
        login.is_click(flight['ViewMessages'])
        sleep(5)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])


if __name__ == '__main__':
        pytest.main(['TestCase/test_message.py'])