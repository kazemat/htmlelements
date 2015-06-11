from htmlelements.elements.element import Element, NoSuchElementException


class CheckBox(Element):

    def __init__(self, element):
        super(CheckBox, self).__init__(element, type='CheckBox')

    def select(self):
        if not self.is_selected():
            self._element.click()

    def deselect(self):
        if self.is_selected():
            self._element.click()

    def get_label(self):
        try:
            return self._element.find_element_by_xpath(".//following-sibling::label")
        except NoSuchElementException:
            return None

    def get_label_text(self):
        label = self.get_label()
        if label is not None:
            return label.text
        else:
            return None