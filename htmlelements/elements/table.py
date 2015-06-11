from htmlelements.elements.element import Element


class Table(Element):

    def __init__(self, element):
        super(Table, self).__init__(element, type='Table')

    def get_header(self, tag):
        if tag == 'th':
            return self._element.find_elements_by_xpath(".//{0}".format(tag))
        elif tag == 'thead':
            return self._element.find_elements_by_xpath(".//{0}//td".format(tag))
        else:
            raise Exception("Incorrect table header tag!")

    def get_header_elements_as_strings(self, tag='thead'):
        header = self.get_header(tag=tag)
        return list(
            map(
                lambda x: x.text,
                header.find_elements_by_xpath(".//td")
            )
        )

    def get_rows(self, tag):
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



