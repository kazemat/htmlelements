from . import Element


class Widget(Element):

    def __init__(self, element):
         super(Widget, self).__init__(element, type='Виджет')