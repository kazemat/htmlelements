from selenium.webdriver.common.by import By


def find(**kwargs):
    class new_find(object):

        def __init__(self, fnc):
            self.fnc = fnc

        def __get__(self, obj, klass):
            if kwargs.get('css'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.CSS_SELECTOR, value=kwargs.get('css')))
            elif kwargs.get('xpath'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.XPATH, value=kwargs.get('xpath')))
            elif kwargs.get('class'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.CLASS_NAME, value=kwargs.get('class_name')))
            elif kwargs.get('id'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.ID, value=kwargs.get('id')))
            elif kwargs.get('name'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.NAME, value=kwargs.get('name')))
            else:
                raise ValueError
    return new_find;