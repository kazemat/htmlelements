from htmlelements.elements.element import Element


class Link(Element):

    def __init__(self, element):
        super(Link, self).__init__(element, type='Link')

    def get_text(self):
        return self.text

    def get_reference(self):
        return self.get_attribute("href")

    def click(self):
        self._element.click()