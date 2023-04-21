class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Example usage
# Create an empty binary tree
root = None

# Values to be inserted into the binary tree
values = [5, 3, 7, 2, 4, 6, 8]

# Insert values into the binary tree using a for loop
for value in values:
    root = insert(root, value)

# Perform inorder traversal to display the values in sorted order
print("Inorder traversal of the binary tree:")
inorder_traversal(root)

print(root.left.value)
print(root.right.value)
print(root.left.left.value)
print(root.right.left.value)
print(root.left.right.value)
print(root.right.right.value)
