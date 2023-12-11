import os
import allure
import pytest

from telnetlib import EC
from dateutil.relativedelta import relativedelta
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.readconfig import ini
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage

flight = Element('flight_071')
flightValue = ElementValue('flightValue_071')
flightAcc = ElementValue('cad_account')
@allure.feature("TC(ECE)-071 02Process_application_by_Officer")
class TestProcessApplicationByOfficer:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    def test_001(self, drivers):
        """登录operator(归属地CPA)用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightAcc['OfficerLoginName'])
            login.input_user_password(flightAcc['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))
        # 跳转到页面
        login.get_url(ini.url + "?#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Messages"
        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path)+'/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， r以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
        with open(filename, 'r') as f:
            refno = f.read()
        # # 打开查询页
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        login.input_text(flight['ViewMessages_Search_ReferenceNo'], refno)
        login.input_text(flight['ViewMessages_Sender'], flightAcc['OperatorcpaLoginName'])
        login.is_click(flight['ViewMessages_Search'])
        sleep(5)
        # 检查查询结果
        # assert drivers.find_element_by_xpath("//*[@id='test0']").text == str(refno)
        # 进入详情页
        login.is_click(flight['ViewMessages_ReferenceNo'])
        sleep(5)
        # 检查跳转
        # assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[1]/div/div/form/div[1]/div[1]/div/div").text == str(refno)
        # 审批
        login.is_click(flight['DetailApproval'])
        # Recommendation
        login.is_click(flight['ApprovalRecommendation'])
        sleep(1)
        login.is_click(flight['ApprovalRecommendationConfirm'])
        login.is_click(flight['ApprovalSucceedPopupOK'])
        sleep(1)
        # generate
        # login.is_click(flight['ApprovalGenerate'])
        # sleep(12)
        # send
        login.is_click(flight['ApprovalSendLetterBTU'])
        sleep(12)
        login.is_click(flight['ApprovalSendLetterPopUpBTU'])
        sleep(2)
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_071/test_e2e_0412.py'])