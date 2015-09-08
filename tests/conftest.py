import pytest
from selenium.webdriver import Firefox
import os
from htmlelements import Page, TextInput, Button, find, CheckBox, Radio, Link, Select, Element, Widget


class MainPage(Page):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    @find(css='#test_input', element_name='тестовое поле')
    def input(self):
        return TextInput

    @find(css='button.test_button', element_name='тестовая')
    def btn(self):
        return Button

    @find(css='button.test_disabled_button', element_name='disabled')
    def btn_disabled(self):
        return Button

    @find(id='ch', element_name='тестировочный')
    def checkbox(self):
        return CheckBox

    @find(css='#radio1', element_name='тестовый')
    def radio(self):
        return Radio

    @find(xpath='//*[@id="test_select"]', element_name='для теста')
    def select(self):
        return Select

    @find(css='a', element_name='для проверки')
    def link(self):
        return Link

    @find(css='.hidden_elem', element_name='hidden')
    def hidden(self):
        return Element

    @find(css='#test_id', element_name='Проверочный')
    def widget(self):
        return Widget

@pytest.fixture(scope='module')
def control(request):
    driver = Firefox()
    site = os.path.abspath(os.path.dirname(__file__))
    site = os.path.join(site, 'test.html')
    driver.get(site)
    request.instance.page = MainPage(driver)
    def fin():
        driver.quit()
    request.addfinalizer(fin)