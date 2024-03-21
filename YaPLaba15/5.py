class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class IntStack:
    def __init__(self):
        self.head = None

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
        line = ''
        while current:
            line = f'{line} {current.data}'
            current = current.next
        if self.head:
            return line, self.head.data
        return None, None


numbers = list(map(int, input(f'\nВведите через пробел набор чисел для списка: ').split()))
P1 = IntStack()
x = None
if len(numbers) >= 1:
    for i in range(len(numbers) - 1, -1, -1):
        y = x
        x = Node(numbers[i])
        x.next = y
P1.head = x
P2 = P1

line, first = P2.display_queue()
print(f'\nКопия списка сейчас:\n{line}')
print(f'\nПервый элемент копии списка сейчас: {first}')
m = int(input('\nВведите значение M: '))
P2.insert_a_value(m)
line, first = P2.display_queue()
print(f'\nКопия списка после изменений:\n{line}')
print(f'\nПервый элемент копии списка после изменений: {first}')
