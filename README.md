# web-UI 自动化测试示例
---

## 框架设计

- pytest
- selenium
- POM页面对象模型（Page Object Model）

---
 
## 目录结构

    common                 ——公共类
    Page                   ——基类
    PageElements           ——页面元素类
    PageObject             ——页面对象类
    TestCase               ——测试用例
    conftest.py            ——pytest胶水文件
    pytest.ini             ——pytest配置文件

---

## 环境
### python3.x安装

* https://blog.csdn.net/weixin_53024080/article/details/119139122

开发Python的IDE推荐PyCharm
官方网站：
https://www.jetbrains.com/pycharm/
---


### 替换pip为本地源
```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```
---

## 运行

### 安装依赖

```shell
pip install -r requirements.txt
```

### 安装py
```shell
pip install py
```


### 浏览器驱动

chrome浏览器驱动下载地址：

https://googlechromelabs.github.io/chrome-for-testing/#stable
前面三部分一直就行比如116.0.5845 一致，这个连接中找对应版本的chromedriver

chrome浏览器对应的chromesdriver版本如何查看：

首先查看chrome浏览器版本：（浏览器设置--关于chrome）

选择下载与chrome浏览器相匹配的chromedriver版本，解压后，

win: 将chromedriver.exe放置到python的目录下

mac: 将驱动放置到/usr/local/bin/

### 其他问题参考
https://blog.51cto.com/u_15784290/5669836#2%E3%80%81requirements.txt%20%E4%BE%9D%E8%B5%96%E5%8C%85

## 执行
* 用例设计原则和规则
```
在TestCase文件夹下，创建一个以测试用例名为文件夹名字，比如测试用例为TC(E2E)-001，文件夹名字为TC_E2E_001，然后这个相关的测试脚本都放在这个文件夹中
文件名以test_*.py文件和*_test.py
以test_开头的函数
以Test开头的类，test_开头的方法，并且不能带有__init__ 方法
所有的包pakege必须要有__init__.py文件
断言使用assert
请参考test_flight1.py和test_flight2.py
其中@allure.feature为测试用例名称， 比如@allure.feature("TC(ECE)-001 Local Operator Create and Processing Scheduled Passenger Application (Approve)")
@allure.story为测试用户故事，比如 @allure.story("Miss inputting mandatory No. of Seats field")
请在代码中加一些必要环节的注释，方便理解代码。
```
* 执行用例规则
```
1.执行某个目录下所有的用例

pytest 文件名/

2.执行某一个py文件下用例

pytest 脚本名称.py

3.-k 按关键字匹配

pytest -k "MyClass and not method"

这将运行包含与给定字符串表达式匹配的名称的测试，其中包括Python
使用文件名，类名和函数名作为变量的运算符。 上面的例子将运行
TestMyClass.test_something但不运行TestMyClass.test_method_simple

4.按节点运行

每个收集的测试都分配了一个唯一的nodeid，它由模块文件名和后跟说明符组成
来自参数化的类名，函数名和参数，由:: characters分隔。

运行.py模块里面的某个函数

pytest test_mod.py::test_func

运行.py模块里面,测试类里面的某个方法

pytest test_mod.py::TestClass::test_method

5.标记表达式

pytest -m slow

将运行用@ pytest.mark.slow装饰器修饰的所有测试。

6.从包里面运行

pytest --pyargs pkg.testing

这将导入pkg.testing并使用其文件系统位置来查找和运行测试。
```

 
 ## 运行allure report:
 python .\run_case.py
 
  
 ## 经验总结
0. chromesdriver版本一定要对应
1. 对于需要加载的页面或者元素，请在取元素前加上sleep(x),x的单位为秒，比如sleep(2)强制等待2秒。当然也可用implicitly_wait(x) 隐性等待,在找到元素的时候就马上去执行下一步，所以是种智能等待方式，如果超过规定时间还找不到，就会抛出异常“TimeoutExceiption”。
2. 如果在SIT环境页面上取的元素Xpath运行时还是无法找到，可以尝试在运行时的页面上定位元素拿到对应的xpath。
3. 其中的下拉框可能需要自己用xpath去写
 页面上直接copy的xpath如下运行有问题
 drivers.find_element_by_xpath("/html/body/div[1]/div/div/section/div/form/div/div[1]/div[2]/div[1]/div/div/div/div/input").send_keys(Keys.ENTER)
 下面的通过contain去查找会直接定位
 drivers.find_element_by_xpath("//label[contains(text(),'ICAO')]//following-sibling::div//input").send_keys(Keys.ENTER)
4. 对于上传文件，请参考test_upload_file.py文件中例子，需要用到pywinauto，请先pip install pywinauto，