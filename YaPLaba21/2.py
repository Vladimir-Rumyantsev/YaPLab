class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def greatest_depth(root, level=-1):
    if root is None:
        return level

    a = greatest_depth(root.left, level + 1)
    b = greatest_depth(root.right, level + 1)
    if a > b:
        return a
    else:
        return b


if __name__ == '__main__':
    #
    #           1
    #         /   \
    #        2     3
    #       / \   / \
    #      4   5 6   7
    #

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print(f"\nНаибольшая глубина: {greatest_depth(root)}")
