from .pages.product_page import ProductPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/"
	page = ProductPage(browser, link)
	page.open()
	page.open_basket()
	page.is_element_present("xpath", '''//*[@id="content_inner"]/p''')
