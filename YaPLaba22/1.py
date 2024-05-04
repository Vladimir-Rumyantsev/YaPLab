class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=" ")


def insert(node, key):
    if node is None:
        return Node(key)
    if key < node.val:
        node.left = insert(node.left, key)
    elif key > node.val:
        node.right = insert(node.right, key)
    return node


def read(file):
    with open(file, 'r') as f:
        arr = list(map(int, f.read().split()))
    return arr


if __name__ == '__main__':

    #        5
    #     /     \
    #    2       8
    #   / \     /  \
    #  1   3   6    9
    #       \   \
    #        4   7

    root = None

    for i in read('TreeWork57_input'):
        root = insert(root, i)

    print(f'\nЗначение корня дерева: {root.val}\nКонцевой обход: ', end='')
    postorder(root)
    print()
