from main_page import BasePage
from order_page import OrderPage


def test_actions(driver):
    bp = BasePage(driver)
    bp.select_clothes()

    op = OrderPage(driver)
    op.make_order()










