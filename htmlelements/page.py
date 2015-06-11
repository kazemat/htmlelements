from selenium.webdriver.common.by import By



class Page(object):

    def __init__(self, driver):
        self._driver = driver

    def find(self, fnc, **kwargs):
        if kwargs.get('css'):
            return fnc(self._driver.find_element(by=By.CSS_SELECTOR, value=kwargs.get('css')))
        elif kwargs.get('xpath'):
            return fnc(self._driver.find_element(by=By.XPATH, value=kwargs.get('xpath')))
        elif kwargs.get('class'):
            return fnc(self._driver.find_element(by=By.CLASS_NAME, value=kwargs.get('class')))
        elif kwargs.get('id'):
            return fnc(self._driver.find_element(by=By.ID, value=kwargs.get('id')))
        elif kwargs.get('name'):
            return fnc(self._driver.find_element(by=By.NAME, value=kwargs.get('name')))
        else:
            raise ValueError
