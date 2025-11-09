import allure

from ui.pages.test_2gis import Realty_Page
from ui.pages.test_2gis import FilterPage
from ui.pages.test_2gis import FormPage

@allure.feature("Фильтрация 2GIS")
@allure.story("Поиск кофеен")
@allure.title("Открыть страницу и выполнить поиск кофеен")
def test_form_submission(setup_browser_filter):
        filter_page = FilterPage()
        filter_page.open()
        filter_page.fill_search("Кофейни")
        filter_page.dostavka_button()
        filter_page.rate_button()
        filter_page.price_button()

@allure.title("Поиск недвижимости по городу")
def test_realty_search(setup_browser_realty):
    realty_page = Realty_Page()
    realty_page.realty_search("Тучково")

@allure.title("Открыть недвижимость и выставить фильтр цены")
def test_realty_filters_price_and_rooms(setup_browser_realty):
    realty_page = Realty_Page()
    realty_page.realty_open()
    realty_page.realty_price_button(4000000, 800000)

@allure.feature("Форма пользователя 2GIS")
@allure.story("Проверка номера телефона")
@allure.title("Вход с корректным номером")
def test_valid_login(setup_browser_form):

    form_page = FormPage()
    form_page.form_open()
    form_page.form_telephone('+7965555555')

@allure.title("Вход с некорректным номером")
def test_unvalid_login(setup_browser_form):
    form_page = FormPage()
    form_page.form_open()
    form_page.form_telephone('+555555555555555555555555555')







