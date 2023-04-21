import random
from linked_queue import Queue
from array_stack import ArrayStack

class TreeNode:
    def __init__(self, label):
        self.element = "apple"
        self.label = label
        self.quality = random.choices(["A", "B", "C"], weights = [1,1,1])
        self.left_child = None
        self.right_child = None

class AppleTree:
    def __init__(self, name):
        self.root = None
        self.name = name

    def is_empty(self):
        return self.root == None

    def create_apple_tree(self, num_apples):
        if num_apples <= 0:
            return
        
        self.root = TreeNode(1)
        queue = [self.root]
        self.apple_count = 1

        while self.apple_count < num_apples:
            parent_node = queue.pop(0)
            left_child = TreeNode(self.apple_count + 1)
            parent_node.left_child = left_child
            self.apple_count += 1

            if self.apple_count < num_apples:
                right_child = TreeNode(self.apple_count + 1)
                parent_node.right_child = right_child
                self.apple_count += 1

            queue.append(left_child)
            queue.append(right_child)

        print(f"\t\tCreated a tree with '{self.apple_count}' apples.\n")

    def traverse_apple_tree_bfs(self):
        if self.root is None:
            print("Apple tree is empty.")
            return
        res = []
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            # print(current_node.label)
            res.append((current_node.label, current_node.quality[0]))

            if current_node.left_child is not None:
                queue.append(current_node.left_child)

            if current_node.right_child is not None:
                queue.append(current_node.right_child)
        return res

    def pick_apple(self, current_tree_being_picked):
        if self.root is None:
            print("Apple tree is empty.")
            return
        if current_tree_being_picked.apple_count == 1:
            self.apple_count -= 1
            # print(f"Apple '{current_tree_being_picked.apple_count}' picked from the left of '{current_tree_being_picked.root.label}'.")
            temp_node = current_tree_being_picked.root
            current_tree_being_picked.root = None
            return temp_node
        else:
            queue = [self.root]
            while queue:
                current_node = queue.pop(0)
                if current_node.left_child is not None and current_node.left_child.label == current_tree_being_picked.apple_count:
                    temp_node = current_node.left_child
                    current_node.left_child = None
                    # print(f"Apple '{current_tree_being_picked.apple_count}' picked from the left of '{current_node.label}'.")
                    current_tree_being_picked.apple_count -= 1
                    return temp_node
                elif current_node.right_child is not None and current_node.right_child.label == current_tree_being_picked.apple_count:
                    temp_node = current_node.right_child
                    current_node.right_child = None
                    # print(f"Apple '{current_tree_being_picked.apple_count}' picked from the right of '{current_node.label}'.")
                    current_tree_being_picked.apple_count -= 1
                    return temp_node
                if current_node.left_child is not None:
                    queue.append(current_node.left_child)
                if current_node.right_child is not None:
                    queue.append(current_node.right_child)

        print(f"Could not find apple '{current_tree_being_picked.apple_count}' in the apple tree.")

class Worker():
    def __init__(self, name, gender, type):
        self.name = name
        self.gender = gender
        self.type = type
        print(f"\t\tWorker name: '{self.name}' gender: '{self.gender}' type: '{self.type}'\n")
        if self.type == "basket":
            if self.name == "John":
                self.basketORwagon = Basket(20)
            if self.name == "Grace":
                self.basketORwagon = Basket(10)
        else:
            self.basketORwagon = Wagon()
        

    def appleToBasket(self, current_tree):
        # pickedApple = current_tree.pick_apple(current_tree)
        self.basketORwagon.basketstack.push(current_tree.pick_apple(current_tree))
        # print(f"--->\t{self.name} put apple in basket from tree")
    
    def basketToWagon(self):
        for i in range(self.basketORwagon.basketstack.get_size()):
            worker3.basketORwagon.wagonstack.push(self.basketORwagon.basketstack.pop())
        print("---><---")
        print(f"-------->\t{self.name} put apples in wagon from basket")
        print("---><---")

    def wagonToStorage(self):
        # print(self.basketORwagon.wagonstack.top().quality[0])
        # quit()
        if self.basketORwagon.wagonstack.is_empty():
            return
        else:
            while not self.basketORwagon.wagonstack.is_empty():
                if self.basketORwagon.wagonstack.top() and self.basketORwagon.wagonstack.top().quality[0] == "A":
                    storageA.storagequeue.enqueue(self.basketORwagon.wagonstack.pop())
                if self.basketORwagon.wagonstack.top() and self.basketORwagon.wagonstack.top().quality[0] == "B":
                    storageB.storagequeue.enqueue(self.basketORwagon.wagonstack.pop())
                if self.basketORwagon.wagonstack.top() and self.basketORwagon.wagonstack.top().quality[0] == "C":
                    storageC.storagequeue.enqueue(self.basketORwagon.wagonstack.pop())
            print("---><---")
            print("---><---")
            print(f"-------->\t{self.name} put apples in storage from wagon")
            print("---><---")
            print("---><---")
     
