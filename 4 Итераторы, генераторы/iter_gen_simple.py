class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.list_iter = iter(self.list_of_lists)
        self.list = []
        self.cursor = -1
        return self

    def __next__(self):

        self.cursor += 1
        if len(self.list) == self.cursor:
            self.list = None
            self.cursor = 0
            while not self.list:
                self.list = next(self.list_iter)
        return self.list[self.cursor]


def flat_generator(list_of_lists):
    for sub_list in list_of_lists:
        for elem in sub_list:
            yield elem


if __name__ == '__main__':

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    print('Простой список итератор')
    for item in FlatIterator(list_of_lists_1):
        print(item)
    print('---------------------------------------------')
    flat_list = [item for item in FlatIterator(list_of_lists_1)]
    print(flat_list)
    print('---------------------------------------------')

    print('Простой список генератор')
    for item in flat_generator(list_of_lists_1):
        print(item)
    print('---------------------------------------------')
    flat_list = [item for item in flat_generator(list_of_lists_1)]
    print(flat_list)
