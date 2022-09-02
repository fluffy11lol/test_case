from time import sleep
import pytest
from links import link_list
from .pages.product_page import ProductPage


@pytest.mark.parametrize('link', link_list)
def test_check_name_and_price_in_basket_page(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.check_name()
	page.check_price()


@pytest.mark.parametrize('link', link_list)
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.is_not_success_message_presented()


@pytest.mark.parametrize('link', link_list)
def test_guest_cant_see_success_message(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.is_not_success_message_presented()


@pytest.mark.parametrize('link', link_list)
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.click_login_link()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.open_basket()
	page.is_element_present("xpath", '''//*[@id="content_inner"]/p''')
