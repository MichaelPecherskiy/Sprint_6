from selenium.webdriver.common.by import By



class OrderPageLocators:

    NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    SELECT_METRO_STATION = (By.XPATH, '//div[@class="select-search__select"]')
    METRO_STATION = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    TELEPHONE = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    BUTTON_FURTHER = (By.XPATH, "//button[text()='Далее']")

    DATE_OF_SAMOKAT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    CHOOSE_DATE_1 = (By.XPATH, '//div[@aria-label="Choose среда, 30-е апреля 2025 г."]')
    CHOOSE_DATE_2 = (By.XPATH, '//div[@aria-label="Choose среда, 30-е марта 2025 г."]')
    CALENDAR = (By.XPATH, '//div[@class="react-datepicker-popper"]')
    DROP_DOWN_ARENDA = (By.XPATH, "//div[@class='Dropdown-root']")
    DROP_DOWN_MENU = (By.XPATH, "//div[@class='Dropdown-menu']")
    CHOOSE_DATA_ARENDA = (By.XPATH, "//div[@class='Dropdown-option' and text()='трое суток']")

    COLOUR_OF_SAMOKAT = (By.XPATH, '//input[@id="black"]')
    COMMENTS = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    BUTTON_AGREE = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]')
    BUTTON_ZAKAZ = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')
    ZAKAZ_OFORMLEN = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Посмотреть статус"]')

    LOGO_SAMOKAT = (By.XPATH, "//img[@src='/assets/scooter.svg' and @alt='Scooter']")
    LOGO_YANDEX = (By.XPATH, "//a[@href='//yandex.ru' and @class='Header_LogoYandex__3TSOI']")

