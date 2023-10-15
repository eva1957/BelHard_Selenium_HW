from main_page import BuyCoat
from order_page import MakeOrder
from personal_info_page import PersonalInfo


def test_actions(driver):
    bc = BuyCoat(driver)
    bc.select_clothes()

    op = MakeOrder(driver)
    op.continue_order()

    pi = PersonalInfo(driver)
    pi.complete_order()










