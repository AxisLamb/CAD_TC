import os
import string
import random
from random import randint

import pytest
import allure

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import log
data = Element('TC(mess)-002')
value = ElementValue('TC(mess)-002value')
@allure.feature("TC(mess)-002 Processing deadline Alert")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Processing deadline Alert")
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
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"
        temp = str(randint(100, 999))+random.choice(string.ascii_letters)
        # step1
        login.is_click(data['Operator(ICAO)'])
        sleep(2)
        login.is_click(data['Operator(ICAO)_CPA'])
        login.input_text(data['FlightNo1'], "CPA1"+temp)
        login.input_text(data['OperationPeriodFrom1'], value['OperationPeriodFrom1'])
        login.input_text(data['OperationPeriodTo1'], value['OperationPeriodTo1'])
        login.is_click(data['DOP1-1'])
        login.is_click(data['DOP1-3'])
        login.is_click(data['DOP1-5'])
        login.is_click(data['AircraftType1'])
        login.is_click(data['AircraftType1_100'])
        login.input_text(data['NoOfSeats1'], value['NoOfSeats1'])
        login.input_text(data['Route1'], value['Route1'])
        login.is_click(data['LocalTimeSTD1'])
        login.input_text(data['LocalTimeSTD1'], value['LocalTimeSTD1'])
        login.input_text(data['Remarks1'], value['Remarks1'])
        login.input_text(data['FlightNo2'], "CPA2"+temp)
        login.is_click(data['AircraftType2'])
        login.is_click(data['AircraftType2_100'])
        login.input_text(data['NoOfSeats2'], value['NoOfSeats2'])
        login.input_text(data['Route2'], value['Route2'])
        login.is_click(data['LocalTimeSTA2'])
        login.input_text(data['LocalTimeSTA2'], value['LocalTimeSTA2'])
        login.input_text(data['Remarks2'], value['Remarks2'])
        login.input_text(data['Remarks'], value['Remarks'])
        login.is_click(data['SelectFromDocumentLibrary'])
        # login.is_click(data['Library_DocumentType'])
        # login.is_click(data['Library_DocumentType_Aerodrome'])
        # login.is_click(data['Library_DocumentType_Air'])
        # login.is_click(data['Library_Search'])
        login.is_click(data['Document_Confirm'])
        login.is_click(data['UploadApplicationRelatedDocument'])
        login.is_click(data['Upload_DocumentType'])
        login.is_click(data['Upload_DocumentType_Others'])
        sleep(2)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        login.input_text(data['Upload_ExpiryDate'], value['ExpiryDate'])
        sleep(2)
        login.is_click(data['UploadButton'])
        sleep(2)
        # step 2
        login.is_click(data['ConfirmConditions'])
        login.is_click(data['PreviewAndSubmit'])
        # step 3
        login.is_click(data['Submit'])
        sleep(2)
        # step 4
        login.is_click(data['Button_No'])
        # step 5
        login.is_click(data['Button_No'])
        # step 6
        login.is_click(data['ApplicationType_ScheduledPassenger'])
        login.is_click(data['Status'])
        login.is_click(data['Status_New'])
        login.is_click(data['SearchApplication'])
        login.is_click(data['ScheduledPassenger_Check'])
        login.is_click(data['RequestFollowUp'])
        # step 7
        refNo = login.element_text(data['RefNo'])
        login.is_click(data['CADUser'])
        login.is_click(data['CADUser_Officer1'])
        login.input_text(data['Deadline'], value['Deadline'])
        # drivers.find_element_by_xpath("//div[contains(label,'Deadline')]//input").send_keys(Keys.ENTER)
        login.input_text(data['Message'], value['Message'])
        login.is_click(data['Save'])

        # step 8
        # 跳转到view - messages页面
        login.get_url(value['Url_ViewMessages'])
        sleep(2)
        # 搜索记录
        login.is_click(data['AdvancedSearch'])
        login.input_text(data['SubjectContains'], value['SubjectContains'])
        login.input_text(data['RefNo_Input'], refNo)
        login.input_text(data['Sender'], value['Sender'])
        login.is_click(data['ApplicationType_ScheduledPassenger'])
        login.is_click(data['SearchButton'])
        # step 9
        login.is_click(data['FollowUpMessage'])
        sleep(2)
        login.is_click(data['Message_Close'])
        # 退出当前账号
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(data["Logout_Yes"])
        sleep(2)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_CODE_006/test_mess_002.py'])

