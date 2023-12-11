import os
import random
import string
import allure
import pytest
import time
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
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

flight = Element('flight_041')
flightValue = ElementValue('flightValue_041')
flightAcc = ElementValue('cad_account')
@allure.feature("TC(ECE)-041 01Create_Application_By_Local_Operator")
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
        login.get_url(ini.url + "?#/ApplicationView/ExtraSection/CreateExtraSectionPassenger")
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
        login.is_click(flight['DOP_3'])
        login.is_click(flight['DOP_5'])

        login.is_click(flight['AircraftType_Select'])
        login.input_text(flight['AircraftType_input'], flightValue['AircraftType1'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats'], flightValue['NoofSeats1'])
        login.input_text(flight['Route'], flightValue['Route1'])
        login.is_click(flight['LocalTime_STD'])
        login.input_text(flight['LocalTime_STD'], flightValue['STD1'])
        login.input_text(flight['Remarks1'], flightValue['Remarks1'])

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
        login.input_text(flight['Remarks2'], flightValue['Remarks2'])

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
        login.is_click(flight['DOP3_3'])
        login.is_click(flight['DOP3_5'])
        login.is_click(flight['DOP3_7'])
        login.is_click(flight['AircraftType_Select_3'])
        login.input_text(flight['AircraftType_input_3'], flightValue['AircraftType3'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_3'], flightValue['NoofSeats3'])
        login.input_text(flight['Route_3'], flightValue['Route3'])
        login.is_click(flight['LocalTime_STD_3'])
        login.input_text(flight['LocalTime_STD_3'], flightValue['STD3'])
        sleep(1)
        login.is_click(flight["Belly_Cargo_Only_Btu_3"])
        sleep(2)
        login.is_click(flight["Belly_Cargo_Only_Val_3"])
        login.input_text(flight['Remarks3'], flightValue['Remarks3'])

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
        sleep(1)
        login.is_click(flight["Belly_Cargo_Only_Btu_4"])
        sleep(2)
        login.is_click(flight["Belly_Cargo_Only_Val_4"])
        login.input_text(flight['Remarks4'], flightValue['Remarks4'])

        # flight5
        # login.input_text(flight['FlightNo5'], flightValue['FlightNo5']+flightNoAdd)
        login.input_text(flight['FlightNo5'], Flight_5)
        login.input_text(flight['From5'], dateFrom)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To5'], dateTo)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP5_2'])
        login.is_click(flight['DOP5_4'])
        login.is_click(flight['DOP5_6'])

        login.is_click(flight['AircraftType_Select_5'])
        login.input_text(flight['AircraftType_input_5'], flightValue['AircraftType5'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)

        login.input_text(flight['NoofSeats_5'], flightValue['NoofSeats5'])
        login.input_text(flight['Route_5'], flightValue['Route5'])

        login.is_click(flight['LocalTime_STD_5'])
        login.input_text(flight['LocalTime_STD_5'], flightValue['STD5'])

        login.input_text(flight['Remarks5'], flightValue['Remarks5'])
        # flight6(跟随5)
        # login.input_text(flight['FlightNo6'], flightValue['FlightNo6']+flightNoAdd)
        login.input_text(flight['FlightNo6'], Flight_6)
        login.is_click(flight['InOut_Flight_Diff_Select_6'])
        login.input_text(flight['InOut_Flight_Diff_input_6'], flightValue['InOut_Flight_Diff_input_6'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input").send_keys(Keys.ENTER)

        login.is_click(flight['AircraftType_Select_6'])
        login.input_text(flight['AircraftType_input_6'], flightValue['AircraftType6'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_6'], flightValue['NoofSeats6'])
        login.input_text(flight['Route_6'], flightValue['Route6'])
        login.is_click(flight['LocalTime_STA_6'])
        login.input_text(flight['LocalTime_STA_6'], flightValue['STA6'])
        login.input_text(flight['Remarks6'], flightValue['Remarks6'])
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
        login.is_click(flight['DOP7_3'])
        login.is_click(flight['DOP7_5'])

        login.is_click(flight['AircraftType_Select_7'])
        login.input_text(flight['AircraftType_input_7'], flightValue['AircraftType7'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_7'], flightValue['NoofSeats7'])
        login.input_text(flight['Route_7'], flightValue['Route7'])
        login.is_click(flight['LocalTime_STD_7'])
        login.input_text(flight['LocalTime_STD_7'], flightValue['STD7'])
        login.input_text(flight['Remarks7'], flightValue['Remarks7'])
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
        login.input_text(flight['Remarks8'], flightValue['Remarks8'])
        # flight9
        # login.input_text(flight['FlightNo9'], flightValue['FlightNo9']+flightNoAdd)
        login.input_text(flight['FlightNo9'], Flight_9)
        login.input_text(flight['From9'], dateFrom)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[9]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To9'], dateTo)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[9]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP9_2'])
        login.is_click(flight['DOP9_4'])

        login.is_click(flight['AircraftType_Select_9'])
        login.input_text(flight['AircraftType_input_9'], flightValue['AircraftType9'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[9]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['NoofSeats_9'], flightValue['NoofSeats9'])
        login.input_text(flight['Route_9'], flightValue['Route9'])
        login.is_click(flight['LocalTime_STA_9'])
        login.input_text(flight['LocalTime_STA_9'], flightValue['STA9'])
        login.is_click(flight['LocalTime_STD_9'])
        login.input_text(flight['LocalTime_STD_9'], flightValue['STD9'])
        login.is_click(flight['Next_Date_Select_9'])
        login.input_text(flight['Next_Date_input_9'], flightValue['Next_Date_input_9'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[9]/td[18]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['Remarks9'], flightValue['Remarks9'])

        login.input_text(flight['Remarks'], flightValue['Remarks'])

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

        login.is_click(flight['Upload_Documents'])
        sleep(1)
        login.is_click(flight['Doc_Type_Other_Select'])
        login.input_text(flight['Doc_Type_Other_Input'], flightValue['Doc_Type_Other_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(uploadFilePath)
        expiryDate = (datetime.now()+relativedelta(days=1)).strftime("%d/%m/%Y")
        login.input_text(flight['ExpiryDate'], expiryDate)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        login.is_click(flight['UploadBTU'])
        sleep(2)
        login.is_click(flight['SaveAsDraft'])
        sleep(2)
        # assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'

        login.is_click(flight['SaveAsTemplate'])
        #预设名称拼接时间戳作为模板名称
        templateName = flightValue['TemplateName']+str(time.time())
        login.input_text(flight['TemplateName'], templateName)
        login.input_text(flight['Description'], flightValue['Description'])
        sleep(2)
        login.is_click(flight['Template_Save'])
        sleep(2)
        # assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'
        login.is_click(flight['Confirm'])
        sleep(1)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(2)
        # login.is_click(flight['Print'])
        # sleep(3)
        # send_keys('{ENTER}')
        # app = pywinauto.Desktop()
        # # 选择文件上传的窗口
        # dlg = app["将打印输出另存为"]
        # # 计算路径
        # current_path = os.path.abspath(__file__)
        # file_path = os.path.dirname(current_path)+'/TestData/Out/print041'+str(time.time())+'.PDF'
        # # 输入上传文件的路径
        # dlg.Edit.set_text(file_path)
        # sleep(3)
        # # 点击打开
        # dlg["保存(&S)"].click_input()
        # sleep(2)
        # assert os.path.exists(file_path)
        login.is_click(flight['BackAndModify'])
        sleep(2)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(3)
        login.is_click(flight['Submit'])
        sleep(13)
        login.is_click(flight['Submit_Yes'])
        sleep(10)
        # assert drivers.find_element_by_css_selector("h2").text == "Search Application"
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
if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_041/test_e2e_0411.py'])