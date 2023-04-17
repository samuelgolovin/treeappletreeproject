class Node:
    def __init__(self, value, letter):
        self.value = value
        self.letter = letter
        self.left = None
        self.right = None

def insert(root, value, letter):
    if root is None:
        return Node(value, letter)
    else:
        if  value < root.value:
            root.left = insert(root.left, value, letter)
        else:
            root.right = insert(root.right, value, letter)
        return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.letter, end=" ")
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.letter, end=" ")
        inorder_traversal(root.left)
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        inorder_traversal(root.right)
        print(root.letter, end=" ")

# Example usage
# Create an empty binary tree
root = None

# Values to be inserted into the binary tree
values = "My last name is Golovin and I am a Computer Science student."

# Insert values into the binary tree using a for loop
for i in range(len(values)):
    root = insert(root, i, values[i])

# Perform inorder traversal to display the values in sorted order
print("This is the string being stored: ")
print(values)
print("\nInorder traversal of the binary tree:")
inorder_traversal(root)
print("\nPreorder traversal of the binary tree:")
preorder_traversal(root)
print("\nPostorder traversal of the binary tree:")
postorder_traversal(root)
