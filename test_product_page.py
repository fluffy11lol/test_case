import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

link_list = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
             pytest.param(
	             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
	             marks=pytest.mark.xfail),
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.need_review
@pytest.mark.parametrize('link', link_list)
def test_guest_can_add_product_to_basket(browser, link):
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


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.click_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.open_basket()
	page.is_element_present("xpath", '''//*[@id="content_inner"]/p''')


class TestUserAddToBasketFromProductPage:

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		import time  # в начале файла

		email = str(time.time()) + "@fakemail.org"
		link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
		page = LoginPage(browser, link)
		page.open()
		page.register_new_user(email, "login_password")

	@pytest.mark.parametrize('link', link_list)
	def test_user_cant_see_success_message(self, browser, link):
		page = ProductPage(browser, link)
		page.open()
		page.is_not_success_message_presented()

	@pytest.mark.need_review
	@pytest.mark.parametrize('link', link_list)
	def test_user_can_add_product_to_basket(self, browser, link):
		page = ProductPage(browser, link)
		page.open()
		page.add_to_basket()
		page.solve_quiz_and_get_code()
		page.check_name()
		page.check_price()
