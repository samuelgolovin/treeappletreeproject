import Tree
import random

class AppleTree:
    def __init__(self):
        self.tree = Tree.BinaryTree()
        
appleTree1 = AppleTree()

quality = ["A", "B", "C"]

for i in range(1, 300):
    appleTree1.tree._root = appleTree1.tree.insert(appleTree1.tree._root, i, random.choices(quality, weights = [1,1,1]))

print("\nInorder traversal of the binary tree:")
temp = Tree.inorderTraversal(appleTree1.tree._root)
print(temp)

print(appleTree1.tree.__len__())
print(appleTree1.tree.is_empty())