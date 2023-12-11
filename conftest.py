#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import base64
import os
import webbrowser

import pytest
from selenium import webdriver
import platform

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        if platform.system() == 'Windows':
            print('Windows系统')
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
#     # report.nodeid = report.nodeid.encode("unicode_escape").decode("utf-8")
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             screen_img = _capture_screenshot()
#             if screen_img:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def pytest_html_results_table_header(cells):
#     cells.insert(1, html.th('用例名称'))
#     cells.insert(2, html.th('Test_nodeid'))
#     cells.pop(2)
#
#
# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     cells.insert(2, html.td(report.nodeid))
#     cells.pop(2)
#
#
# def pytest_html_results_table_html(report, data):
#     if report.passed:
#         del data[:]
#         data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))
#
#
# def pytest_html_report_title(report):
#     report.title = "人才发展测试报告"
#
#
# def pytest_configure(config):
#     config._metadata.clear()
#     config._metadata['测试项目'] = "人才发展"
#     config._metadata['测试地址'] = ini.url
#     if config.getoption('--html'):
#         # 核心是每次测试更改参数传入的htmlpath
#         path_list = list(os.path.split(config.option.htmlpath))
#         new_path_list = list(path_list)
#         new_path_list[1] = new_path_list[1].split('.')[0] + '_' + dt_strftime('%Y%m%d%H%M%S') + '.html'
#         path_list = tuple(new_path_list)
#         # path_list.insert(-1, dt_strftime('%Y-%m-%d %H-%M-%S'))
#         config.option.htmlpath = os.path.join(*tuple(path_list))
#
#
# def pytest_html_results_summary(prefix, summary, postfix):
#     # prefix.clear() # 清空summary中的内容
#     prefix.extend([html.p("测试部门: 人才发展")])
#     prefix.extend([html.p("测试执行人: ZM")])
#
#
# def pytest_terminal_summary(terminalreporter, exitstatus, config):
#     """收集测试结果"""
#     result = {
#         "total": terminalreporter._numcollected,
#         'passed': len(terminalreporter.stats.get('passed', [])),
#         'failed': len(terminalreporter.stats.get('failed', [])),
#         'error': len(terminalreporter.stats.get('error', [])),
#         'skipped': len(terminalreporter.stats.get('skipped', [])),
#         # terminalreporter._sessionstarttime 会话开始时间
#         'total times': timestamp() - terminalreporter._sessionstarttime
#     }
#     print(result)
#     open_report(list(os.path.split(config.option.htmlpath))[0])
#     # if result['failed'] or result['error']:
#     #     send_report()
#
#
# def _capture_screenshot():
#     """截图保存为base64"""
#     now_time, screen_file = cm.screen_path
#     driver.save_screenshot(screen_file)
#     allure.attach.file(screen_file,
#                        "失败截图{}".format(now_time),
#                        allure.attachment_type.PNG)
#     with open(screen_file, 'rb') as f:
#         imagebase64 = base64.b64encode(f.read())
#     return imagebase64.decode()


# @pytest.fixture(scope="session", autouse=True)
# def open_report():
#     yield
#     sleep(20)
#     log.info("打开报告")
#     path = './reports/'
#     # 列出目录的下所有文件和文件夹保存到lists
#     # lists = os.listdir(path)
#     # lists.sort(key=lambda fn: os.path.getmtime(path + "\\" + fn))  # 按时间排序
#     # # 获取最新的文件保存到file
#     # file_report = os.path.join(path, lists[-1])
#     # log.info(file_report)
#     # webbrowser.open(file_report)
#     time_loc = dt_strftime('%Y-%m-%d-%H-%M-%S')
#     files = os.listdir(path)
#     # 查找报告文件
#     for f in files:
#         if time_loc in f and f.endswith('.html'):
#             print('Found it!' + f)
#             file_report = os.getcwd() + '/reports/' + f
#             webbrowser.open(file_report)

# def pytest_collection_modifyitems(items):
#     # 解决pytest执行用例，标题有中文时显示编码不正确的问题
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
