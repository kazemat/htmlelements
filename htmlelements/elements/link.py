from htmlelements.elements.element import Element
from ..log import CLICK


class Link(Element):

    def __init__(self, element, name=None, logger=None):
        super(Link, self).__init__(element, type='Ссылка', name=name, logger=logger)

    def get_text(self):
        return self.text

    def get_reference(self):
        return self.get_attribute("href")

    def click(self):
        self.logger.info(CLICK.format(self))
        self._element.click()

    def is_selected(self):
         return super(Link, self).is_selected()

    def is_displayed(self):
        return super(Link, self).is_displayed()

    def is_enabled(self):
        return super(Link, self).is_enabled()