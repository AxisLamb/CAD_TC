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
@allure.feature("TC(ECE)-071 05Check_Message_By_Operator")
class TestCheckChangeMessageByOperator:
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
            login.input_user_name(flightAcc['OperatorcpaLoginName'])
            login.input_user_password(flightAcc['OperatorcpaPassword'])
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
        login.is_click(flight['OptAdvancedSearch'])
        login.input_text(flight['OptSearch_ReferenceNo'], refno)
        login.input_text(flight['OptSearch_Sender'], flightAcc['OfficerLoginName'])
        login.is_click(flight['OptSearch_BTU'])
        sleep(5)
        # 检查查询结果
        # assert drivers.find_element_by_xpath("//*[@id='test0']").text == str(refno)
        # 进入详情页
        login.is_click(flight['OptMessageDetail'])
        sleep(2)
        # login.is_click(flight['OptDetailAttachment'])
        sleep(1)
        login.is_click(flight['OptDetailRefno'])
        sleep(6)
        # 检查跳转
        assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div[1]/div/div/form/div[1]/div[1]/div/div").text == str(refno)
        assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div[1]/div/div/form/div[1]/div[2]/div/div").text == 'Approved'
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        current_path = os.path.abspath(__file__)
        # 清空文件内容
        # '该文件夹下所有的文件（包括文件夹）'
        file_path = os.path.dirname(current_path)+'/TestData/Out'
        FileList = os.listdir(file_path)
        # '遍历所有文件'
        for files in FileList:
            files = os.path.join(file_path, files)
            # 清空文件内容
            with open(files, 'a+') as f:
                f.truncate(0)