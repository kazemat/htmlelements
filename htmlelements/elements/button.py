from htmlelements.elements.element import Element
from ..log import CLICK


class Button(Element):

    def __init__(self, element, name=None, logger=None):
        super(Button, self).__init__(element, type='Кнопка', name=name, logger=logger)

    def click(self):
        self.logger.info(CLICK.format(self))
        self._element.click()

    def is_selected(self):
         return super(Button, self).is_selected()

    def is_displayed(self):
        return super(Button, self).is_displayed()

    def is_enabled(self):
        return super(Button, self).is_enabled()