import pytest
from selenium.webdriver import Firefox
from htmlelements import HTMLElement, TextInput, Button
from htmlelements.decorators.finder import find


class SearchForm(HTMLElement):

    def __init__(self, driver):
        super(SearchForm, self).__init__(driver)

    @find(css='#text')
    def input(self):
        return TextInput

    @find(css='.suggest2-form__button')
    def btnSearch(self):
        return Button


@pytest.fixture
def control(request):
    driver = Firefox()
    driver.get('http://www.yandex.ru/')
    def fin():
        driver.quit()
    request.addfinalizer(fin)
    return driver


def test_one(control):
    driver = control
    frm = SearchForm(driver)
    frm.input.send_keys('test', clear=True)
    frm.btnSearch.click()
    assert 'Яндекс: нашлось' in driver.title
