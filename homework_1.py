class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = iter(list_of_list)

    def __iter__(self):
        self.cursor = iter(next(self.list_of_list))
        return self

    def __next__(self):
        try:
            next_value = next(self.cursor)
        except StopIteration:
            try:
                self.cursor = iter(next(self.list_of_list))
                next_value = next(self.cursor)
            except StopIteration:
                raise StopIteration
        return next_value


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
