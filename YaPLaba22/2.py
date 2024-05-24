class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def inoder(root):
    if root is not None:
        print("(", end="")
        inoder(root.left)
        print(root.val, end="")
        inoder(root.right)
        print(")", end="")


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)


def new_deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = new_deleteNode(root.left, key)
    elif key > root.val:
        root.right = new_deleteNode(root.right, key)
    else:
        if root.right is not None:
            root.val = root.right.val
            root.right = root.right.right
        else:
            root = root.left

    return root


def minValueNode(node):
    current = node
    while current and current.left is not None:
        current = current.left
    return current


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # узел концевой или с одним дочерним
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # узел с двумя дочерними:
        temp = minValueNode(root.right)
        root.val = temp.val
        root.right = deleteNode(root.right, temp.val)

    return root


if __name__ == '__main__':

    #        5
    #     /     \
    #    2       8
    #   / \     /  \
    #  1   3   6    9
    #       \   \
    #        4   7

    #        6
    #     /     \
    #    2       8
    #   / \     /  \
    #  1   3   7    9
    #       \   \
    #        4

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

    root = deleteNode(root, int(input('\n\nВведите значение удаляемой вершины: ')))

    print('\nДерево после удаления: ', end='')
    inoder(root)
    print()
