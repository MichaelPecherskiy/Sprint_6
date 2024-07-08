from tests.locators import main_page_locators
from pages.main_page import MainPage
import allure


class TestQuestion:
    @allure.title("Тест ответ на первый вопрос")
    @allure.description("Этот тест проверяет ответ на первый вопрос в FAQ")
    def test_question_1(self, driver, wait):
        with allure.step("Открытие страницы"):
            main_page = MainPage(driver)
        with allure.step("Принятие cookies"):
            main_page.cookie()
        with allure.step("нахождение первого вопроса"):
            main_page.scroll_page_to_view(main_page_locators.MainPageLocators.QUESTION1)
            main_page.wait_for_element_after_scroll(main_page_locators.MainPageLocators.QUESTION1, wait)
        with allure.step("клик на первый вопрос и проверка ответа"):
            main_page.click_and_check_answer(
                main_page_locators.MainPageLocators.QUESTION1,
                main_page_locators.MainPageLocators.ANSWER1,
                "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
            )

    @allure.title("Тест ответ на второй вопрос")
    @allure.description("Этот тест проверяет ответ на второй вопрос в FAQ")
    def test_question_2(self, driver, wait):
        with allure.step("Открытие страницы"):
            main_page = MainPage(driver)
        with allure.step("Принятие cookies"):
            main_page.cookie()
        with allure.step("нахождение второго вопроса"):
            main_page.scroll_page_to_view(main_page_locators.MainPageLocators.QUESTION2)
            main_page.wait_for_element_after_scroll(main_page_locators.MainPageLocators.QUESTION2, wait)
        with allure.step("клик на второй вопрос и проверка ответа"):
            main_page.click_and_check_answer(
                main_page_locators.MainPageLocators.QUESTION2,
                main_page_locators.MainPageLocators.ANSWER2,
                "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
            )

    @allure.title("Тест ответ на третий вопрос")
    @allure.description("Этот тест проверяет ответ на третий вопрос в FAQ")
    def test_question_3(self, driver, wait):
        with allure.step("Открытие страницы"):
            main_page = MainPage(driver)
        with allure.step("Принятие cookies"):
            main_page.cookie()
        with allure.step("нахождение третьего вопроса"):
            main_page.scroll_page_to_view(main_page_locators.MainPageLocators.QUESTION3)
            main_page.wait_for_element_after_scroll(main_page_locators.MainPageLocators.QUESTION3, wait)
        with allure.step("клик на третий вопрос и проверка ответа"):
            main_page.click_and_check_answer(
                main_page_locators.MainPageLocators.QUESTION3,
                main_page_locators.MainPageLocators.ANSWER3,
                "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
            )

    @allure.title("Тест ответ на четвертый вопрос")
    @allure.description("Этот тест проверяет ответ на четверты вопрос в FAQ")
    def test_question_4(self, driver, wait):
        with allure.step("Открытие страницы"):
            main_page = MainPage(driver)
        with allure.step("Принятие cookies"):
            main_page.cookie()
        with allure.step("нахождение четвертого вопроса"):
            main_page.scroll_page_to_view(main_page_locators.MainPageLocators.QUESTION4)
            main_page.wait_for_element_after_scroll(main_page_locators.MainPageLocators.QUESTION4, wait)
        with allure.step("клик на четвертый вопрос и проверка ответа"):
            main_page.click_and_check_answer(
                main_page_locators.MainPageLocators.QUESTION4,
                main_page_locators.MainPageLocators.ANSWER4,
                "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
            )

    @allure.title("Тест ответ на пятый вопрос")
    @allure.description("Этот тест проверяет ответ на пятый вопрос в FAQ")
    def test_question_5(self, driver, wait):
        with allure.step("Открытие страницы"):
            main_page = MainPage(driver)
        with allure.step("Принятие cookies"):
            main_page.cookie()
        with allure.step("нахождение пятого вопроса"):
            main_page.scroll_page_to_view(main_page_locators.MainPageLocators.QUESTION5)
            main_page.wait_for_element_after_scroll(main_page_locators.MainPageLocators.QUESTION5, wait)
        with allure.step("клик на пятый вопрос и проверка ответа"):
            main_page.click_and_check_answer(
                main_page_locators.MainPageLocators.QUESTION5,
                main_page_locators.MainPageLocators.ANSWER5,
                "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
            )

    @allure.title("Тест ответ на шестой вопрос")
    @allure.description("Этот тест проверяет ответ на шестой вопрос в FAQ")
    def test_question_6(self, driver, wait):
        with allure.step("Открытие страницы"):
            main_page = MainPage(driver)
        with allure.step("Принятие cookies"):
            main_page.cookie()
        with allure.step("нахождение шестого вопроса"):
            main_page.scroll_page_to_view(main_page_locators.MainPageLocators.QUESTION6)
            main_page.wait_for_element_after_scroll(main_page_locators.MainPageLocators.QUESTION6, wait)
        with allure.step("клик на шестой вопрос и проверка ответа"):
            main_page.click_and_check_answer(
                main_page_locators.MainPageLocators.QUESTION6,
                main_page_locators.MainPageLocators.ANSWER6,
                "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
            )

    @allure.title("Тест ответ на сеьмой вопрос")
    @allure.description("Этот тест проверяет ответ на седьмой вопрос в FAQ")
    def test_question_7(self, driver, wait):
        with allure.step("Открытие страницы"):
            main_page = MainPage(driver)
        with allure.step("Принятие cookies"):
            main_page.cookie()
        with allure.step("нахождение седьмого вопроса"):
            main_page.scroll_page_to_view(main_page_locators.MainPageLocators.QUESTION7)
            main_page.wait_for_element_after_scroll(main_page_locators.MainPageLocators.QUESTION7, wait)
        with allure.step("клик на седьмой вопрос и проверка ответа"):
            main_page.click_and_check_answer(
                main_page_locators.MainPageLocators.QUESTION7,
                main_page_locators.MainPageLocators.ANSWER7,
                "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
            )

    @allure.title("Тест ответ на восьмой вопрос")
    @allure.description("Этот тест проверяет ответ на восьмой вопрос в FAQ")
    def test_question_8(self, driver, wait):
        with allure.step("Открытие страницы"):
            main_page = MainPage(driver)
        with allure.step("Принятие cookies"):
            main_page.cookie()
        with allure.step("нахождение восьмого вопроса"):
            main_page.scroll_page_to_view(main_page_locators.MainPageLocators.QUESTION8)
            main_page.wait_for_element_after_scroll(main_page_locators.MainPageLocators.QUESTION8, wait)
        with allure.step("клик на восьмой вопрос и проверка ответа"):
            main_page.click_and_check_answer(
                main_page_locators.MainPageLocators.QUESTION8,
                main_page_locators.MainPageLocators.ANSWER8,
                "Да, обязательно. Всем самокатов! И Москве, и Московской области."
            )
