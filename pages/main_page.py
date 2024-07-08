import allure
from tests.locators import main_page_locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    @allure.step("Открытие сайта")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Принятие cookies")
    def cookie(self):
        self.driver.find_element(*main_page_locators.MainPageLocators.cookie).click()

    @allure.step("скролл до нужного элемента")
    def scroll_page_to_view(self, locator):
        find_element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", find_element)

    @allure.step("ожидание элемента после скроллинга")
    def wait_for_element_after_scroll(self, locator, wait: WebDriverWait):
        self.scroll_page_to_view(locator)
        wait.until(EC.visibility_of_element_located(locator))

    @allure.step("клик на вопрос и ответ")
    def click_and_check_answer(self, question_locator, answer_locator, expected_text):
        self.driver.find_element(*question_locator).click()
        answer = self.driver.find_element(*answer_locator)
        text = answer.text
        assert text == expected_text, f"Expected text: {expected_text}, but got: {text}"
