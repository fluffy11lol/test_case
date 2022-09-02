import math
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла


class BasePage:
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url

	def open(self):
		self.browser.get(self.url)

	def click_element(self, how, what):
		self.browser.find_element(how, what).click()

	def get_element(self, how, what):
		return self.browser.find_element(how, what)


	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")
