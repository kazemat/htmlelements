from htmlelements.elements.element import Element
from selenium.webdriver.support import select


class Select(Element):

    def __init__(self, element, name=None, logger=None):
        super(Select, self).__init__(element, type='Селект', name=name, logger=logger)

    def get_select(self):
        return select.Select(self._element)

    def is_multiple(self):
        return self.get_select().is_multiple()

    def get_options(self):
        return self.get_select().options

    def get_all_selected_options(self):
        return self.get_select().all_selected_options

    def get_first_selected_option(self):
        return self.get_select().first_selected_option

    def has_selected_options(self):
        for item in self.get_options():
            if item.selected():
                return True
        return False

    def select_by_visible_text(self, text):
        self.get_select().select_by_visible_text(text=text)

    def select_by_index(self, index):
        self.get_select().select_by_index(index=index)

    def select_by_value(self, value):
        self.get_select().select_by_value(value=value)

    def deselect_all(self):
        self.get_select().deselect_all()

    def deselect_by_visible_text(self, text):
        self.get_select().deselect_by_visible_text(text=text)

    def deselect_by_index(self, index):
        self.get_select().deselect_by_index(index=index)

    def deselect_by_value(self, value):
        self.get_select().deselect_by_value(value=value)

    def is_selected(self):
         return super(Select, self).is_selected()

    def is_displayed(self):
        return super(Select, self).is_displayed()

    def is_enabled(self):
        return super(Select, self).is_enabled()