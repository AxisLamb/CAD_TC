import os
import pytest
import allure
from selenium.webdriver.common.keys import Keys
import string
import random
from random import randint
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('flight_040')
flightvalue = ElementValue('flightvalue_040')
accountValue = ElementValue('cad_account')
@allure.feature("TC(ECE)-040 ")
class TestCreateTrafficRules:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Maintain Traffic Right Rules")
    def test_040(self, drivers):
        print(flight['Step02_Countries'])
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
          login.is_click(flight["Logout"])
          login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(accountValue['OfficerLoginName'])
            login.input_user_password(accountValue['OfficerPassword'])
            login.click_login_button()
            sleep(10)

        # # step 01
        '''跳转到#/Misc/MaintainAirTraffic/MaintainPort页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainPort")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step01_New'])
        sleep(2)
        login.is_click(flight['Step01_Ports'])
        sleep(5)
        login.is_click(flight['Step01_Advanced'])
        sleep(2)
        login.input_text(flight['Step01_Airport_Code'], flightvalue['Step01_Airport_Code'])
        sleep(1)
        login.is_click(flight['Step01_Search'])
        sleep(3)
        login.is_click(flight['Step01_Click_Port'])
        sleep(2)
        login.input_text(flight['Step01_Description'], flightvalue['Step01_Description'])
        sleep(1)
        login.is_click(flight['Step01_Save'])
        sleep(2)
        login.is_click(flight['Step01_Sort'])
        sleep(2)
        login.is_click(flight['Step01_Sort'])
        sleep(1)
        login.is_click(flight['Step01_Preview'])
        sleep(5)
        login.is_click(flight['Step01_Preview_Close'])
        sleep(2)

        # step 02
        login.is_click(flight['Step02_New'])
        sleep(2)
        login.is_click(flight['Step02_Countries'])
        sleep(5)
        login.is_click(flight['Step02_Advanced'])
        sleep(2)
        login.input_text(flight['Step02_English_Description'], flightvalue['Step02_English_Description'])
        sleep(1)
        login.is_click(flight['Step02_Search'])
        sleep(2)
        login.is_click(flight['Step02_Click_Country'])
        sleep(2)
        login.input_text(flight['Step02_Description'], flightvalue['Step02_Description'])
        sleep(1)
        login.is_click(flight['Step02_Save'])
        sleep(2)
        login.is_click(flight['Step02_Sort'])
        sleep(2)
        login.is_click(flight['Step02_Sort'])
        sleep(1)
        login.is_click(flight['Step02_Preview'])
        sleep(5)
        login.is_click(flight['Step02_Preview_Close'])
        sleep(2)

        # step 03
        '''跳转到#/Misc/MaintainAirTraffic/MaintainRuleSets页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainRuleSets")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step03_New'])
        sleep(2)
        login.is_click(flight['Step03_Country_Select'])
        login.input_text(flight['Step03_Country_Input'], "Hong Kong (SAR, China)")
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[2]/div/div/div/div/input").send_keys(
            Keys.ENTER)
        sleep(2)
        login.is_click(flight['Step03_Type_Select'])
        login.input_text(flight['Step03_Type_Input'], flightvalue['Step01_TypeValue'])
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[3]/div/div[2]/form/div/div[4]/div/div/div/div/input").send_keys(
            Keys.ENTER)
        sleep(2)
        login.input_text(flight['Step03_Remarks'], "Rule for Hong Kong")
        sleep(2)
        login.is_click(flight['Step03_Save'])

        # step 04
        sleep(2)
        login.is_click(flight['Step04_RuleSort'])
        sleep(2)
        login.is_click(flight['Step04_Select'])
        sleep(2)
        login.is_click(flight['Step04_Configure_Route_Definition'])
        sleep(2)

        login.is_click(flight['Step04_HomePorts'])
        sleep(2)
        login.is_click(flight['Step04_HomePorts_Last_Updated_Sort'])
        sleep(2)
        login.is_click(flight['Step04_HomePorts_Click'])
        sleep(2)
        login.is_click(flight['Step04_ForeignPorts'])
        sleep(2)
        # login.is_click(flight['Step04_ForeignPorts_Last_Updated_Sort'])
        login.is_click(flight['Step04_ForeignPorts_Click'])
        sleep(2)
        login.input_text(flight['Step04_Description'], flightvalue['Step04_Description'])
        sleep(1)
        login.input_text(flight['Step04_Remarks'], flightvalue['Step04_Remarks'])
        sleep(1)
        login.is_click(flight['Step04_Save'])
        sleep(2)

        # # step 05
        '''跳转到#/Misc/MaintainAirTraffic/MaintainEntitlement页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainEntitlement")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step05_New'])
        sleep(2)
        login.is_click(flight['Step05_Frequency_Click'])
        sleep(2)
        login.input_text(flight['Step05_Frequency'], "5")
        sleep(1)
        # login.is_click(flight['Step05_Passenger_Limit_Click'])
        # login.input_text(flight['Step05_Passenger_Limit'], "500")
        # login.is_click(flight['Step05_Per_Flight_Passenger_Limit_Click'])
        # login.input_text(flight['Step05_Per_Flight_Passenger_Limit'], "100")
        login.is_click(flight['Step05_Cargo_limit_Click'])
        sleep(2)
        login.input_text(flight['Step05_Cargo_limit'], "50000")
        sleep(1)
        login.input_text(flight['Step05_Load_Factor'], "50")
        sleep(1)
        login.input_text(flight['Step05_Description'], "W:5 Cargo:  PL:50000 PP: 10000")
        sleep(1)
        login.input_text(flight['Step05_Remarks'], "UAT Testing")
        sleep(1)
        login.is_click(flight['Step05_Save'])
        sleep(2)

        # step 06
        '''跳转到#/Misc/MaintainAirTraffic/MaintainAssociations页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/MaintainAssociations")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step06_New'])
        sleep(2)
        login.is_click(flight['Step06_Traffic_Route_Id_Click'])
        sleep(2)
        login.is_click(flight['Step06_Traffic_Route_Id'])
        sleep(2)
        login.is_click(flight['Step06_Entitlement_Id_Click'])
        sleep(2)
        login.is_click(flight['Step06_Entitlement_Id'])
        sleep(2)
        login.is_click(flight['Step06_Entitlement_Id_Button'])
        sleep(2)
        login.input_text(flight['Step06_Remarks'], "UAT Testing")
        sleep(1)
        login.is_click(flight['Step06_Save'])
        sleep(2)


        # step 07
        '''跳转到#/Misc/MaintainAirTraffic/RuleLogic页面'''
        login.get_url(ini.url + "#/Misc/MaintainAirTraffic/RuleLogic")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step07_Rule_Set_ID'])
        sleep(2)
        login.is_click(flight['Step07_Rule_Set'])
        sleep(2)

        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01_Click'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01_Entitlements'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel01_Entitlements_Click'])
        sleep(2)

        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel02'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel02_Click'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel02_Entitlements'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel02_Entitlements_Click'])
        sleep(2)

        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel03'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel03_Click'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel03_Entitlements'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel03_Entitlements_Click'])
        sleep(2)

        login.is_click(flight['Step07_ADD_MORE_CONDITIONS'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel04'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel04_Click'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel04_Entitlements'])
        sleep(2)
        login.is_click(flight['Step07_RuleLabel04_Entitlements_Click'])
        sleep(2)

        login.is_click(flight['Step07_True_Response'])
        sleep(1)
        login.input_text(flight['Step07_Response_Input'], flightvalue['Step07_True_Response_Input'])
        sleep(1)
        login.is_click(flight['Step07_Response_Save'])
        sleep(2)
        login.is_click(flight['Step07_False_Response'])
        sleep(1)
        login.input_text(flight['Step07_Response_Input'], flightvalue['Step07_False_Response_Input'])
        sleep(1)
        login.is_click(flight['Step07_Response_Save'])
        sleep(2)
        login.is_click(flight['Step07_Save'])

        sleep(2)
        # step 08
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(accountValue['CpaOfficerLoginName'])
        login.input_user_password(accountValue['CpaOfficerPassword'])
        login.click_login_button()
        drivers.implicitly_wait(30)
        sleep(10)
        '''跳转到#/ApplicationView/CharterFlight/CreateCharterFlightCargo页面'''
        login.get_url(ini.url + "#/ApplicationView/CharterFlight/CreateCharterFlightCargo")
        drivers.implicitly_wait(30)
        sleep(5)
        login.input_text(flight['Step08_RegistrationMark'], flightvalue['Step08_RegistrationMark'])
        login.is_click(flight['Step08_LeaveAirCheckbox'])
        login.is_click(flight['Step08_AircraftType'])
        sleep(2)
        login.input_text(flight['Step08_AircraftTypeInput'], flightvalue['Step08_AircraftTypeInput'])
        drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div[1]/div/div[5]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['Step08_AircraftNationality'])
        sleep(2)
        login.input_text(flight['Step08_AircraftNationaInput'], flightvalue['Step08_AircraftNationaInput'])
        drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div[1]/div/div[5]/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['Step08_NumberOfCharterer'], flightvalue['Step08_NumberOfCharterer'])
        login.input_text(flight['Step08_AddressOfCharterer'], flightvalue['Step08_AddressOfCharterer'])
        login.is_click(flight['Step08_LocalHandingAgent'])
        sleep(2)
        login.input_text(flight['Step08_LocalHandingAgentInput'], flightvalue['Step08_LocalHandingAgentInput'])
        drivers.find_element_by_xpath(
            "/html/body/div[1]/div/div/section/div/form/div[1]/div/div[8]/div/div/div[1]/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step08_PurpostOfService'], flightvalue['Step08_PurpostOfService'])
        login.input_text(flight['Step08_PointsOfLanding'], flightvalue['Step08_PointsOfLanding'])
        sleep(2)

        #表单
        s = string.ascii_letters
        r = random.choice(s)
        # 航班号用CPA+4位整数和一个随机字母
        Flight_1 = "CPA" + str(randint(1000, 9999)) + r
        Flight_2 = "CPA" + str(randint(1000, 9999)) + r

        login.is_click(flight['Step08_Lint1ServiceType'])
        sleep(1)
        login.input_text(flight['Step08_Lint1ServiceTypeInput'], flightvalue['Step08_Lint1ServiceTypeInput'])
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[2]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step08_Lint1FlightNO'], Flight_1)

        login.input_text(flight['Step08_Lint1From'], flightvalue['Step08_Lint1From'])
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.input_text(flight['Step08_Lint1To'], flightvalue['Step08_Lint1To'])
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[6]/div/span/div/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.is_click(flight['Step08_Lint1Dop1'])
        login.is_click(flight['Step08_Lint1Dop3'])
        login.is_click(flight['Step08_Lint1Dop5'])

        login.input_text(flight['Step08_Lint1CargoKg'], flightvalue['Step08_Lint1CargoKg'])
        login.input_text(flight['Step08_Lint1RouteFrom'], flightvalue['Step08_Lint1RouteFrom'])
        login.input_text(flight['Step08_Lint1RouteTo'], flightvalue['Step08_Lint1RouteTo'])
        login.input_text(flight['Step08_Lint1Std'], flightvalue['Step08_Lint1Std'])

        login.is_click(flight['Step08_Lint2ServiceType'])
        login.input_text(flight['Step08_Lint2ServiceTypeInput'], flightvalue['Step08_Lint2ServiceTypeInput'])
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[1]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.input_text(flight['Step08_Lint2FlightNO'], Flight_2)
        login.is_click(flight['Step08_Lint2InOut'])
        sleep(1)
        login.input_text(flight['Step08_Lint2InOutInput'], flightvalue['Step08_Lint2InOutInput'])
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[3]/div/div/div/input").send_keys(
            Keys.ENTER)
        sleep(1)
        login.input_text(flight['Step08_Lint2CargoKg'], flightvalue['Step08_Lint2CargoKg'])
        login.input_text(flight['Step08_Lint2RouteFrom'], flightvalue['Step08_Lint2RouteFrom'])
        login.input_text(flight['Step08_Lint2RouteTo'], flightvalue['Step08_Lint2RouteTo'])
        login.input_text(flight['Step08_Lint2Sta'], flightvalue['Step08_Lint2Sta'])

        login.input_text(flight['Step08_Remarks'], flightvalue['Step08_Remarks'])
        sleep(1)
        login.is_click(flight['Step08_UploadRelateDocumentButton'])
        sleep(2)
        login.is_click(flight['Step08_UploadRelateDocumentType'])
        login.input_text(flight['Step08_UploadRelateDocumentInput'], "Others")
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']").send_keys(
            Keys.ENTER)
        sleep(2)
        # login.is_click(flight['Step08_UploadRelateDocumentSelect'])
        # sleep(1)
        # login.is_click(flight['Step08_UploadRelateDocumentBrowse'])
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(1)
        login.input_text(flight['Step08_UploadRelateDocumentExDate'], flightvalue['Step08_UploadRelateDocumentExDate'])
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight['Step08_UploadRelateDocumentUpload'])
        sleep(1)
        assert drivers.find_element_by_xpath(
            "//table/tbody/tr/td[contains(div,'other_supports.pdf')]/div").text == "other_supports.pdf"
        sleep(1)
        login.is_click(flight['Step08_ConfirmCheckbox'])

        sleep(2)
        login.is_click(flight['Step09_PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['Step10_Submit'])
        sleep(2)

        warning=""
        try:
            warning=login.element_text(flight['Step11_Warning'])
        except Exception:
            print("upload file normal")

        print(warning)
        if warning == "Do you wish to proceed with your application submission?":
            login.is_click(flight['Step11_Proceed'])
        sleep(2)

        # try:
        #     login.input_text(flight['Step11_NewCodeDesc'],"test code")
        #     login.is_click(flight['Step11_Save'])
        # except Exception:
        #     print("not a new code")
        #
        # sleep(2)
        login.is_click(flight['Step11_No'])
        sleep(10)



        # step 12
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(accountValue['OfficerLoginName'])
        login.input_user_password(accountValue['OfficerPassword'])
        login.click_login_button()
        sleep(10)
        '''跳转到#/View/Messages页面'''
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        login.is_click(flight['Step12_Advanced_Search'])
        login.input_text(flight['Step12_Sender'], accountValue['CpaOfficerLoginName'])
        login.is_click(flight['Step12_Charter_All_Cargo'])
        login.is_click(flight['Step12_Search'])
        sleep(2)

        # step 13
        login.is_click(flight['Step13_Open_Message'])
        sleep(2)

        # step 14
        login.is_click(flight['Step14_Message_Ref_No'])
        sleep(6)

        # step 15
        login.is_click(flight['Step15_Select_Record'])
        # login.is_click(flight['Step15_Check_Traffic_Rights'])
        # sleep(2)
        # login.is_click(flight['Step15_Import_Data_No'])
        sleep(3)

        # step 16
        # login.is_click(flight['Step15_Traffic_Rights_Export'])
        # sleep(3)
        # login.is_click(flight['Step15_Exit'])
        # sleep(3)
        # login.is_click(flight['Step15_Export'])
        # appp = pywinauto.Desktop()
        # # 选择文件上传的窗口
        # dlgg = appp["另存为"]
        # sleep(2)
        # dlgg["保存(&S)"].click_input()
        # sleep(2)
        # login.is_click(flight['Step15_Select_Record'])

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        drivers.implicitly_wait(30)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_040/test_e2e_040.py'])