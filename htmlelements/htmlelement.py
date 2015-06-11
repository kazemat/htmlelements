class HTMLElement(object):

    def __init__(self, element):
        self._element = element

    def find_element(self, by, value):
        self._element.find_element(by, value)

    def find_elements(self, by, value):
        self._element.find_elements(by, value)

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
