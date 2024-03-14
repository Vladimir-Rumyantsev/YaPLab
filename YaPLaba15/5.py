#4

class Node:
    def __init__(self, data):
        # Инициализирует узел с данными, следующим и предыдущим узлами
        self.data = data
        self.next = None
        self.prev = None

class SortedList:
    def __init__(self):
        # Создаёт узел-связку, который будет служить началом и концом списка
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def add(self, data):
        # Создаёт новый узел с данными, которые нужно добавить
        new_node = Node(data)

        # Находим правильную позицию для вставки нового узла
        current = self.sentinel
        while current.next != self.sentinel and current.next.data > data:
            current = current.next

        # Вставляет новый узел между текущим и следующим за ним узлами
        new_node.prev = current
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node

    def get_sorted_list(self):
        # Создаёт список для хранения отсортированных данных
        result = []

        # Перебирает узлы в нашем связном списке и добавляем данные в результирующий список
        current = self.sentinel.next
        while current != self.sentinel:
            result.append(current.data)
            current = current.next

        # Возвращает результирующий список в порядке возрастания
        return result[::1]

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        numbers = [int(x) for x in file.readline().strip().split()]

    return n, numbers

def main():
    file_path = "input.txt"  # Заменяет путь к входному файлу
    n, numbers = read_input_file(file_path)

    sorted_list = SortedList()
    for num in numbers:
        sorted_list.add(num)

    result = sorted_list.get_sorted_list()
    print(result)

if name == "__main__":
    main()