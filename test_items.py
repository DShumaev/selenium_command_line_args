from selenium.common.exceptions import NoSuchElementException
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class Test_shop:
    def test_product_page_have_button_for_add_to_basket(self, browser):
        browser.get(link)
        time.sleep(30)
        try:
            browser.find_element_by_class_name("btn-add-to-basket")
        except NoSuchElementException:
            assert False, "Button for add product to basket not found"

