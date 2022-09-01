from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
	def add_to_basket(self):
		add_to_basket = self.browser.find_element(*MainPageLocators.BASKET_ADD_LINK)
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
