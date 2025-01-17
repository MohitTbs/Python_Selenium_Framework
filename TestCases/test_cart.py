import time

import pytest

from Pages.home_page import HomePage
from Pages.product_detail_page import ProductDetailPage
from Pages.product_page import ProductPage
from Pages.view_cart_page import ViewCartPage
from Utilities.ConfigReader import read_configuration
from collections import Counter


class Test_Cart:

    def test_selected_items_added_to_cart(self):
        self.driver.get(read_configuration('urls', "mainUrl"))
        homePage = HomePage(self.driver)
        homePage.click_on_product_link()
        productPage = ProductPage(self.driver)
        l1 = productPage.click_on_add_to_cart_btn(2)
        print(l1)
        viewCartPage = ViewCartPage(self.driver)
        l2 = viewCartPage.get_name_and_price()
        print(l2)
        assert Counter(map(tuple, l1)) == Counter(map(tuple, l2))

    def test_count_quantity(self):
        self.driver.get(read_configuration('urls', "mainUrl"))
        homePage = HomePage(self.driver)
        homePage.click_on_view_product_btn(5)
        productDetailPage = ProductDetailPage(self.driver)
        quantity = 5
        productDetailPage.enter_quantity(quantity)
        productDetailPage.click_on_add_to_cart_btn()
        productDetailPage.click_on_view_cart_btn()
        viewCartPage = ViewCartPage(self.driver)
        assert quantity != int(viewCartPage.get_quantity())
