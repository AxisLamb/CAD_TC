import datetime
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

    @allure.story("Create application by Local Operator")
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

        # 跳转到/ApplicationView/ScheduleChange/FlightSchedule页面
        login.get_url(ini.url + "#/ApplicationView/ScheduleChange/FlightSchedule")
        drivers.implicitly_wait(30)

        # 获取查询数据
        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path) + '/TestData/Out/FlightNo.txt'
        # 如果filename不存在会自动创建， r以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
        with open(filename, 'r') as f:
            for num, line in enumerate(f):
                if num == 0:
                    flightNo1 = line.rstrip()
                    print(flightNo1)
                if num == 2:
                    flightNo2 = line.rstrip()
                    print(flightNo2)
                if num == 4:
                    flightNo3 = line.rstrip()
                    print(flightNo3)
                if num == 6:
                    flightNo4 = line.rstrip()
                    print(flightNo4)

        # step1
        login.input_text(flight['FlightNo/CallSign'], flightNo1)
        sleep(2)
        login.input_text(flight['EffectivePeriodFrom'], flightvalue['From'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['EffectivePeriodTo'], flightvalue['To'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input").send_keys(Keys.ENTER)
        sleep(3)
        login.is_click(flight['ApplicationType_CharterAllCargo'])
        sleep(3)
        login.is_click(flight['DisplayByPeriod'])
        sleep(3)
        login.is_click(flight['Search'])
        sleep(10)

        # step2
        login.is_click(flight['CheckBox'])
        sleep(3)
        login.is_click(flight['Revise'])
        sleep(3)

        # step3
        login.is_click(flight['ChangeDop1'])
        sleep(2)
        login.is_click(flight['ChangeDop3'])
        sleep(2)
        login.is_click(flight['ChangeDop5'])
        sleep(2)
        login.is_click(flight['ChangeDop7'])
        sleep(2)
        login.input_text(flight['ChangeSTD1'], flightvalue['ST1530'])
        sleep(2)
        login.input_text(flight['ChangeSTA2'], flightvalue['ST0830'])
        sleep(5)
        # login.is_click(flight['Belly1'])
        # sleep(5)
        # login.is_click(flight['Carriage1'])
        # sleep(2)
        # login.is_click(flight['Carriage2'])
        # sleep(2)
        # login.is_click(flight['PCCL2'])
        # sleep(2)

        # step4
        login.is_click(flight['ChangeSave'])
        sleep(5)

        # step5
        login.input_text(flight['FlightNo/CallSign'], flightNo2)
        sleep(2)
        login.is_click(flight['Search'])
        sleep(5)

        # step6
        login.is_click(flight['CheckBox'])
        sleep(2)
        login.is_click(flight['Revise'])
        sleep(2)

        # step7
        login.input_text(flight['ChangeFrom'], "08/07/2023")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['ChangeTo'], "15/07/2023")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/span/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['ChangeSTD1'], flightvalue['ST1930'])
        sleep(2)
        login.input_text(flight['ChangeSTA2'], flightvalue['ST1030'])
        sleep(2)

        # step8
        login.is_click(flight['ChangeSave'])
        sleep(5)

        # step9
        login.input_text(flight['FlightNo/CallSign'], flightNo3)
        sleep(2)
        login.is_click(flight['Search'])
        sleep(5)

        # step10
        login.is_click(flight['CheckBox'])
        sleep(2)
        login.is_click(flight['Revise'])
        sleep(2)

        # step11
        login.input_text(flight['ChangeSTA1'], flightvalue['ST0830'])
        sleep(2)
        login.input_text(flight['ChangeSTD2'], flightvalue['ST1930'])
        sleep(2)
        # login.is_click(flight['Belly1'])
        # sleep(2)
        # login.is_click(flight['Belly2'])
        # sleep(2)

        # step12
        login.is_click(flight['ChangeSave'])
        sleep(5)

        # step13
        login.input_text(flight['FlightNo/CallSign'], flightNo4)
        sleep(2)
        login.input_text(flight['EffectivePeriodTo'], flightvalue['From'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['DisplayByDay'])
        sleep(2)
        login.is_click(flight['Search'])
        sleep(50)

        # step14
        login.is_click(flight['CheckBox'])
        sleep(2)
        login.is_click(flight['Revise'])
        sleep(2)

        # step15
        login.input_text(flight['ChangeSTD1'], flightvalue['ST1630'])
        sleep(2)
        login.input_text(flight['ChangeSTA2'], flightvalue['ST1030'])
        sleep(2)
        # login.is_click(flight['Carriage1'])
        # sleep(2)
        # login.is_click(flight['Carriage2'])
        # sleep(2)

        # step16
        login.is_click(flight['ChangeSave'])
        sleep(60)

        # step17
        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        sleep(2)
        login.is_click(flight['SelectDoc'])
        sleep(2)
        # login.is_click(flight['SelectDocType'])
        # sleep(2)
        # login.input_text(flight['SelectDocType'], "Aerodrome Operating Minima")
        # sleep(2)
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[14]/div/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.is_click(flight['SelectDocSearch'])
        # sleep(2)
        login.is_click(flight['SelectDocCheckBox'])
        sleep(2)
        login.is_click(flight['SelectDocConfirm'])
        sleep(2)

        login.is_click(flight['UploadDoc'])
        sleep(2)
        login.is_click(flight['UploadDocType'])
        sleep(2)
        login.input_text(flight['UploadDocType'], flightvalue['DocType'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestData/In/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight['UploadExpiryDate'], flightvalue['ClickDate'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['Upload'])
        sleep(2)

        # step18
        login.is_click(flight['SaveAsDraft'])
        sleep(5)

        # step19
        login.is_click(flight['PreviewAndSubmit2'])
        sleep(5)

        # step20
        login.is_click(flight['Submit2'])
        sleep(5)
        login.is_click(flight['Submit2_ok'])
        sleep(2)

        date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
        login.is_click(flight['ClickScheduleChange'])
        sleep(2)
        login.input_text(flight['SubmittedTo'], date)
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[7]/div[1]/div/div/div[2]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['SearchMsg'])
        sleep(2)

        refNo = drivers.find_element_by_xpath("//*[@id='testRefNo00']").text
        filename = os.path.dirname(current_path) + '/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        with open(filename, 'w') as f:
            f.write(refNo)

        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight['Logout_Yes'])


if __name__ == '__main__':
    pytest.main(['TestCase/test_tc_e2e_083_2.py'])