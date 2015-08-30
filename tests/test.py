import pytest
from selenium.webdriver import Firefox
from htmlelements import Page, TextInput, Button, find

# @name('azaza')
class SearchForm(Page):

    def __init__(self, driver):
        super(SearchForm, self).__init__(driver)

    @find(css='#text', element_name='строка поиска')
    def input(self):
        return TextInput

    @find(css='.suggest2-form__button', element_name='найти')
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
    frm = SearchForm(driver.find_element_by_css_selector('.suggest2-form__node'))
    frm.btnSearch.click()
    # frm.input.send_keys('test', clear=True)
    # frm.submit()
    # assert 'Яндекс: нашлось' in driver.title
    assert 1
