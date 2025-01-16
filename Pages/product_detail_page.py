from selenium.webdriver.common.by import By


class ProductDetailPage:
    product_name = "//div[@class='product-information']/h2"
    category_name = "//div[@class='product-information']/p[contains(text(),'Category')]"
    amount = "//div[@class='product-information']/span/span[contains(text(),'Rs')]"
    quantity = "//div[@class='product-information']/span/label[contains(text(),'Quantity')]"
    availability = "//div[@class='product-information']/p[2]/b[contains(text(),'Availability')]"
    condition = "//div[@class='product-information']/p[3]/b[contains(text(),'Condition')]"
    brand = "//div[@class='product-information']/p[4]/b[contains(text(),'Brand')]"

    def __init__(self, driver):
        self.driver = driver

    def is_product_name_visible(self):
        return self.driver.find_element(by=By.XPATH, value=self.product_name).is_displayed()

    def is_category_name_visible(self):
        return self.driver.find_element(by=By.XPATH, value=self.category_name).is_displayed()

    def is_amount_visible(self):
        return self.driver.find_element(by=By.XPATH, value=self.amount).is_displayed()

    def is_quantity_visible(self):
        return self.driver.find_element(by=By.XPATH, value=self.quantity).is_displayed()

    def is_availability_visible(self):
        return self.driver.find_element(by=By.XPATH, value=self.availability).is_displayed()

    def is_condition_visible(self):
        return self.driver.find_element(by=By.XPATH, value=self.condition).is_displayed()

    def is_brand_visible(self):
        return self.driver.find_element(by=By.XPATH, value=self.brand).is_displayed()

