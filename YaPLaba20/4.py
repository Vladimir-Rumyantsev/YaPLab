class CustomIterator:
    def __init__(self, data):
        self.data = data
        self.even_indices = []
        self.odd_indices = []
        for i in range(len(data) - 1, -1, -1):
            if i % 2 == 1:
                self.even_indices.append(i)
            else:
                self.odd_indices.append(i)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.even_indices):
            result = self.data[self.even_indices[self.index]]
        elif self.index < len(self.data):
            result = self.data[self.odd_indices[self.index - len(self.even_indices)]]
        else:
            raise StopIteration

        self.index += 1
        return result


if __name__ == '__main__':

    nums = list(map(int, input('\nВведите через пробел последовательность чисел: ').split()))
    custom_iterator = CustomIterator(nums)
    line = ''

    for element in custom_iterator:
        line = f'{line}{element}, '

    print(f'\nРезультат: [{line[:-2]}]')
