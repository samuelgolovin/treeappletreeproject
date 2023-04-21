import Tree
import random
from array_queue import ArrayQueue
from array_stack import ArrayStack

class AppleTree:
    def __init__(self, startAppleNum):
        self.tree = Tree.BinaryTree()
        self.tree_test = Tree.BinaryTree()
        self.first_root = self.tree._root
        self.startapplenum = startAppleNum

class Worker:
    def __init__(self, name, gender, workertype):
        self.name = name
        self.gender = gender
        self.workertype = workertype

    def pickApple(self):
        for i in Tree.inorderTraversalApplePicker(appleTree1.tree._root):
            print(i)

class Basket:
    def __init__(self, capacity):
        self.capacity = capacity
        self.basket = ArrayStack()
        
appleTree1 = AppleTree(11)
worker1 = Worker("John", "M", "basket")

quality = ["A", "B", "C"]

print(appleTree1.tree._root)

for i in range(1, appleTree1.startapplenum):
    appleTree1.tree._root = appleTree1.tree.insert(appleTree1.tree._root, i, random.choices(quality, weights = [1,1,1]))
    if i == 1:
        appleTree1.first_root = appleTree1.tree._root

# print("\nInorder traversal of the binary tree:")
# temp = Tree.inorderTraversal(appleTree1.first_root)
# print(temp)

print(appleTree1.tree.__len__())
# print(appleTree1.tree._root._label)
# print(appleTree1.tree._root._right)
# print(appleTree1.tree._root._right._label)
# # print(appleTree1.tree._root._right._left)
# print(appleTree1.tree._root._right._right)
# # print(appleTree1.tree._root._left._left)
# print(appleTree1.tree._root._right._right._label)

for i in range(appleTree1.startapplenum,1,-1):
    # print("Original node:")
    # print(Tree.inorderTraversal(appleTree1.tree._root))
    appleTree1.tree._root, appleTree1.tree_test._root = Tree.delete_Node(appleTree1.tree._root, i)
    if appleTree1.tree._root:
        print("old node")
        print(appleTree1.tree._root._label)
    # if deleted_node:
    #     print("deleted node")
    #     print(deleted_node._label)
    print("After deleting specified node:")
    print(Tree.inorderTraversal(appleTree1.tree._root))