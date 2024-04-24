class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def postorder_traversal(root):
    if root is None:
        return

    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.val)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    postorder_traversal(root)
