import pytest
import allure
from page.webpage import sleep
from common.readconfig import ini
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from common.readelement import Element
import string
import random
import os
from selenium.webdriver.common.keys import Keys
from random import randint
flight=Element('flight_012')
flightvalue=ElementValue('flightvalue_012')

@allure.feature("TC(ECE)-012 Local Operator Create Scheduled All-Cargo Application with invalid data")
class TestCreateAllCargo:
    @pytest.fixture(scope='function', autouse=True)
    def open_codeshare(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create Scheduled All-Cargo Application with invalid data")
    # 每次测试前需要在flightvalue.yaml文件中更新FlightNo和TemplateName值，不然会报重复航班号和模板名错误
    def test_087(self, drivers):
        """登录CPATEST03用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
          login.is_click(flight["Logout"])
          login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name("CPATEST03")
            login.input_user_password("12345678a")
            login.click_login_button()


        # '''跳转到#/ApplicationView/SeasonalSchedule/AddCargoInfo页面'''
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(2)

        # # 表单
        s = string.ascii_letters
        r = random.choice(s)
        # 航班号用CPA+4位整数和一个随机字母
        Flight_1 = "CPA" + str(randint(1000, 9999)) + r
        Flight_2 = "CPA" + str(randint(1000, 9999)) + r

        login.input_text(flight['row1Flight'], Flight_1)
        login.input_text(flight['row1From'], flightvalue['row1From'])
        login.input_text(flight['row1To'], flightvalue['row1To'])
        login.is_click(flight['row1Dop'])
        login.is_click(flight['row1AirTypei'])
        sleep(1)
        login.input_text(flight['row1AirTypeInput'], flightvalue['row1AirTypeInput'])
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['row1Cargo'], flightvalue['row1Cargo'])
        login.input_text(flight['row1Route'], "HKG-LAX")
        login.is_click(flight['row1Local'])
        login.input_text(flight['row1Local'], flightvalue['row1Local'])

        #row2
        login.input_text(flight['row2Flight'], Flight_2)
        login.is_click(flight['row2InoutTypeI'])
        sleep(1)
        login.input_text(flight['row2InoutTypeInput'], flightvalue['row2InoutTypeInput'])
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)

        login.is_click(flight['row2AirTypeI'])
        sleep(1)
        login.input_text(flight['row2AirTypeInput'], flightvalue['row2AirTypeInput'])
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['row2Cargo'], flightvalue['row2Cargo'])

        login.input_text(flight['row2Route'], "LAX-HKG")
        login.is_click(flight['row2Local'])
        login.input_text(flight['row2Local'], flightvalue['row2Local'])

        login.input_text(flight['Remarks'], flightvalue['Remarks'])

        login.is_click(flight['confirmButton'])
        login.is_click(flight['SaveAsDraft'])
        sleep(1)
        login.is_click(flight['SaveAsTemplate'])
        sleep(1)
        login.input_text(flight['TemplateName'], "TemplateName")
        login.input_text(flight['Description'], "Description")
        try:
            login.is_click(flight['TemplateSave'])
            sleep(2)
            login.is_click(flight['CancelButton'])
        except Exception:
            print("Template not duplicate")
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['SubmitButton'])
        drivers.implicitly_wait(30)
        login.is_click(flight['NoButton'])
        sleep(1)
        login.is_click(flight['NoSubmit'])
        sleep(5)

        # 航班号用CPA+4位整数和一个随机字母
        Flight_1 = "CPA" + str(randint(1000, 9999)) + r
        Flight_2 = "CPA" + str(randint(1000, 9999)) + r
        Flight_3 = "CPA" + str(randint(1000, 9999)) + r
        Flight_4 = "CPA" + str(randint(1000, 9999)) + r
        '''跳转到#/ApplicationView/SeasonalSchedule/AddCargoInfo页面'''
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        #row1
        login.input_text(flight['Step5Row1Flight'],Flight_1)
        login.input_text(flight['Step5Row1From'], "01/11/2023")
        login.input_text(flight['Step5Row1To'], "30/11/2023")
        login.is_click(flight['Step5Row1Dop'])
        login.is_click(flight['Step5Row1AirTypei'])
        sleep(1)
        login.input_text(flight['Step5Row1AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step5Row1Cargo'], "1000")
        login.input_text(flight['Step5Row1Route'], "HKG-LAX")
        # row2
        login.input_text(flight['Step5row2Flight'], Flight_2)
        login.is_click(flight['Step5row2InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step5row2InoutTypeInput'], "+0")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step5row2AirTypeI'])
        sleep(1)
        login.input_text(flight['Step5row2AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step5row2Cargo'], "1000")
        login.input_text(flight['Step5row2Route'], "LAX-HKG")

        #row3
        login.input_text(flight['Step5Row3Flight'], Flight_3)
        login.input_text(flight['Step5Row3From'], "01/11/2023")
        login.input_text(flight['Step5Row3To'], "30/11/2023")
        login.is_click(flight['Step5Row3Dop'])
        login.is_click(flight['Step5Row3AirTypei'])
        sleep(1)
        login.input_text(flight['Step5Row3AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step5Row3Cargo'], "1000")
        login.input_text(flight['Step5Row3Route'], "HKG-LAX")
        login.is_click(flight['Step5Row3STD'])
        login.input_text(flight['Step5Row3STD'], "2590")
        login.is_click(flight['Step5row4Flight'])
        sleep(1)
        login.is_click(flight['Step5Row3STDOK'])
        login.input_text(flight['Step5Row3STD'], "1111")

        #row4
        login.input_text(flight['Step5row4Flight'], Flight_4)
        login.is_click(flight['Step5row4InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step5row4InoutTypeInput'], "+0")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[4]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step5row4AirTypeI'])
        sleep(1)
        login.input_text(flight['Step5row4AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[4]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step5row4Cargo'], "1000")
        login.input_text(flight['Step5row4Route'], "LAX-HKG")
        login.is_click(flight['Step5row4STA'])
        login.input_text(flight['Step5row4STA'], "11XX")
        login.is_click(flight['Step5row5F'])
        login.is_click(flight['Step5Row4STAOK'])
        login.input_text(flight['Step5row4STA'], "1111")

        # login.input_text(flight['Remarks'], "STA STD Testing")
        login.input_text(flight['Remarks'], flightvalue['Remarks'])

        login.is_click(flight['confirmButton'])
        login.is_click(flight['SaveAsDraft'])
        sleep(5)
        #提示stdsta
        login.input_text(flight['Step5Row1STD'], "1111")
        login.input_text(flight['Step5Row2STA'], "1111")
        login.is_click(flight['SaveAsDraft'])


        login.is_click(flight['SaveAsTemplate'])
        sleep(2)
        login.input_text(flight['TemplateName'], "TemplateName")
        login.input_text(flight['Description'], "Description")
        try:
            login.is_click(flight['TemplateSave'])
            sleep(2)
            login.is_click(flight['CancelButton'])
        except Exception:
            print("Template not duplicate")
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['SubmitButton'])
        drivers.implicitly_wait(30)
        login.is_click(flight['NoButton'])
        sleep(1)
        login.is_click(flight['NoSubmit'])
        sleep(5)

        '''9'''
        Flight_1 = "CPA" + str(randint(1000, 9999)) + r
        Flight_2 = "CPA" + str(randint(1000, 9999)) + r

        '''跳转到#/ApplicationView/SeasonalSchedule/AddCargoInfo页面'''
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        login.input_text(flight['Step9Row1Flight'], Flight_1)

        login.input_text(flight['Step9Row1From'], "01/11/2023")
        login.input_text(flight['Step9Row1To'], "30/11/2023")
        login.is_click(flight['Step9Row1Dop'])

        login.is_click(flight['Step9Row1AirTypei'])
        sleep(1)
        login.input_text(flight['Step9Row1AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step9Row1Cargo'], "1000")
        login.input_text(flight['Step9Row1Route'], "HKG-LAX")
        login.is_click(flight['Step9Row1STD'])
        login.input_text(flight['Step9Row1STD'], "1030")

        login.input_text(flight['Step9row2Flight'], Flight_2)
        login.is_click(flight['Step9row2InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step9row2InoutTypeInput'], "+0")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step9row2AirTypeI'])
        sleep(1)
        login.input_text(flight['Step9row2AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step9row2Cargo'], "1000")
        login.input_text(flight['Step9row2Route'], "LAX-HKG")
        login.is_click(flight['Step9row2STA'])
        login.input_text(flight['Step9row2STA'], "1930")
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])
        sleep(1)

        login.is_click(flight['confirmButton'])
        login.is_click(flight['SaveAsDraft'])
        sleep(5)

        login.is_click(flight['SeasonI'])
        sleep(1)
        login.is_click(flight['SeasonI'])
        sleep(1)
        login.input_text(flight['SeasonInput'], "Winter 2023")
        drivers.find_element_by_xpath(
            "//div[contains(label,'Season')]/div/div/div/input").send_keys(
            Keys.ENTER)

        login.is_click(flight['SaveAsDraft'])
        login.is_click(flight['SaveAsTemplate'])
        sleep(2)
        login.input_text(flight['TemplateName'], "TemplateName")
        login.input_text(flight['Description'], "Description")
        try:
            login.is_click(flight['TemplateSave'])
            sleep(2)
            login.is_click(flight['CancelButton'])
        except Exception:
            print("Template not duplicate")
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['SubmitButton'])
        drivers.implicitly_wait(30)
        login.is_click(flight['NoButton'])
        sleep(1)
        login.is_click(flight['NoSubmit'])
        sleep(5)


        '''13'''
        Flight_1 = "CPA" + str(randint(1000, 9999)) + r
        Flight_2 = "CPA" + str(randint(1000, 9999)) + r
        Flight_3 = "CPA" + str(randint(1000, 9999)) + r
        Flight_4 = "CPA" + str(randint(1000, 9999)) + r
        Flight_5 = "CPA" + str(randint(1000, 9999)) + r
        Flight_6 = "CPA" + str(randint(1000, 9999)) + r
        Flight_7 = "CPA" + str(randint(1000, 9999)) + r
        Flight_8 = "CPA" + str(randint(1000, 9999)) + r
        Flight_9 = "CPA" + str(randint(1000, 9999)) + r
        Flight_10 = "CPA" + str(randint(1000, 9999)) + r
        Flight_11 = "CPA" + str(randint(1000, 9999)) + r
        Flight_12 = "CPA" + str(randint(1000, 9999)) + r
        Flight_13 = "CPA" + str(randint(1000, 9999)) + r
        Flight_14 = "CPA" + str(randint(1000, 9999)) + r
        Flight_15 = "CPA" + str(randint(1000, 9999)) + r
        Flight_16 = "CPA" + str(randint(1000, 9999)) + r

        '''跳转到#/ApplicationView/SeasonalSchedule/AddCargoInfo页面'''
        #row1
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        login.is_click(flight['AddRow'])
        sleep(2)
        login.input_text(flight['Step13Row1Flight'], Flight_1)

        login.input_text(flight['Step13Row1From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row1To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13Row1Dop'])

        login.is_click(flight['Step13Row1AirTypei'])
        sleep(1)
        login.input_text(flight['Step13Row1AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row1Cargo'], "1000")
        # login.input_text(flight['Step13Row1Route'], "HKG-LAX")
        # login.is_click(flight['Step13Row1STD'])
        # login.input_text(flight['Step13Row1STD'], "1030")

        #row2
        login.input_text(flight['Step13row2Flight'], Flight_2)
        login.is_click(flight['Step13row2InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step13row2InoutTypeInput'], "+1")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13row2AirTypeI'])
        sleep(1)
        login.input_text(flight['Step13row2AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13row2Cargo'], "1000")
        # login.input_text(flight['Step13row2Route'], "LAX-HKG")
        # login.is_click(flight['Step13row2STA'])
        # login.input_text(flight['Step13row2STA'], "1930")

        #row3
        login.input_text(flight['Step13Row3Flight'], Flight_3)

        login.input_text(flight['Step13Row3From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[3]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row3To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[3]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13Row3Dop'])
        sleep(2)
        login.is_click(flight['Step13Row3AirTypei'])
        sleep(2)
        login.input_text(flight['Step13Row3AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row3Cargo'], "1000")
        login.input_text(flight['Step13Row3Route'], "HKGG-SIN")
        login.is_click(flight['Step13Row3STD'])
        sleep(1)
        login.is_click(flight['InvalidRouteOK'])
        login.input_text(flight['Step13Row3Route'], "HKG-SIN")

        # login.input_text(flight['Step13Row3STD'], "1030")

        #row4
        login.input_text(flight['Step13row4Flight'], Flight_4)
        login.is_click(flight['Step13row4InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step13row4InoutTypeInput'], "+0")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[4]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13row4AirTypeI'])
        sleep(1)
        login.input_text(flight['Step13row4AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[4]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13row4Cargo'], "1000")
        login.input_text(flight['Step13row4Route'], "SIN-HKG")
        login.is_click(flight['Step13row4STA'])
        login.input_text(flight['Step13row4STA'], "1000")

        #row5
        login.input_text(flight['Step13Row5Flight'], Flight_5)

        login.input_text(flight['Step13Row5From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[5]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row5To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[5]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13Row5Dop'])

        login.is_click(flight['Step13Row5AirTypei'])
        sleep(1)
        login.input_text(flight['Step13Row5AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[5]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row5Cargo'], "1000")
        login.input_text(flight['Step13Row5Route'], "HKG*-SIN")
        login.is_click(flight['Step13Row5STD'])
        sleep(1)
        login.is_click(flight['InvalidRouteOK'])
        login.input_text(flight['Step13Row5Route'], "HKG-SIN")

        #row6
        login.input_text(flight['Step13row6Flight'], Flight_6)
        login.is_click(flight['Step13row6InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step13row6InoutTypeInput'], "+1")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[6]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13row6AirTypeI'])
        sleep(1)
        login.input_text(flight['Step13row6AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[6]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13row6Cargo'], "1000")
        login.input_text(flight['Step13row6Route'], "SIN-HKG")

        #row7
        login.input_text(flight['Step13Row7Flight'], Flight_7)

        login.input_text(flight['Step13Row7From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[7]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row7To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[7]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13Row7Dop'])

        login.is_click(flight['Step13Row7AirTypei'])
        sleep(1)
        login.input_text(flight['Step13Row7AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[7]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row7Cargo'], "1000")
        login.input_text(flight['Step13Row7Route'], "HKG-HKG")
        login.is_click(flight['Step13Row7STD'])
        login.is_click(flight['InvalidRouteOK'])
        login.input_text(flight['Step13Row7Route'], "HKG-SIN")
        login.is_click(flight['Step13Row7STD'])
        login.input_text(flight['Step13Row7STD'], "1000")

        #row8
        login.input_text(flight['Step13row8Flight'], Flight_8)
        login.is_click(flight['Step13row8InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step13row8InoutTypeInput'], "+0")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[8]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13row8AirTypeI'])
        sleep(1)
        login.input_text(flight['Step13row8AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[8]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13row8Cargo'], "1000")
        login.input_text(flight['Step13row8Route'], "SIN-HKG")
        login.is_click(flight['Step13row8STA'])
        login.input_text(flight['Step13row8STA'], "1000")

        #row9
        login.input_text(flight['Step13Row9Flight'], Flight_9)

        login.input_text(flight['Step13Row9From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[9]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row9To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[9]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13Row9Dop'])

        login.is_click(flight['Step13Row9AirTypei'])
        sleep(1)
        login.input_text(flight['Step13Row9AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[9]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row9Cargo'], "1000")
        login.input_text(flight['Step13Row9Route'], "SIN-HKG")
        login.is_click(flight['Step13Row9STA'])
        login.input_text(flight['Step13Row9STA'], "1000")

        #row10
        login.input_text(flight['Step13row10Flight'], Flight_10)
        login.is_click(flight['Step13row10InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step13row10InoutTypeInput'], "+1")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[10]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13row10AirTypeI'])
        sleep(1)
        login.input_text(flight['Step13row10AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[10]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13row10Cargo'], "1000")
        login.input_text(flight['Step13row10Route'], "LAX-HKG")
        login.is_click(flight['Step13row10STA'])
        login.input_text(flight['Step13row10STA'], "1000")

        #row11
        login.input_text(flight['Step13Row11Flight'], Flight_11)

        login.input_text(flight['Step13Row11From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[11]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row11To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[11]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13Row11Dop'])

        login.is_click(flight['Step13Row11AirTypei'])
        sleep(1)
        login.input_text(flight['Step13Row11AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[11]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row11Cargo'], "1000")
        login.input_text(flight['Step13Row11Route'], "SIN-HKG-LAX-MEM")
        login.is_click(flight['Step13Row11STA'])
        login.input_text(flight['Step13Row11STA'], "1000")
        login.is_click(flight['Step13Row11STD'])
        login.input_text(flight['Step13Row11STD'], "1000")

        #row12
        login.input_text(flight['Step13row12Flight'], Flight_2)
        login.is_click(flight['Step13row12InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step13row12InoutTypeInput'], "+1")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[12]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13row12AirTypeI'])
        sleep(1)
        login.input_text(flight['Step13row12AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[12]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13row12Cargo'], "1000")
        login.input_text(flight['Step13row12Route'], "HKG-MEM")
        login.is_click(flight['Step13row12STD'])
        login.input_text(flight['Step13row12STD'], "1000")

        #row13
        login.input_text(flight['Step13Row13Flight'], Flight_13)

        login.input_text(flight['Step13Row13From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[13]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row13To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[13]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13Row13Dop'])

        login.is_click(flight['Step13Row13AirTypei'])
        sleep(1)
        login.input_text(flight['Step13Row13AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[13]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row13Cargo'], "1000")
        login.input_text(flight['Step13Row13Route'], "SIN-HKG-LAX")
        login.is_click(flight['Step13Row13STA'])
        login.input_text(flight['Step13Row13STA'], "1000")
        login.is_click(flight['Step13Row13STD'])
        login.input_text(flight['Step13Row13STD'], "1000")

        #row14
        login.input_text(flight['Step13row14Flight'], Flight_14)
        login.is_click(flight['Step13row14InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step13row14InoutTypeInput'], "+1")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[14]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13row14AirTypeI'])
        sleep(1)
        login.input_text(flight['Step13row14AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[14]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13row14Cargo'], "1000")
        login.input_text(flight['Step13row14Route'], "HKG-MEM")
        login.is_click(flight['Step13row14STD'])
        login.input_text(flight['Step13row14STD'], "1000")

        #row15
        login.input_text(flight['Step13Row15Flight'], Flight_15)

        login.input_text(flight['Step13Row15From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[15]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row15To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[15]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13Row15Dop'])

        login.is_click(flight['Step13Row15AirTypei'])
        sleep(1)
        login.input_text(flight['Step13Row15AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[15]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row15Cargo'], "1000")
        login.input_text(flight['Step13Row15Route'], "SIN*-HKG")
        login.is_click(flight['Step13row16Flight'])
        sleep(1)
        login.is_click(flight['Confirm'])
        # login.is_click(flight['Step13Row15STA'])
        # login.input_text(flight['Step13Row15STA'], "1000")

        #row16
        login.input_text(flight['Step13row16Flight'], Flight_16)
        login.is_click(flight['Step13row16InoutTypeI'])
        sleep(1)
        login.input_text(flight['Step13row16InoutTypeInput'], "+1")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[16]/td[2]/div/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step13row16AirTypeI'])
        sleep(1)
        login.input_text(flight['Step13row16AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[16]/td[12]/div/span/div/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13row16Cargo'], "1000")
        login.input_text(flight['Step13row16Route'], "HKG-MEM")
        # login.is_click(flight['Step13row16STD'])
        # login.input_text(flight['Step13row16STD'], "1000")

        login.is_click(flight['confirmButton'])

        login.is_click(flight['SaveAsDraft'])
        sleep(10)
        #填空缺
        login.is_click(flight['Step13Row1DOP2'])
        login.is_click(flight['Step13Row1DOP3'])
        login.input_text(flight['Step13Row1Route2'], "HKG-SIN")
        login.is_click(flight['Step13Row1STD'])
        login.input_text(flight['Step13Row1STD'], "1000")

        login.input_text(flight['Step13row2Route2'], "SIN-HKG")
        login.is_click(flight['Step13row2Sta'])
        login.input_text(flight['Step13row2Sta'], "1000")

        login.is_click(flight['Step13Row3STD'])
        login.input_text(flight['Step13Row3STD'], "1000")

        login.is_click(flight['Step13Row5STD'])
        login.input_text(flight['Step13Row5STD'], "1000")

        login.is_click(flight['Step13row6STA'])
        login.input_text(flight['Step13row6STA'], "1000")

        login.input_text(flight['Step13row10Route2'], "HKG-SIN")
        login.is_click(flight['Step13row10STD'])
        login.input_text(flight['Step13row10STD'], "1000")

        login.input_text(flight['Step13Row11Route2'], "MEM-HKG")
        login.is_click(flight['Step13Row11STA'])
        login.input_text(flight['Step13Row11STA'], "1000")

        login.input_text(flight['Step13Row13Route2'], "MEM-HKG")
        login.is_click(flight['Step13Row13STA'])
        login.input_text(flight['Step13Row13STA'], "1000")

        login.is_click(flight['Step13Row15STA'])
        login.input_text(flight['Step13Row15STA'], "1000")

        login.is_click(flight['Step13row16STD'])
        login.input_text(flight['Step13row16STD'], "1000")
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])

        #重新提交
        login.is_click(flight['SaveAsDraft'])
        sleep(2)


        login.is_click(flight['SaveAsTemplate'])
        sleep(2)
        login.input_text(flight['TemplateName'], "TemplateName")
        login.input_text(flight['Description'], "Description")
        try:
            login.is_click(flight['TemplateSave'])
            sleep(2)
            login.is_click(flight['CancelButton'])
        except Exception:
            print("Template not duplicate")
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['SubmitButton'])
        drivers.implicitly_wait(30)
        login.is_click(flight['NoButton'])
        sleep(1)
        login.is_click(flight['NoSubmit'])
        sleep(5)

        #17
        '''跳转到#/ApplicationView/SeasonalSchedule/AddCargoInfo页面'''
        #row1
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        Flight_1 = "CPA" + str(randint(1000, 9999)) + r
        Flight_2 = "CPA" + str(randint(1000, 9999)) + r
        login.input_text(flight['Step13Row1Flight'], Flight_1)

        login.input_text(flight['Step13Row1From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row1To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step17Row1DOP1'])
        login.is_click(flight['Step17Row1DOP2'])
        login.is_click(flight['Step17Row1DOP3'])
        login.is_click(flight['Step17Row1DOP4'])
        login.is_click(flight['Step17Row1DOP5'])
        login.is_click(flight['Step17Row1DOP6'])
        login.is_click(flight['Step17Row1DOP7'])

        login.is_click(flight['Step17Row1AirTypeI'])
        sleep(1)
        login.input_text(flight['Step17Row1AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step17Row1CarGo'], "2000")
        login.input_text(flight['Step17Row1Route'], "HKG-LAX")
        login.is_click(flight['Step17Row1STD'])
        login.input_text(flight['Step17Row1STD'], "1030")

        #row2
        login.input_text(flight['Step17Row2Flight'], Flight_2)
        login.is_click(flight['Step17Row2AirTypeI'])
        sleep(1)
        login.input_text(flight['Step17Row2AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step17Row2Cargo'], "2000")
        login.input_text(flight['Step17Row2Route'], "LAX-HKG")
        login.is_click(flight['Step17Row2STA'])
        login.input_text(flight['Step17Row2STA'], "1630")

        # login.input_text(flight['Remarks'], "Flight Duplication Check #1")
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])

        login.is_click(flight['UploadFileButton'])
        sleep(1)
        login.is_click(flight['UploadInput'])
        sleep(2)
        login.input_text(flight['UploadInput'], "Others")
        drivers.find_element_by_xpath(
            "//input[@id='testNewDocumentUpload']").send_keys(
            Keys.ENTER)
        login.is_click(flight['ExDate'])
        login.is_click(flight['Upload'])


        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/sample_file.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(1)
        login.is_click(flight['Upload'])
        sleep(1)

        login.is_click(flight['confirmButton'])

        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['SubmitButton'])
        drivers.implicitly_wait(30)
        login.is_click(flight['NoButton'])
        sleep(1)
        login.is_click(flight['NoSubmit'])

        # 审批
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['OfficerUserName'])
            login.input_user_password(flightvalue['OfficerPassword'])
            login.click_login_button()

        '''审批数据'''
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(2)
        login.is_click(flight["AdvancedSearch"])
        sleep(2)
        login.is_click(flight["AllCargoCheck"])
        login.is_click(flight["Search"])
        sleep(1)
        login.is_click(flight["FirshRecord"])
        sleep(2)
        login.is_click(flight["ApproveButton"])
        sleep(2)
        login.is_click(flight["ConfirmButton"])
        sleep(1)
        login.is_click(flight["OKbutton"])
        login.is_click(flight["DiscardButton"])
        login.is_click(flight["YesButton"])

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name("CPATEST03")
            login.input_user_password("12345678a")
            login.click_login_button()

        '''跳转到#/ApplicationView/SeasonalSchedule/AddCargoInfo页面 验证重复flight'''
        # #row1
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        login.input_text(flight['Step13Row1Flight'], Flight_1)

        login.input_text(flight['Step13Row1From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row1To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step17Row1DOP1'])
        login.is_click(flight['Step17Row1DOP2'])
        login.is_click(flight['Step17Row1DOP3'])
        login.is_click(flight['Step17Row1DOP4'])
        login.is_click(flight['Step17Row1DOP5'])
        login.is_click(flight['Step17Row1DOP6'])
        login.is_click(flight['Step17Row1DOP7'])

        login.is_click(flight['Step17Row1AirTypeI'])
        sleep(1)
        login.input_text(flight['Step17Row1AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step17Row1CarGo'], "2000")
        login.input_text(flight['Step17Row1Route'], "HKG-LAX")
        login.is_click(flight['Step17Row1STD'])
        login.input_text(flight['Step17Row1STD'], "1030")

        #row2
        login.input_text(flight['Step17Row2Flight'], Flight_2)
        login.is_click(flight['Step17Row2AirTypeI'])
        sleep(1)
        login.input_text(flight['Step17Row2AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step17Row2Cargo'], "2000")
        login.input_text(flight['Step17Row2Route'], "LAX-HKG")
        login.is_click(flight['Step17Row2STA'])
        login.input_text(flight['Step17Row2STA'], "1630")

        # login.input_text(flight['Remarks'], "Flight Duplication Check #1")
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])

        login.is_click(flight['confirmButton'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['SubmitButton'])
        sleep(5)
        login.is_click(flight['BackAndModify'])

        '''21'''
        #row3
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        login.input_text(flight['Step13Row3Flight'], Flight_1)

        login.input_text(flight['Step13Row3From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[3]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row3To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[3]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step21Row3DOP1'])
        login.is_click(flight['Step21Row3DOP2'])
        login.is_click(flight['Step21Row3DOP3'])
        login.is_click(flight['Step21Row3DOP4'])
        login.is_click(flight['Step21Row3DOP5'])
        login.is_click(flight['Step21Row3DOP6'])
        login.is_click(flight['Step21Row3DOP7'])

        login.is_click(flight['Step21Row3AirTypeI'])
        sleep(1)
        login.input_text(flight['Step21Row3AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step21Row3CarGo'], "2000")
        login.input_text(flight['Step21Row3Route'], "HKG-LAX")
        login.is_click(flight['Step21Row3STD'])
        login.input_text(flight['Step21Row3STD'], "1030")

        # row4
        login.input_text(flight['Step21Row4Flight'], Flight_2)
        login.is_click(flight['Step21Row4AirTypeI'])
        sleep(1)
        login.input_text(flight['Step21Row4AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[4]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step21Row4Cargo'], "2000")
        login.input_text(flight['Step21Row4Route'], "LAX-HKG")
        login.is_click(flight['Step21Row4STA'])
        login.input_text(flight['Step21Row4STA'], "1630")

        # login.input_text(flight['Remarks'], "Flight Duplication Check #2")
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])

        login.is_click(flight['PreviewAndSubmit'])
        sleep(1)
        login.is_click(flight['SubmitButton'])
        sleep(5)
        login.is_click(flight['BackAndModify'])
        sleep(10)

        '''25'''
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name("CPATEST03")
            login.input_user_password("12345678a")
            login.click_login_button()
        '''跳转到#/ApplicationView/SeasonalSchedule/AddCargoInfo页面'''
        #row1
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        Flight_1 = "CPA" + str(randint(1000, 9999)) + r
        Flight_2 = "CPA" + str(randint(1000, 9999)) + r
        login.input_text(flight['Step13Row1Flight'], Flight_1)

        login.input_text(flight['Step13Row1From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row1To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step17Row1DOP1'])
        login.is_click(flight['Step17Row1DOP2'])
        login.is_click(flight['Step17Row1DOP3'])
        login.is_click(flight['Step17Row1DOP4'])
        login.is_click(flight['Step17Row1DOP5'])
        login.is_click(flight['Step17Row1DOP6'])
        login.is_click(flight['Step17Row1DOP7'])

        login.is_click(flight['Step17Row1AirTypeI'])
        sleep(1)
        login.input_text(flight['Step17Row1AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step17Row1CarGo'], "2000")
        login.input_text(flight['Step17Row1Route'], "HKG-LAX")
        login.is_click(flight['Step17Row1STD'])
        login.input_text(flight['Step17Row1STD'], "1030")

        #row2
        login.input_text(flight['Step17Row2Flight'], Flight_2)
        login.is_click(flight['Step17Row2AirTypeI'])
        sleep(1)
        login.input_text(flight['Step17Row2AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step17Row2Cargo'], "2000")
        login.input_text(flight['Step17Row2Route'], "LAX-HKG")
        login.is_click(flight['Step17Row2STA'])
        login.input_text(flight['Step17Row2STA'], "1630")

        # login.input_text(flight['Remarks'], "Flight Duplication Check #3")
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])

        login.is_click(flight['UploadFileButton'])
        sleep(1)
        login.is_click(flight['UploadInput'])
        sleep(2)
        login.input_text(flight['UploadInput'], "Others")
        drivers.find_element_by_xpath(
            "//input[@id='testNewDocumentUpload']").send_keys(
            Keys.ENTER)
        login.is_click(flight['ExDate'])
        login.is_click(flight['Upload'])


        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/sample_file.pdf"
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(1)
        login.is_click(flight['Upload'])
        sleep(1)

        login.is_click(flight['confirmButton'])

        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['SubmitButton'])
        drivers.implicitly_wait(30)
        login.is_click(flight['NoButton'])
        sleep(1)
        login.is_click(flight['NoSubmit'])

        # 审批
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightvalue['OfficerUserName'])
            login.input_user_password(flightvalue['OfficerPassword'])
            login.click_login_button()

        '''审批数据'''
        login.get_url(ini.url + "#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(2)
        login.is_click(flight["AdvancedSearch"])
        sleep(2)
        login.is_click(flight["AllCargoCheck"])
        login.is_click(flight["Search"])
        sleep(1)
        login.is_click(flight["FirshRecord"])
        sleep(2)
        login.is_click(flight["ApproveButton"])
        sleep(2)
        login.is_click(flight["ConfirmButton"])
        sleep(1)
        login.is_click(flight["OKbutton"])
        login.is_click(flight["DiscardButton"])
        login.is_click(flight["YesButton"])

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name("CPATEST03")
            login.input_user_password("12345678a")
            login.click_login_button()

        '''跳转到#/ApplicationView/SeasonalSchedule/AddCargoInfo页面 验证重复flight'''
        # #row1
        login.get_url(ini.url + "#/ApplicationView/SeasonalSchedule/AddCargoInfo")
        drivers.implicitly_wait(30)
        sleep(2)
        login.input_text(flight['Step13Row1Flight'], Flight_1)

        login.input_text(flight['Step13Row1From'], "01/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step13Row1To'], "30/11/2023")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(
            Keys.ENTER)
        login.is_click(flight['Step17Row1DOP1'])


        login.is_click(flight['Step25Row1AriTypei'])
        sleep(1)
        login.input_text(flight['Step25Row1AriTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step25Row1Cargo'], "100")
        login.input_text(flight['Step25Row1Route'], "HKG-LAX")
        login.is_click(flight['Step25Row1STD'])
        login.input_text(flight['Step25Row1STD'], "1230")

        #row2
        login.input_text(flight['Step17Row2Flight'], Flight_2)
        login.is_click(flight['Step17Row2AirTypeI'])
        sleep(1)
        login.input_text(flight['Step17Row2AirTypeInput'], "77F")
        drivers.find_element_by_xpath(
            "//table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(
            Keys.ENTER)
        login.input_text(flight['Step17Row2Cargo'], "100")
        login.input_text(flight['Step17Row2Route'], "LAX-HKG")
        login.is_click(flight['Step17Row2STA'])
        login.input_text(flight['Step17Row2STA'], "1730")

        # login.input_text(flight['Remarks'], "Flight Duplication Check #3")
        sleep(1)
        login.input_text(flight['Remarks'], flightvalue['Remarks'])

        login.is_click(flight['confirmButton'])
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['SubmitButton'])
        sleep(5)
        login.is_click(flight['Step25SubmitNO'])
        login.is_click(flight['BackAndModify'])
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])



        sleep(10)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_012/test_e2e_012.py'])
