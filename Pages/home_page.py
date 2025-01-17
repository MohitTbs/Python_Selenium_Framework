from selenium.webdriver.common.by import By


class HomePage:
    product_link = "//a[contains(@href,'/products')]"
    subscribe_email_box = "susbscribe_email"
    subscribe_btn = "subscribe"
    subscribe_success_msg = "//*[text()='You have been successfully subscribed!' ]"
    view_product_btn = "//a[text()='View Product']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_product_link(self):
        self.driver.find_element(by=By.XPATH, value=self.product_link).click()

    def enter_email_in_subscription_box(self, email):
        self.driver.find_element(by=By.ID, value=self.subscribe_email_box).send_keys(email)

    def click_on_subscribe_btn(self):
        self.driver.find_element(by=By.ID, value=self.subscribe_btn).click()

    def get_subscription_success_msg(self):
        return self.driver.find_element(by=By.XPATH, value=self.subscribe_success_msg).is_displayed()

    def click_on_view_product_btn(self, index):
        eles = self.driver.find_elements(by=By.XPATH, value=self.view_product_btn)
        self.driver.execute_script("arguments[0].scrollIntoView();", eles[index])
        eles[index].click()
