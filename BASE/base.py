#coding=utf-8
from appium import webdriver
import time

def get_android_driver():
    """
    :param pac: 包名
    :param act: 启动名
    :return: 驱动对象
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'  # 测试平台
    desired_caps['platformVersion'] = '11'  # 测试平台系统版本
    desired_caps['deviceName'] = 'HT79B1A01817'  # 设备名字 -随便写
    desired_caps['appPackage'] = 'com.xueqiu.android'  # app包名 com.intsig.camscanner
    desired_caps['appActivity'] = ".view.WelcomeActivityAlias"  # app启动名  .MainMenuActivity
    desired_caps['noReset'] = 'True'  # 不用重置
    desired_caps['skipServerInstallation'] = True # 不用重置
    desired_caps['skipServerInitialization'] = True
    desired_caps['automationName'] = 'Uiautomator2'  #获取toast消息
    # 声明手机驱动对象 POST接口 创建session 自启动 启动参数中指定的包名和启动名的app
    return webdriver.Remote("http://127.0.0.2:4723/wd/hub", desired_caps)




if __name__ == '__main__':
    get_android_driver()
    time.sleep(2)
