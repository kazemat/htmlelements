from htmlelements.elements.element import Element


class Button(Element):

    def __init__(self, element, name=None):
        super(Button, self).__init__(element, type='Кнопка', name=name)

    def click(self):
        self._element.click()

    
