import pytest
from selenium.common.exceptions import ElementNotSelectableException


@pytest.mark.usefixtures("control")
class TestButton():

    def test_click(self):
        self.page.btn.click()

    def test_button_text(self):
        assert self.page.btn.text == 'test button'

    def test_button_displayed(self):
        assert self.page.btn.is_displayed() is True

    def test_button_not_displayed(self):
        assert self.page.hidden.is_displayed() is False
        
    def test_disabled_button(self):
        assert self.page.btn_disabled.is_enabled() is False

    def test_enabled_button(self):
        assert self.page.btn.is_enabled() is True

    def test_unabled_click(self):
        try:
            self.page.btn_disabled.click()
        except ElementNotSelectableException:
            pass
        else:
            raise Exception('Disabled element to be clicked!')


