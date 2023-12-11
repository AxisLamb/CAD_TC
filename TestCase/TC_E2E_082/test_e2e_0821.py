#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import random
import os
import string

import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue

flight = Element('flight_082')
flightValue = ElementValue('flightValue_082')
accountValue = ElementValue('cad_account')

@allure.feature("[TC(E2E)-082] 01: Create and Approve Charter Passenger application")
class TestCreateAndApproveCharterPassenger:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create and Approve Charter Passenger application")
    def test_e2e_0821(self, drivers):
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            login.is_click(flight["Logout"])
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(accountValue['CpaOfficerLoginName'])
            login.input_user_password(accountValue['CpaOfficerPassword'])
            login.click_login_button()
        WebDriverWait(drivers, 15, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到CreateCharterFlight页面
        login.get_url(ini.url + "#/ApplicationView/CharterFlight/CreateCharterFlight")
        drivers.implicitly_wait(30)
        sleep(5)
        assert drivers.find_element_by_css_selector("h2").text == "Create Charter Passenger Application"

        # 填写Basic Information
        login.input_text(flight['Registration_mark'], flightValue['Registration_Mark'])
        # login.is_click(flight['Lease_Aircraft'])
        login.is_click(flight['Aircraft_type_select'])
        login.input_text(flight['Aircraft_type_input'], flightValue['Aircraft_Type'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[5]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['Aircraft_nationality_select'])
        login.input_text(flight['Aircraft_nationality_input'], flightValue['Aircraft_Nationality'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[5]/div[2]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Name_of_charterer'], flightValue['Name_of_Charterer'])
        login.input_text(flight['Address_of_charterer'], flightValue['Address_of_Charterer'])
        login.is_click(flight['Local_handling_agent_select'])
        login.input_text(flight['Local_handling_agent_input'], flightValue['Local_Handling_Agent'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[1]/div/div/div[8]/div/div/div[1]/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['Purpose_of_service'], flightValue['Purpose_of_Service'])
        login.input_text(flight['Points_of_landing'], flightValue['Points_of_landing'])
        sleep(2)

        # 填写Flight Schedules表格信息
        rl = random.choice(string.ascii_letters)
        flightNo1 = "CPA" + str(random.randint(1000, 9999)) + rl
        flightNo3 = "CPA" + str(random.randint(1000, 9999)) + rl
        flightNo5 = "CPA" + str(random.randint(1000, 9999)) + rl
        flightNo6 = "CPA" + str(random.randint(1000, 9999)) + rl
        flightNo7 = "CPA" + str(random.randint(1000, 9999)) + rl
        # line 1 and line2
        login.is_click(flight['Service_Type_select'])
        login.input_text(flight['Service_Type_input'], flightValue['Service_Type1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo'], flightNo1)
        login.input_text(flight['From'], flightValue['Operation_Period_From'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To'], flightValue['Operation_Period_To'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[1]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1'])
        login.is_click(flight['DOP_2'])
        login.is_click(flight['DOP_3'])
        login.is_click(flight['DOP_4'])
        login.is_click(flight['DOP_5'])
        login.is_click(flight['DOP_6'])
        login.is_click(flight['DOP_7'])
        login.input_text(flight['No_of_Pax'], flightValue['No_of_Pax1'])
        login.input_text(flight['Port_From'], flightValue['Port_From1'])
        login.input_text(flight['Port_To'], flightValue['Port_To1'])
        # login.input_text(flight['LocalTime_STA'], flightvalue['Local_Time_STA1'])
        login.input_text(flight['LocalTime_STD'], flightValue['Local_Time1'])
        login.input_text(flight['Table_Remarks'], flightValue['Table_Remarks'] + "1")

        login.is_click(flight['Service_Type_select_2'])
        login.input_text(flight['Service_Type_input_2'], flightValue['Service_Type1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[2]/td[1]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_2'], "CPA" + str(random.randint(1000, 9999)) + rl)
        login.input_text(flight['No_of_Pax_2'], flightValue['No_of_Pax2'])
        login.input_text(flight['Port_From_2'], flightValue['Port_To1'])
        login.input_text(flight['Port_To_2'], flightValue['Port_From1'])
        login.input_text(flight['LocalTime_STA_2'], flightValue['Local_Time2'])
        # login.input_text(flight['LocalTime_STD_2'], flightvalue['Local_Time_STD2'])
        login.input_text(flight['Table_Remarks_2'], flightValue['Table_Remarks'] + "2")

        # line 3 and line4
        login.is_click(flight['Service_Type_select_3'])
        login.input_text(flight['Service_Type_input_3'], flightValue['Service_Type2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[3]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_3'], flightNo3)
        login.input_text(flight['From_3'], flightValue['Operation_Period_From'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[3]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To_3'], flightValue['Operation_Period_To'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[3]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1_3'])
        login.is_click(flight['DOP_2_3'])
        login.is_click(flight['DOP_3_3'])
        login.is_click(flight['DOP_4_3'])
        login.is_click(flight['DOP_5_3'])
        login.is_click(flight['DOP_6_3'])
        login.is_click(flight['DOP_7_3'])
        login.input_text(flight['No_of_Pax_3'], flightValue['No_of_Pax1'])
        login.input_text(flight['Port_From_3'], flightValue['Port_From2'])
        login.input_text(flight['Port_To_3'], flightValue['Port_To2'])
        # login.input_text(flight['LocalTime_STA_3'], flightvalue['Local_Time_STA1'])
        login.input_text(flight['LocalTime_STD_3'], flightValue['Local_Time1'])
        login.input_text(flight['Table_Remarks_3'], flightValue['Table_Remarks'] + "3")

        login.is_click(flight['Service_Type_select_4'])
        login.input_text(flight['Service_Type_input_4'], flightValue['Service_Type2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[4]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_4'], "CPA" + str(random.randint(1000, 9999)) + rl)
        login.input_text(flight['No_of_Pax_4'], flightValue['No_of_Pax2'])
        login.input_text(flight['Port_From_4'], flightValue['Port_To2'])
        login.input_text(flight['Port_To_4'], flightValue['Port_From2'])
        login.input_text(flight['LocalTime_STA_4'], flightValue['Local_Time3'])
        # login.input_text(flight['LocalTime_STD_4'], flightvalue['Local_Time_STD2'])
        login.input_text(flight['Table_Remarks_4'], flightValue['Table_Remarks'] + "4")

        # #line 5 and line6
        login.is_click(flight['Service_Type_select_5'])
        login.input_text(flight['Service_Type_input_5'], flightValue['Service_Type3'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[5]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_5'], flightNo5)
        login.input_text(flight['From_5'], flightValue['Operation_Period_From'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[5]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To_5'], flightValue['Operation_Period_To'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[5]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1_5'])
        login.is_click(flight['DOP_2_5'])
        login.is_click(flight['DOP_3_5'])
        login.is_click(flight['DOP_4_5'])
        login.is_click(flight['DOP_5_5'])
        login.is_click(flight['DOP_6_5'])
        login.is_click(flight['DOP_7_5'])
        login.input_text(flight['No_of_Pax_5'], flightValue['No_of_Pax3'])
        login.input_text(flight['Port_From_5'], flightValue['Port_From3'])
        login.input_text(flight['Port_To_5'], flightValue['Port_To3'])
        login.input_text(flight['LocalTime_STA_5'], flightValue['Local_Time4'])
        # login.input_text(flight['LocalTime_STD_5'], flightvalue['Local_Time_STD1'])
        login.input_text(flight['Table_Remarks_5'], flightValue['Table_Remarks'] + "5")

        login.is_click(flight['Service_Type_select_6'])
        login.input_text(flight['Service_Type_input_6'], flightValue['Service_Type3'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[6]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_6'], flightNo6)
        login.is_click(flight['In_Out_Diff_select_6'])
        login.input_text(flight['In_Out_Diff_input_6'], flightValue['In_Out_Diff'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[6]/td[3]/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_of_Pax_6'], flightValue['No_of_Pax1'])
        login.input_text(flight['Port_From_6'], flightValue['Port_To3'])
        login.input_text(flight['Port_To_6'], flightValue['Port_From3'])
        # login.input_text(flight['LocalTime_STA_6'], flightvalue['Local_Time_STA2'])
        login.input_text(flight['LocalTime_STD_6'], flightValue['Local_Time5'])
        login.input_text(flight['Table_Remarks_6'], flightValue['Table_Remarks'] + "6")

        # #line 7 and line8
        login.is_click(flight['Service_Type_select_7'])
        login.input_text(flight['Service_Type_input_7'], flightValue['Service_Type1'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[7]/td[2]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_7'], flightNo7)
        login.input_text(flight['From_7'], flightValue['Operation_Period_From'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[7]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To_7'], flightValue['Operation_Period_To'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[7]/td[6]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1_7'])
        login.is_click(flight['DOP_2_7'])
        login.is_click(flight['DOP_3_7'])
        login.is_click(flight['DOP_4_7'])
        login.is_click(flight['DOP_5_7'])
        login.is_click(flight['DOP_6_7'])
        login.is_click(flight['DOP_7_7'])
        login.input_text(flight['No_of_Pax_7'], flightValue['No_of_Pax4'])
        login.input_text(flight['Port_From_7'], flightValue['Port_From4'])
        login.input_text(flight['Port_To_7'], flightValue['Port_To4'])
        # login.input_text(flight['LocalTime_STA_7'], flightvalue['Local_Time_STA1'])
        login.input_text(flight['LocalTime_STD_7'], flightValue['Local_Time1'])
        login.input_text(flight['Table_Remarks_7'], flightValue['Table_Remarks'] + "7")

        login.is_click(flight['Service_Type_select_8'])
        login.input_text(flight['Service_Type_input_8'], flightValue['Service_Type2'])
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div[3]/div/div[3]/table/tbody/tr[8]/td[1]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['FlightNo_8'], "CPA" + str(random.randint(1000, 9999)) + rl)
        login.input_text(flight['No_of_Pax_8'], flightValue['No_of_Pax3'])
        login.input_text(flight['Port_From_8'], flightValue['Port_To4'])
        login.input_text(flight['Port_To_8'], flightValue['Port_From4'])
        login.input_text(flight['LocalTime_STA_8'], flightValue['Local_Time6'])
        # login.input_text(flight['LocalTime_STD_8'], flightvalue['Local_Time_STD2'])
        login.input_text(flight['Table_Remarks_8'], flightValue['Table_Remarks'] + "8")
        sleep(2)

        # 保存flightNo
        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path)+'/TestFile/FlightNo.txt'
        name_list = [flightNo1, flightNo3, flightNo5, flightNo6, flightNo7]
        # 'w'表示覆盖写
        with open(filename, "w") as f:
            for i in name_list:
                f.writelines("{}\n".format(i))

        login.input_text(flight['Remarks'], flightValue['Remarks'])
        sleep(2)
        # Upload file
        login.is_click(flight['Upload_Related_Documents'])
        sleep(2)
        login.is_click(flight['Doc_Type_Input'])
        login.input_text(flight['Doc_Type_Input'], flightValue['Document_Type_Others'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(1)
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/sample_file.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        login.is_click(flight['Indefinite'])
        sleep(2)
        login.is_click(flight['UploadButton'])
        sleep(2)
        login.is_click(flight['Click_Condition'])
        sleep(1)
        login.is_click(flight['Preview_And_Submit'])
        sleep(2)
        login.is_click(flight['Click_Submit'])
        sleep(8)
        login.is_click(flight['Submit_OK'])
        sleep(3)

        # 从CPATEST03用户到 Officer1用户切换
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        login.input_user_name(accountValue['OfficerLoginName'])
        login.input_user_password(accountValue['OfficerPassword'])
        login.click_login_button()
        WebDriverWait(drivers, 15, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        login.get_url(ini.url + "#/View/Messages")
        sleep(5)
        login.is_click(flight['Advanced_Search'])
        sleep(1)
        login.input_text(flight['Sender'], accountValue['CpaOfficerLoginName'])
        sleep(1)
        login.is_click(flight['Charter_Passenger'])
        sleep(1)
        login.is_click(flight['Search'])
        sleep(2)
        login.is_click(flight['Message_Ref_No'])
        sleep(6)
        login.is_click(flight['Approve'])
        sleep(2)
        # step 36
        login.is_click(flight['Approve_Proceed'])
        sleep(5)
        login.is_click(flight['Send_Letter'])
        sleep(10)
        resultText = login.element_text(flight['Send_letter_failed_Text'])
        if resultText == 'Failed to send an external email. Procedure.':
            # send 失败
            login.is_click(flight['Send_Letter_failed_ok'])
            login.is_click(flight['Discard'])
            login.is_click(flight['Yes_After_Discard'])
            sleep(3)
        else:
            # send 成功   'Email has been sent.'
            login.is_click(flight['Send_letter_Close'])
            sleep(3)

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_082/test_e2e_0821.py'])
