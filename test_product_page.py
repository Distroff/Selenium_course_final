import time

from .pages.product_page import ProductPage


# def test_guest_can_add_product_to_cart(browser):
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(browser, link)
#     page.open()
#     page.press_button_add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_message_about_adding()
#     page.should_be_message_basket_total()

import pytest
# @pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param(7, marks=pytest.mark.xfail), "8", "9"])
@pytest.mark.parametrize('promo_offer', ["6", pytest.param(7, marks=pytest.mark.xfail), "8"])
def test_offers(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.press_button_add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    time.sleep(2)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.press_button_add_to_basket()  # Добавляем товар в корзину
    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)  # Открываем страницу товара
    page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с  помощью is_not_element_present


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()  # Открываем страницу товара
    page.press_button_add_to_basket()  # Добавляем товар в корзину
    page.should_is_disappeared()  # Проверяем, что нет сообщения об успехе с помощью is_disappeared
