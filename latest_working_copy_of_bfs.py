




import random
from array_queue import ArrayQueue
from array_stack import ArrayStack

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class AppleTree:
    def __init__(self):
        self.root = None

    def create_apple_tree(self, num_apples):
        if num_apples <= 0:
            return

        self.root = TreeNode("Apple 1")
        queue = [self.root]
        apple_count = 1

        while apple_count < num_apples:
            parent_node = queue.pop(0)
            left_child = TreeNode(f"Apple {apple_count + 1}")
            parent_node.left_child = left_child
            apple_count += 1

            if apple_count < num_apples:
                right_child = TreeNode(f"Apple {apple_count + 1}")
                parent_node.right_child = right_child
                apple_count += 1

            queue.append(left_child)
            queue.append(right_child)

    def traverse_apple_tree_bfs(self):
        if self.root is None:
            print("Apple tree is empty.")
            return

        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            print(current_node.data)

            if current_node.left_child is not None:
                queue.append(current_node.left_child)

            if current_node.right_child is not None:
                queue.append(current_node.right_child)


    def pick_apple(self, apple_label):
        if self.root is None:
            print("Apple tree is empty.")
            return

        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            print(current_node.left_child.data, apple_label)
            if current_node.left_child is not None and current_node.left_child.data == apple_label:
                temp_node = current_node.left_child
                current_node.left_child = None
                print(f"Apple '{apple_label}' picked from the left of '{current_node.data}'.")
                return temp_node
            elif current_node.right_child is not None and current_node.right_child.data == apple_label:
                temp_node = current_node.right_child
                current_node.right_child = None
                print(f"Apple '{apple_label}' picked from the right of '{current_node.data}'.")
                return temp_node
            if current_node.left_child is not None:
                queue.append(current_node.left_child)
            if current_node.right_child is not None:
                queue.append(current_node.right_child)

        print(f"Could not find apple '{apple_label}' in the apple tree.")

class Worker():
    def __init__(self, name, gender, type):
        self.name = name
        self.gender = gender
        self.type = type
        if self.type == "basket": 
            self.basketORwagon = Basket()
        else:
            self.basketORwagon = Wagon()

    def appleToBasket(self, apple_label):

        if apple_label == 1:
            temp_node = tree1.root
            tree1.root = None
            return temp_node.data
        else:
            return tree1.pick_apple(f"Apple {apple_label}")
     
class Basket():
    def __init__(self):
        self.capacity = 5
        self.basketstack = ArrayStack()

class Wagon():
    def __init__(self):
        self.capacity = 50
        self.wagonstack = ArrayStack()

class Storage():
    def __init__(self):
        self.capacity = 500
        self.storagequeue = ArrayQueue()




tree1 = AppleTree()
tree2 = AppleTree()
tree3 = AppleTree()
worker1 = Worker("John", "M", "basket")
worker2 = Worker("Grace", "F", "basket")
worker3 = Worker("Rachel", "F", "wagon")

tree1.create_apple_tree(10)

tree1.traverse_apple_tree_bfs()


worker1.appleToBasket(5)
worker1.appleToBasket(6)

tree1.traverse_apple_tree_bfs()


