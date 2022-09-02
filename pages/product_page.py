from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ProductPage(BasePage):
	def add_to_basket(self):
		add_to_basket = self.browser.find_element(*ProductPageLocators.BASKET_ADD_LINK)
		add_to_basket.click()

	def check_name(self):
		product_name = self.browser.find_element("tag name", "h1").text
		print(product_name)
		product_name_in_basket = self.browser.find_element("css selector",
		                                                   "#messages > div:nth-child(1) > div > strong").text
		print(product_name_in_basket)
		assert product_name == product_name_in_basket, f"not a valid name/n {self.browser.current_url}"

	def check_price(self):
		product_price = self.browser.find_elements("class name", "price_color")[1].text
		print(product_price)
		product_price_in_basket = self.browser.find_element("class name",
		                                                    "basket-mini").text
		print(product_price_in_basket)
		assert product_price in product_price_in_basket, f"not a valid price/n {self.browser.current_url}"

	def is_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
		except TimeoutException:
			return False

		return True

	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
		except TimeoutException:
			return True

		return False

	def is_not_success_message_presented(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"

	def is_disappear(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException). \
				until_not(expected_conditions.presence_of_element_located((how, what)))
		except TimeoutException:
			return False

		return True

	def is_disappeared(self):
		assert self.is_disappear(*ProductPageLocators.SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"

	def should_be_login_link(self):
		assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"

	def is_clickable(self, button):
		try:
			button.click()
			return True
		except WebDriverException:
			return False

	def click_login_link(self):
		button = self.get_element(*ProductPageLocators.LOGIN_LINK)
		assert self.is_clickable(button), "button is not clickable"
