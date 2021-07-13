import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver: WebDriver
    _black_list =[(By.ID,'iv_close')]
    def __init__(self,driver: WebDriver = None):
        self._driver =driver
    def find(self,locator,value,timeout=30, poll_frequency=1.0):
        try:
            element= WebDriverWait(self._driver, timeout, poll_frequency).until(lambda x: x.find_element(locator,value))
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_element(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return  self.find(locator,value)


    def steps(self,path):
        with open(path) as f:
            steps=yaml.safe_load(f)
            element = None
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step['by'],step['locator'])
                if "action" in step.keys():
                    action = step['action']
                    if action == "click":
                        element.click()



