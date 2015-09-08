from htmlelements.elements.element import Element
from ..log import SEND_KEYS


class TextInput(Element):

    def __init__(self, element, name=None, logger=None):
        super(TextInput, self).__init__(element, type='Поле ввода', name=name, logger=logger)
        self.entered_value = None

    def clear(self):
        self.logger.info('Очищаю {0}'.format(self))
        self._element.clear()

    def send_keys(self, value, clear=True):
        if clear is True:
            self.clear()
        self.entered_value = value
        self.logger.info(SEND_KEYS.format(self))
        self._element.send_keys(value)

    @property
    def text(self):
        return self._element.text

    def is_selected(self):
         return super(TextInput, self).is_selected()

    def is_displayed(self):
        return super(TextInput, self).is_displayed()

    def is_enabled(self):
        return super(TextInput, self).is_enabled()