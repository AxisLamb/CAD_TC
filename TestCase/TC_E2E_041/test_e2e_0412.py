import logging
import os
import time
import allure
import pytest


from datetime import datetime
from telnetlib import EC
from dateutil.relativedelta import relativedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.readconfig import ini
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage

flight = Element('flight_041')
flightValue = ElementValue('flightValue_041')
flightAcc = ElementValue('cad_account')
@allure.feature("TC(ECE)-041 02Process_application_by_Officer")
class TestProcessApplicationByOfficer:
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
            login.input_user_name(flightAcc['OfficerLoginName'])
            login.input_user_password(flightAcc['OfficerPassword'])
            login.click_login_button()

        WebDriverWait(drivers, 20, 0.8).until(EC.presence_of_element_located((By.TAG_NAME,'h2')))
        # 跳转到页面
        login.get_url(ini.url + "?#/View/Messages")
        drivers.implicitly_wait(30)
        sleep(5)
        # assert drivers.find_element_by_css_selector("h2").text == "Messages"
        current_path = os.path.abspath(__file__)
        filename = os.path.dirname(current_path)+'/TestData/Out/AppRefNo.txt'
        # 如果filename不存在会自动创建， r以只读方式打开文件。文件的指针将会放在文件的开头。这是**默认模式**。
        with open(filename, 'r') as f:
            refno = f.read()
        # # 打开查询页
        login.is_click(flight['ViewMessages_AdvancedSearch'])
        login.input_text(flight['ViewMessages_Search_ReferenceNo'], refno)
        login.input_text(flight['ViewMessages_Sender'], flightAcc['OperatorcpaLoginName'])
        login.is_click(flight['ViewMessages_Search'])
        sleep(5)
        # 检查查询结果
        # assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[6]/div[2]/div[3]/table/tbody/tr[1]/td[6]/div/a[1]/a/span/span[1]").text == str(refno)
        # 进入详情页
        login.is_click(flight['ViewMessages_ReferenceNo'])
        sleep(10)
        # 检查跳转
        # assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[1]/div/div/form/div[1]/div[1]/div/div").text == str(refno)
        # 测试基础信息保存
        login.is_click(flight['DetailModifyBasicBTU'])
        login.is_click(flight['DetailSaveBTU'])
        sleep(2)
        login.is_click(flight['DetailSavePopUpBTU'])
        # 修改flight——1
        login.is_click(flight['DetailFlightForm_1'])
        login.is_click(flight['DetailModifyFlightBTU'])
        login.is_click(flight['DetailDop1_1'])
        login.is_click(flight['DetailDop2_1'])
        login.is_click(flight['DetailDop3_1'])
        login.is_click(flight['DetailDop4_1'])
        login.is_click(flight['DetailDop5_1'])
        sleep(3)
        login.is_click(flight['DetailDop6_1'])
        # # 取消
        # sleep(6)
        # login.is_click(flight['DetailAircraft_Select_1'])
        # sleep(6)
        # # 重新注入
        # login.is_click(flight['DetailAircraft_Select_1'])
        # sleep(3)
        # login.input_text(flight['DetailAircraft_Input_1'], flightValue['DetailAircraft_Input_1'])
        # sleep(1)
        # drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[12]/div/span/div/div[1]/input").send_keys(Keys.ENTER)
        login.input_text(flight['DetailSeats_1'], flightValue['DetailSeats_1'])
        login.input_text(flight['DetailSTD_1'], flightValue['DetailSTD_1'])
        login.is_click(flight['DetailEB_1'])
        login.is_click(flight['DetailBellyCargoOnly_1'])
        login.is_click(flight['DetailRepatriation_1'])
        login.input_text(flight['DetailRemark_1'], flightValue['DetailRemark_1'])
        login.is_click(flight['DetailSaveFlight'])
        sleep(5)
        # 修改窗口正常保存关闭
        # assert drivers.find_element_by_xpath("//h2[contains(.,'Successful')]").text == 'Successful'
        # 选择文档按钮
        login.is_click(flight['DetailSelectDocument'])
        login.is_click(flight['DetailDocumentOperatorICAO'])
        login.is_click(flight['DetailDocumentSearch'])
        login.is_click(flight['DetailDocumentLibRecord_1'])
        login.is_click(flight['DetailDocumentLibConfirm'])
        # 文档表格中的upload按钮
        login.is_click(flight['DetailDocumentUpload'])
        login.is_click(flight['DetailDocumentUploadPopUp'])
        # 选择leaseAir
        login.is_click(flight['LeaseAirLessorOptICAO_Select'])
        login.input_text(flight['LeaseAirLessorOptICAO_Input'], flightValue['LeaseAirLessorOptICAO_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[6]/div[1]/div/div/div/div[1]/input").send_keys(Keys.ENTER)

        login.is_click(flight['LeaseAirDocType_Select'])
        login.input_text(flight['LeaseAirDocType_Input'], flightValue['LeaseAirDocType_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[7]/div/div/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['LeaseAirRegistrationMark'], flightValue['LeaseAirRegistrationMark'])

        login.is_click(flight['LeaseAirAircraftType_Select'])
        login.input_text(flight['LeaseAirAircraftType_Input'], flightValue['LeaseAirAircraftType_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[8]/div[2]/div/div/div/div[1]/input").send_keys(Keys.ENTER)
        now = datetime.now()
        leaseAirExpiryDate = (now + relativedelta(days=3)).strftime("%d/%m/%Y")
        login.input_text(flight['LeaseAirExpiryDate'], leaseAirExpiryDate)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[9]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['LeaseAirEnclosureRef'], flightValue['LeaseAirEnclosureRef'])
        login.input_text(flight['LeaseAirRemark'], flightValue['LeaseAirRemark'])
        login.is_click(flight['LeaseAirUploadBTU'])
        sleep(8)
        login.is_click(flight['LeaseAirUploadBTUPopUpOK'])
        # 上传文档按钮
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
            uploadFilePath = uploadFilePath.replace("\\", "/")
        sleep(5)
        login.is_click(flight['DetailUploadDocument'])
        login.is_click(flight['DetailUploadDocumentDocType_Select'])
        login.input_text(flight['DetailUploadDocumentDocType_Input'], flightValue['DetailUploadDocumentDocType_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(1)
        logging.info(uploadFilePath)
        upload_input = drivers.find_element_by_xpath("//*[@id='testBrowse']/following-sibling::input")
        upload_input.send_keys(uploadFilePath)
        expiryDate = (now+relativedelta(days=3)).strftime("%d/%m/%Y")
        login.input_text(flight['DetailUploadDocumentExpiryDate'], expiryDate)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        login.is_click(flight['DetailUploadDocumentUploadBTU'])
        sleep(2)
        # 点击view按钮
        login.is_click(flight['DetailViewUploadDocument'])
        sleep(1)
        # 关闭对话框
        login.is_click(flight['DetailViewUploadDocExitBTU'])

        # # 点击Message按钮打开对话框
        # login.is_click(flight['DetailMessaging'])
        # login.input_text(flight['MessagingBox'], "Messaging Test")
        # login.is_click(flight['MessagingSend'])

        # remark输入
        sleep(2)
        login.input_text(flight['DetailRemarksBTU_Input'], flightValue['DetailRemarksBTU_Input'])
        # CADReamrk
        sleep(2)
        login.is_click(flight['DetailCADRemarksBTU'])
        sleep(1)
        login.input_text(flight['DetailCADRemarksBTU_Input'], flightValue['DetailCADRemarksBTU_Input'])
        sleep(1)
        login.is_click(flight['DetailSaveBTU'])
        sleep(2)
        login.is_click(flight['DetailSavePopUpBTU2'])
        # Auto Counting Frequency
        login.is_click(flight['DetailAutoCountingFrequency'])
        sleep(1)
        login.is_click(flight['DetailAutoCountingFrequencyDisBTU'])
        # 打印机打印
        # login.is_click(flight['DetailPrintApp'])
        # sleep(3)
        # send_keys('{ENTER}')
        # # 使用pywinauto来选择文件
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
        # 审批
        login.is_click(flight['DetailApproval'])
        # Recommendation
        login.is_click(flight['ApprovalRecommendation'])
        sleep(1)
        login.is_click(flight['ApprovalRecommendationConfirm'])
        login.is_click(flight['ApprovalSucceedPopupOK'])
        sleep(2)
        # Generate
        login.is_click(flight['ApprovalGenerate'])
        sleep(12)
        login.is_click(flight['ApprovalGenerateAndEdit'])
        sleep(1)
        login.input_text(flight['GenerateOffPhone'], flightValue['GenerateOffPhone'])
        login.input_text(flight['GenerateOffFax'], flightValue['GenerateOffFax'])
        login.input_text(flight['GenerateUserName'], flightValue['GenerateUserName'])
        login.input_text(flight['GeneratePost'], flightValue['GeneratePost'])
        login.input_text(flight['GenerateCompanyName'], flightValue['GenerateSubOffName'])
        login.input_text(flight['GenerateSubOffName'], flightValue['GenerateOffPhone'])
        login.input_text(flight['GenerateAddress_1'], flightValue['GenerateAddress_1'])
        login.input_text(flight['GenerateAddress_2'], flightValue['GenerateAddress_2'])
        login.input_text(flight['GenerateAddress_3'], flightValue['GenerateAddress_3'])
        login.input_text(flight['GenerateSignedArea'], flightValue['GenerateSignedArea'])
        sleep(1)
        # Refresh Preview
        login.is_click(flight['GenerateRefreshPreview'])
        sleep(3)
        # down
        login.is_click(flight['GenerateDownloadAsWord'])
        sleep(1)
        # generate
        login.is_click(flight['GeneratePDF'])
        sleep(20)
        # send
        login.is_click(flight['ApprovalSendLetterBTU'])
        sleep(10)
        login.is_click(flight['ApprovalSendLetterPopUpBTU'])
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
    pytest.main(['TestCase/TC_E2E_041/test_e2e_0412.py'])