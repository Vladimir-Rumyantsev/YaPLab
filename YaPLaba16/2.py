class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None


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


    def make_it_cyclical(self):

        if self.head is None:
            return None

        self.last.next = self.head
        self.head.prev = self.last


numbers = list(map(int, input(f'\nВведите через пробел набор чисел для списка: ').split()))
dll = DoublyLinkedList()
for i in numbers:
    dll.push(i)
print(f'\nСписок до преобразований: {dll.get_list()}'
      f'\nСсылка на последний элемент списка: {dll.last}')
dll.make_it_cyclical()
print(f'\nСписок после преобразований: {dll.get_list()}'
      f'\nСсылка на последний элемент списка: {dll.last}')
