import yaml
from appium import webdriver
from page.base_page import BasePage
from page.main import Main


class APP(BasePage):
    _pac="com.xueqiu.android"
    _act=".view.WelcomeActivityAlias"
    def start(self):
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'  # 测试平台
            desired_caps['platformVersion'] = '11'  # 测试平台系统版本
            desired_caps['deviceName'] = 'HT79B1A01817'  # 设备名字 -随便写
            desired_caps['appPackage'] = self._pac  # app包名 com.intsig.camscanner
            desired_caps['appActivity'] = self._act  # app启动名  .MainMenuActivity
            desired_caps['noReset'] = 'True'  # 不用重置
            desired_caps['skipServerInstallation'] = True  # 不用重置
            desired_caps['skipServerInitialization'] = True
            desired_caps['udid'] = yaml.safe_load(open("../page/configuration.yml"))['desired_caps']['udid']
            desired_caps['automationName'] = 'Uiautomator2'  # 获取toast消息
            # 声明手机驱动对象 POST接口 创建session 自启动 启动参数中指定的包名和启动名的app
            # 初始化driver
            self._driver = webdriver.Remote("http://127.0.0.2:4723/wd/hub", desired_caps)

        else:
            self._driver.start_activity(self._pac,self._act)
        self._driver.implicitly_wait(5)
        return self




    def main(self) ->Main:
        return Main(self._driver)