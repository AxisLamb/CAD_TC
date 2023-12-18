import os
import allure
import pytest
import time
import logging

from telnetlib import EC
from dateutil.relativedelta import relativedelta
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.readconfig import ini
from page.webpage import sleep
from common.readelement import Element
from common.readvalue import ElementValue
from page_object.LoginPage import LoginPage
from selenium.webdriver.common.keys import Keys


flight = Element('flight_071')
flightValue = ElementValue('flightValue_071')
flightAcc = ElementValue('cad_account')
@allure.feature("TC(ECE)-071 04Process_application_by_Officer")
class TestChangeProcessApplicationByOfficer:
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
        assert drivers.find_element_by_css_selector("h2").text == "Messages"
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
        # assert drivers.find_element_by_xpath("//*[@id='test0']").text == str(refno)
        # 进入详情页
        login.is_click(flight['ViewMessages_ReferenceNo'])
        sleep(5)
        # 检查跳转
        # assert drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[1]/form/div/div[1]/div/div/form/div[1]/div[1]/div/div").text == str(refno)
        login.is_click(flight['DetailReviseFlightForm_1'])
        login.is_click(flight['DetailReviseModifyFlightBTU'])
        sleep(1)
        login.is_click(flight['DetailReviseDop1_1'])
        sleep(1)
        login.is_click(flight['DetailReviseDop1_2'])
        sleep(1)
        login.is_click(flight['DetailReviseDop1_3'])
        sleep(1)
        login.is_click(flight['DetailReviseDop1_4'])
        sleep(1)
        login.is_click(flight['DetailReviseDop1_5'])
        sleep(1)
        login.is_click(flight['DetailReviseDop1_6'])
        sleep(1)
        login.is_click(flight['DetailReviseAircraft_Select_1'])
        sleep(1)
        login.is_click(flight['DetailReviseAircraft_Select_1'])
        login.input_text(flight['DetailReviseAircraft_Input_1'], "143")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[14]/div/span/div/div/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['DetailReviseSeats_1'], "500")
        #移动横轴滚动条到右侧修改数据
        scrollbar = drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]"
        )
        sleep(1)
        drivers.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth", scrollbar)
        sleep(3)
        login.input_text(flight['DetailReviseSTD_1'], "1045")
        login.is_click(flight['DetailReviseEB_1'])
        # flight2
        login.is_click(flight['DetailReviseAircraft_Select_2'])
        sleep(1)
        login.is_click(flight['DetailReviseAircraft_Select_2'])
        login.input_text(flight['DetailReviseAircraft_Input_2'], "141")
        sleep(1)
        drivers.find_element_by_xpath(
            "//*[@id='app']/div/div/section/div/div[3]/div[1]/div/div[2]/div/div[3]/table/tbody/tr[2]/td[14]/div/span/div/div[1]/input"
        ).send_keys(Keys.ENTER)
        login.input_text(flight['DetailReviseSeats_2'], "500")
        login.input_text(flight['DetailReviseSTA_2'], "2130")
        login.is_click(flight['DetailReviseEB_2'])
        login.is_click(flight['DetailReviseSaveFlightBTU'])
        sleep(5)
        # 选择文档按钮
        login.is_click(flight['DetailChangeSelectDocument'])
        login.is_click(flight['DetailChangeDocumentOperatorICAO'])
        login.is_click(flight['DetailChangeDocumentSearch'])
        login.is_click(flight['DetailChangeDocumentLibRecord_1'])
        login.is_click(flight['DetailChangeDocumentLibConfirm'])
        # 文档表格中的upload按钮
        login.is_click(flight['DetailChangeDocumentUpload'])
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
        leaseAirExpiryDate = (now+relativedelta(days=3)).strftime("%d/%m/%Y")
        login.input_text(flight['LeaseAirExpiryDate'], leaseAirExpiryDate)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='app']/div/div/section/div/div[13]/div[1]/div/div[2]/form/div[9]/div/div/div/div/input").send_keys(Keys.ENTER)
        login.input_text(flight['LeaseAirEnclosureRef'], flightValue['LeaseAirEnclosureRef'])
        login.input_text(flight['LeaseAirRemark'], flightValue['LeaseAirRemark'])
        login.is_click(flight['LeaseAirUploadBTU'])
        sleep(3)
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
        sleep(1)
        login.is_click(flight['DetailChangeUploadDocument'])
        login.is_click(flight['DetailChangeUploadDocumentDocType_Select'])
        login.input_text(flight['DetailChangeUploadDocumentDocType_Input'], flightValue['DetailUploadDocumentDocType_Input'])
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testNewDocumentUpload']").send_keys(Keys.ENTER)
        sleep(1)
        logging.info(uploadFilePath)
        drivers.find_element_by_xpath("//*[@id='testBrowse']/following::input[@type ='file']").send_keys(uploadFilePath)
        expiryDate = (now+relativedelta(days=3)).strftime("%d/%m/%Y")
        login.input_text(flight['DetailChangeUploadDocumentExpiryDate'], expiryDate)
        sleep(1)
        drivers.find_element_by_xpath("//*[@id='testExpiryDate']/input").send_keys(Keys.ENTER)
        login.is_click(flight['DetailChangeUploadDocumentUploadBTU'])
        sleep(2)
        # 点击view按钮
        login.is_click(flight['DetailChangeViewUploadDocument'])
        sleep(1)
        # 展示对话框
        login.is_click(flight['DetailChangeViewUploadDocExitBTU'])

        # # 点击Message按钮打开对话框
        # login.is_click(flight['DetailMessaging'])
        # login.input_text(flight['MessagingBox'], "Messaging Test")
        # login.is_click(flight['MessagingSend'])

        # remark输入
        sleep(2)
        login.input_text(flight['DetailChangeRemarksBTU_Input'], flightValue['DetailRemarksBTU_Input'])
        # CADReamrk
        sleep(2)
        login.is_click(flight['DetailChangeCADRemarksBTU'])
        sleep(1)
        login.input_text(flight['DetailChangeCADRemarksBTU_Input'], flightValue['DetailCADRemarksBTU_Input'])
        sleep(1)
        login.is_click(flight['DetailChangeSaveBTU'])
        sleep(2)
        login.is_click(flight['DetailChangeSavePopUpBTU'])
        # 审批
        login.is_click(flight['DetailApprovalChange'])
        # Recommendation
        login.is_click(flight['ApprovalRecommendation'])
        sleep(1)
        login.is_click(flight['ApprovalRecommendationConfirm'])
        sleep(10)
        login.is_click(flight['ApprovalSucceedPopupOK'])
        sleep(1)
        # generate
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
        sleep(12)
        # send
        login.is_click(flight['ApprovalChangeSendLetterBTU'])
        sleep(12)
        login.is_click(flight['ApprovalSendLetterPopUpBTU'])
        sleep(1)
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
    pytest.main(['TestCase/TC_E2E_071/test_e2e_0412.py'])