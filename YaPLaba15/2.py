class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


numbers = list(map(int, input(f'\nВведите через пробел набор из 10 чисел: ').split()))
odd_queue = Queue()
even_queue = Queue()

for i in range(len(numbers)):
    if i % 2 == 1:
        even_queue.enqueue(numbers[i])
    else:
        odd_queue.enqueue(numbers[i])

print(f'\n(ссылка: odd_queue.head.data) Начало нечётной очереди: {odd_queue.head.data}'
      f'\n(ссылка: odd_queue.tail.data) Конец нечётной очереди: {odd_queue.tail.data}\n'
      f'\n(ссылка: even_queue.head.data) Начало чётной очереди: {even_queue.head.data}'
      f'\n(ссылка: even_queue.tail.data) Конец нечётной очереди: {even_queue.tail.data}')
