class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def search(self, key):
        if key == self.key:
            return self
        elif key < self.key and self.left is not None:
            return self.left.search(key)
        elif key > self.key and self.right is not None:
            return self.right.search(key)
        else:
            return None


node5 = Node(5)
node22 = Node(22, left=Node(20))
tree = Node(
    9,
    Node(
        4,
        Node(3),
        Node(
            6,
            node5,
            Node(7),
        ),
    ),
    Node(
        17,
        right=node22,
    ),
)

result1 = tree.search(6)
print(result1.key)  # Output: 6
print(result1.left.key)  # Output: 5
print(result1.right.key)  # Output: 7

result2 = tree.search(5)
print(result2 is node5)  # Output: True

result3 = tree.left.left
print(result3.key)  # Output: 3
