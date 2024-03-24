class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class IntList:
    def __init__(self):
        self.head = None
        self.last = None
        self.current = None


    def push(self, new_data):

        new_node = Node(new_data)

        if self.last is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node


    def get_list(self):

        if self.head is None:
            return None

        node = self.head
        start = node
        line = ''

        while node is not None:
            line = f'{line}, {node.data}'
            node = node.next
            if node == start:
                return f'<Cycle> —> [{line[2:]}]'

        return f'[{line[2:]}]'


    def Insert(self, L2):

        if L2.head is None:
            L2 = self
            self.head = None
            self.last = None
            self.current = None
            return L2

        if self.head is None:
            return L2

        if L2.head is L2.current:
            L2.head = self.head
            self.last.next = L2.current
        else:
            L2.current.prev.next = self.head
            self.head.prev = L2.current.prev
            self.last.next = L2.current

        L2.current.prev = self.last
        L2.current = self.head
        self.head = None
        self.last = None
        self.current = None
        return L2


numbers_1 = list(map(int, input(f'\nВведите через пробел набор чисел для списка номер 1: ').split()))
numbers_2 = list(map(int, input(f'\nВведите через пробел набор чисел для списка номер 2: ').split()))
index = int(input('Введите номер элемента, с которым работаем в списке номер 2 (считать от 1): ')) - 1

if index >= len(numbers_2):
    print('Вы ввели слишком большой номер элемента для работы')

else:
    dll_1 = IntList()
    dll_2 = IntList()

    for i in numbers_1:
        dll_1.push(i)

    for i in numbers_2:
        dll_2.push(i)

    print(f'\nСписок 1 до преобразований: {dll_1.get_list()}'
          f'\nСписок 2 до преобразований: {dll_2.get_list()}')

    current = dll_2.head
    for i in range(index):
        current = current.next
    dll_2.current = current

    dll_2 = dll_1.Insert(dll_2)

    print(f'\nСписок 1 после преобразований: {dll_1.get_list()}'
          f'\nСписок 2 после преобразований: {dll_2.get_list()}'
          f'\n\nНачало второго списка: {dll_2.head.data}'
          f'\nСсылка на начало: {dll_2.head}'
          f'\n\nКонец второго списка: {dll_2.last.data}'
          f'\nСсылка на конец: {dll_2.last}'
          f'\n\nУказатель второго списка: {dll_2.current.data}'
          f'\nСсылка на указатель: {dll_2.current}')
