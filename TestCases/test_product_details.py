import time

import pytest

from Pages.home_page import HomePage
from Pages.product_detail_page import ProductDetailPage
from Pages.product_page import ProductPage
from Utilities.ConfigReader import read_configuration


class Test_ProductDetail:

    # @pytest.mark.usefixtures('fic')
    def test_verify_product_detail(self):
        self.driver.get(read_configuration('urls', "mainUrl"))
        homePage = HomePage(self.driver)
        homePage.click_on_product_link()
        productPage = ProductPage(self.driver)
        productPage.click_on_view_product_btn(0)
        productDetailPage = ProductDetailPage(self.driver)
        assert productDetailPage.is_amount_visible()
        assert productDetailPage.is_product_name_visible()
        assert productDetailPage.is_brand_visible()
        assert productDetailPage.is_availability_visible()
        assert productDetailPage.is_category_name_visible()
        assert productDetailPage.is_quantity_visible()
        assert productDetailPage.is_condition_visible()
        time.sleep(2)

    # @pytest.fixture
    # def fic(self):
    #     print('I am a fixtire')
