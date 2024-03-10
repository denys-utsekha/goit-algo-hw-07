class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

root = None
keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14]
for key in keys:
  root = insert(root, key)

# Завдання 1
def max_value_node(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val
print(f"Найбільше значення - {max_value_node(root)}")

# Завдання 2
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.val
print(f"Найменше значення - {min_value_node(root)}")

# Завдання 3
def total_sum(node):
    if node is None:
        return 0
    return node.val + total_sum(node.left) + total_sum(node.right)
print(f"Сума всіх значень - {total_sum(root)}")
