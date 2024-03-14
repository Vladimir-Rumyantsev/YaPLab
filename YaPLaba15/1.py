# Ещё не готово


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class IntStack:
#     def __init__(self, aTop):
#         self.top = aTop

#     def Push(self, D):
#         new_node = Node(D)
#         new_node.next = self.top
#         self.top = new_node

#     def Pop(self):
#         if self.top is None:
#             return None
#         popped_value = self.top.data
#         self.top = self.top.next
#         return popped_value

#     def Put(self):
#         return self.top


# node5 = Node(5)
# node4 = Node(4)
# node3 = Node(3)
# node2 = Node(2)
# node1 = Node(1)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# int_stack = IntStack(node1)

# for i in range(5):
#     popped_value = int_stack.Pop()
#     print(popped_value)

# print(int_stack.Put())



# # #4
# #
# # import gc
# #
# # class Node:
# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# #
# #     def dispose(self):
# #         del self.data
# #         del self.next
# #
# # class Stack:
# #     def __init__(self):
# #         self.top = None
# #
# #     def push(self, data):
# #         new_node = Node(data)
# #         new_node.next = self.top
# #         self.top = new_node
# #
# #     def pop(self):
# #         if self.top is None:
# #             return None
# #         popped_node = self.top
# #         self.top = self.top.next
# #         popped_node.next = None
# #         return popped_node.data
# #
# #     def dispose(self):
# #         while self.top is not None:
# #             popped_node = self.top
# #             self.top = self.top.next
# #             popped_node.dispose()
# #
# # stack = Stack()
# #
# # while True:
# #     n = int(input("Введите количество элементов, которые нужно поместить в стек(количество элеменов должно быть больше 9): " ))
# #     if n > 9:
# #         break
# #     else:
# #         print("Ошибка: количество элеменов должно быть больше 9. Повторите попытку.")
# #
# #
# # for i in range(n):
# #     data = input("Введите данные для элемента {}: ".format(i+1))
# #     stack.push(data)
# #
# # for i in range(9):
# #     print("Удалённое значение: ", stack.pop())
# #
# # print("Новая вершина стека: ", stack.top.data if stack.top is not None else None)
# # print("Новая вершина стека ссылка: ", stack.top if stack.top is not None else None)
# # gc.collect()
# # print("Сборщик мусора: собран", gc.collect())
