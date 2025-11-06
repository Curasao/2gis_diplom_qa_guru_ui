from selene import browser, be, have, by, command
from allure import step

class FilterPage:
    def open(self):
        browser.open('/ruza/')
        return self

    def fill_search(self, query):
        browser.element('input[placeholder*="Поиск"]').should(be.visible).set_value(query).press_enter()
        return self

    def dostavka_button(self):
        browser.element('label._w9ask7').click()
        return self

    def rate_button(self):
        browser.element('label._1btz1t0f').click()
        return self

    def price_button(self, min_price=180, max_price=500):
        browser.element('input._tupxg39').should(be.visible).clear().type(str(min_price))
        browser.element('input._1kvvnrkq').should(be.visible).clear().type(str(max_price)).press_enter()
        return self

class Realty_Page:

    def realty_open(self):
        browser.open('/ruza/realty/sale')
        return self


    def realty_price_button(self, min_price=4000000, max_price=8000000):
        browser.all('div._1qyj3m0 > input').should(have.size_greater_than(1))
        browser.all('div._1qyj3m0 > input')[0].should(be.visible).clear().type(str(min_price))
        browser.all('div._1qyj3m0 > input')[1].should(be.visible).clear().type(str(max_price)).press_enter()

        return self



    def realty_should_be_loaded(self):
        browser.element('h1, h2').should(have.text('Продажа недвижимости'))
        browser.element('button, [role="button"], a').with_(timeout=10).should(have.text('Фильтры'))
        return self

    def realty_search(self, query):
        browser.open('https://2gis.ru/ruza/realty/sale')
        browser.element('input[placeholder*="Район, улица, дом..."]').should(be.visible).set_value(query).press_enter()
        '''browser.all('div[class*="_s717vn"]').first.click()
        browser.all('._s717vn').first.should(be.visible).click()'''
        return self
class FormPage:

    def form_open(self):
        browser.open('/ruza')
        browser.element('._sp9hpd').should(be.visible)
        browser.element('._sp9hpd').with_(timeout=15).perform(command.js.click)

        return self

    def form_telephone(self,tel):
        browser.element('div').should(have.text('Войти')).should(be.visible).click()
        browser.element('input[placeholder*="Телефон"]').should(be.visible).clear().type(tel).press_enter()
        return self


