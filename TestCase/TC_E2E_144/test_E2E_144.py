#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import pytest
import allure
import string
import random
from selenium.webdriver.common.keys import Keys
from random import randint
from common.readconfig import ini
from page_object.LoginPage import LoginPage
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

flight = Element('flight_144')
flightvalue = ElementValue('flightvalue_144')
flightAccValue = ElementValue('cad_account')

@allure.feature("TC(ECE)-144 Local Operator Create and Officer Processing Helicopter (thru Extra Section Passenger) Application with new code(Approve)")
class TestCreateAndOfficerHelicopter:
    @pytest.fixture(scope='function', autouse=True)
    def open_flight(self, drivers):
        """打开登录页面"""
        login = LoginPage(drivers)
        login.get_url(ini.url)

    @allure.story("Create Extra Section Passenger Application")
    def test_144(self, drivers):
        """登录CPATEST03用户"""
        login = LoginPage(drivers)
        logout_elements = drivers.find_elements_by_xpath("//i[contains(@class, 'el-icon-caret-bottom')]")
        if len(logout_elements) > 0:
            drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
            login.is_click(flight["Logout_Yes"])
        elements = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elements) > 0:
            login.input_user_name(flightAccValue['CpaOfficerLoginName'])
            login.input_user_password(flightAccValue['CpaOfficerPassword'])
            login.click_login_button()

        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        '''跳转到CreateExtraSectionPassenger页面'''
        login.get_url(ini.url + "#/ApplicationView/ExtraSection/CreateExtraSectionPassenger")

        drivers.implicitly_wait(30)
        sleep(5)

        assert drivers.find_element_by_css_selector("h2").text == "Create Extra Section Passenger Application"

        # 填写Flight Schedules表格信息 Start
        # basic
        login.is_click(flight['Helicopter_Application'])
        #航班号用CPA+4位整数和一位随机字母组成
        s=string.ascii_letters
        r=random.choice(s)
        FlightNoA1="CPA"+str(randint(1000, 9999))+r
        FlightNoA2="CPA"+str(randint(1000, 9999))+r
        FlightNoB1="CPA"+str(randint(1000, 9999))+r
        FlightNoB2="CPA"+str(randint(1000, 9999))+r
        FlightNoC1="CPA"+str(randint(1000, 9999))+r
        FlightNoC2="CPA"+str(randint(1000, 9999))+r
        FlightNoD1="CPA"+str(randint(1000, 9999))+r
        FlightNoD2="CPA"+str(randint(1000, 9999))+r

    # A1行
        login.input_text(flight['FlightNoA1'], FlightNoA1)
        login.input_text(flight['From_A1'], "01/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To_A1'], "30/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1_A1'])
        login.is_click(flight['DOP_3_A1'])
        login.is_click(flight['DOP_5_A1'])
        login.is_click(flight['AircraftType_Select_A1'])
        sleep(1)
        login.input_text(flight['AircraftType_input_A1'], "A139")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[1]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_Of_Seats_A1'], "10")
        login.input_text(flight['Route_A1'], "25L-25R")
        # login.is_click(flight['LocalTime_STA_A1'])
        login.input_text(flight['LocalTime_STA_A1'], "1230")
        sleep(1)
        login.input_text(flight['LocalTime_STD_A1'], "1030")

        # A2行
        login.input_text(flight['FlightNoA2'], FlightNoA2)
        login.is_click(flight['FlightDiff_Select_A2'])
        sleep(1)
        login.input_text(flight['FlightDiff_input_A2'], "+0")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[2]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select_A2'])
        sleep(1)
        login.input_text(flight['AircraftType_input_A2'], "A139")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[2]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_Of_Seats_A2'], "10")
        login.input_text(flight['Route_A2'], "25R-25L")
        login.input_text(flight['LocalTime_STA_A2'], "1930")
        login.input_text(flight['LocalTime_STD_A2'], "1530")
        sleep(1)

        # B1行
        login.input_text(flight['FlightNoB1'], FlightNoB1)
        login.input_text(flight['From_B1'], "01/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To_B1'], "30/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1_B1'])
        login.is_click(flight['DOP_3_B1'])
        login.is_click(flight['DOP_5_B1'])
        login.is_click(flight['DOP_7_B1'])
        login.is_click(flight['AircraftType_Select_B1'])
        sleep(2)
        login.input_text(flight['AircraftType_input_B1'], "A139")
        sleep(2)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[3]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_Of_Seats_B1'], "0")
        sleep(2)
        login.input_text(flight['Route_B1'], "25L-25R")
        sleep(2)
        login.input_text(flight['LocalTime_STA_B1'], "1230")
        sleep(2)
        login.input_text(flight['LocalTime_STD_B1'], "1030")
        sleep(2)
        login.is_click(flight['Belly_Cargo_Only_B1'])
        sleep(3)
        login.is_click(flight['Comfirm_Belly_B1'])
        sleep(2)


        # B2行
        login.input_text(flight['FlightNoB2'], FlightNoB2)
        login.is_click(flight['FlightDiff_Select_B2'])
        sleep(1)
        login.input_text(flight['FlightDiff_input_B2'], "+0")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[4]/td[2]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select_B2'])
        sleep(1)
        login.input_text(flight['AircraftType_input_B2'], "A139")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[4]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_Of_Seats_B2'], "0")
        login.input_text(flight['Route_B2'], "25R-25L")
        login.input_text(flight['LocalTime_STA_B2'], "1930")
        login.input_text(flight['LocalTime_STD_B2'], "1530")
        sleep(1)
        login.is_click(flight['Belly_Cargo_Only_B2'])
        sleep(3)
        login.is_click(flight['Comfirm_Belly_B2'])
        sleep(3)

        # C1行
        login.input_text(flight['FlightNoC1'], FlightNoC1)
        login.input_text(flight['From_C1'], "01/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To_C1'], "30/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_2_C1'])
        login.is_click(flight['DOP_4_C1'])
        login.is_click(flight['DOP_6_C1'])
        login.is_click(flight['AircraftType_Select_C1'])
        sleep(1)
        login.input_text(flight['AircraftType_input_C1'], "A139")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[5]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_Of_Seats_C1'], "10")
        login.input_text(flight['Route_C1'], "CC01-CC02")
        # login.is_click(flight['LocalTime_STA_A1'])
        login.input_text(flight['LocalTime_STA_C1'], "1230")
        sleep(2)
        login.input_text(flight['LocalTime_STD_C1'], "1030")

        # C2行
        login.input_text(flight['FlightNoC2'], FlightNoC2)
        login.is_click(flight['FlightDiff_Select_C2'])
        sleep(1)
        login.input_text(flight['FlightDiff_input_C2'], "+1")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[2]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select_C2'])
        sleep(1)
        login.input_text(flight['AircraftType_input_C2'], "A139")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[6]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_Of_Seats_C2'], "10")
        login.input_text(flight['Route_C2'], "CC02-CC01")
        login.input_text(flight['LocalTime_STA_C2'], "1930")
        login.input_text(flight['LocalTime_STD_C2'], "1530")
        sleep(2)

        # D1行
        login.input_text(flight['FlightNoD1'], FlightNoD1)
        login.input_text(flight['From_D1'], "01/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[4]/div/span/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['To_D1'], "30/11/2023")
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[5]/div/span/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DOP_1_D1'])
        login.is_click(flight['DOP_3_D1'])
        login.is_click(flight['DOP_5_D1'])
        login.is_click(flight['AircraftType_Select_D1'])
        sleep(1)
        login.input_text(flight['AircraftType_input_D1'], "A139")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[7]/td[13]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_Of_Seats_D1'], "5")
        login.input_text(flight['Route_D1'], "CC03-CC04")

        login.input_text(flight['LocalTime_STA_D1'], "1230")
        sleep(1)
        login.input_text(flight['LocalTime_STD_D1'], "1030")

        # D2行
        login.input_text(flight['FlightNoD2'], FlightNoD2)
        login.is_click(flight['FlightDiff_Select_D2'])
        sleep(1)
        login.input_text(flight['FlightDiff_input_D2'], "+0")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[8]/td[2]/div/div/div[1]/input").send_keys(Keys.ENTER)
        login.is_click(flight['AircraftType_Select_D2'])
        sleep(1)
        login.input_text(flight['AircraftType_input_D2'], "A139")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/form/div/div[3]/div[3]/table/tbody/tr[8]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['No_Of_Seats_D2'], "5")
        login.input_text(flight['Route_D2'], "CC04-CC05")
        login.input_text(flight['LocalTime_STA_D2'], "1930")
        login.input_text(flight['LocalTime_STD_D2'], "1530")
        sleep(1)
        # end

        # Remarks
        login.input_text(flight['Remarks'], "UAT End2End Testing")
        sleep(3)

        # Upload Document Start

        login.is_click(flight['Upload_Application_Related_Documents'])
        sleep(2)
        login.is_click(flight['Upload_Application_Related_Documents_Type_Select'])
        sleep(1)
        login.input_text(flight['Upload_Application_Related_Documents_Type_input'], "Others")
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        # sleep(1)
        # login.is_click(flight['Upload_Application_Related_Documents_Browse'])
        sleep(2)
        # # 使用pywinauto来选择文件
        # app = pywinauto.Desktop()
        # # 选择文件上传的窗口
        # dlg = app["打开"]
        # # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path) + "/TestFile/other_support.pdf"
        # # 输入上传文件的路径
        # dlg.Edit.set_text(file_path)
        # sleep(3)
        # # 点击打开
        # dlg["打开(&O)"].click_input()
        drivers.find_element_by_xpath("//input[@type ='file']").send_keys(file_path)
        sleep(2)
        expiryDate = (datetime.today().date() + timedelta(days=1)).strftime("%d/%m/%Y")
        login.input_text(flight['Upload_Application_Related_Documents_Expiry_Date'], expiryDate)
        sleep(1)
        login.is_click(flight['Upload_Application_Related_Documents_Btn'])
        sleep(2)
        # Upload Document End

        #save
        login.is_click(flight['SaveAsDraft'])
        sleep(2)

        login.is_click(flight['SaveAsTemplate'])
        #预设名称拼接时间戳作为模板名称
        templateName = "TestByWJW"+str(random.uniform(1, 1000))
        login.input_text(flight['TemplateName'], templateName)
        login.input_text(flight['Description'], 'Description')
        sleep(3)
        login.is_click(flight['Template_Save'])
        sleep(3)
        # assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'
        login.is_click(flight['Confirm'])
        sleep(3)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(3)
        # login.is_click(flight['Print'])
        # sleep(3)
        # send_keys('{ENTER}')
        # app = pywinauto.Desktop()
        # # 选择文件上传的窗口
        # dlg = app["将打印输出另存为"]
        # # 计算路径
        # current_path = os.path.abspath(__file__)
        # file_path = os.path.dirname(current_path)+'\TestData\Out\print041'+str(time.time())+'.PDF'
        # # 输入上传文件的路径
        # dlg.Edit.set_text(file_path)
        # sleep(3)
        # # 点击打开
        # dlg["保存(&S)"].click_input()
        # sleep(2)
        # assert os.path.exists(file_path)
        login.is_click(flight['BackAndModify'])
        sleep(3)
        login.is_click(flight['PreviewAndSubmit'])
        sleep(3)
        login.is_click(flight['Submit'])
        sleep(20)
        # login.input_text(flight['NewCode_1'], 'UAT New Code Testing 1')
        # login.input_text(flight['NewCode_2'], 'UAT New Code Testing 2')
        # login.is_click(flight['Submit_Yes'])
        # sleep(1)
        # login.is_click(flight['save_OK'])
        # drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary testConfirmButtonClass013']").click()
        drivers.find_element_by_class_name("testConfirmButtonClass013").click()
        sleep(10)

        # 切换officer用户
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(3)
        login.is_click(flight["Logout_Yes"])
        sleep(3)
        elementsOfficer = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elementsOfficer) > 0:
            login.input_user_name(flightAccValue['OfficerLoginName'])
            login.input_user_password(flightAccValue['OfficerPassword'])
            login.click_login_button()
        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到页面
        login.get_url(ini.url + "?#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        # # 打开查询页
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        login.input_text(flight['ViewMessages_Sender'], flightAccValue['CpaOfficerLoginName'])
        login.is_click(flight['Extra_Section_Passenger'])
        login.is_click(flight['ViewMessages_Search'])
        sleep(5)
        # 进入详情页
        login.is_click(flight['ViewMessages_ReferenceNo'])
        sleep(5)
        # 测试基础信息保存
        login.is_click(flight['DetailModifyBasicBTU'])
        login.is_click(flight['DetailSaveBTU'])
        sleep(4)
        login.is_click(flight['DetailSavePopUpBTU'])
        # drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()

        # 修改flight——1
        login.is_click(flight['DetailFlightForm_1'])
        sleep(3)
        login.is_click(flight['DetailModifyFlightBTU'])
        login.is_click(flight['DetailDop1_1'])
        login.is_click(flight['DetailDop2_1'])
        login.is_click(flight['DetailDop3_1'])
        login.is_click(flight['DetailDop4_1'])
        login.is_click(flight['DetailDop5_1'])
        login.is_click(flight['DetailDop6_1'])
        # 取消
        # login.is_click(flight['DetailAircraft_Select_1'])
        # sleep(1)
        # 重新注入
        # login.is_click(flight['DetailAircraft_Select_1'])
        # login.input_text(flight['DetailAircraft_Input_1'], flightvalue['DetailAircraft_Input_1'])
        # sleep(1)
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['DetailSeats_1'], "0")
        # login.input_text(flight['DetailSTD_1'], flightvalue['DetailSTD_1'])
        login.is_click(flight['DetailEB_1'])
        login.is_click(flight['DetailBellyCargoOnly_1'])
        login.is_click(flight['DetailRepatriation_1'])
        login.input_text(flight['DetailRemark_1'], flightvalue['DetailRemark_1'])
        login.is_click(flight['DetailSaveFlight'])
        sleep(5)
        # 修改窗口正常保存关闭
        # assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'
        # 选择文档按钮
        login.is_click(flight['DetailSelectDocument'])
        login.is_click(flight['DetailDocumentOperatorICAO'])
        login.is_click(flight['DetailDocumentSearch'])
        login.is_click(flight['DetailDocumentLibRecord_1'])
        sleep(2)
        login.is_click(flight['DetailDocumentLibConfirm'])
        # 文档表格中的upload按钮
        login.is_click(flight['DetailDocumentUpload'])
        sleep(1)
        login.is_click(flight['DetailDocumentUploadPopUp'])
        sleep(1)
        # 选择leaseAir
        login.is_click(flight['LeaseAirLessorOptICAO_Select'])
        login.input_text(flight['LeaseAirLessorOptICAO_Input'], flightvalue['LeaseAirLessorOptICAO_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[6]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)

        login.is_click(flight['LeaseAirDocType_Select'])
        login.input_text(flight['LeaseAirDocType_Input'], flightvalue['LeaseAirDocType_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[7]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['LeaseAirRegistrationMark'], flightvalue['LeaseAirRegistrationMark'])

        login.is_click(flight['LeaseAirAircraftType_Select'])
        login.input_text(flight['LeaseAirAircraftType_Input'], flightvalue['LeaseAirAircraftType_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[8]/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        leaseAirExpiryDate = (datetime.now()+relativedelta(day=datetime.now().day+3)).strftime("%d/%m/%Y")
        login.input_text(flight['LeaseAirExpiryDate'], leaseAirExpiryDate)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[9]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['LeaseAirEnclosureRef'], flightvalue['LeaseAirEnclosureRef'])
        login.input_text(flight['LeaseAirRemark'], flightvalue['LeaseAirRemark'])
        login.is_click(flight['LeaseAirUploadBTU'])
        sleep(3)
        login.is_click(flight['LeaseAirUploadBTUPopUpOK'])
        # 上传文档按钮
        # 计算路径
        current_path = os.path.abspath(__file__)
        file_path = os.path.dirname(current_path)+'/TestFile/other_support.pdf'
        # 修改上传文件名
        # '该文件夹下所有的文件（包括文件夹）'
        # FileList = os.listdir(file_path)
        # # '遍历所有文件'
        # for files in FileList:
        #     # '原来的文件路径'
        #     oldDirPath = os.path.join(file_path, files)
        #     # 设置时间戳加other_support.pdf为新名称
        #     newFileName ='other_support.pdf'
        #     # 完整路径
        #     newDirPath = os.path.join(file_path, newFileName)
        #     # 修改
        #     os.rename(oldDirPath, newDirPath)
        #     # 变更上传文件的路径
        #     uploadFilePath = newDirPath
        sleep(1)
        login.is_click(flight['DetailUploadDocument'])
        login.is_click(flight['DetailUploadDocumentDocType_Select'])
        login.input_text(flight['DetailUploadDocumentDocType_Input'], flightvalue['DetailUploadDocumentDocType_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(2)
        # drivers.find_element_by_xpath("/html/body/div[7]/div/div[2]/form/div[1]/div/div/div/span/div[2]/div/div/input").send_keys(file_path)
        # sleep(1)
        # login.is_click(flight['DetailUploadDocumentBrowse'])
        # sleep(2)
        # # 使用pywinauto来选择文件
        # app = pywinauto.Desktop()
        # # 选择文件上传的窗口
        # dlg = app["打开"]
        # # 输入上传文件的路径
        # dlg.Edit.set_text(uploadFilePath)
        # sleep(3)
        # # 点击打开
        # dlg["打开(&O)"].click_input()
        drivers.find_element_by_xpath("/html/body/div[7]/div/div[2]/form/div[1]/div/div/div/span/div[2]/div/div/input").send_keys(file_path)
        sleep(2)
        expiryDateUpdate = (datetime.today().date() + timedelta(days=3)).strftime("%d/%m/%Y")

        login.input_text(flight['DetailUploadDocumentExpiryDate'], expiryDateUpdate)
        sleep(1)
        drivers.find_element_by_xpath("/html/body/div[7]/div/div[2]/form/div[5]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.is_click(flight['DetailUploadDocumentUploadBTU'])
        sleep(2)
        # 点击view按钮
        login.is_click(flight['DetailViewUploadDocument'])
        sleep(1)
        # 展示对话框
        login.is_click(flight['DetailViewUploadDocExitBTU'])

        # # 点击Message按钮打开对话框
        # login.is_click(flight['DetailMessaging'])
        # sleep(8)
        # login.input_text(flight['MessagingBox'], "Messaging Test")
        # login.is_click(flight['MessagingSend'])

        # remark输入
        sleep(2)
        login.input_text(flight['DetailRemarksBTU_Input'], flightvalue['DetailRemarksBTU_Input'])
        # CADReamrk
        sleep(2)
        login.is_click(flight['DetailCADRemarksBTU'])
        sleep(1)
        login.input_text(flight['DetailCADRemarksBTU_Input'], flightvalue['DetailCADRemarksBTU_Input'])
        sleep(1)
        login.is_click(flight['DetailSaveBTU'])
        sleep(2)
        login.is_click(flight['DetailSavePopUpBTU2'])
        # drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary el-button el-button--primary el-button--mini']").click()

        # Auto Counting Frequency
        login.is_click(flight['DetailAutoCountingFrequency'])
        sleep(1)
        login.is_click(flight['DetailAutoCountingFrequencyDisBTU'])
        # 打印机打印

        # 审批
        login.is_click(flight['DetailApproval'])
        # Recommendation
        login.is_click(flight['ApprovalRecommendation'])
        sleep(1)
        login.is_click(flight['ApprovalRecommendationConfirm'])

        sleep(5)
        # drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary testConfirmButtonClass054']").click()
        drivers.find_element_by_class_name("testConfirmButtonClass054").click()
        # login.is_click(flight['ApprovalSucceedPopupOK'])
        sleep(2)
        # Generate
        login.is_click(flight['ApprovalGenerate'])
        sleep(8)
        login.is_click(flight['ApprovalGenerateAndEdit'])
        sleep(1)
        login.input_text(flight['GenerateOffPhone'], flightvalue['GenerateOffPhone'])
        login.input_text(flight['GenerateOffFax'], flightvalue['GenerateOffFax'])
        login.input_text(flight['GenerateUserName'], flightvalue['GenerateUserName'])
        login.input_text(flight['GeneratePost'], flightvalue['GeneratePost'])
        login.input_text(flight['GenerateCompanyName'], flightvalue['GenerateSubOffName'])
        login.input_text(flight['GenerateSubOffName'], flightvalue['GenerateOffPhone'])
        login.input_text(flight['GenerateAddress_1'], flightvalue['GenerateAddress_1'])
        login.input_text(flight['GenerateAddress_2'], flightvalue['GenerateAddress_2'])
        login.input_text(flight['GenerateAddress_3'], flightvalue['GenerateAddress_3'])
        login.input_text(flight['GenerateSignedArea'], flightvalue['GenerateSignedArea'])
        sleep(1)
        # Refresh Preview
        login.is_click(flight['GenerateRefreshPreview'])
        sleep(3)
        # down
        login.is_click(flight['GenerateDownloadAsWord'])
        sleep(1)
        # generate
        login.is_click(flight['GeneratePDF'])
        sleep(15)
        # send
        login.is_click(flight['ApprovalSendLetterBTU'])
        sleep(12)
        # drivers.find_element_by_xpath("//button[@class='el-button el-button--default el-button--small el-button--primary testConfirmButtonClass02']").click()
        drivers.find_element_by_class_name("testConfirmButtonClass02").click()
        # login.is_click(flight['ApprovalSendLetterPopUpBTU'])
        sleep(5)

        # 重新切换到CPA用户
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        login.is_click(flight["Logout_Yes"])
        elementsCpa = drivers.find_elements_by_xpath("//button[contains(span,'Login ')]")
        if len(elementsCpa) > 0:
            login.input_user_name(flightAccValue['CpaOfficerLoginName'])
            login.input_user_password(flightAccValue['CpaOfficerPassword'])
            login.click_login_button()
        sleep(20)
        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME, 'h2')))

        # 跳转到页面
        login.get_url(ini.url + "?#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        # 打开查询页
        login.is_click(flight['OptAdvancedSearch'])
        login.input_text(flight['OptSearch_Sender'], flightAccValue['OfficerLoginName'])
        login.is_click(flight['Application_Type'])
        login.is_click(flight['OptSearch_BTU'])
        sleep(5)
        # 进入详情页
        login.is_click(flight['OptMessageDetail'])
        sleep(2)
        login.is_click(flight['OptDetailAttachment'])
        sleep(1)
        login.is_click(flight['OptDetailRefno'])
        sleep(5)
        # login.is_click(flight["Logout"])
        drivers.find_element_by_xpath("//i[@class='el-tooltip el-icon-caret-bottom']").click()
        sleep(1)
        login.is_click(flight["Logout_Yes"])
        sleep(2)

if __name__ == '__main__':
    pytest.main(['TestCase/TC_E2E_144/test_E2E_144.py'])