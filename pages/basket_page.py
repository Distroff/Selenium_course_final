from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), ("The basket is not empty")
        pass

    def no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), ("There are goods in the basket")
        pass

'''
basket_page.py - создаем для двух методов. В которых и реализуем две проверки.

Позитивную - проверяет текст что корзина пуста.
Негативную - проверяет что в корзине нет товара, и если он есть, написать осмысленное сообщение ассерта.
В BasePage нужно реализовать метод перехода в корзину, с любой страницы guest_click_button_see_basket

.table-condensed - он есть, когда корзина не пуста
'''