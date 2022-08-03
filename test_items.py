import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.regression
@pytest.mark.smoke
def test_add_to_basket_button_is_visible(browser):
    browser.get(link)
    #time.sleep(30)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    try:
        browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
        present_elem = True
    except:
        present_elem = False
    assert present_elem, "No add_card button on page"


#add_to_basket_form .btn.btn-lg.btn-primary.btn-add-to-basket
