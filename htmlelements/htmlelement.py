from selenium.webdriver.common.by import By


class HTMLElement(object):

    def __init__(self, element):
        self._element = element

    def find(self, **kwargs):
        def decor(fnc):
            def searcher(self):
                if kwargs.get('css'):
                    return fnc(self._element.find_element(by=By.CSS_SELECTOR, value=kwargs.get('css')))
                elif kwargs.get('xpath'):
                    return fnc(self._element.find_element(by=By.XPATH, value=kwargs.get('xpath')))
                elif kwargs.get('class'):
                    return fnc(self._element.find_element(by=By.CLASS_NAME, value=kwargs.get('class')))
                elif kwargs.get('id'):
                    return fnc(self._element.find_element(by=By.ID, value=kwargs.get('id')))
                elif kwargs.get('name'):
                    return fnc(self._element.find_element(by=By.NAME, value=kwargs.get('name')))
                else:
                    raise ValueError
            return searcher
        return decor

    def is_selected(self):
        return self._element.is_selected()

    def is_displayed(self):
        return self._element.is_displayed()

    def is_enabled(self):
        return self._element.is_enabled()

    def get_attribute(self, attr):
        return self._element.get_attribute(attr)

    def clear(self):
        self._element.clear()

    def send_keys(self, *args):
        self._element.send_keys(*args)

    @property
    def text(self):
        return self._element.text

    def click(self):
        self._element.click()

    def submit(self):
        self._element.submit()
