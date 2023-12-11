import random
import string
from random import randint
import pytest
import allure
import os
from selenium.webdriver.common.keys import Keys
from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

flight_128 = Element('flight_128')
flightvalue_128 = ElementValue('flightvalue_128')
cad_account = ElementValue('cad_account')
@allure.feature("TC(ECE)-128 Local Operator Create and Officer Processing Helicopter (thru Scheduled Passenger) Application with new code (Approve)")
class TestHelicopterSchedulePassengerApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Local Operator Create and Officer Processing Helicopter (thru Scheduled Passenger) Application with new code (Approve)")
    def test_128(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight_128["Logout"])
            login.is_click(flight_128['Logout_Yes'])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['CpaOfficerLoginName'])
            login.input_user_password(cad_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到Application-Seasonal Schedule-passenger页面
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Seasonal Schedule Passenger Application"
        sleep(2)

        r = random.choice(string.ascii_letters)
        FlightNo1 = "CPA" + str(randint(1, 9999)) + r
        FlightNo2 = "CPA" + str(randint(1, 9999)) + r
        FlightNo3 = "CPA" + str(randint(1, 9999)) + r
        FlightNo4 = "CPA" + str(randint(1, 9999)) + r
        FlightNo5 = "CPA" + str(randint(1, 9999)) + r
        FlightNo6 = "CPA" + str(randint(1, 9999)) + r
        FlightNo7 = "CPA" + str(randint(1, 9999)) + r
        FlightNo8 = "CPA" + str(randint(1, 9999)) + r
        TemplateName = "Temp" + str(random.uniform(1, 9999))

        login.is_click(flight_128['Season'])
        login.input_text(flight_128['Season'], flightvalue_128['Season'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[1]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)

        # step1
        login.is_click(flight_128['Helicopter'])
        sleep(2)
        # FlightNo1
        login.input_text(flight_128['FlightNo1'], FlightNo1)
        sleep(1)
        login.input_text(flight_128['From1'], flightvalue_128['From1'])
        sleep(1)
        login.input_text(flight_128['To1'], flightvalue_128['To1'])
        sleep(1)
        login.is_click(flight_128['DOP1_1'])
        sleep(1)
        login.is_click(flight_128['DOP1_3'])
        sleep(1)
        login.is_click(flight_128['DOP1_5'])
        sleep(1)
        login.is_click(flight_128['AircraftType_Select1'])
        sleep(1)
        login.input_text(flight_128['AircraftType_input1'], flightvalue_128['AircraftType_input1'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_128['NoofSeats1'], flightvalue_128['NoofSeats1'])
        sleep(1)
        login.input_text(flight_128['Route1'], flightvalue_128['Route1'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STA1'], flightvalue_128['LocalTime_STA1'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STD1'], flightvalue_128['LocalTime_STD1'])
        sleep(2)
        # FlightNo1_2
        login.input_text(flight_128['FlightNo1_2'], FlightNo2)
        sleep(1)
        login.is_click(flight_128['AircraftType_Select1_2'])
        sleep(1)
        login.input_text(flight_128['AircraftType_input1_2'], flightvalue_128['AircraftType_input1_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_128['NoofSeats1_2'], flightvalue_128['NoofSeats1_2'])
        sleep(1)
        login.input_text(flight_128['Route1_2'], flightvalue_128['Route1_2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STA1_2'], flightvalue_128['LocalTime_STA1_2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STD1_2'], flightvalue_128['LocalTime_STD1_2'])
        sleep(2)

        # FlightNo2
        login.input_text(flight_128['FlightNo2'], FlightNo3)
        sleep(1)
        login.input_text(flight_128['From2'], flightvalue_128['From2'])
        sleep(1)
        login.input_text(flight_128['To2'], flightvalue_128['To2'])
        sleep(1)
        login.is_click(flight_128['DOP2_1'])
        sleep(1)
        login.is_click(flight_128['DOP2_3'])
        sleep(1)
        login.is_click(flight_128['DOP2_5'])
        sleep(1)
        login.is_click(flight_128['DOP2_7'])
        sleep(1)
        login.is_click(flight_128['AircraftType_Select2'])
        sleep(1)
        login.input_text(flight_128['AircraftType_input2'], flightvalue_128['AircraftType_input2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_128['NoofSeats2'], flightvalue_128['NoofSeats2'])
        sleep(1)
        login.input_text(flight_128['Route2'], flightvalue_128['Route2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STA2'], flightvalue_128['LocalTime_STA2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STD2'], flightvalue_128['LocalTime_STD2'])
        sleep(1)
        login.is_click(flight_128['BellyCargoOnly2'])
        sleep(1)
        drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()
        sleep(2)
        # FlightNo2_2
        login.input_text(flight_128['FlightNo2_2'], FlightNo4)
        sleep(1)
        login.is_click(flight_128['AircraftType_Select2_2'])
        sleep(1)
        login.input_text(flight_128['AircraftType_input2_2'], flightvalue_128['AircraftType_input2_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[4]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_128['NoofSeats2_2'], flightvalue_128['NoofSeats2_2'])
        sleep(1)
        login.input_text(flight_128['Route2_2'], flightvalue_128['Route2_2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STA2_2'], flightvalue_128['LocalTime_STA2_2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STD2_2'], flightvalue_128['LocalTime_STD2_2'])
        sleep(1)
        login.is_click(flight_128['BellyCargoOnly2_2'])
        sleep(1)
        drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()
        sleep(2)

        # FlightNo3
        login.input_text(flight_128['FlightNo3'], FlightNo5)
        sleep(1)
        login.input_text(flight_128['From3'], flightvalue_128['From3'])
        sleep(1)
        login.input_text(flight_128['To3'], flightvalue_128['To3'])
        sleep(1)
        login.is_click(flight_128['DOP3_4'])
        sleep(1)
        login.is_click(flight_128['DOP3_6'])
        sleep(1)
        login.is_click(flight_128['DOP3_2'])
        sleep(1)
        login.is_click(flight_128['AircraftType_Select3'])
        sleep(1)
        login.input_text(flight_128['AircraftType_input3'], flightvalue_128['AircraftType_input3'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_128['NoofSeats3'], flightvalue_128['NoofSeats3'])
        sleep(1)
        login.input_text(flight_128['Route3'], flightvalue_128['Route3'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STA3'], flightvalue_128['LocalTime_STA3'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STD3'], flightvalue_128['LocalTime_STD3'])
        sleep(2)
        # FlightNo3_2
        login.input_text(flight_128['FlightNo3_2'], FlightNo6)
        sleep(1)
        login.is_click(flight_128['FlightDiff_Select3_2'])
        sleep(1)
        login.input_text(flight_128['FlightDiff_Input3_2'], flightvalue_128['FlightDiff_Input3_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight_128['AircraftType_Select3_2'])
        sleep(1)
        login.input_text(flight_128['AircraftType_input3_2'], flightvalue_128['AircraftType_input3_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_128['NoofSeats3_2'], flightvalue_128['NoofSeats3_2'])
        sleep(1)
        login.input_text(flight_128['Route3_2'], flightvalue_128['Route3_2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STA3_2'], flightvalue_128['LocalTime_STA3_2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STD3_2'], flightvalue_128['LocalTime_STD3_2'])
        sleep(2)

        # FlightNo4
        login.input_text(flight_128['FlightNo4'], FlightNo7)
        sleep(1)
        login.input_text(flight_128['From4'], flightvalue_128['From4'])
        sleep(1)
        login.input_text(flight_128['To4'], flightvalue_128['To4'])
        sleep(1)
        login.is_click(flight_128['DOP4_1'])
        sleep(1)
        login.is_click(flight_128['DOP4_3'])
        sleep(1)
        login.is_click(flight_128['DOP4_5'])
        sleep(1)
        login.is_click(flight_128['AircraftType_Select4'])
        sleep(1)
        login.input_text(flight_128['AircraftType_input4'], flightvalue_128['AircraftType_input4'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_128['NoofSeats4'], flightvalue_128['NoofSeats4'])
        sleep(1)
        login.input_text(flight_128['Route4'], flightvalue_128['Route4'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STA4'], flightvalue_128['LocalTime_STA4'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STD4'], flightvalue_128['LocalTime_STD4'])
        sleep(2)
        # FlightNo4_2
        login.input_text(flight_128['FlightNo4_2'], FlightNo8)
        sleep(1)
        login.is_click(flight_128['AircraftType_Select4_2'])
        sleep(1)
        login.input_text(flight_128['AircraftType_input4_2'], flightvalue_128['AircraftType_input4_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[8]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_128['NoofSeats4_2'], flightvalue_128['NoofSeats4_2'])
        sleep(1)
        login.input_text(flight_128['Route4_2'], flightvalue_128['Route4_2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STA4_2'], flightvalue_128['LocalTime_STA4_2'])
        sleep(1)
        login.input_text(flight_128['LocalTime_STD4_2'], flightvalue_128['LocalTime_STD4_2'])
        sleep(2)

        login.input_text(flight_128['Remarks'], flightvalue_128['Remarks'])
        sleep(2)

        # 选择文件
        login.is_click(flight_128['SelectDoc'])
        sleep(2)
        login.input_text(flight_128['DocType_input'], flightvalue_128['DocType_input1'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight_128['DocType_input'], flightvalue_128['DocType_input2'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight_128['Doc_search'])
        sleep(2)
        login.is_click(flight_128['Doc_confirm'])
        sleep(2)

        # 上传文件
        login.is_click(flight_128['UploadDoc'])
        sleep(2)
        login.is_click(flight_128['UploadDoc_input_others'])
        sleep(2)
        login.input_text(flight_128['UploadDoc_input_others'], flightvalue_128['UploadDoc_input_others'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # login.is_click(flight_128['BrowseButton'])
        sleep(2)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight_128['ExpiryDate'], flightvalue_128['ExpiryDate'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight_128['UploadButton'])
        sleep(2)
        assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[2]/div").text == "other_supports.pdf"
        sleep(2)

        # step2
        login.is_click(flight_128['SaveAsDraft'])
        sleep(2)
        assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'
        sleep(2)

        # step3
        login.is_click(flight_128['SaveAsTemplate'])
        sleep(2)
        login.input_text(flight_128['TempName'], TemplateName)
        sleep(2)
        login.input_text(flight_128['Description'], flightvalue_128['Description'])
        sleep(2)
        login.is_click(flight_128['Template_Save'])
        sleep(2)
        login.is_click(flight_128['Confirm'])
        sleep(2)

        # step4
        login.is_click(flight_128['PreviewAndSubmit'])
        sleep(2)

        # step5 Print

        # step6
        login.is_click(flight_128['BackAndModify'])
        sleep(2)
        login.is_click(flight_128['PreviewAndSubmit'])
        sleep(2)

        # step7
        login.is_click(flight_128['Submit'])
        sleep(2)
        drivers.find_element_by_xpath("//button[contains(@class, 'testConfirmButtonClass016')]").click()
        sleep(2)

        # step8

        # step9
        login.is_click(flight_128['LessorOperator_select'])
        sleep(2)
        login.input_text(flight_128['LessorOperator_input'], flightvalue_128['LessorOperator_input'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight_128['LessorOperator_PeriodFrom'], flightvalue_128['LessorOperator_PeriodFrom'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight_128['LessorOperator_PeriodTo'], flightvalue_128['LessorOperator_PeriodTo'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight_128['LessorOperator_AddDoc'])
        sleep(2)
        login.is_click(flight_128['LessorOperator_Support_DocType_select'])
        sleep(2)
        login.input_text(flight_128['LessorOperator_Support_DocType_input'], flightvalue_128['LessorOperator_Support_DocType_input'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        # login.is_click(flight_128['LessorOperator_Support_AddDoc_Browse'])
        sleep(2)
        # 上传文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight_128['LessorOperator_Support_AddDoc_Remarks'], flightvalue_128['LessorOperator_Support_AddDoc_Remarks'])
        sleep(2)
        login.is_click(flight_128['LessorOperator_Support_AddDoc_Upload'])
        sleep(2)

        login.input_text(flight_128['LessorOperator_RegistrationMark'], flightvalue_128['LessorOperator_RegistrationMark'])
        sleep(2)
        login.is_click(flight_128['LessorOperator_AircraftType_select'])
        sleep(2)
        login.input_text(flight_128['LessorOperator_AircraftType_input'], flightvalue_128['LessorOperator_AircraftType_input'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[8]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight_128['LessorOperator_Aircraft_AddDoc'])
        sleep(2)
        login.is_click(flight_128['LessorOperator_Aircraft_DocType_select'])
        sleep(2)
        login.input_text(flight_128['LessorOperator_Aircraft_DocType_input'], flightvalue_128['LessorOperator_Aircraft_DocType_input'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        # login.is_click(flight_128['LessorOperator_Aircraft_AddDoc_Browse'])
        sleep(2)
        # 上传文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports2.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight_128['LessorOperator_Aircraft_AddDoc_Remarks'], flightvalue_128['LessorOperator_Aircraft_AddDoc_Remarks'])
        sleep(2)
        login.is_click(flight_128['LessorOperator_Aircraft_AddDoc_Upload'])
        sleep(2)
        login.is_click(flight_128['LessorOperator_Submit'])
        sleep(2)

        # step10 click no
        drivers.find_element_by_xpath("//button[contains(@class, 'testCancelButtonClass062')]").click()
        sleep(2)
        # click ok
        drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()
        sleep(2)

        # 从CPATEST03用户切换到officer1用户
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight_128["Logout"])
            login.is_click(flight_128['Logout_Yes'])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['OfficerLoginName'])
            login.input_user_password(cad_account['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # step11 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        login.is_click(flight_128['ViewMessages_AdvancedSearch'])
        sleep(2)

        # step12
        login.input_text(flight_128['ViewMessages_Sender'], cad_account['CpaOfficerLoginName'])
        sleep(2)
        login.is_click(flight_128['ViewMessages_ApplicationType'])
        sleep(2)
        login.is_click(flight_128['ViewMessages_Search'])
        sleep(3)

        # step13
        login.is_click(flight_128['ViewMessages_ReferenceNo'])
        sleep(3)

        # step21 Step 22~23 are optional, can skip to step #28 for direct processing
        # step22
        login.is_click(flight_128['ViewMessages_ModifyBasicImf'])
        sleep(2)
        login.is_click(flight_128['ViewMessages_SaveBasicImf'])
        sleep(2)
        drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()
        sleep(2)

        # step23
        login.is_click(flight_128['Modify_Select'])
        sleep(2)
        login.is_click(flight_128['ViewMessages_ModifySchedules'])
        sleep(2)
        login.is_click(flight_128['Modify_Dop1'])
        sleep(2)
        login.is_click(flight_128['Modify_Dop2'])
        sleep(2)
        login.is_click(flight_128['Modify_Dop3'])
        sleep(2)
        login.is_click(flight_128['Modify_Dop4'])
        sleep(2)
        login.is_click(flight_128['Modify_Dop5'])
        sleep(2)
        login.is_click(flight_128['Modify_Dop6'])
        sleep(2)
        login.is_click(flight_128['ViewMessages_SaveSchedules'])
        sleep(2)

        # step24 Click "Upload" in newly submitted documents section

        # step25
        login.is_click(flight_128['SelectDocLibrary'])
        # sleep(5)
        # login.is_click(flight_128['SelectDocLibrary_DocType_select'])
        # sleep(5)
        # login.input_text(flight_128['SelectDocLibrary_DocType_input'], "Aerodrome Operating Minima")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[8]/div[2]/div/div[3]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.input_text(flight_128['SelectDocLibrary_FileName'], "FileName")
        # login.input_text(flight_128['SelectDocLibrary_RegistrationMark'], "HK2024")
        # sleep(2)
        # login.input_text(flight_128['SelectDocLibrary_AircraftType_input'], "A139")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[8]/div[2]/div/div[3]/div/div[2]/form/div[2]/div[3]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.input_text(flight_128['SelectDocLibrary_Remarks'], "Testing")
        # login.input_text(flight_128['SelectDocLibrary_ExpiryDateFrom'], "21/12/2024")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[8]/div[2]/div/div[3]/div/div[2]/form/div[3]/div[2]/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.input_text(flight_128['SelectDocLibrary_ExpiryDateTo'], "31/12/2099")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[8]/div[2]/div/div[3]/div/div[2]/form/div[3]/div[2]/div/div/div[2]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.input_text(flight_128['SelectDocLibrary_LessorOperator_input'], "8AD")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[8]/div[2]/div/div[3]/div/div[2]/form/div[4]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.is_click(flight_128['SelectDocLibrary_Search'])
        sleep(2)
        login.is_click(flight_128['SelectDocument'])
        sleep(2)
        login.is_click(flight_128['SelectDocLibrary_Confirm'])
        sleep(2)

        # step21 Click "Upload application related document"
        login.is_click(flight_128['UploadDocument'])
        sleep(2)
        login.is_click(flight_128['UploadDocument_input'])
        sleep(2)
        login.input_text(flight_128['UploadDocument_input'], flightvalue_128['UploadDocument_input'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # login.is_click(flight_128['UploadDocument_browse'])
        sleep(2)
        # 上传文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight_128['UploadDocument_expiryDate'], flightvalue_128['UploadDocument_expiryDate'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight_128['UploadDocument_upload'])
        sleep(2)

        # step27
        login.is_click(flight_128['ViewUploadDoc'])
        sleep(2)
        login.is_click(flight_128['ViewUploadDoc_close'])
        sleep(2)

        # step28
        login.is_click(flight_128['Messaging'])
        sleep(2)
        # 所有窗口计数
        i = 0
        # 获得当前主窗口
        nowhandle = drivers.current_window_handle
        # 获取所有窗口
        allhandles = drivers.window_handles
        for handle in allhandles:
            i = i + 1
        if (i > 1):
            # 切换到最新打开的窗口
            drivers.switch_to.window(allhandles[-1])
        login.input_text(flight_128['Email_Message'], flightvalue_128['Email_Message'])
        sleep(2)
        # 关闭新窗口
        drivers.close()
        # 回到原来主窗口
        drivers.switch_to.window(nowhandle)
        sleep(3)

        # step29
        # login.is_click(flight_128['Remarks_click'])
        login.input_text(flight_128['Remarks_input'], flightvalue_128['Remarks_input'])
        sleep(2)

        # step30
        login.is_click(flight_128['CADRemarks_click'])
        sleep(2)
        login.input_text(flight_128['CADRemarks_input'], flightvalue_128['CADRemarks_input'])
        sleep(2)

        # step31
        login.is_click(flight_128['AutoCountingfrequency'])
        sleep(2)
        login.is_click(flight_128['AutoCountingfrequency_discard'])
        sleep(2)

        # step32 Print

        # step33
        login.is_click(flight_128['ViewMessages_Approve'])
        sleep(2)

        # step34
        login.is_click(flight_128['ViewMessages_Recommendation'])
        sleep(2)
        login.is_click(flight_128['ViewMessages_Confirm'])
        sleep(2)
        login.is_click(flight_128['Confirm_OK'])
        sleep(2)

        # step30
        login.is_click(flight_128['ViewMessages_Generate'])
        sleep(2)

        # step31
        login.is_click(flight_128['ViewMessages_GenerateAndEdit'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_OfficePhoneNo'], flightvalue_128['TemplateGenerate_OfficePhoneNo'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_OfficeFaxNo'], flightvalue_128['TemplateGenerate_OfficeFaxNo'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_UserName'], flightvalue_128['TemplateGenerate_UserName'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_Post'], flightvalue_128['TemplateGenerate_Post'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_SeasonInTitle'], flightvalue_128['TemplateGenerate_SeasonInTitle'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_CompanyName'], flightvalue_128['TemplateGenerate_CompanyName'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_Address1'], flightvalue_128['TemplateGenerate_Address1'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_SeasonInContent'], flightvalue_128['TemplateGenerate_SeasonInContent'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_Address2'], flightvalue_128['TemplateGenerate_Address2'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_SubjectOfficerName'], flightvalue_128['TemplateGenerate_SubjectOfficerName'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_Address3'], flightvalue_128['TemplateGenerate_Address3'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_PermitNo'], flightvalue_128['TemplateGenerate_PermitNo'])
        sleep(2)
        login.input_text(flight_128['TemplateGenerate_SignedArea'], flightvalue_128['TemplateGenerate_SignedArea'])
        sleep(2)
        login.is_click(flight_128['TemplateGenerate_RefreshPreview'])
        sleep(2)
        login.is_click(flight_128['TemplateGenerate_DownloadAsWord'])
        sleep(2)
        login.is_click(flight_128['TemplateGenerate_GeneratePDF'])
        sleep(10)

        # step32
        login.is_click(flight_128['Send'])
        sleep(2)
        login.is_click(flight_128['SendOK'])
        sleep(2)

        # 从Officer1用户切换到CPATEST03用户
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight_128["Logout"])
            login.is_click(flight_128['Logout_Yes'])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['CpaOfficerLoginName'])
            login.input_user_password(cad_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # step33 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        login.is_click(flight_128['ViewMessages_AdvancedSearch_CAP'])
        login.input_text(flight_128['ViewMessages_SubjectContains_CAP'], flightvalue_128['ViewMessages_SubjectContains_CAP'])
        sleep(2)
        login.input_text(flight_128['ViewMessages_Sender_CAP'], cad_account['OfficerLoginName'])
        sleep(2)
        login.is_click(flight_128['ViewMessages_ApplicationType_CAP'])
        sleep(2)
        login.is_click(flight_128['ViewMessages_Search_CAP'])
        sleep(2)
        login.is_click(flight_128['ViewMessages_ApprovedMessage_CAP'])
        sleep(2)
        login.is_click(flight_128['ApprovedAttachment_CAP'])
        sleep(3)
        login.is_click(flight_128['ApprovedReferenceNo_CAP'])
        sleep(5)
        assert login.element_text(flight_128['ApprovedStatus']) == 'Approved'
        sleep(2)

        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight_128["Logout"])
            login.is_click(flight_128['Logout_Yes'])


if __name__ == '__main__':
    pytest.main(['TestCase/test_helicopter_schedule_passenger_approve.py'])