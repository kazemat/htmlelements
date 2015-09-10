Html Elements framework
=======================



This framework is Python implementation of good java framework [HtmlElements](https://github.com/yandex-qatools/htmlelements/) from Yandex.


#Short description
Main parent class for Web elements - Element.
Input parameters:
1) Web element - Required;
2) Item Type - optional;
3) Item Name - optional;
4) An instance of logger - optional;
Options 2-4 are required if you need logging operations. If it does not matter, you can leave as is. 


To search for items written decorator "find". It takes the input parameters and the function / class and interacts with the class, within which a challenge will be made.
The decorator takes a named parameters to search for an item and set his name. To search you must specify the type of selector. List the names of the parameters:

- css - CSS selector of the element
- xpath - XPATH selector of the element
- class_name - Name of class webelement for the selector
- id - ID of webelement
- name - Name of the webelement for the selector

The second parameter is optional - "element_name". Not to be confused with the "name"!


I'm not in vain mentioned that the decorator takes a function / class. He does not care which element comes.
But the function must return a class member is not initialized. As a result of the decorator, the function returns an initialized class. Do not call this.

If you use a class, not a function, it is sufficient to inherit from the desired class and use within the parent. Personally, I am impressed to use the classes, since then working autocompletion in my IDE 




#Example
For example, let's create a block for the search form on the page http://www.yandex.com:
```python
from htmlelements import Page, find, TextInput, Button


class MainPage(Page):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

    @find(css=".input__control.input__input", element_name="Search narrow")
    class SearchNarrow(TextInput):
        pass

    @find(xpath="//button[contains(@class, 'button_theme_websearch')]", element_name="search button")
    def search_button(self):
        return Button

    def search(self, text):
        self.SearchNarrow.send_keys(text, clear=True)
        self.search_button.click()

```

Enjoy)