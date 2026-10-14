import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import data
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        if not data.URBAN_ROUTES_URL:
            pytest.skip("URBAN_ROUTES_URL is not set: the bootcamp-hosted Urban Routes server is no longer available")
        # Performance logging is required to read the SMS confirmation code (see helpers.retrieve_phone_code).
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()
        cls.driver.get(data.URBAN_ROUTES_URL)

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route_addresses(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert routes_page.get_from_field_text() == data.ADDRESS_FROM
        assert routes_page.get_to_field_text() == data.ADDRESS_TO

    def test_select_plan(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_a_taxi_button()
        routes_page.click_comfort_option()
        assert "active" in routes_page.get_selected_tariff_option()

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_phone(data.PHONE_NUMBER)
        assert routes_page.get_inserted_phone_number() == data.PHONE_NUMBER

    def test_fill_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_card(data.CARD_NUMBER, data.CARD_CODE)
        assert routes_page.get_current_payment_method() != ""

    def test_comment_for_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_and_handkerchiefs_option()
        assert routes_page.is_blanket_and_handkerchiefs_option_checked() == True

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_add_ice_cream_button(2)
        assert routes_page.get_current_icecream_amount() == "2"

    def test_car_search_model_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_button()
        assert routes_page.is_order_taxi_popup_displayed() == True