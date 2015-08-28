from htmlelements.elements.element import Element


class Button(Element):

    def __init__(self, element):
        super(Button, self).__init__(element, type='Кнопка')

    def click(self):
        self._element.click()

    
