class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class IntStack:
    def __init__(self):
        self.head = None

    def push(self, new_data):

        current = self.head
        if current is None:
            self.head = Node(new_data)
        else:
            while current.next:
                current = current.next
            current.next = Node(new_data)


    def insert_a_value(self, value):
        new_node = Node(value)
        if (self.head is None) or (self.head.data > value):
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and (current.next.data <= value):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display_queue(self):
        current = self.head
        if not current:
            return '[]'
        line = ''
        while current:
            line = f'{line}, {current.data}'
            current = current.next
        return f'[{line[2:]}]'


    def copy(self):
        new_stack = IntStack()

        if not self.head:
            return new_stack

        current = self.head
        while current:
            new_stack.push(current.data)
            current = current.next

        return new_stack


numbers = list(map(int, input(f'\nВведите через пробел набор чисел для списка: ').split()))
P1 = IntStack()
for i in numbers:
    P1.push(i)

P2 = P1.copy()
print(f'\nСписок P1: {P1.display_queue()}'
      f'\nПервый элемент: {P1.head}'
      f'\n\nСписок P2: {P2.display_queue()}'
      f'\nПервый элемент: {P2.head}')

m = int(input('\nВведите значение M: '))
P2.insert_a_value(m)
print(f'\nСписок P2 после изменений: {P2.display_queue()}'
      f'\nПервый элемент: {P2.head}')
