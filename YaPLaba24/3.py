import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def height(node):
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))


def rotate_right(node):
    key = node.key
    node.key = node.left.key
    node.left.key = key

    key = node.right
    node.right = node.left
    node.left = node.left.left

    node.right.left = node.right.right
    node.right.right = key

    return node


def rotate_left(node):
    key = node.key
    node.key = node.right.key
    node.right.key = key

    key = node.left
    node.left = node.right
    node.right = node.right.right

    node.left.right = node.left.left
    node.left.left = key

    return node


def rebalance(node):
    balance = height(node.right) - height(node.left)
    if balance <= -2:
        node.left = rebalance(node.left)
        node = rotate_right(node)
    elif balance >= 2:
        node.right = rebalance(node.right)
        node = rotate_left(node)
    return node


def insert(node, key):
    if node is None:
        node = Node(key)
    elif key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node


def inorder(root):
    if root is not None:

        print(root.key, end=" ")
        G.add_node(root.key)
        if root.left != None:
            G.add_edge(root.key, root.left.key)
        if root.right != None:
            G.add_edge(root.key, root.right.key)
        inorder(root.left)
        inorder(root.right)


if __name__ == '__main__':
    with open('3.txt', 'r', encoding='utf-8') as f:
        arr = f.read().split()

    root = None
    for i in arr:
        root = insert(root, i)

    rebalance(root)

    G = nx.Graph()
    inorder(root)
    print(G)

    nx.draw(G, with_labels = True)
    plt.savefig("filename.png")

    print(f'\nКорень: {root}\nЗначение: {root.key}')