class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class IntStack:
    def __init__(self):
        self.head = None

    def insert_a_value(self, value):
        current = self.head
        i = 0
        while current:
            i += 1
            if i % 3 == 0:
                x = Node(value)
                x.next = current.next
                current.next = x
                current = current.next
            current = current.next

    def display_queue(self):
        current = self.head
        last = None
        while current:
            last = current.data
            print(last)
            current = current.next
        return last


numbers = list(map(int, input(f'\nВведите через пробел набор чисел для списка: ').split()))
llist = IntStack()
x = None
if len(numbers) >= 1:
    for i in range(len(numbers) - 1, -1, -1):
        y = x
        x = Node(numbers[i])
        x.next = y
llist.head = x

print('\nЛист сейчас:')
last = llist.display_queue()
print(f'\nПоследний элемент списка сейчас: {last}')
m = int(input('\nВведите значение M: '))
llist.insert_a_value(m)
print('\nЛист после изменений:')
last = llist.display_queue()
print(f'\nПоследний элемент списка после изменений: {last}')
