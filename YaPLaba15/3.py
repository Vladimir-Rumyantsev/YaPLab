class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def find_first_multiple_of_4(self):
        current = self.head
        while current:
            if current.data % 4 == 0:
                return current
            current = current.next


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(4)
fourth = Node(5)
fifth = Node(8)
sixth = Node(9)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

result = llist.find_first_multiple_of_4()
print(result.data)
