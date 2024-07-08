import pytest
import allure
from tests.locators import order_page_locators
from tests.locators.main_page_locators import MainPageLocators
from tests.locators.order_page_locators import OrderPageLocators
from pages.order_page import OrderPage




class TestOrderPage:
    @allure.title("Тест оформления заказа через хедер")
    @allure.description("Этот тест проверяет оформление заказа через кнопку в хедере")
    @pytest.mark.parametrize("name, surname, address, phone, station, date, comments", [
        ('Миша', 'Иванов', 'ул. Пушкина, д. 10', '79651111111', 'Бульвар Рокосовского', '20.05.2025', 'comments21'),
    ])
    def test_order_page_by_header(self, driver, wait, name, surname, address, phone, station, date, comments):
        with allure.step("Открытие страницы заказа"):
            order_page = OrderPage(driver)
        with allure.step("Принятие cookies"):
            order_page.cookie()
        with allure.step("нажатие на кнопку заказа"):
            driver.find_element(*MainPageLocators.BUTTON_ORDER).click()
        with allure.step("заполнение первой страницы"):
            order_page.first_page_order(name, surname, address, phone, station)
        with allure.step("ожидание кнопки далее и нажатие на кнопку"):
            order_page.wait_for_element_after_scroll(order_page_locators.OrderPageLocators.BUTTON_FURTHER, wait)
            driver.find_element(*OrderPageLocators.BUTTON_FURTHER).click()
        with allure.step("заполнение второй страницы"):
            order_page.second_page_order(date, comments)
        with allure.step("нажатие на кнопку согласен"):
            driver.find_element(*OrderPageLocators.BUTTON_AGREE).click()
        with allure.step("нажатие на кнопку в окне оформление заказа"):
            driver.find_element(*OrderPageLocators.ZAKAZ_OFORMLEN).click()
        with allure.step("клик на страницу самоката"):
            order_page.click_on_samokat()
        with allure.step("клик на страницу яндекса"):
            order_page.click_on_yandex()



    @allure.title("Тест оформления заказа через футер")
    @allure.description("Этот тест проверяет оформление заказа через кнопку в футере")
    @pytest.mark.parametrize("name, surname, address, phone, station, date, comments", [
        ('Олег', 'Петров', 'ул. Лермонтова, д. 11', '79653333333', 'Бульвар Рокосовского', '30.04.2025', 'comments34'),
    ])
    def test_order_page_by_footer(self, driver, wait, name, surname, address, phone, station, date, comments):
        with allure.step("Открытие страницы заказа"):
            order_page = OrderPage(driver)
        with allure.step("Принятие cookies"):
            order_page.cookie()
        with allure.step("нажатие на кнопку заказа"):
            order_page.scroll_page_to_view(OrderPageLocators.BUTTON_ZAKAZ)
        with allure.step("Открытие страницы заказа"):
            driver.find_element(*OrderPageLocators.BUTTON_ZAKAZ).click()
        with allure.step("заполнение первой страницы"):
            order_page.first_page_order(name, surname, address, phone, station)
        with allure.step("ожидание кнопки далее и нажатие на кнопку"):
            order_page.wait_for_element_after_scroll(order_page_locators.OrderPageLocators.BUTTON_FURTHER, wait)
            driver.find_element(*OrderPageLocators.BUTTON_FURTHER).click()
        with allure.step("заполнение второй страницы"):
            order_page.second_page_order(date, comments)
        with allure.step("нажатие на кнопку согласен"):
            driver.find_element(*OrderPageLocators.BUTTON_AGREE).click()
        with allure.step("нажатие на кнопку в окне оформление заказа"):
            driver.find_element(*OrderPageLocators.ZAKAZ_OFORMLEN).click()
        with allure.step("клик на страницу самоката"):
            order_page.click_on_samokat()
        with allure.step("клик на страницу яндекса"):
            order_page.click_on_yandex()
