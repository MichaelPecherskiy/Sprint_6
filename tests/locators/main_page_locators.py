from selenium.webdriver.common.by import By


class MainPageLocators:
    cookie = (By.XPATH, "//button[@id='rcc-confirm-button']")
    BUTTON_ORDER = (By.XPATH, '//button[@class="Button_Button__ra12g"]')

    QUESTION1 = (By.XPATH, "//div[@id='accordion__heading-0']")
    QUESTION2 = (By.XPATH, "//div[@id='accordion__heading-1']")
    QUESTION3 = (By.XPATH, "//div[@id='accordion__heading-2']")
    QUESTION4 = (By.XPATH, "//div[@id='accordion__heading-3']")
    QUESTION5 = (By.XPATH, "//div[@id='accordion__heading-4']")
    QUESTION6 = (By.XPATH, "//div[@id='accordion__heading-5']")
    QUESTION7 = (By.XPATH, "//div[@id='accordion__heading-6']")
    QUESTION8 = (By.XPATH, "//div[@id='accordion__heading-7']")

    ANSWER1 = (By.XPATH, "//div[@id='accordion__panel-0']//p")
    ANSWER2 = (By.XPATH, "//div[@id='accordion__panel-1']//p")
    ANSWER3 = (By.XPATH, "//div[@id='accordion__panel-2']//p")
    ANSWER4 = (By.XPATH, "//div[@id='accordion__panel-3']//p")
    ANSWER5 = (By.XPATH, "//div[@id='accordion__panel-4']//p")
    ANSWER6 = (By.XPATH, "//div[@id='accordion__panel-5']//p")
    ANSWER7 = (By.XPATH, "//div[@id='accordion__panel-6']//p")
    ANSWER8 = (By.XPATH, "//div[@id='accordion__panel-7']//p")