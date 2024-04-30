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


def add_a_leaf_to_the_leaves(root):
    if root.left is not None:
        add_a_leaf_to_the_leaves(root.left)

    if root.right is not None:
        add_a_leaf_to_the_leaves(root.right)

    else:
        if root.val % 2 == 1:
            root.left = Node(root.val)
        else:
            root.right = Node(root.val)
        return


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

    add_a_leaf_to_the_leaves(root)

    print('\nДерево после изменений: ', end='')
    inoder(root)
    print()
