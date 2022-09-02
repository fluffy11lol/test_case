from .base_page import BasePage


class LoginPage(BasePage):
	def register_new_user(self, email, password):
		self.get_element("css selector", "#id_registration-email").send_keys(email)
		self.get_element("css selector", "#id_registration-password1").send_keys(password)
		self.get_element("css selector", "#id_registration-password2").send_keys(password)
		self.click_element("css selector", "#register_form > button")
