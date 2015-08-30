from selenium.webdriver.common.by import By


class Page(object):

    def __init__(self, element, name=None):
        self._element = element

    def is_displayed(self):
        return self._element.is_displayed()

    def is_enabled(self):
        return self._element.is_enabled()

    def get_attribute(self, attr):
        return self._element.get_attribute(attr)

    @property
    def text(self):
        return self._element.text

    def find_element(self, by, value):
        return self._element.find_element(by, value)
