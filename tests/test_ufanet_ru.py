import allure
from allure_commons.types import Severity

from models.models import ufanet_page


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Авторизация")
@allure.story("Проверка успешной авторизации")
def test_auth_by_log():
    ufanet_page.open()
    ufanet_page.auth_with_login('72660822', '2053118943')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Базовый функционал")
@allure.story("Проверка перехода на страницу с тарифами")
def test_internet_in_apartment():
    ufanet_page.open()
    ufanet_page.internet_in_apartment_info()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Базовый функционал")
@allure.story("Проверка смены локации")
def test_choose_orsk_city():
    ufanet_page.open()
    ufanet_page.choose_city('Орск')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Базовый функционал")
@allure.story("Проверка перехода на страницу с адресом офисов")
def test_check_office_address():
    ufanet_page.open()
    ufanet_page.check_address_of_offices('Орск')


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Форма заявки на подключение")
@allure.story("Проверка работоспособности формы заявки")
def test_become_a_client_form():
    ufanet_page.open()
    ufanet_page.open_application_form()
