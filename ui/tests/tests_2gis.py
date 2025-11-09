import allure

from ui.pages.test_2gis import Realty_Page
from ui.pages.test_2gis import FilterPage
from ui.pages.test_2gis import FormPage


def test_form_submission(setup_browser_filter):
 @allure.step("Проверка поиска кофеен"):
    filter_page = FilterPage()
    filter_page.open()
    filter_page.fill_search("Кофейни")
 @allure.step("Применить фильтры: доставка, рейтинг, цена"):
    filter_page.dostavka_button()
    filter_page.rate_button()
    filter_page.price_button()


def test_realty_search(setup_browser_realty):
 @allure.step("Поиск недвижимости по городу"):
    realty_page = Realty_Page()
    realty_page.realty_search("Тучково")


def test_realty_filters_price_and_rooms(setup_browser_realty):
 @allure.step("Открыть недвижимость и выставить фильтр цены"):
    realty_page = Realty_Page()
    realty_page.realty_open()
    realty_page.realty_price_button(4000000, 800000)  # Пример установки цены

def test_valid_login(setup_browser_form):
 @allure.step("Вход с корректным номером"):
    form_page = FormPage()
    form_page.form_open()
    form_page.form_telephone('+7965555555')


def test_unvalid_login(setup_browser_form):
 @allure.step("Вход с некорректным номером"):
    form_page = FormPage()
    form_page.form_open()
    form_page.form_telephone('+555555555555555555555555555')







