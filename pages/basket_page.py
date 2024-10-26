from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), ("The basket is not empty")

    def no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), ("There are goods in the basket")


