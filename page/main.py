from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Main(BasePage):
    def goto_serach(self):
        self.steps("../page/main.yml")
    def goto_windows(self):
        self.find(By.ID,'post_status').click()
        self.find(By.ID,'home_search').click()