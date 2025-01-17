import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ProductPage:
    view_product_btns = "//a[text()='View Product']"
    search_box = "search_product"
    submit_search_btn = "submit_search"
    product_names = "//div[@class='features_items']//div[@class='single-products']/div/p"
    add_to_cart_center = "//div[@class='productinfo text-center']//a[@data-product-id]"
    add_to_cart_overlay = "//div[@class='product-overlay']//a[@data-product-id]"
    continue_shopping_btn = "//div[@id='cartModal']//button[text()='Continue Shopping']"
    add_to_cart_overlay_price = "//div[@class='overlay-content']/h2"
    add_to_cart_overlay_name = "//div[@class='overlay-content']/p"
    view_cart_btn = "//div[@id='cartModal']//a[contains(@href,'view_cart')]"

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

    def _get_add_to_cart_center(self):
        return self.driver.find_elements(by=By.XPATH, value=self.add_to_cart_center)

    def _get_add_to_cart_overlay(self):
        return self.driver.find_elements(by=By.XPATH, value=self.add_to_cart_overlay)

    def _get_add_to_cart_overlay_price(self):
        return self.driver.find_elements(by=By.XPATH, value=self.add_to_cart_overlay_price)

    def _get_add_to_cart_overlay_name(self):
        return self.driver.find_elements(by=By.XPATH, value=self.add_to_cart_overlay_name)

    def click_on_continue_shopping_btn(self):
        self.driver.find_element(by=By.XPATH, value=self.continue_shopping_btn).click()

    def click_on_view_cart_btn(self):
        self.driver.find_element(by=By.XPATH, value=self.view_cart_btn).click()

    def click_on_add_to_cart_btn(self, number_of_items_to_be_added):
        btn1 = self._get_add_to_cart_center()
        btn2 = self._get_add_to_cart_overlay()
        prices = self._get_add_to_cart_overlay_price()
        names = self._get_add_to_cart_overlay_name()
        act = ActionChains(self.driver)
        l1 = []
        for i in range(0, number_of_items_to_be_added):
            l2 = []
            self.driver.execute_script("arguments[0].scrollIntoView();", btn1[i])
            act.move_to_element(btn1[i]).perform()
            time.sleep(1)
            price = prices[i].text
            name = names[i].text
            l2.append(name)
            l2.append(price)
            l1.append(l2)
            btn2[i].click()
            time.sleep(1)
            if i != (number_of_items_to_be_added - 1):
                self.click_on_continue_shopping_btn()
                time.sleep(1.5)
            else:
                self.click_on_view_cart_btn()
        return l1