class Basket():
    def __init__(self, capacity):
        self.capacity = capacity
        self.basketstack = ArrayStack()
        print(f"\t\t\tBasket Capacity is: '{self.capacity}'\n")

class Wagon():
    def __init__(self):
        self.capacity = 50
        self.wagonstack = ArrayStack()
        print(f"\t\t\tWagon Capacity is: '{self.capacity}'\n")

class Storage():
    def __init__(self):
        self.capacity = 500
        self.storagequeue = Queue()
        print(f"\t\tStorage Capacity is: '{self.capacity}'\n")

def printoutinfo():
    print("-----------------------------------------")
    print(f"\tApples in basket of worker1: {worker1.basketORwagon.basketstack.get_size()}")
    print(f"\tApples in basket of worker2: {worker2.basketORwagon.basketstack.get_size()}")
    print(f"\tApples in wagon of worker3: {worker3.basketORwagon.wagonstack.get_size()}")
    print(f"\tApples in storageA: {storageA.storagequeue.get_size()}")
    print(f"\tApples in storageB: {storageB.storagequeue.get_size()}")
    print(f"\tApples in storageC: {storageC.storagequeue.get_size()}")
    print(f"\tCurrent tree: {current_tree.name}")
    print(f"\tApples left in tree: {current_tree.apple_count}")
    print("-----------------------------------------")



print("<=============================================================================>")
tree1 = AppleTree("tree1")
tree1.create_apple_tree(300)
tree2 = AppleTree("tree2")
tree2.create_apple_tree(300)
tree3 = AppleTree("tree3")
tree3.create_apple_tree(300)
worker1 = Worker("John", "M", "basket")
worker2 = Worker("Grace", "F", "basket")
worker3 = Worker("Rachel", "F", "wagon")
storageA = Storage()
storageB = Storage()
storageC = Storage()
print("<=============================================================================>\n\n")



# print(tree1.traverse_apple_tree_bfs())
trees = [tree1, tree2, tree3]
current_tree_counter = 0
current_tree = trees[current_tree_counter]


for time in range(1, 5001, 1):
    if current_tree.apple_count <= 0 and current_tree_counter < len(trees) - 1:
        current_tree_counter += 1
        current_tree = trees[current_tree_counter]

    if time % 10 == 0:
        if not current_tree.is_empty():
            if time % 200 != 0:
                    worker1.appleToBasket(current_tree)
            else: 
                worker1.basketToWagon()
            if time % 100 != 0:
                    worker2.appleToBasket(current_tree)
            else: 
                worker2.basketToWagon()
    if time % 500 == 0:
        printoutinfo()
    if time % 100 == 0:
        worker3.wagonToStorage()

# empty all if anything is left
worker1.basketToWagon()
worker2.basketToWagon()
worker3.wagonToStorage()

printoutinfo()

print("<------------------------ All apples inside of storageA ------------------------>\n")
print(storageA.storagequeue.view_all())
print("<------------------------ All apples inside of storageB ------------------------>\n")
print(storageB.storagequeue.view_all())
print("<------------------------ All apples inside of storageC ------------------------>\n")
print(storageC.storagequeue.view_all())


