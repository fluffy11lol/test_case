import time

import pytest
from links import link_list
from .pages.main_page import MainPage


@pytest.mark.parametrize('link', link_list)
def test_check_name_and_price_in_basket_page(browser, link):
	page = MainPage(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.check_name()
	page.check_price()


@pytest.mark.parametrize('link', link_list)
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
	page = MainPage(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.is_not_element_presented()


@pytest.mark.parametrize('link', link_list)
def test_guest_cant_see_success_message(browser, link):
	page = MainPage(browser, link)
	page.open()
	page.is_not_element_presented()


@pytest.mark.parametrize('link', link_list)
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser, link):
	page = MainPage(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.is_disappeared()
