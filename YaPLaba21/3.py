class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def max_and_min_length(node):
    if node is None:
        return 0, 0

    else:
        max_l, min_l = max_and_min_length(node.left)
        max_r, min_r = max_and_min_length(node.right)

        return max(max_l, max_r) + 1, min(min_l, min_r) + 1


def is_avl(root):
    a, b = max_and_min_length(root)
    if a > b + 1:
        return False
    return True


if __name__ == "__main__":
    #
    #           1
    #         /   \
    #        2     3
    #       / \   / \
    #      4   5 6   7
    #     /
    #    8
    #

    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    if is_avl(root):
        print('\nДерево сбалансированно!')
    else:
        print('\nДерево НЕ сбалансированно!')

    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)

    if is_avl(root):
        print('\nДерево сбалансированно!')
    else:
        print('\nДерево НЕ сбалансированно!')
