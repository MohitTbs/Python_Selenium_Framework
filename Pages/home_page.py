from selenium.webdriver.common.by import By


class HomePage:
    product_link = "//a[contains(@href,'/products')]"

    def __init__(self, driver):
        self.driver = driver

    def click_on_product_link(self):
        self.driver.find_element(by=By.XPATH, value=self.product_link).click()
