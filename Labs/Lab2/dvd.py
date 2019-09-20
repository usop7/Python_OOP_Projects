from item import Item


class DVD(Item):
    def __init__(self, name, call_number, num_copies, release_date, region_code):
        super().__init__(name, call_number, num_copies)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        description = (f"[DVD] title: {self._title}, call number: {self._call_number}, issue number: {self._issue_number},"
                       f"publisher: {self._author}, number of copies: {self._num_copies}")
        return description
