class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def add(self, new_data):
        new_node = Node(new_data)

        if self.last is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node

    def get_list(self):
        node = self.head
        line = ''
        while node is not None:
            line = f'{line}, {node.data}'
            node = node.next
        return f'[{line[2:]}]'

    def len_list(self):
        node = self.head
        result = 0
        while node is not None:
            result += 1
            node = node.next
        return result

    def duplicate_odd_values(self):
        current = self.head
        while current:
            if current.data % 2 == 1:
                new_node = Node(current.data)
                if current == self.last:
                    self.last = new_node
                    current.next = new_node
                    new_node.prev = current
                else:
                    new_node.next = current.next
                    new_node.prev = current
                    current.next = new_node
                    if new_node.next is not None:
                        new_node.next.prev = new_node
                current = current.next.next
            else:
                current = current.next

    def __iter__(self):
        self.current = self.head
        self.reverse = False
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration

        result = self.current.data

        if not self.reverse:
            if self.current.next is None:
                self.reverse = True
                self.current = self.last
            else:
                self.current = self.current.next
        else:
            if self.current.prev is None:
                self.reverse = False
                self.current = self.head
            else:
                self.current = self.current.prev

        return result


if __name__ == '__main__':

    numbers = list(map(int, input(f'\nВведите через пробел набор чисел для списка: ').split()))
    dll = DoublyLinkedList()
    for i in numbers:
        dll.add(i)

    print(f'\nСписок до преобразований: {dll.get_list()}\nСсылка на последний элемент списка: {dll.last}')

    dll.duplicate_odd_values()

    print(f'\nСписок после преобразований: {dll.get_list()}\nСсылка на последний элемент списка: {dll.last}')

    len_dll = dll.len_list()
    number_of_iterator_cycles = 3

    n = 0
    line = ''

    for element in dll:
        n += 1
        line = f'{line}{element}, '
        if n >= (len_dll * number_of_iterator_cycles):
            break

    print(f'\nИтератор: [{line[:-2]}]')
