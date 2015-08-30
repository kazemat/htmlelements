from htmlelements.elements.element import Element


class Link(Element):

    def __init__(self, element, name=None):
        super(Link, self).__init__(element, type='Ссылка', name=name)

    def get_text(self):
        return self.text

    def get_reference(self):
        return self.get_attribute("href")

    def click(self):
        self._element.click()