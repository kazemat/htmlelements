from . import Element
from ..log import CLICK


class Widget(Element):

    def __init__(self, element, name=None, logger=None):
         super(Widget, self).__init__(element, type='Виджет', name=name, logger=logger)

    def click(self):
        self.logger.info(CLICK.format(self))
        self._element.click()

    def is_selected(self):
         return super(Widget, self).is_selected()

    def is_displayed(self):
        return super(Widget, self).is_displayed()

    def is_enabled(self):
        return super(Widget, self).is_enabled()
