import os
import time

import allure
import pytest
import logging

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
@allure.feature("TC(ECE)-071 03Create application by Local Operator")
class TestCreateChangeApplicationByLocalOperator:
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
        WebDriverWait(drivers, 30, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))
        # 跳转到Application-Seasonal Schedule-passenger页面
        login.get_url(ini.url + "?#/ApplicationView/ScheduleChange/FlightSchedule")
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
        #获取查询数据
        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path)+'/TestData/Out/FlightNo.txt'
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
                    flightNo31 = line.rstrip()
                    print(flightNo31)
                if num == 5:
                    flightNo32 = line.rstrip()
                    print(flightNo32)
                if num == 6:
                    flightNo4 = line.rstrip()
                    print(flightNo4)
        #revise 1
        #查询flight1
        login.input_text(flight['ChangeCallSign'], flightNo1)
        login.input_text(flight['ChangeEffFrom'], dateFrom)
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[1]/input"
        ).send_keys(Keys.ENTER)
        dateTo1 = (now+relativedelta(days=20)).strftime("%d/%m/%Y")
        login.input_text(flight['ChangeEffTo'], dateTo1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input"
        ).send_keys(Keys.ENTER)
        login.is_click(flight["ChangeAppTypeSP"])
        login.is_click(flight["ChangeDisplayByPeriod"])
        login.is_click(flight["ChangeSearchBTU"])
        sleep(3)
        #添加到revise
        login.is_click(flight["ChangeSelectSearch1"])
        sleep(1)
        login.is_click(flight["ChangeRevise"])
        #改数据
        login.is_click(flight["ChangeDop1_1"])
        sleep(1)
        login.is_click(flight["ChangeDop1_3"])
        sleep(1)
        login.is_click(flight["ChangeDop1_5"])
        sleep(1)
        login.is_click(flight["ChangeDop1_7"])
        sleep(2)
        # login.is_click(flight["ChangeAircraftType_Select1"])
        # sleep(2)
        # login.is_click(flight["ChangeAircraftType_Select1"])
        sleep(1)
        # login.input_text(flight['ChangeAircraftType_Input1'], '141')
        # sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[15]/div/span/div/div/input"
        ).send_keys(Keys.ENTER)
        sleep(1)
        login.input_text(flight['ChangeSeats1'], '300')
        sleep(1)
        #移动横轴滚动条到右侧修改数据
        scrollbar = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]"
        )
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        sleep(3)
        #获取route1的位置，然后js修改其值
        ChangeRoute1 = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[20]/div/span/div/input"
        )
        drivers.execute_script("arguments[0].value = 'HKG-SFO';", ChangeRoute1)
        login.input_text(flight['ChangeStd1'], '1130')
        #移动横轴滚动条到左侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = 0", scrollbar)
        sleep(3)
        login.is_click(flight["ChangeAircraftType_Select2"])
        sleep(1)
        login.is_click(flight["ChangeAircraftType_Select2"])
        login.input_text(flight['ChangeAircraftType_Input2'], '143')
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[14]/div/span/div/div[1]/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['ChangeSeats2'], '350')
        #移动横轴滚动条到右侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        sleep(3)
        #获取route2的位置，然后js修改其值
        ChangeRoute2 = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[19]/div/span/div/input"
        )
        drivers.execute_script("arguments[0].value = 'SFO-HKG';", ChangeRoute2)
        login.input_text(flight['ChangeSta2'], '1930')
        login.is_click(flight["ChangeReviseSaveBTU"])
        sleep(2)
        #revise 2
        #查询
        login.input_text(flight['ChangeCallSign'], flightNo2)
        sleep(1)
        login.is_click(flight["ChangeSearchBTU"])
        sleep(3)
        #添加到revise
        login.is_click(flight["ChangeSelectSearch1"])
        login.is_click(flight["ChangeRevise"])
        #改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = 0", scrollbar)
        sleep(3)
        login.is_click(flight["ChangeAircraftType_Select1"])
        sleep(1)
        dateFrom2 = (now+relativedelta(days=7)).strftime("%d/%m/%Y")
        dateTo2 = (now+relativedelta(days=13)).strftime("%d/%m/%Y")
        login.input_text(flight['ChangeReviseEffFrom'], dateFrom2)
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span/div/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['ChangeReviseEffTo'], dateTo2)
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/span/div/input"
        ).send_keys(Keys.ENTER)
        login.is_click(flight["ChangeAircraftType_Select1"])
        login.input_text(flight['ChangeAircraftType_Input1'], '141')
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[15]/div/span/div/div/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['ChangeSeats1'], '300')
        #移动横轴滚动条到右侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        sleep(3)
        ChangeRoute3 = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[20]/div/span/div/input"
        )
        drivers.execute_script("arguments[0].value = 'HKG-MFM';", ChangeRoute3)
        login.input_text(flight['ChangeStd1'], '1130')
        #移动横轴滚动条到左侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = 0", scrollbar)
        sleep(3)
        login.is_click(flight["ChangeAircraftType_Select2"])
        sleep(1)
        login.is_click(flight["ChangeAircraftType_Select2"])
        login.input_text(flight['ChangeAircraftType_Input2'], '143')
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[14]/div/span/div/div[1]/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['ChangeSeats2'], '350')
        #移动横轴滚动条到右侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        sleep(3)
        ChangeRoute4 = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[19]/div/span/div/input"
        )
        # logging.info(ChangeRoute4)
        drivers.execute_script("arguments[0].value = 'MFM-HKG';", ChangeRoute4)
        # login.input_text(flight['ChangeRoute2'], 'MFM-HKG')
        login.input_text(flight['ChangeSta2'], '1930')
        login.is_click(flight["ChangeReviseSaveBTU"])
        sleep(2)
        #revise 31
        #查询
        login.input_text(flight['ChangeCallSign'], flightNo31)
        sleep(1)
        login.is_click(flight["ChangeSearchBTU"])
        sleep(3)
        #添加到revise
        login.is_click(flight["ChangeSelectSearch1"])
        login.is_click(flight["ChangeRevise"])
        #改数据
        sleep(1)
        dateFrom31 = (now).strftime("%d/%m/%Y")
        dateTo31 = (now+relativedelta(days=6)).strftime("%d/%m/%Y")
        #移动横轴滚动条到左侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = 0", scrollbar)
        sleep(3)
        login.input_text(flight['ChangeReviseEffFrom'], dateFrom31)
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span/div/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['ChangeReviseEffTo'], dateTo31)
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/span/div/input"
        ).send_keys(Keys.ENTER)
        login.is_click(flight["ChangeAircraftType_Select1"])
        sleep(1)
        login.is_click(flight["ChangeAircraftType_Select1"])
        login.input_text(flight['ChangeAircraftType_Input1'], '141')
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[15]/div/span/div/div/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['ChangeSeats1'], '300')
        #移动横轴滚动条到右侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        sleep(3)
        ChangeRoute5 = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[20]/div/span/div/input"
        )
        drivers.execute_script("arguments[0].value = 'HKG-MFM';", ChangeRoute5)
        # login.input_text(flight['ChangeRoute1'], 'HKG-MFM')
        login.input_text(flight['ChangeStd1'], '1130')
        #移动横轴滚动条到左侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = 0", scrollbar)
        sleep(3)
        login.is_click(flight["ChangeAircraftType_Select2"])
        sleep(1)
        login.is_click(flight["ChangeAircraftType_Select2"])
        login.input_text(flight['ChangeAircraftType_Input2'], '143')
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[14]/div/span/div/div[1]/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['ChangeSeats2'], '350')
        #移动横轴滚动条到右侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        sleep(3)
        ChangeRoute6 = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[19]/div/span/div/input"
        )
        drivers.execute_script("arguments[0].value = 'MFM-HKG';", ChangeRoute6)
        # login.input_text(flight['ChangeRoute2'], 'MFM-HKG')
        login.input_text(flight['ChangeSta2'], '1930')
        # login.is_click(flight["ChangeReviseAddBTU"])
        # #移动横轴滚动条到左侧修改数据
        # sleep(1)
        # drivers.execute_script("arguments[0].scrollLeft = 0", scrollbar)
        # sleep(3)
        # #为第三个添加一个flight 32 1
        # login.input_text(flight['ChangeFlight3'], flightNo31)
        # dateFrom32 = (now+relativedelta(days=21)).strftime("%d/%m/%Y")
        # dateTo32 = (now+relativedelta(days=27)).strftime("%d/%m/%Y")
        # login.input_text(flight['ChangeReviseEffFrom3'], dateFrom32)
        # sleep(1)
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[6]/div/span/div/input"
        # ).send_keys(Keys.ENTER)
        # login.input_text(flight['ChangeReviseEffTo3'], dateTo32)
        # sleep(1)
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[7]/div/span/div/input"
        # ).send_keys(Keys.ENTER)
        # login.is_click(flight["ChangeDop3_1"])
        # login.is_click(flight["ChangeDop3_2"])
        # login.is_click(flight["ChangeDop3_3"])
        # login.is_click(flight["ChangeDop3_4"])
        # login.is_click(flight["ChangeDop3_5"])
        # login.is_click(flight["ChangeDop3_6"])
        # login.is_click(flight["ChangeDop3_7"])
        # login.is_click(flight["ChangeAircraftType_Select3"])
        # login.input_text(flight['ChangeAircraftType_Input3'], '141')
        # sleep(1)
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[3]/td[15]/div/span/div/div[1]/input"
        # ).send_keys(Keys.ENTER)
        # login.input_text(flight['ChangeSeats3'], '300')
        # #移动横轴滚动条到右侧修改数据
        # sleep(1)
        # drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        # sleep(3)
        # # drivers.execute_script("arguments[0].value = 'HKG-PDX';", ChangeRoute7)
        # login.input_text(flight['ChangeRoute3'], 'HKG-PDX')
        # login.is_click(flight["ChangeSeats3"])
        # login.input_text(flight['ChangeStd3'], '1130')
        # #移动横轴滚动条到左侧修改数据
        # sleep(1)
        # drivers.execute_script("arguments[0].scrollLeft = 0", scrollbar)
        # sleep(3)
        # #32 2
        # login.input_text(flight['ChangeFlight4'], flightNo32)
        # login.is_click(flight["ChangeInOutFlightDiff3_Select4"])
        # login.input_text(flight['ChangeInOutFlightDiff3_Input4'], '+0')
        # sleep(1)
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[4]/div/span/div/div/div/input"
        # ).send_keys(Keys.ENTER)
        # login.is_click(flight["ChangeAircraftType_Select4"])
        # login.input_text(flight['ChangeAircraftType_Input4'], '143')
        # sleep(1)
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[4]/td[14]/div/span/div/div[1]/input"
        # ).send_keys(Keys.ENTER)
        # login.input_text(flight['ChangeSeats4'], '350')
        # #移动横轴滚动条到右侧修改数据
        # sleep(1)
        # drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        # sleep(3)
        # # drivers.execute_script("arguments[0].value = 'PDX-HKG';", ChangeRoute8)
        # login.input_text(flight['ChangeRoute4'], 'PDX-HKG')
        # login.is_click(flight["ChangeSeats4"])
        # login.input_text(flight['ChangeSta4'], '1930')
        login.is_click(flight["ChangeReviseSaveBTU"])
        # sleep(2)
        #revise 4
        #查询
        login.input_text(flight['ChangeCallSign'], flightNo4)
        sleep(1)
        login.input_text(flight['ChangeEffTo'], dateFrom)
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/form/div[4]/div/div/div/div[2]/input"
        ).send_keys(Keys.ENTER)
        login.is_click(flight["ChangeDisplayByDay"])
        sleep(1)
        login.is_click(flight["ChangeSearchBTU"])
        sleep(30)
        #添加到revise
        login.is_click(flight["ChangeSelectSearch1"])
        login.is_click(flight["ChangeRevise"])
        #改数据
        #移动横轴滚动条到左侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = 0", scrollbar)
        sleep(3)
        login.is_click(flight["ChangeAircraftType_Select1"])
        sleep(1)
        # dateFrom4 = (now).strftime("%d/%m/%Y")
        # dateTo4 = (now).strftime("%d/%m/%Y")
        # #获取dop点击的日
        # #当前第一天
        # date_obj = date(now.year, now.month, now.day)
        # logging.info(date_obj)
        # #第一天是星期几
        # weekday = date_obj.weekday()
        # logging.info(weekday)
        # login.input_text(flight['ChangeReviseEffFrom'], dateFrom4)
        # sleep(1)
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/span/div/input"
        # ).send_keys(Keys.ENTER)
        # login.input_text(flight['ChangeReviseEffTo'], dateTo4)
        # sleep(1)
        # drivers.find_element_by_xpath(
        #     "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/span/div/input"
        # ).send_keys(Keys.ENTER)
        # #循环判断点击非第一天那天的星期x
        # for i in range(1, 8):
        #     next_day = date_obj + timedelta(days=i)
        #     nextWeekDay = next_day.weekday()
        #     logging.info(nextWeekDay)
        #     # 如果接下来的日期与第一天所在的星期几相同，则跳过
        #     if nextWeekDay == weekday:
        #         continue
        #     # 在这里执行点击操作
        #     login.is_click(flight["ChangeDop1_" + str(nextWeekDay+1)])
        login.is_click(flight["ChangeAircraftType_Select1"])
        login.input_text(flight['ChangeAircraftType_Input1'], '141')
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[15]/div/span/div/div/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['ChangeSeats1'], '300')
        #移动横轴滚动条到右侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        sleep(3)
        ChangeRoute7 = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[1]/td[20]/div/span/div/input"
        )
        drivers.execute_script("arguments[0].value = 'HKG-SYD';", ChangeRoute7)
        login.input_text(flight['ChangeStd1'], '1130')
        #移动横轴滚动条到左侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = 0", scrollbar)
        sleep(3)
        login.is_click(flight["ChangeAircraftType_Select2"])
        sleep(1)
        login.is_click(flight["ChangeAircraftType_Select2"])
        login.input_text(flight['ChangeAircraftType_Input2'], '143')
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[14]/div/span/div/div[1]/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['ChangeSeats2'], '350')
        #移动横轴滚动条到右侧修改数据
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        sleep(3)
        ChangeRoute8 = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[19]/div[1]/div/div[2]/div[2]/div[3]/table/tbody/tr[2]/td[19]/div/span/div/input"
        )
        drivers.execute_script("arguments[0].value = 'SYD-HKG';", ChangeRoute8)
        # login.input_text(flight['ChangeRoute2'], 'MFM-HKG')
        login.input_text(flight['ChangeSta2'], '1930')
        login.is_click(flight["ChangeReviseSaveBTU"])
        login.input_text(flight['ChangeRemark'], 'UAT End2End Testing')
        login.is_click(flight["ChangeUploadRelatedDocBTU"])
        login.is_click(flight["ChangeUploadDocType_Select"])
        sleep(1)
        login.input_text(flight['ChangeUploadDocType_Input'], 'Others')
        drivers.find_element_by_xpath(
            "//*[@id='testNewDocumentUpload']"
        ).send_keys(Keys.ENTER)
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path)+'/TestData/In'
        # 修改上传文件名
        # '该文件夹下所有的文件（包括文件夹）'
        FileList = os.listdir(file_path)
        # '遍历所有文件'
        for files in FileList:
            # '原来的文件路径'
            oldDirPath = os.path.join(file_path, files)
            # 设置时间戳加other_support.pdf为新名称
            newFileName = str(time.time())+'other_support.pdf'
            # 完整路径
            newDirPath = os.path.join(file_path, newFileName)
            # 修改
            os.rename(oldDirPath, newDirPath)
            # 变更上传文件的路径
            uploadFilePath = newDirPath
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(uploadFilePath)
        sleep(1)
        expiryDate = (now+relativedelta(days=1)).strftime("%d/%m/%Y")
        login.input_text(flight['ChangeExpiryDateInput'], expiryDate)
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='testExpiryDate']/input"
        ).send_keys(Keys.ENTER)
        login.is_click(flight["ChangeUploadSaveBTU"])
        sleep(2)
        login.is_click(flight["ChangeSaveAsDraft"])
        sleep(5)
        # login.is_click(flight["ChangeConfirm"])
        # login.is_click(flight["ChangePreviewAndSubmit"])
        # login.is_click(flight["ChangeSubmit"])
        #保存草稿后变成修改页面
        login.is_click(flight["ChangePreviewAndSubmitUpdate"])
        sleep(2)
        login.is_click(flight["ChangeSubmitUpdate"])
        sleep(8)
        login.is_click(flight["ChangeSubmitOK"])
        sleep(10)
        refNoValue = drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[5]/div/div[3]/table/tbody/tr[1]/td[4]/div/a/span/span")
        filename = os.path.dirname(current_path)+'/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        with open(filename, 'w') as f:
            f.write(refNoValue.text)
        # 恢复上传文件名
        # '该文件夹下所有的文件（包括文件夹）'
        FileList = os.listdir(file_path)
        # '遍历所有文件'
        for files in FileList:
            # '原来的文件路径'
            oldDirPath = os.path.join(file_path, files)
            # 设置时间戳加other_support.pdf为新名称
            newFileName = 'other_support.pdf'
            # 完整路径
            newDirPath = os.path.join(file_path, newFileName)
            # 修改
            os.rename(oldDirPath, newDirPath)
        login.is_click(flight["Logout"])
        login.is_click(flight["Logout_Yes"])
        # # 清空文件内容
        # # '该文件夹下所有的文件（包括文件夹）'
        # file_path = os.path.dirname(current_path)+'/TestData/Out'
        # FileList = os.listdir(file_path)
        # # '遍历所有文件'
        # for files in FileList:
        #     files = os.path.join(file_path, files)
        #     # 清空文件内容
        #     with open(files, 'a+') as f:
        #         f.truncate(0)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_071/test_e2e_0411.py'])