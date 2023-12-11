import os
import string
import random
import allure
import pytest
import logging

from random import randint
from telnetlib import EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.readconfig import ini
from common.readelement import Element
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

flight = Element('flight_071')
flightValue = ElementValue('flightValue_071')
flightAcc = ElementValue('cad_account')
@allure.feature("TC(ECE)-071 01Create_Application_By_Local_Operator")
class TestCreateApplicationByLocalOperator:
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
        # 跳转到Application-Seasonal Schedule-passenger页面
        login.get_url(ini.url + "?#/ApplicationView/SeasonalSchedule/AddPassengerInfo")
        drivers.implicitly_wait(30)
        sleep(5)
        # assert drivers.find_element_by_css_selector("h2").text == "Create Extra Section Passenger Application"
        now = datetime.now()
        # 获取夏令时开始时间（三月最后一个星期日）
        dst_start = datetime(now.year, 3, 31) - timedelta(days=(datetime(now.year, 3, 31).weekday() + 1) % 7)
        # 获取夏令时结束时间（十月最后一个星期六）
        dst_end = datetime(now.year, 10, 31) - timedelta(days=(datetime(now.year, 10, 31).weekday() + 1) % 7)
        logging.info(dst_start)
        logging.info(dst_end)
        # 夏令时之间
        if (now >= dst_start) and (now < dst_end):
            # 三到十月之间直接1-28号
            if ((now.month > 3) and (now.month < 10)):
                dateFrom = (now+relativedelta(day=1)).strftime("%d/%m/%Y")
                dateTo = (now+relativedelta(day=28)).strftime("%d/%m/%Y")
            #三月夏令时 （今天--今天加27天）
            elif now.month == 3:
                dateFrom = now.strftime("%d/%m/%Y")
                dateTo = (now+relativedelta(days=27)).strftime("%d/%m/%Y")
            #十月从1号到夏令时结束(今天-28天  --  今天)
            elif now.month == 10:
                dateFrom = (now-relativedelta(days=27)).strftime("%d/%m/%Y")
                dateTo = now.strftime("%d/%m/%Y")
        else:
            # 冬令时 3或10俩边
            if(now.month < 3) or (now.month > 10):
                dateFrom = (now+relativedelta(day=1)).strftime("%d/%m/%Y")
                dateTo = (now+relativedelta(day=28)).strftime("%d/%m/%Y")
            # 3月冬令时(减27天，今天)
            if now.month == 3:
                dateFrom = (now-relativedelta(days=27)).strftime("%d/%m/%Y")
                dateTo = now.strftime("%d/%m/%Y")
            #10月冬令时（今天到今天加27天）
            elif now.month == 10:
                dateFrom = now.strftime("%d/%m/%Y")
                dateTo = (now+relativedelta(days=27)).strftime("%d/%m/%Y")
        print(dateFrom, dateTo)
        # flightNoAdd = str(flightValue['Count']+now.day)
        s = string.ascii_letters
        r = random.choice(s)
        #航班号用CPA+4位整数和一个随机字母
        Flight_1 = "CPA"+str(randint(1000, 9999))+r
        Flight_2 = "CPA"+str(randint(1000, 9999))+r
        Flight_3 = "CPA"+str(randint(1000, 9999))+r
        Flight_4 = "CPA"+str(randint(1000, 9999))+r
        Flight_5 = "CPA"+str(randint(1000, 9999))+r
        Flight_6 = "CPA"+str(randint(1000, 9999))+r
        Flight_7 = "CPA"+str(randint(1000, 9999))+r
        Flight_8 = "CPA"+str(randint(1000, 9999))+r
        Flight_9 = "CPA"+str(randint(1000, 9999))+r
        print(Flight_1,Flight_2,Flight_3,Flight_4,Flight_5,Flight_6,Flight_7,Flight_8,Flight_9)
        # 填写Flight Schedules表格信息
        # flight_1(1)
        # login.input_text(flight['FlightNo'], flightValue['FlightNo']+flightNoAdd)
        login.input_text(flight['FlightNo'], Flight_1)
        login.input_text(flight['From'], dateFrom)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To'], dateTo)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1'])
        login.is_click(flight['DOP_2'])
        login.is_click(flight['DOP_3'])
        login.is_click(flight['DOP_4'])
        login.is_click(flight['DOP_5'])
        login.is_click(flight['DOP_6'])
        login.is_click(flight['DOP_7'])

        login.is_click(flight['AircraftType_Select'])
        login.input_text(flight['AircraftType_input'], flightValue['AircraftType1'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats'], flightValue['NoofSeats1'])
        login.input_text(flight['Route'], flightValue['Route1'])
        login.is_click(flight['LocalTime_STD'])
        login.input_text(flight['LocalTime_STD'], flightValue['STD1'])

        # flight 2(时间和dop跟随flight_1的In-out Flight Diff和选择的时间和dop变动，不做设置)
        # login.input_text(flight['FlightNo2'], flightValue['FlightNo2']+flightNoAdd)
        login.input_text(flight['FlightNo2'], Flight_2)
        login.is_click(flight['AircraftType_Select_2'])
        login.input_text(flight['AircraftType_input_2'], flightValue['AircraftType2'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)

        login.input_text(flight['NoofSeats_2'], flightValue['NoofSeats2'])
        login.input_text(flight['Route_2'], flightValue['Route2'])

        login.is_click(flight['LocalTime_STA_2'])
        login.input_text(flight['LocalTime_STA_2'], flightValue['STA2'])

        # flight3
        # login.input_text(flight['FlightNo3'], flightValue['FlightNo3']+flightNoAdd)
        login.input_text(flight['FlightNo3'], Flight_3)
        login.input_text(flight['From3'], dateFrom)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To3'], dateTo)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP3_1'])
        login.is_click(flight['DOP3_2'])
        login.is_click(flight['DOP3_3'])
        login.is_click(flight['DOP3_4'])
        login.is_click(flight['DOP3_5'])
        login.is_click(flight['DOP3_6'])
        login.is_click(flight['DOP3_7'])
        login.is_click(flight['AircraftType_Select_3'])
        login.input_text(flight['AircraftType_input_3'], flightValue['AircraftType3'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_3'], flightValue['NoofSeats3'])
        login.input_text(flight['Route_3'], flightValue['Route3'])
        login.is_click(flight['LocalTime_STD_3'])
        login.input_text(flight['LocalTime_STD_3'], flightValue['STD3'])

        # flight4(跟随3)
        # login.input_text(flight['FlightNo4'], flightValue['FlightNo4']+flightNoAdd)
        login.input_text(flight['FlightNo4'], Flight_4)
        login.is_click(flight['AircraftType_Select_4'])
        login.input_text(flight['AircraftType_input_4'], flightValue['AircraftType4'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[4]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_4'], flightValue['NoofSeats4'])
        login.input_text(flight['Route_4'], flightValue['Route4'])
        login.is_click(flight['LocalTime_STA_4'])
        login.input_text(flight['LocalTime_STA_4'], flightValue['STA4'])

        # flight5
        # login.input_text(flight['FlightNo5'], flightValue['FlightNo5']+flightNoAdd)
        login.input_text(flight['FlightNo5'], Flight_5)
        login.input_text(flight['From5'], dateFrom)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To5'], dateTo)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP5_1'])
        login.is_click(flight['DOP5_2'])
        login.is_click(flight['DOP5_3'])
        login.is_click(flight['DOP5_4'])
        login.is_click(flight['DOP5_5'])
        login.is_click(flight['DOP5_6'])
        login.is_click(flight['DOP5_7'])

        login.is_click(flight['AircraftType_Select_5'])
        login.input_text(flight['AircraftType_input_5'], flightValue['AircraftType5'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_5'], flightValue['NoofSeats5'])
        login.input_text(flight['Route_5'], flightValue['Route5'])
        login.is_click(flight['LocalTime_STD_5'])
        login.input_text(flight['LocalTime_STD_5'], flightValue['STD5'])

        # flight6(跟随5)
        # login.input_text(flight['FlightNo6'], flightValue['FlightNo6']+flightNoAdd)
        login.input_text(flight['FlightNo6'], Flight_6)
        login.is_click(flight['AircraftType_Select_6'])
        login.input_text(flight['AircraftType_input_6'], flightValue['AircraftType6'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_6'], flightValue['NoofSeats6'])
        login.input_text(flight['Route_6'], flightValue['Route6'])
        login.is_click(flight['LocalTime_STA_6'])
        login.input_text(flight['LocalTime_STA_6'], flightValue['STA6'])
        # flight7
        # login.input_text(flight['FlightNo7'], flightValue['FlightNo7']+flightNoAdd)
        login.input_text(flight['FlightNo7'], Flight_7)
        login.input_text(flight['From7'], dateFrom)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To7'], dateTo)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP7_1'])
        login.is_click(flight['DOP7_2'])
        login.is_click(flight['DOP7_3'])
        login.is_click(flight['DOP7_4'])
        login.is_click(flight['DOP7_5'])
        login.is_click(flight['DOP7_6'])
        login.is_click(flight['DOP7_7'])

        login.is_click(flight['AircraftType_Select_7'])
        login.input_text(flight['AircraftType_input_7'], flightValue['AircraftType7'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_7'], flightValue['NoofSeats7'])
        login.input_text(flight['Route_7'], flightValue['Route7'])
        login.is_click(flight['LocalTime_STD_7'])
        login.input_text(flight['LocalTime_STD_7'], flightValue['STD7'])
        # flight8(跟随7)
        # login.input_text(flight['FlightNo8'], flightValue['FlightNo8']+flightNoAdd)
        login.input_text(flight['FlightNo8'], Flight_8)
        login.is_click(flight['AircraftType_Select_8'])
        login.input_text(flight['AircraftType_input_8'], flightValue['AircraftType8'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[8]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_8'], flightValue['NoofSeats8'])
        login.input_text(flight['Route_8'], flightValue['Route8'])
        login.is_click(flight['LocalTime_STA_8'])
        login.input_text(flight['LocalTime_STA_8'], flightValue['STA8'])

        login.is_click(flight['Confirm'])
        sleep(1)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        login.is_click(flight['Submit'])
        sleep(7)
        login.is_click(flight['SubmitLessorNo'])
        sleep(3)
        login.is_click(flight['SubmitLessorNo'])
        sleep(10)
        # assert drivers.find_element_by_css_selector("h2").text == "Search Application"
        refNoValue = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[5]/div/div[3]/table/tbody/tr[1]/td[4]/div/a/span/span")
        #保存refNo
        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path)+'/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        with open(filename, 'w') as f:
            f.write(refNoValue.text)
        #保存flightNo
        name_list = [Flight_1, Flight_2, Flight_3, Flight_4,
                     Flight_5, Flight_6, Flight_7, Flight_8]
        filename2 = os.path.dirname(current_path)+'/TestData/Out/FlightNo.txt'
        with open(filename2, "w") as f:
            for i in name_list:
                f.writelines("{}\n".format(i))

        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_071/test_e2e_0411.py'])