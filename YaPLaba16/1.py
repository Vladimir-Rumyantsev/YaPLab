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
        line = ''

        while node is not None:
            line = f'{line}, {node.data}'
            node = node.next

        return f'[{line[2:]}]'


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


numbers = list(map(int, input(f'\nВведите через пробел набор чисел для списка: ').split()))
dll = DoublyLinkedList()
for i in numbers:
    dll.push(i)
print(f'\nСписок до преобразований: {dll.get_list()}'
      f'\nСсылка на последний элемент списка: {dll.last}')
dll.duplicate_odd_values()
print(f'\nСписок после преобразований: {dll.get_list()}'
      f'\nСсылка на последний элемент списка: {dll.last}')
