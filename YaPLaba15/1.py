class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class IntStack:
    def __init__(self, aTop):
        self.top = aTop
        
    def Pop(self):
        if self.top is None:
            return None
        popped_value = self.top.data
        self.top = self.top.next
        return popped_value

    def Put(self):
        return self.top


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

int_stack = IntStack(node1)

for i in range(5):
    popped_value = int_stack.Pop()
    print(popped_value)

print(int_stack.Put())
