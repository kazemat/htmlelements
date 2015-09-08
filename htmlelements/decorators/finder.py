from selenium.webdriver.common.by import By
import inspect


def find(**kwargs):
    """

    :param kwargs:
        - css - CSS selector of the element
        - xpath - XPATH selector of the element
        - class_name - Name of class webelement for the selector
        - id - ID of webelement
        - name - Name of the webelement for the selector
        - element_name - Name of the webelement for the logging
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
            name = kwargs.get('element_name', None)
            logger = getattr(obj, 'logger', None)
            if kwargs.get('css'):
                by = By.CSS_SELECTOR
                selector = kwargs.get('css')
            elif kwargs.get('xpath'):
                by = By.XPATH
                selector = kwargs.get('xpath')
            elif kwargs.get('class_name'):
                by = By.CLASS_NAME
                selector = kwargs.get('class_name')
            elif kwargs.get('id'):
                by = By.ID
                selector = kwargs.get('id')
            elif kwargs.get('name'):
                by = By.NAME
                selector = kwargs.get('name')
            else:
                raise ValueError
            if hasattr(obj, 'find_element'):
                searcher = obj.find_element
            else:
                searcher = obj._element.find_element
            if inspect.isclass(self.fnc):
                return self.fnc(element=searcher(by=by, value=selector), name=name, logger=logger)
            elif inspect.isfunction(self.fnc):
                return self.fnc(obj)(element=searcher(by=by, value=selector), name=name, logger=logger)
    return new_find