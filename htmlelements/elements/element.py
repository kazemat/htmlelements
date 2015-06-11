from selenium.common.exceptions import NoSuchElementException


class Element(object):

    def __init__(self, element, type='Element'):
        self._element = element
        self.__type = type
        self.locator = None

    def __str__(self):
        return "<{0}({1})>".format(self.__type, self._element)

    __repr__ = __str__

    def is_selected(self):
        return self._element.is_selected()

    def is_displayed(self):
        return self._element.is_displayed()

    def is_enabled(self):
        return self._element.is_enabled()

    def get_attribute(self, attr):
        return self._element.get_attribute(attr)

    @property
    def text(self):
        return self._element.text
