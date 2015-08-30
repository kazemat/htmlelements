from htmlelements.elements.element import Element, NoSuchElementException


class CheckBox(Element):

    def __init__(self, element, name=None):
        super(CheckBox, self).__init__(element, type='Чекбокс', name=name)

    def select(self):
        if not self.is_selected():
            self._element.click()

    def deselect(self):
        if self.is_selected():
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
            return self.label.text
        else:
            return None