from htmlelements.elements.element import Element


class Table(Element):

    def __init__(self, element, name=None):
        super(Table, self).__init__(element, type='Таблица', name=name)

    def get_header(self):
        return self._element.find_elements_by_xpath(".//th")

    def get_header_elements_as_strings(self):
        header = self.get_header()
        return list(
            map(
                lambda x: x.text,
                header.find_elements_by_xpath(".//td")
            )
        )

    def get_rows(self, tag='tbody'):
        if tag == 'tbody':
            return self._element.find_elements_by_xpath(".//tbody//tr")
        else:
            return self._element.find_elements_by_xpath(".//tr")

    def get_columns(self, tag):
        rows = self.get_rows(tag)
        return list(map(lambda x: x.find_elements_by_xpath(".//td"), rows))

    def get_columns_text(self, tag):
        columns = self.get_columns(tag=tag)
        col_with_text = list()
        for row in columns:
            col_with_text.append(
                list(map(lambda x: x.text, row))
            )
        return col_with_text

    def get_row_by_index(self, index, tag=None):
        cols = self.get_columns_text(tag=tag)
        if index < 0 or index > len(cols) - 1:
            raise Exception()
        return cols[index]

    def table_to_dict(self):
        one = self.get_header_elements_as_strings()
        rows = self.get_rows()
        result = list()
        for row in rows:
            q = dict()
            for i in range(len(one)):
                q[one[i]] = row[i]
            result.append(q)
        return result

    def is_selected(self):
         return super(Table, self).is_selected()

    def is_displayed(self):
        return super(Table, self).is_displayed()

    def is_enabled(self):
        return super(Table, self).is_enabled()
