from htmlelements.elements.element import Element, NoSuchElementException
from ..log import CLICK


class CheckBox(Element):

    def __init__(self, element, name=None, logger=None):
        super(CheckBox, self).__init__(element, type='Чекбокс', name=name, logger=logger)

    def select(self):
        if not self.is_selected():
            self.logger.info(CLICK.format(self))
            self._element.click()

    def deselect(self):
        if self.is_selected():
            self.logger.info(CLICK.format(self))
            self._element.click()

    @property
    def label(self):
        try:
            return self._element.find_element_by_xpath(".//following-sibling::label")
        except NoSuchElementException:
            return None

    @property
    def label_text(self):
        if self.label is not None:
            result = self.label.text
            self.logger.debug('Текст метки "{0}" соответствует "{1}"'.format(self, result))
            return result
        else:
            return None