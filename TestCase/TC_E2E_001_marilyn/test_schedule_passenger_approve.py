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

flight_001 = Element('flight_001')
flightvalue_001 = ElementValue('flightvalue_001')
cad_account = ElementValue('cad_account')
@allure.feature("TC(ECE)-001 Local Operator Create and Processing Scheduled Passenger Application (Approve)")
class TestSchedulePassengerApprove:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create Seasonal Schedule Passenger Application and approve")
    def test_001(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight_001["Logout"])
            login.is_click(flight_001['Logout_Yes'])

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

        r = random.choice(string.ascii_letters)
        FlightNo1 = "CPA" + str(randint(1, 9999)) + r
        FlightNo2 = "CPA" + str(randint(1, 9999)) + r
        FlightNo3 = "CPA" + str(randint(1, 9999)) + r
        FlightNo4 = "CPA" + str(randint(1, 9999)) + r
        FlightNo5 = "CPA" + str(randint(1, 9999)) + r
        FlightNo6 = "CPA" + str(randint(1, 9999)) + r
        FlightNo7 = "CPA" + str(randint(1, 9999)) + r
        FlightNo8 = "CPA" + str(randint(1, 9999)) + r
        FlightNo9 = "CPA" + str(randint(1, 9999)) + r
        TemplateName = "Temp" + str(random.uniform(1, 9999))

        login.is_click(flight_001['Season'])
        login.input_text(flight_001['Season'], "Summer")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[1]/div[1]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)

        # step1 填写flight Schedules表格信息
        # FlightNo1
        login.input_text(flight_001['FlightNo1'], FlightNo1)
        sleep(1)
        login.input_text(flight_001['From1'], flightvalue_001['From1'])
        sleep(1)
        login.input_text(flight_001['To1'], flightvalue_001['To1'])
        sleep(1)
        login.is_click(flight_001['DOP1_1'])
        sleep(1)
        login.is_click(flight_001['DOP1_3'])
        sleep(1)
        login.is_click(flight_001['DOP1_5'])
        sleep(1)
        login.is_click(flight_001['AircraftType_Select1'])
        sleep(1)
        login.input_text(flight_001['AircraftType_input1'], flightvalue_001['AircraftType_input1'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['NoofSeats1'], flightvalue_001['NoofSeats1'])
        sleep(1)
        login.input_text(flight_001['Route1'], flightvalue_001['Route1'])
        sleep(1)
        login.is_click(flight_001['LocalTime_STD1'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STD1'], flightvalue_001['LocalTime_STD1'])
        sleep(1)
        login.input_text(flight_001['Remarks1'], flightvalue_001['Remarks1'])
        sleep(2)
        # FlightNo1_2
        login.input_text(flight_001['FlightNo1_2'], FlightNo2)
        sleep(1)
        login.is_click(flight_001['AircraftType_Select1_2'])
        sleep(1)
        login.input_text(flight_001['AircraftType_input1_2'], flightvalue_001['AircraftType_input1_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['NoofSeats1_2'], flightvalue_001['NoofSeats1_2'])
        sleep(1)
        login.input_text(flight_001['Route1_2'], flightvalue_001['Route1_2'])
        sleep(1)
        login.is_click(flight_001['LocalTime_STA1_2'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STA1_2'], flightvalue_001['LocalTime_STA1_2'])
        sleep(1)
        login.input_text(flight_001['Remarks1_2'], flightvalue_001['Remarks1_2'])
        sleep(2)

        # FlightNo2
        login.input_text(flight_001['FlightNo2'], FlightNo3)
        sleep(1)
        login.input_text(flight_001['From2'], flightvalue_001['From2'])
        sleep(1)
        login.input_text(flight_001['To2'], flightvalue_001['To2'])
        sleep(1)
        login.is_click(flight_001['DOP2_1'])
        sleep(1)
        login.is_click(flight_001['DOP2_3'])
        sleep(1)
        login.is_click(flight_001['DOP2_5'])
        sleep(1)
        login.is_click(flight_001['DOP2_7'])
        sleep(1)
        login.is_click(flight_001['AircraftType_Select2'])
        sleep(1)
        login.input_text(flight_001['AircraftType_input2'], flightvalue_001['AircraftType_input2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['NoofSeats2'], flightvalue_001['NoofSeats2'])
        sleep(1)
        login.input_text(flight_001['Route2'], flightvalue_001['Route2'])
        sleep(1)
        login.is_click(flight_001['LocalTime_STD2'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STD2'], flightvalue_001['LocalTime_STD2'])
        sleep(1)
        login.is_click(flight_001['BellyCargoOnly2'])
        sleep(1)
        drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()
        sleep(1)
        login.input_text(flight_001['Remarks2'], flightvalue_001['Remarks2'])
        sleep(2)
        # FlightNo2_2
        login.input_text(flight_001['FlightNo2_2'], FlightNo4)
        sleep(1)
        login.is_click(flight_001['AircraftType_Select2_2'])
        sleep(1)
        login.input_text(flight_001['AircraftType_input2_2'], flightvalue_001['AircraftType_input2_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[4]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['NoofSeats2_2'], flightvalue_001['NoofSeats2_2'])
        sleep(1)
        login.input_text(flight_001['Route2_2'], flightvalue_001['Route2_2'])
        sleep(1)
        login.is_click(flight_001['LocalTime_STA2_2'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STA2_2'], flightvalue_001['LocalTime_STA2_2'])
        sleep(1)
        login.is_click(flight_001['BellyCargoOnly2_2'])
        sleep(1)
        drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()
        sleep(1)
        login.input_text(flight_001['Remarks2_2'], flightvalue_001['Remarks2_2'])
        sleep(2)

        # FlightNo3
        login.input_text(flight_001['FlightNo3'], FlightNo5)
        sleep(1)
        login.input_text(flight_001['From3'], flightvalue_001['From3'])
        sleep(1)
        login.input_text(flight_001['To3'], flightvalue_001['To3'])
        sleep(1)
        login.is_click(flight_001['DOP3_4'])
        sleep(1)
        login.is_click(flight_001['DOP3_6'])
        sleep(1)
        login.is_click(flight_001['DOP3_2'])
        sleep(1)
        login.is_click(flight_001['AircraftType_Select3'])
        sleep(1)
        login.input_text(flight_001['AircraftType_input3'], flightvalue_001['AircraftType_input3'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['NoofSeats3'], flightvalue_001['NoofSeats3'])
        sleep(1)
        login.input_text(flight_001['Route3'], flightvalue_001['Route3'])
        sleep(1)
        login.is_click(flight_001['LocalTime_STD3'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STD3'], flightvalue_001['LocalTime_STD3'])
        sleep(1)
        login.input_text(flight_001['Remarks3'], flightvalue_001['Remarks3'])
        sleep(2)
        # FlightNo3_2
        login.input_text(flight_001['FlightNo3_2'], FlightNo6)
        sleep(1)
        login.is_click(flight_001['FlightDiff_Select3_2'])
        sleep(1)
        login.input_text(flight_001['FlightDiff_Input3_2'], flightvalue_001['FlightDiff_Input3_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight_001['AircraftType_Select3_2'])
        sleep(1)
        login.input_text(flight_001['AircraftType_input3_2'], flightvalue_001['AircraftType_input3_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['NoofSeats3_2'], flightvalue_001['NoofSeats3_2'])
        sleep(1)
        login.input_text(flight_001['Route3_2'], flightvalue_001['Route3_2'])
        sleep(1)
        login.is_click(flight_001['LocalTime_STA3_2'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STA3_2'], flightvalue_001['LocalTime_STA3_2'])
        sleep(1)
        login.input_text(flight_001['Remarks3_2'], flightvalue_001['Remarks3_2'])
        sleep(2)

        # FlightNo4
        login.input_text(flight_001['FlightNo4'], FlightNo7)
        sleep(1)
        login.input_text(flight_001['From4'], flightvalue_001['From4'])
        sleep(1)
        login.input_text(flight_001['To4'], flightvalue_001['To4'])
        sleep(1)
        login.is_click(flight_001['DOP4_1'])
        sleep(1)
        login.is_click(flight_001['DOP4_3'])
        sleep(1)
        login.is_click(flight_001['DOP4_5'])
        sleep(1)
        login.is_click(flight_001['AircraftType_Select4'])
        sleep(1)
        login.input_text(flight_001['AircraftType_input4'], flightvalue_001['AircraftType_input4'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['NoofSeats4'], flightvalue_001['NoofSeats4'])
        sleep(1)
        login.input_text(flight_001['Route4'], flightvalue_001['Route4'])
        sleep(1)
        login.is_click(flight_001['LocalTime_STD4'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STD4'], flightvalue_001['LocalTime_STD4'])
        sleep(1)
        login.input_text(flight_001['Remarks4'], flightvalue_001['Remarks4'])
        sleep(2)
        # FlightNo4_2
        login.input_text(flight_001['FlightNo4_2'], FlightNo8)
        sleep(1)
        login.is_click(flight_001['AircraftType_Select4_2'])
        sleep(1)
        login.input_text(flight_001['AircraftType_input4_2'], flightvalue_001['AircraftType_input4_2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[8]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['NoofSeats4_2'], flightvalue_001['NoofSeats4_2'])
        sleep(1)
        login.input_text(flight_001['Route4_2'], flightvalue_001['Route4_2'])
        sleep(1)
        login.is_click(flight_001['LocalTime_STA4_2'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STA4_2'], flightvalue_001['LocalTime_STA4_2'])
        sleep(1)
        login.input_text(flight_001['Remarks4_2'], flightvalue_001['Remarks4_2'])
        sleep(2)

        # FlightNo5
        login.input_text(flight_001['FlightNo5'], FlightNo9)
        sleep(1)
        login.input_text(flight_001['From5'], flightvalue_001['From5'])
        sleep(1)
        login.input_text(flight_001['To5'], flightvalue_001['To5'])
        sleep(1)
        login.is_click(flight_001['DOP5_2'])
        sleep(1)
        login.is_click(flight_001['DOP5_4'])
        sleep(1)
        login.is_click(flight_001['AircraftType_Select5'])
        sleep(1)
        login.input_text(flight_001['AircraftType_input5'], flightvalue_001['AircraftType_input5'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[9]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['NoofSeats5'], flightvalue_001['NoofSeats5'])
        sleep(1)
        login.input_text(flight_001['Route5'], flightvalue_001['Route5'])
        sleep(1)
        login.is_click(flight_001['LocalTime_STA5'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STA5'], flightvalue_001['LocalTime_STA5'])
        sleep(1)
        login.input_text(flight_001['LocalTime_STD5'], flightvalue_001['LocalTime_STD5'])
        sleep(1)
        login.is_click(flight_001['NextDate_Select5'])
        sleep(1)
        login.input_text(flight_001['NextDate_input5'], flightvalue_001['NextDate_input5'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[9]/td[18]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight_001['Remarks5'], flightvalue_001['Remarks5'])
        sleep(1)
        login.input_text(flight_001['Remarks'], flightvalue_001['Remarks'])
        sleep(2)

        # 选择文件
        login.is_click(flight_001['SelectDoc'])
        sleep(1)
        login.input_text(flight_001['DocType_input'], flightvalue_001['DocType_input1'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight_001['DocType_input'], flightvalue_001['DocType_input2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[4]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(1)
        login.is_click(flight_001['Doc_search'])
        sleep(2)
        login.is_click(flight_001['Doc_confirm'])
        sleep(2)

        # 上传文件
        login.is_click(flight_001['UploadDoc'])
        sleep(2)
        login.is_click(flight_001['UploadDoc_input_others'])
        sleep(1)
        login.input_text(flight_001['UploadDoc_input_others'], flightvalue_001['UploadDoc_input_others'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # login.is_click(flight_001['BrowseButton'])
        sleep(2)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight_001['ExpiryDate'], flightvalue_001['ExpiryDate'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight_001['UploadButton'])
        sleep(2)
        assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[7]/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[2]/div").text == "other_supports.pdf"
        sleep(2)

        # step2
        login.is_click(flight_001['SaveAsDraft'])
        sleep(2)
        assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'
        sleep(2)

        # step3
        login.is_click(flight_001['SaveAsTemplate'])
        sleep(2)
        login.input_text(flight_001['TemplateName'], TemplateName)
        sleep(2)
        login.input_text(flight_001['Description'], flightvalue_001['Description'])
        sleep(2)
        login.is_click(flight_001['Template_Save'])
        sleep(2)
        login.is_click(flight_001['Confirm'])
        sleep(2)

        # step4
        login.is_click(flight_001['PreviewAndSubmit'])
        sleep(2)

        # step5 Print

        # step6
        login.is_click(flight_001['BackAndModify'])
        sleep(2)
        login.is_click(flight_001['PreviewAndSubmit'])
        sleep(2)

        # step7
        login.is_click(flight_001['Submit'])
        sleep(2)

        # step8
        drivers.find_element_by_xpath("//button[contains(@class, 'testConfirmButtonClass016')]").click()
        sleep(2)
        login.is_click(flight_001['LessorOperator_select'])
        sleep(1)
        login.input_text(flight_001['LessorOperator_input'], flightvalue_001['LessorOperator_input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight_001['EffectivePeriod1'], flightvalue_001['EffectivePeriod1'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight_001['EffectivePeriod2'], flightvalue_001['EffectivePeriod2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input").send_keys(Keys.ENTER)
        sleep(2)

        login.is_click(flight_001['SupportingDoc_AddDoc'])
        sleep(1)
        login.is_click(flight_001['SupportingDoc_AddDoc_select'])
        sleep(1)
        login.input_text(flight_001['SupportingDoc_AddDoc_input'], flightvalue_001['SupportingDoc_AddDoc_input'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        # login.is_click(flight_001['SupportingDoc_AddDoc_browse'])
        sleep(2)
        # 上传文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight_001['SupportingDoc_AddDoc_remarks'], flightvalue_001['SupportingDoc_AddDoc_remarks'])
        sleep(2)
        login.is_click(flight_001['SupportingDoc_AddDoc_upload'])
        sleep(2)

        login.input_text(flight_001['ListOfAircraft_RegistrationMark'], flightvalue_001['ListOfAircraft_RegistrationMark'])
        sleep(2)
        login.is_click(flight_001['ListOfAircraft_AircraftType_input'])
        sleep(2)
        login.input_text(flight_001['ListOfAircraft_AircraftType_input'], flightvalue_001['ListOfAircraft_AircraftType_input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[8]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.is_click(flight_001['ListOfAircraft_AddDoc'])
        sleep(2)
        login.is_click(flight_001['ListOfAircraft_AddDoc_select'])
        sleep(1)
        login.input_text(flight_001['ListOfAircraft_AddDoc_input'], flightvalue_001['ListOfAircraft_AddDoc_input'])
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/div/div[2]/form/div[1]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        # login.is_click(flight_001['ListOfAircraft_AddDoc_browse'])
        # 上传文件
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_supports2.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.input_text(flight_001['ListOfAircraft_AddDoc_remarks'], flightvalue_001['ListOfAircraft_AddDoc_remarks'])
        sleep(2)
        login.is_click(flight_001['ListOfAircraft_AddDoc_upload'])
        sleep(2)
        login.is_click(flight_001['LeaseAircraftOperation_Submit'])
        sleep(2)

        # step9 Click "No" in special operation application dialog
        drivers.find_element_by_xpath("//button[contains(@class, 'testCancelButtonClass062')]").click()
        sleep(2)
        # click ok
        drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()
        sleep(2)

        # 从CPATEST03用户切换到officer1用户
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight_001["Logout"])
            login.is_click(flight_001['Logout_Yes'])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['OfficerLoginName'])
            login.input_user_password(cad_account['OfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # step10 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        login.is_click(flight_001['ViewMessages_AdvancedSearch'])
        sleep(2)

        # step11
        login.input_text(flight_001['ViewMessages_Sender'], cad_account['CpaOfficerLoginName'])
        sleep(2)
        login.is_click(flight_001['ViewMessages_ApplicationType'])
        sleep(2)
        login.is_click(flight_001['ViewMessages_Search'])
        sleep(3)

        # step12
        login.is_click(flight_001['ViewMessages_ReferenceNo'])
        sleep(3)

        # step13 Step 14~27 are optional, can skip to step #28 for direct processing
        # step14
        login.is_click(flight_001['ViewMessages_ModifyBasicImf'])
        sleep(2)
        login.is_click(flight_001['ViewMessages_SaveBasicImf'])
        sleep(1)
        drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()
        sleep(2)

        # step15
        login.is_click(flight_001['Modify_Select'])
        sleep(2)
        login.is_click(flight_001['ViewMessages_ModifySchedules'])
        sleep(1)
        login.is_click(flight_001['Modify_Dop1'])
        sleep(1)
        login.is_click(flight_001['Modify_Dop2'])
        sleep(1)
        login.is_click(flight_001['Modify_Dop3'])
        sleep(1)
        login.is_click(flight_001['Modify_Dop4'])
        sleep(1)
        login.is_click(flight_001['Modify_Dop5'])
        sleep(1)
        login.is_click(flight_001['Modify_Dop6'])
        sleep(1)
        login.is_click(flight_001['Modify_AircraftType_input'])
        sleep(2)
        login.input_text(flight_001['Modify_AircraftType_input'], flightvalue_001['Modify_AircraftType_input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[12]/div/span/div/div/input").send_keys(Keys.ENTER)
        sleep(2)
        login.input_text(flight_001['Modify_NoOfSeats'], flightvalue_001['Modify_NoOfSeats'])
        sleep(2)
        login.input_text(flight_001['Modify_STD'], flightvalue_001['Modify_STD'])
        sleep(2)
        login.is_click(flight_001['Modify_EB'])
        sleep(2)
        login.is_click(flight_001['Modify_Repatriation'])
        sleep(2)
        login.input_text(flight_001['Modify_Remarks'], flightvalue_001['Modify_Remarks'])
        sleep(2)
        login.is_click(flight_001['ViewMessages_SaveSchedules'])
        sleep(2)
        #
        # # step16
        # login.is_click(flight_001['Modify_Select'])
        # sleep(1)
        # login.is_click(flight_001['ViewMessages_CheckLicence'])
        # sleep(2)

        # step17
        # login.is_click(flight_001['ViewMessages_CheckTrafficRights'])
        # sleep(1)
        # login.is_click(flight_001['ViewMessages_CheckTrafficRights_close'])
        # sleep(2)

        # step18 Click Check SCORE

        # step19 Click Upload

        # step20
        # login.is_click(flight_001['SelectDocLibrary'])
        # sleep(2)
        # login.input_text(flight_001['SelectDocLibrary_DocType'], "Aerodrome Operating Minima")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[8]/div[2]/div/div[3]/div/div[2]/form/div[1]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.input_text(flight_001['SelectDocLibrary_FileName'], "FileName")
        # login.input_text(flight_001['SelectDocLibrary_RegistrationMark'], "HK2025")
        # sleep(2)
        # login.input_text(flight_001['SelectDocLibrary_AircraftType'], "ABY")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[8]/div[2]/div/div[3]/div/div[2]/form/div[2]/div[3]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.input_text(flight_001['SelectDocLibrary_Remarks'], "Testing")
        # login.input_text(flight_001['SelectDocLibrary_ExpiryDateFrom'], "01/12/2024")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[8]/div[2]/div/div[3]/div/div[2]/form/div[3]/div[2]/div/div/div[1]/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.input_text(flight_001['SelectDocLibrary_ExpiryDateTo'], "31/12/2099")
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[5]/div[8]/div[2]/div/div[3]/div/div[2]/form/div[3]/div[2]/div/div/div[2]/input").send_keys(Keys.ENTER)
        # sleep(5)
        # login.is_click(flight_001['SelectDocLibrary_Search'])
        # sleep(5)
        # login.is_click(flight_001['SelectDocument'])
        # sleep(2)
        # login.is_click(flight_001['SelectDocLibrary_Confirm'])
        # sleep(2)

        # step21 Click "Upload application related document"
        # login.is_click(flight_001['UploadDocument'])
        # sleep(2)
        # login.is_click(flight_001['UploadDocument_input'])
        # sleep(2)
        # login.input_text(flight_001['UploadDocument_input'], flightvalue_001['UploadDocument_input'])
        # sleep(2)
        # drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        # sleep(2)
        # # 上传文件
        # current_path = os.path.abspath(__file__)
        # file_path = os.path.dirname(current_path) + "/TestFile/other_supports.pdf"
        # drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        # sleep(2)
        # login.input_text(flight_001['UploadDocument_expiryDate'], flightvalue_001['UploadDocument_expiryDate'])
        # sleep(1)
        # drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        # sleep(2)
        # login.is_click(flight_001['UploadDocument_upload'])
        # sleep(2)

        # step22
        # login.is_click(flight_001['ViewUploadDoc'])
        # sleep(2)
        # login.is_click(flight_001['ViewUploadDoc_close'])
        # sleep(2)

        # step23
        # login.is_click(flight_001['Messaging'])
        # sleep(2)
        # # 所有窗口计数
        # i = 0
        # # 获得当前主窗口
        # nowhandle = drivers.current_window_handle
        # # 获取所有窗口
        # allhandles = drivers.window_handles
        # for handle in allhandles:
        #     i = i + 1
        # if (i > 1):
        #     # 切换到最新打开的窗口
        #     drivers.switch_to.window(allhandles[-1])
        # login.input_text(flight_001['Email_Message'], flightvalue_001['Email_Message'])
        # sleep(2)
        # # 关闭新窗口
        # drivers.close()
        # # 回到原来主窗口
        # drivers.switch_to.window(nowhandle)
        # sleep(3)

        # step24
        # login.is_click(flight_001['Remarks_click'])
        # login.input_text(flight_001['Remarks_input'], flightvalue_001['Remarks_input'])
        # sleep(2)

        # step25
        # login.is_click(flight_001['CADRemarks_click'])
        # sleep(2)
        # login.input_text(flight_001['CADRemarks_input'], flightvalue_001['CADRemarks_input'])
        # sleep(2)

        # step26
        # login.is_click(flight_001['AutoCountingfrequency'])
        # sleep(2)
        # login.is_click(flight_001['AutoCountingfrequency_discard'])
        # sleep(2)

        # step27 Print

        # step28
        login.is_click(flight_001['ViewMessages_Approve'])
        sleep(2)

        # step29
        login.is_click(flight_001['ViewMessages_Recommendation'])
        sleep(2)
        login.is_click(flight_001['ViewMessages_Confirm'])
        sleep(2)
        login.is_click(flight_001['Confirm_OK'])
        sleep(2)

        # step30
        login.is_click(flight_001['ViewMessages_Generate'])
        sleep(2)

        # step31
        login.is_click(flight_001['ViewMessages_GenerateAndEdit'])
        sleep(2)
        login.input_text(flight_001['TemplateGenerate_OfficePhoneNo'], flightvalue_001['TemplateGenerate_OfficePhoneNo'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_OfficeFaxNo'], flightvalue_001['TemplateGenerate_OfficeFaxNo'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_UserName'], flightvalue_001['TemplateGenerate_UserName'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_Post'], flightvalue_001['TemplateGenerate_Post'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_SeasonInTitle'], flightvalue_001['TemplateGenerate_SeasonInTitle'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_CompanyName'], flightvalue_001['TemplateGenerate_CompanyName'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_Address1'], flightvalue_001['TemplateGenerate_Address1'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_SeasonInContent'], flightvalue_001['TemplateGenerate_SeasonInContent'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_Address2'], flightvalue_001['TemplateGenerate_Address2'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_SubjectOfficerName'], flightvalue_001['TemplateGenerate_SubjectOfficerName'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_Address3'], flightvalue_001['TemplateGenerate_Address3'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_PermitNo'], flightvalue_001['TemplateGenerate_PermitNo'])
        sleep(1)
        login.input_text(flight_001['TemplateGenerate_SignedArea'], flightvalue_001['TemplateGenerate_SignedArea'])
        sleep(1)
        login.is_click(flight_001['TemplateGenerate_RefreshPreview'])
        sleep(1)
        login.is_click(flight_001['TemplateGenerate_DownloadAsWord'])
        sleep(1)
        login.is_click(flight_001['TemplateGenerate_GeneratePDF'])
        sleep(10)

        # step32
        login.is_click(flight_001['Send'])
        sleep(15)
        login.is_click(flight_001['SendOK'])
        sleep(5)

        # 从Officer1用户切换到CPATEST03用户
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight_001["Logout"])
            login.is_click(flight_001['Logout_Yes'])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(cad_account['CpaOfficerLoginName'])
            login.input_user_password(cad_account['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 25, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # step33 跳转到View->Messages页面
        login.get_url(ini.url + "#/View/Messages")
        sleep(2)
        login.is_click(flight_001['ViewMessages_AdvancedSearch_CAP'])
        sleep(2)
        login.input_text(flight_001['ViewMessages_SubjectContains_CAP'], flightvalue_001['ViewMessages_SubjectContains_CAP'])
        sleep(2)
        login.input_text(flight_001['ViewMessages_Sender_CAP'], cad_account['OfficerLoginName'])
        sleep(2)
        login.is_click(flight_001['ViewMessages_ApplicationType_CAP'])
        sleep(2)
        login.is_click(flight_001['ViewMessages_Search_CAP'])
        sleep(2)
        login.is_click(flight_001['ViewMessages_ApprovedMessage_CAP'])
        sleep(2)
        login.is_click(flight_001['ApprovedAttachment_CAP'])
        sleep(3)
        login.is_click(flight_001['ApprovedReferenceNo_CAP'])
        sleep(5)
        assert login.element_text(flight_001['ApprovedStatus']) == 'Approved'
        sleep(2)

        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight_001["Logout"])
            login.is_click(flight_001['Logout_Yes'])

if __name__ == '__main__':
    pytest.main(['TestCase/test_schedule_passenger_approve.py'])

