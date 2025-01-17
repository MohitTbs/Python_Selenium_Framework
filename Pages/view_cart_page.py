from selenium.webdriver.common.by import By


class ViewCartPage:
    product_name = "//table[@id='cart_info_table']/tbody/tr/td[@class='cart_description']//a"
    product_price = "//table[@id='cart_info_table']/tbody/tr/td[@class='cart_price']/p"
    quantity_box = "//td[@class='cart_quantity']/button"

    def __init__(self, driver):
        self.driver = driver

    def get_name_and_price(self):
        names = self.driver.find_elements(by=By.XPATH, value=self.product_name)
        prices = self.driver.find_elements(by=By.XPATH, value=self.product_price)
        l1 = []
        for i in range(0, len(names)):
            l2 = []
            l2.append(names[i].text)
            l2.append(prices[i].text)
            l1.append(l2)

        return l1

    def get_quantity(self):
        return self.driver.find_element(by=By.XPATH, value=self.quantity_box).text
