from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ProductPage:
    view_product_btns = "//a[text()='View Product']"
    search_box = "search_product"
    submit_search_btn = "submit_search"
    product_names = "//div[@class='features_items']//div[@class='single-products']/div/p"

    def __init__(self, driver):
        self.driver = driver

    def click_on_view_product_btn(self, index):
        btns = self.driver.find_elements(by=By.XPATH, value=self.view_product_btns)
        self.driver.execute_script("arguments[0].scrollIntoView();", btns[0])
        btns[0].click()

    def enter_product_name(self, p_name):
        self.driver.find_element(by=By.ID, value=self.search_box).send_keys(p_name)

    def click_on_submit_search_btn(self):
        self.driver.find_element(by=By.ID, value=self.submit_search_btn).click()

    def get_name_of_all_products(self):
        eles = self.driver.find_elements(by=By.XPATH, value=self.product_names)
        names = []
        for i in eles:
            names.append(i.text)

        return names
