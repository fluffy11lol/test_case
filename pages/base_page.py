import math
from .locators import BasePageLocators
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


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

	def is_element_present(self, how, what, timeout=1):
		try:
			WebDriverWait(self.browser, timeout).until(expected_conditions.presence_of_element_located((how, what)))
		except TimeoutException:
			return False

		return True

	def should_be_authorized_user(self):
		assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
		                                                             " probably unauthorised user"

	def open_basket(self):
		self.browser.find_element("xpath", '''//*[@id="default"]/header/div[1]/div/div[2]/span/a''').click()
