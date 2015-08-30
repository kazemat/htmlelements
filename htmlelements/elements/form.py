from htmlelements.elements import Element


class Form(Element):

    def __init__(self, element, name=None):
        super(Form, self).__init__(element, type='Форма', name=name)


