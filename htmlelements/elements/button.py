from htmlelements.elements.element import Element
from ..log import CLICK


class Button(Element):

    def __init__(self, element, name=None, logger=None):
        super(Button, self).__init__(element, type='Кнопка', name=name, logger=logger)

    def click(self):
        self.logger.info(CLICK.format(self))
        self._element.click()
