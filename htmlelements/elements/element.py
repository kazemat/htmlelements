from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from ..log import class_logger, IS_DISPLAYED, IS_ENABLED, IS_SELECTED


class Element(object):
    def __init__(self, element, type='Элемент', name=None, logger=None):
        """

        :param element - webelement:
        :param type - type of webelement:
        :param name - name of webelement:
        """
        # assert isinstance(element, WebElement)
        self._element = element
        self.__type = type
        self._name = name
        self.logger = logger or class_logger(self)

    def __str__(self):
        return '{0} "{1}"'.format(self.__type, self._name)

    def is_selected(self):
        """Returns whether the element is selected.

        Can be used to check if a checkbox or radio button is selected.
        """
        self.logger.info(IS_SELECTED.format(self))
        result = self._element.is_selected()
        self.logger.debug(result)
        return result

    def is_displayed(self):
        """Whether the element is visible to a user."""
        self.logger.info(IS_DISPLAYED.format(self))
        result = self._element.is_displayed()
        self.logger.debug(result)
        return result

    def is_enabled(self):
        """Returns whether the element is enabled."""
        self.logger.info(IS_ENABLED.format(self))
        result = self._element.is_enabled()
        self.logger.debug(result)
        return result

    def get_attribute(self, attr):
        """Gets the given attribute or property of the element.

        This method will first try to return the value of a property with the
        given name. If a property with that name doesn't exist, it returns the
        value of the attribute with the same name. If there's no attribute with
        that name, ``None`` is returned.

        Values which are considered truthy, that is equals "true" or "false",
        are returned as booleans.  All other non-``None`` values are returned
        as strings.  For attributes or properties which do not exist, ``None``
        is returned.

        :Args:
            - name - Name of the attribute/property to retrieve.

        Example::

            # Check if the "active" CSS class is applied to an element.
            is_active = "active" in target_element.get_attribute("class")

        """
        return self._element.get_attribute(attr)

    @property
    def text(self):
        """The text of the element."""
        return self._element.text
