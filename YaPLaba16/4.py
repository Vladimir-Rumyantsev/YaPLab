class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class IntListB:
    def __init__(self):
        self.head = None
        self.last = None
        self.barrier = None
        self.current = None


    def add(self, new_data=None, get_barrier=False, get_current=False):

        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            self.last = new_node
            self.current = new_node
        else:
            self.last.next = new_node
            new_node.prev = self.last
            self.last = new_node
            if get_current:
                self.current = new_node

        if get_barrier:
            self.barrier = new_node


    def get_list(self):

        node = self.head
        line = ''

        while node is not None:
            line = f'{line}, {node.data}'
            node = node.next
            if node == self.head:
                return f'<Cycle> —> [{line[2:]}]'

        return f'[{line[2:]}]'


    def toLast(self):
        self.current = self.last


    def toPrev(self):
        if self.current is not self.head:
            self.current = self.current.prev


    def getData(self):
        return self.current.data


    def isBarrier(self):
        return self.current is self.barrier


    def getBarrier(self, current=None):
        if current is None:
            current = self.current
        self.barrier = current


    def print_even_numbers(self):

        line = ''
        current = self.last

        while current is not self.barrier:
            if current.data % 2 == 0:
                line = f'{line}, {current.data}'
            current = current.prev

        return f'[{line[2:]}]'


numbers = list(map(int, input(f'\nВведите через пробел набор чисел для списка: ').split()))
bar = int(input('Введите номер элемента, который будет барьерным (считать от 1): ')) - 1
# cur = int(input('Введите номер текущего элемента (считать от 1): ')) - 1

dll = IntListB()
for i in range(len(numbers)):
    if i == bar:
        dll.add(numbers[i], True)
    # elif i == cur:
    #     dll.add(numbers[i], False, True)
    else:
        dll.add(numbers[i])

print(f'\nВсе чётные от конца до барьера: {dll.print_even_numbers()}')
