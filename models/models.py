from selene import browser, have, be
import allure


class MainPage:

    def open(self):
        with allure.step("Открыть сайт"):
            browser.open('/')

    def auth_with_login(self, login, password):
        with allure.step("Авторизоваться в личном кабинете"):
            browser.element('.link-lk').click()
            browser.element('[autocomplete="new-login"]').type(login)
            browser.element('[autocomplete="new-password"]').type(password)
            browser.element('[type="submit"]').click()


    def internet_in_apartment_info(self):
        with allure.step("Открыть информацию о тарифах интернета в квартире"):
            browser.element('.link-menu').click()
            browser.element('[href="/ufa/kvartira/internet/"]').click()
            browser.element('h1.title').should(have.text('Интернет и телевидение от Уфанет'))

    def choose_city(self, city):
        with allure.step("Выбрать населенный пункт"):
            browser.element('.city').click()
            browser.element('h2.modal-title').should(have.text('Выберите ваш населенный пункт'))
            browser.element('.modal-bubbles-list').element(f'[data-name="{city}"]').click()
            browser.element('.city').should(have.text(city))

    def check_address_of_offices(self, city):
        with allure.step("Найти адрес офиса в выбранном городе"):
            self.choose_city(city)
            browser.element('[href="/orsk/pages/futer-adresa-ofisov_orsk/"]').click()
            browser.element('h5.addres').should(have.text('ул. Краматорская, 4Б'))

    def open_application_form(self):
        with allure.step("Оставить заявку на подключение услуг"):
            browser.element('.widget__wrapper').element('#btnShowOrderForm').click()
            browser.element('#orderForm-header').element('.title').should(have.text('Укажите ваши данные'))


ufanet_page = MainPage()