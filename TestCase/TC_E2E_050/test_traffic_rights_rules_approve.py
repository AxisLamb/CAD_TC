import allure
import pytest
import os
from selenium.webdriver.common.keys import Keys
from page_object.LoginPage import LoginPage
from common.readconfig import ini
from page.webpage import sleep
from common.readvalue import ElementValue
from common.readelement import Element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import string
from random import randint

flight = Element('flight_050')
flightvalue = ElementValue('flightvalue_050')
cad_account = ElementValue('cad_account')
@allure.feature("TC(ECE)-050 Officer Create traffic rights rules and check traffic rights in Extra Section Passenger Application")
class TestTrafficRightsRulesApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Officer Create traffic rights rules and check traffic rights in Extra Section Passenger Application")
    def test_050(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['OfficerLoginName'])
            login.input_user_password(cad_account['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到/Misc/MaintainAirTraffic/MaintainPort页面
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainPort")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Maintain Port Sets"
        sleep(1)

        # step1
        login.is_click(flight['New'])
        sleep(1)
        login.is_click(flight['Ports'])
        sleep(1)
        login.is_click(flight['Advanced_Search_Ports'])
        sleep(3)
        login.input_text(flight['Advanced_Search_Ports_IATA'], flightvalue['Advanced_Search_IATA'])
        sleep(3)
        login.is_click(flight['Search'])
        sleep(3)
        login.is_click(flight['Ports_HKG'])
        sleep(3)
        login.input_text(flight['Description'], flightvalue['Port_Description'])
        sleep(1)
        login.is_click(flight['Save'])
        sleep(2)
        login.is_click(flight['Preview'])
        sleep(2)
        login.is_click(flight['Preview_Close'])
        sleep(2)

        # step2
        login.is_click(flight['New'])
        sleep(1)
        login.is_click(flight['Countries'])
        sleep(1)
        login.is_click(flight['Advanced_Search_Country'])
        sleep(3)
        login.input_text(flight['Advanced_Search_Country_English'], flightvalue['Advanced_Search_Country_English'])
        sleep(3)
        login.is_click(flight['Search_Country'])
        sleep(3)
        login.is_click(flight['Country_Singapore'])
        sleep(3)
        login.input_text(flight['Description'], flightvalue['Country_Description'])
        sleep(1)
        login.is_click(flight['Save'])
        sleep(2)
        login.is_click(flight['Preview'])
        sleep(2)
        login.is_click(flight['Preview_Close'])
        sleep(2)

        # step3
        # 跳转到/Misc/MaintainAirTraffic/MaintainRuleSets页面
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainRuleSets")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Maintain Traffic Rights Rule Sets"
        sleep(1)
        login.is_click(flight['Rule_New'])
        sleep(2)
        login.is_click(flight['Country_Name_Select'])
        login.input_text(flight['Country_Name_Input'], flightvalue['Country_Name_Input'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['Type_Select'])
        login.input_text(flight['Type_Input'], flightvalue['Type_Input'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[4]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        sleep(1)
        login.is_click(flight['Rule_Save'])

        # step4
        login.is_click(flight['CheckBox'])
        sleep(1)
        login.is_click(flight['ConfigureRouteDefinition'])
        sleep(2)
        login.is_click(flight['HomePorts'])
        sleep(3)
        login.is_click(flight['HomePorts_select'])
        sleep(3)
        login.is_click(flight['ForeignPorts'])
        sleep(3)
        login.is_click(flight['ForeignPorts_select'])
        sleep(3)
        login.input_text(flight['ConfigureRouteDefinition_Description'], flightvalue['ConfigureRouteDefinition_Description'])
        sleep(1)
        login.input_text(flight['ConfigureRouteDefinition_Remarks'], flightvalue['ConfigureRouteDefinition_Remarks'])
        sleep(1)
        login.is_click(flight['ConfigureRouteDefinition_Save'])
        sleep(2)

        # step5
        # 跳转到/Misc/MaintainAirTraffic/MaintainEntitlement页面
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainEntitlement")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Maintain Route Entitlements"
        sleep(1)
        login.is_click(flight['Entitlements_New'])
        sleep(1)
        login.is_click(flight['Frequency_select'])
        login.input_text(flight['Frequency_input'], flightvalue['Frequency_input'])
        sleep(2)
        login.is_click(flight['AdditionalFrequencyIndicator'])
        sleep(1)
        login.is_click(flight['PassengerLimit_select'])
        login.input_text(flight['PassengerLimit_input'], flightvalue['PassengerLimit_input'])
        sleep(2)
        login.is_click(flight['PerFlightPassenger_select'])
        login.input_text(flight['PerFlightPassenger_input'], flightvalue['PerFlightPassenger_input'])
        sleep(2)
        login.input_text(flight['LoadFactor'], flightvalue['LoadFactor'])
        sleep(1)
        login.input_text(flight['Entitlements_Description'], flightvalue['Entitlements_Description'])
        sleep(1)
        login.input_text(flight['Entitlements_Remarks'], flightvalue['Entitlements_Remarks'])
        sleep(1)
        login.is_click(flight['Entitlements_Save'])
        sleep(2)

        # step6
        # 跳转到/Misc/MaintainAirTraffic/MaintainAssociations页面
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainAssociations")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Maintain Route Entitlements Associations"
        sleep(1)
        login.is_click(flight['Associations_New'])
        sleep(1)
        login.is_click(flight['TrafficRouteID_button'])
        sleep(1)
        login.is_click(flight['TrafficRouteID_select'])
        sleep(1)
        login.is_click(flight['EntitlementID_button'])
        sleep(1)
        login.is_click(flight['EntitlementID_checkbox'])
        sleep(1)
        login.is_click(flight['EntitlementID_Add'])
        sleep(1)
        login.input_text(flight['Associations_Remarks'], flightvalue['Associations_Remarks'])
        sleep(1)
        login.is_click(flight['Associations_Save'])
        sleep(2)

        # step7
        # 跳转到/Misc/MaintainAirTraffic/RuleLogic
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/RuleLogic")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Rules Logic"
        sleep(1)
        login.is_click(flight['RuleLogic_setId'])
        sleep(1)
        login.is_click(flight['RuleLogic_set'])
        sleep(1)
        login.is_click(flight['RuleLogic_AddMoreCondition'])
        sleep(1)
        login.is_click(flight['RuleLabel01'])
        login.is_click(flight['RuleLabel01_Click'])
        login.is_click(flight['RuleLabel01_Entitlements'])
        login.is_click(flight['RuleLabel01_Entitlements_Click'])
        login.is_click(flight['RuleLabel01_True_Mag'])
        login.input_text(flight['RuleLabel01_True_Res'], flightvalue['RuleLabel01_True_Res'])
        sleep(2)
        login.is_click(flight['RuleLabel01_True_Save'])
        login.is_click(flight['RuleLabel01_False_Mag'])
        login.input_text(flight['RuleLabel01_False_Res'], flightvalue['RuleLabel01_False_Res'])
        sleep(2)
        login.is_click(flight['RuleLabel01_False_Save'])
        sleep(2)
        login.is_click(flight['RuleLogic_AddMoreCondition'])
        login.is_click(flight['RuleLabel02'])
        login.is_click(flight['RuleLabel02_Click'])
        login.is_click(flight['RuleLabel02_Entitlements'])
        login.is_click(flight['RuleLabel02_Entitlements_Click'])
        login.is_click(flight['RuleLabel02_True_Mag'])
        login.input_text(flight['RuleLabel02_True_Res'], flightvalue['RuleLabel02_True_Res'])
        sleep(2)
        login.is_click(flight['RuleLabel02_True_Save'])
        login.is_click(flight['RuleLabel02_False_Mag'])
        login.input_text(flight['RuleLabel02_False_Res'], flightvalue['RuleLabel02_False_Res'])
        sleep(2)
        login.is_click(flight['RuleLabel02_False_Save'])
        sleep(2)
        login.is_click(flight['RuleLogic_AddMoreCondition'])
        login.is_click(flight['RuleLabel03'])
        login.is_click(flight['RuleLabel03_Click'])
        login.is_click(flight['RuleLabel03_Entitlements'])
        login.is_click(flight['RuleLabel03_Entitlements_Click'])
        login.is_click(flight['RuleLabel03_True_Mag'])
        login.input_text(flight['RuleLabel03_True_Res'], flightvalue['RuleLabel03_True_Res'])
        sleep(2)
        login.is_click(flight['RuleLabel03_True_Save'])
        login.is_click(flight['RuleLabel03_False_Mag'])
        login.input_text(flight['RuleLabel03_False_Res'], flightvalue['RuleLabel03_False_Res'])
        sleep(2)
        login.is_click(flight['RuleLabel03_False_Save'])
        sleep(2)
        login.is_click(flight['RuleLogic_AddMoreCondition'])
        login.is_click(flight['RuleLabel04'])
        login.is_click(flight['RuleLabel04_Click'])
        login.is_click(flight['RuleLabel04_Entitlements'])
        login.is_click(flight['RuleLabel04_Entitlements_Click'])
        login.is_click(flight['RuleLabel04_True_Mag'])
        login.input_text(flight['RuleLabel04_True_Res'], flightvalue['RuleLabel04_True_Res'])
        sleep(2)
        login.is_click(flight['RuleLabel04_True_Save'])
        login.is_click(flight['RuleLabel04_False_Mag'])
        login.input_text(flight['RuleLabel04_False_Res'], flightvalue['RuleLabel04_False_Res'])
        sleep(2)
        login.is_click(flight['RuleLabel04_False_Save'])
        sleep(2)
        login.is_click(flight['True_Res'])
        login.input_text(flight['True_msg'], flightvalue['True_msg'])
        sleep(2)
        login.is_click(flight['True_Save'])
        login.is_click(flight['False_Res'])
        login.input_text(flight['False_msg'], flightvalue['False_msg'])
        sleep(2)
        login.is_click(flight['False_Save'])
        login.is_click(flight['RuleLogic_Save'])

        # step8
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['CpaOfficerLoginName'])
            login.input_user_password(cad_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到/ApplicationView/ExtraSection/CreateExtraSectionPassenger
        login.get_url(ini.url + "#/ApplicationView/ExtraSection/CreateExtraSectionPassenger")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Extra Section Passenger Application"
        sleep(1)

        r = random.choice(string.ascii_letters)
        FlightNo1 = "CPA" + str(randint(1, 9999)) + r
        FlightNo2 = "CPA" + str(randint(1, 9999)) + r

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
        # FlightNo2
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
        sleep(1)
        login.input_text(flight['Remarks3'], flightvalue['Remarks3'])
        sleep(1)
        # select doc
        login.is_click(flight['Select_Doc'])
        sleep(1)
        login.is_click(flight['Select_DocType'])
        sleep(1)
        login.input_text(flight['Select_DocType_input'], flightvalue['Select_DocType_input1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight['Select_DocType_input'], flightvalue['Select_DocType_input2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight['Select_Doc_Search'])
        sleep(1)
        login.is_click(flight['Select_Doc_Confirm'])
        sleep(2)
        # upload doc
        login.is_click(flight['Upload_Doc'])
        sleep(1)
        login.is_click(flight['Upload_Doc_Select'])
        login.input_text(flight['Upload_DocType_Input'], flightvalue['Upload_DocType_Input'])
        drivers.find_element_by_xpath("/html/body/div[8]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        # 上传文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight['Upload_Doc_Date'], flightvalue['Upload_Doc_Date'])
        drivers.find_element_by_xpath("/html/body/div[8]/div/div[2]/form/div[5]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['Upload_Doc_Upload'])
        sleep(2)

        # step9
        login.is_click(flight['PreviewAndSubmit_Confirm'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)

        # step10
        login.is_click(flight['Submit'])
        sleep(5)
        drivers.find_element_by_xpath("//button[contains(@class, 'testConfirmButtonClass013')]").click()
        sleep(2)

        # step11
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['OfficerLoginName'])
            login.input_user_password(cad_account['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到/View/Messages
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Messages"
        sleep(1)

        # step12
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        sleep(1)
        login.input_text(flight['ViewMessages_Sender'], cad_account['CpaOfficerLoginName'])
        sleep(1)
        login.is_click(flight['ViewMessages_ApplicationType'])
        sleep(1)
        login.is_click(flight['ViewMessages_Search'])
        sleep(1)

        # step13
        login.is_click(flight['ViewMessages_ApprovedMessage'])
        sleep(2)

        # step14
        login.is_click(flight['ViewMessages_checkbox'])
        sleep(1)
        login.is_click(flight['ViewMessages_CheckTrafficRights'])
        sleep(1)
        login.is_click(flight['ExportTrafficRights'])
        sleep(1)
        login.is_click(flight['ViewMessages_CheckTrafficRights_close'])
        sleep(2)

        # step15
        login.is_click(flight['Export'])
        sleep(2)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/test_traffic_rights_rules_approve.py'])