import os
import allure
import pytest
from selenium.webdriver.common.keys import Keys
from page_object.LoginPage import LoginPage
from common.readconfig import ini
from page.webpage import sleep
from common.readvalue import ElementValue
from common.readelement import Element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

flight = Element('flight_083')
flightvalue = ElementValue('flightvalue_083')
cad_account = ElementValue('cad_account')
@allure.feature("TC(ECE)-083 Local Operator Create and Officer Processing Schedule Change Application (Approve) for Charter Cargo application")
class TestTrafficRightsRulesApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("View application result  by Local Operator")
    def test_083(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight['Logout_Yes'])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['CpaOfficerLoginName'])
            login.input_user_password(cad_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到/View/Messages页面
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)

        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path) + '/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， r以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
        with open(filename, 'r') as f:
            refno = f.read()

        # step41
        login.is_click(flight['AdvancedSearch'])
        sleep(2)
        login.input_text(flight['SearchSender'], cad_account['OfficerLoginName'])
        sleep(2)
        login.input_text(flight['SearchReferenceNo'], refno)
        sleep(2)
        login.is_click(flight['SearchScheduleChange'])
        sleep(2)
        login.is_click(flight['SearchButton'])
        sleep(2)

        # step42
        # login.is_click(flight['msg'])
        # sleep(2)

        # step43 Click and download the attachment

        # step44
        # assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div[1]/div/div/form/div[1]/div[2]/div/div/span").text == 'Approved'
        # sleep(2)

        # step45
        # 跳转到/View/FlightSchedule页面
        # login.get_url(ini.url + "#/View/FlightSchedule")
        # drivers.implicitly_wait(30)
        #
        # login.is_click(flight['FixedWing'])
        # sleep(2)
        # login.is_click(flight['DateFrom'])
        # sleep(2)
        # login.input_text(flight['DateFrom'], flightvalue['From'])
        # sleep(2)
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[5]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.is_click(flight['DateTo'])
        # sleep(2)
        # login.input_text(flight['DateTo'], flightvalue['To'])
        # sleep(2)
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[5]/div/div/div/div[2]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.is_click(flight['CharterCargo'])
        # sleep(2)
        # login.is_click(flight['Ferry'])
        # sleep(2)
        #
        # # step46
        # login.is_click(flight['SearchBtn'])
        # sleep(5)

        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight['Logout_Yes'])

        current_path = os.path.abspath(__file__)
        # 清空文件内容
        # '该文件夹下所有的文件（包括文件夹）'
        file_path = os.path.dirname(current_path) + '/TestData/Out'
        FileList = os.listdir(file_path)
        # '遍历所有文件'
        for files in FileList:
            files = os.path.join(file_path, files)
            # 清空文件内容
            with open(files, 'a+') as f:
                f.truncate(0)


if __name__ == '__main__':
    pytest.main(['TestCase/test_tc_e2e_083_4.py'])