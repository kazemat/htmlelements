from htmlelements.elements.element import Element, NoSuchElementException


class Radio(Element):

    def __init__(self, element, name=None, logger=None):
        super(Radio, self).__init__(element, type='Радио-кнопка', name=name, logger=logger)

    def get_buttons(self):
        name = self.get_attribute("name")
        if name is not None:
            xpath = ".//self::* | following::input[@type = 'radio' and @name = '{0}'] | " \
                    "preceding::input[@type = 'radio' and @name = '{0}']".format(name)
        else:
            xpath = ".//self::* | following::input[@type = 'radio'] | preceding::input[@type = 'radio']"
        elems = list()
        for item in self._element.find_elements_by_xpath(xpath):
            elems.append(Radio(item, name=item.text))
        return elems


    def get_selected_button(self):
        for btn in self.get_buttons():
            if btn.is_selected():
                return Radio(btn)
        return None

    def has_selected_button(self):
        for i in self.get_buttons():
            if i.is_selected():
                return True
        return False

    def select_by_value(self, value):
        for btn in self.get_buttons():
            if btn.get_attribute("value") == value:
                btn.click()

    def select_by_index(self, index):
        btns = self.get_buttons()
        if index < 0 or index > len(btns) - 1:
            raise NoSuchElementException("Cannot locate radio button with index: {0}".format(index))
        else:
            btns[index].click()

    def is_selected(self):
         return super(Radio, self).is_selected()

    def is_displayed(self):
        return super(Radio, self).is_displayed()

    def is_enabled(self):
        return super(Radio, self).is_enabled()