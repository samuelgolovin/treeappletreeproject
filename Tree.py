class BinaryTree:
    class _Node:
        def __init__(self, label, quality, parent=None, left=None, right=None):
            self._label = label
            self._parent = parent
            self._quality = quality
            self._left = left
            self._right = right
            
    def __init__(self):
        self._root = None          # member variable of BT (Binary Tree), not node
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def add_root(self, l, q):
        self._size += 1
        t = self._root = self._Node(l, q)
        return t
        
    def add_left(self, p, l, q):
        self._size += 1
        t = p._left = self._Node(l, q, p)         # t is current node and p is parent node
        return t
       
    def add_right(self, p, l, q):
        self._size +=1
        t = p._right = self._Node(l, q, p)
        return t
    
    def __len__(self):
        return self._size
    
    def num_children(self, p):
        count = 0
        if p._left is not None:
            count += 1
        if p._right is not None:
            count += 1
        return count
    
    def sibling(self, p):
        if p == p._parent._left:
            if p._parent._right is not None:
                t = p._parent._right
        if p == p._parent._right:
            if p._parent._left is not None:
                t = p._parent._left
        return t
    
    def insert(self, p, l, q):
        if p is None:
            return self._Node(l, q, p)
        else:
            if  l < p._label:
                p._left = self.insert(p._left, l, q)
            else:
                p._right = self.insert(p._right, l, q)
            return p
        
    def insert1(self, p, l, q):
        if not p:
            print("\nmade a root")
            return self.add_root(l, q)
        elif p._left == None:
            print("\nmade a left")
            self.add_left(p, l, q)
            return p
        elif p._right == None:
            print("\nmade a right")
            self.add_right(p, l, q)
            return p
        else:
            if p._left._left == None:
                print("\nchanging to left child")
                self.insert1(p._left, l, q)
            elif p._left._right == None:
                print("\nchanging to left child")
                self.insert1(p._left, l, q)
            elif p._right._left == None:
                print("\nchanging to right child")
                self.insert1(p._right, l, q)
            elif p._right._right == None:
                print("\nchanging to right child")
                self.insert1(p._right, l, q)

 

def inorderTraversalApplePicker(root):
    res = []
    if root:
        latest_root = inorderTraversalApplePicker(root._left)
        res.append(root._label)
        res.append(root._quality)
        latest_root = inorderTraversalApplePicker(root._right)
    return res, latest_root

def return_deleted_node()

def delete_Node(root, key):
    # if root doesn't exist, just return it
    if not root: 
        print("root because not existed")
        return root
    # Find the node in the left subtree	if key value is less than root value
    if root._left and root._label > key: 
        root._left = delete_Node(root._left, key)
    # Find the node in right subtree if key value is greater than root value, 
    elif root._right and root._label < key: 
        root._right= delete_Node(root._right, key)
    # Delete the node if root.value == key
    else: 
    # If there is no right children delete the node and new root would be root.left
        if not root._right:
            print("root._right")
            return root._left
    # If there is no left children delete the node and new root would be root.right	
        if not root._left:
            print("root._left")
            return root._right
    # If both left and right children exist in the node replace its value with 
    # the minmimum value in the right subtree. Now delete that minimum node
    # in the right subtree
        temp_val = root._right
        
        mini_lab, mini_qua = temp_val._label, temp_val._quality

        while temp_val._left:
            temp_val = temp_val._left
            mini_lab, mini_qua = temp_val._label, temp_val._quality

    # Delete the minimum node in right subtree
        root._right = delete_Node(root._right,root._label)
    return root