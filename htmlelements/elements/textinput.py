from htmlelements.elements.element import Element


class TextInput(Element):

    def __init__(self, element):
        super(TextInput, self).__init__(element, type='TextInput')

    def clear(self):
        self._element.clear()

    def send_keys(self, *value, clear=True):
        if clear is True:
            self.clear()
        self._element.send_keys(*value)

    @property
    def text(self):
        return self._element.text