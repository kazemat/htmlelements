from . import Element


class Widget(Element):

    def __init__(self, element, name=None):
         super(Widget, self).__init__(element, type='Виджет', name=name)

    def click(self):
        self._element.click()
