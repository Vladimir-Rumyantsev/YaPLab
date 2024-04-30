class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inoder(root):
    if root is not None:
        print("(", end="")
        print(root.val, end="")
        inoder(root.left)
        inoder(root.right)
        print(")", end="")


def new_deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = new_deleteNode(root.left, key)
    elif key > root.val:
        root.right = new_deleteNode(root.right, key)
    else:
        root = root.right

    return root


if __name__ == '__main__':

    #        5
    #     /     \
    #    2       8
    #   / \     /  \
    #  1   3   6    9
    #       \   \
    #       4   7

    root = Node(5)
    root.left = Node(2)
    root.right = Node(8)

    root.left.left = Node(1)
    root.left.right = Node(3)
    root.left.right.right = Node(4)
    root.right.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right = Node(9)

    print('\nСостояние дерева сейчас: ', end='')
    inoder(root)

    root = new_deleteNode(root, int(input('\n\nВведите значение удаляемой вершины: ')))

    print('\nДерево после удаления: ', end='')
    inoder(root)
    print()
