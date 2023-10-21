from main_page import LoginPage
from main_page import Filters
from main_page import DropdownMenu
from coat_page import CoatPage
from help_with_size import HelpWithSize
from wishlist_page import AddToWishlist
from wishlist_page import Wishlist
from order_page import MakeOrder
from order_page import ChooseDeliveryAndPayment
from personal_info_page import PersonalInfo


def test_accept_cookie(driver):
    lp = LoginPage(driver)
    lp.go_to_site()


def test_choose_filters(driver):
    fil = Filters(driver)
    fil.select_filters()


def test_click_dropdown_menu(driver):
    dm = DropdownMenu(driver)
    dm.select_clothes()


def test_select_size(driver):
    cp = CoatPage(driver)
    cp.select_size()


def test_click_list_with_size(driver):
    hw = HelpWithSize(driver)
    hw.help_with_size()


def test_add_to_wishlist(driver):
    wl = AddToWishlist(driver)
    wl.add_to_wl()


def test_go_to_basket(driver):
    wab = Wishlist(driver)
    wab.wishlist_and_basket()


def test_make_order(driver):
    op = MakeOrder(driver)
    op.continue_order()


def test_choose_delivery(driver):
    cd = ChooseDeliveryAndPayment(driver)
    cd.delivery_and_payment()


def test_finish_order(driver):
    pi = PersonalInfo(driver)
    pi.complete_order()
