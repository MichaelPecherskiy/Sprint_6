from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait

from tests.locators import main_page_locators, order_page_locators
from selenium.webdriver.support import expected_conditions as EC
import allure

URL_YANDEX = 'https://dzen.ru/?yredirect=true'


class OrderPage:
    @allure.step("Открытие сайта")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Принятие cookies")
    def cookie(self):
        self.driver.find_element(*main_page_locators.MainPageLocators.cookie).click()

    @allure.step("ввод текста в поле")
    def input_text(self, value: str, order_page_locator: tuple):
        find_place = self.driver.find_element(*order_page_locator)
        find_place.click()
        find_place.send_keys(value)

    @allure.step("ожилание элемента после скроллинга")
    def wait_for_element_after_scroll(self, locator, wait: WebDriverWait):
        self.scroll_page_to_view(locator)
        wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Заполнение первой страницы заказа")
    def first_page_order(self, name, surname, address, phone, station):
        self.input_text(name, order_page_locators.OrderPageLocators.NAME)
        self.input_text(surname, order_page_locators.OrderPageLocators.SURNAME)
        self.input_text(address, order_page_locators.OrderPageLocators.ADDRESS)
        self.input_text(station, order_page_locators.OrderPageLocators.METRO_STATION)
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*order_page_locators.OrderPageLocators.SELECT_METRO_STATION)) \
            .click().perform()
        self.input_text(phone, order_page_locators.OrderPageLocators.TELEPHONE)

    @allure.step("Заполнение второй страницы заказа")
    def second_page_order(self, date, comments):
        #выбор даты доставки
        date_field = self.driver.find_element(*order_page_locators.OrderPageLocators.DATE_OF_SAMOKAT)
        date_field.send_keys(date)
        date_field.send_keys(Keys.RETURN)
        #выбор срока аренды
        arenda = self.driver.find_element(*order_page_locators.OrderPageLocators.DROP_DOWN_ARENDA)
        arenda.click()
        menu = self.driver.find_element(*order_page_locators.OrderPageLocators.DROP_DOWN_MENU)
        menu.click()
        #выбор цвета самоката
        color = self.driver.find_element(*order_page_locators.OrderPageLocators.COLOUR_OF_SAMOKAT)
        color.click()
        #комментарии
        self.input_text(comments, order_page_locators.OrderPageLocators.COMMENTS)
        #кнопка заказать
        button_further = self.driver.find_element(*order_page_locators.OrderPageLocators.BUTTON_ZAKAZ)
        button_further.click()

    @allure.step("скролл до нужного элемента")
    def scroll_page_to_view(self, locator):
        find_element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", find_element)

    @allure.step("Переход на страницу 'Самокат'")
    def click_on_samokat(self):
        self.driver.find_element(*order_page_locators.OrderPageLocators.LOGO_SAMOKAT).click()
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/", "Переход на страницу 'Самокат' не осуществлен"

    @allure.step("Переход на страницу 'Яндекс'")
    def click_on_yandex(self):
        self.driver.find_element(*order_page_locators.OrderPageLocators.LOGO_YANDEX).click()
