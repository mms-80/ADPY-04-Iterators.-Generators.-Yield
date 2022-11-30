class FlatIteratornested:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_queue = []
        self.current_iterator = iter(self.multi_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
            except StopIteration:
                if not self.iterators_queue:
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                return self.current_element


def flat_generator_nested(multi_list):
    for elem in multi_list:
        if isinstance(elem, list):
            for sub_elem in flat_generator_nested(elem):
                yield sub_elem
        else:
            yield elem


if __name__ == '__main__':

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    print('Вложенный список итератор')

    for item in FlatIteratornested(list_of_lists_2):
        print(item)
    print('---------------------------------------------------')
    nested_list = [item for item in FlatIteratornested(list_of_lists_2)]
    print(nested_list)
    print('---------------------------------------------------')


    print('Вложенный список генераторр')

    for item in flat_generator_nested(list_of_lists_2):
        print(item)
    print('---------------------------------------------------')
    nested_list = [item for item in flat_generator_nested(list_of_lists_2)]
    print(nested_list)

