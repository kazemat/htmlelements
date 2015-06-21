from selenium.webdriver.common.by import By


def find(**kwargs):
    """

    :param kwargs:
        - css - CSS selector of the element
        - xpath - XPATH selector of the element
        - class_name - Name of class webelement for the selector
        - id - ID of webelement
        - name - Name of the webelement for the selector
    :return: :raise ValueError:
    """

    class new_find(object):

        def __init__(self, fnc):
            """

            :param fnc:
                fnc - class element to be found
            """
            self.fnc = fnc

        def __get__(self, obj, klass):
            if kwargs.get('css'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.CSS_SELECTOR, value=kwargs.get('css')))
            elif kwargs.get('xpath'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.XPATH, value=kwargs.get('xpath')))
            elif kwargs.get('class_name'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.CLASS_NAME, value=kwargs.get('class_name')))
            elif kwargs.get('id'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.ID, value=kwargs.get('id')))
            elif kwargs.get('name'):
                return self.fnc(obj)(element=obj._element.find_element(by=By.NAME, value=kwargs.get('name')))
            else:
                raise ValueError

        def __setattr__(self, key, value):
            if key.lower() == 'name':
                self.fnc.name = value
            else:
                setattr(self, key, value)
    return new_find