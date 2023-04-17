class BinaryTree:
    class _Node:
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
            
    def __init__(self):
        self._root = None          # member variable of BT (Binary Tree), not node
        self._size = 0
    
    def is_empty(self):
        return self._size == 0
    
    def add_root(self, e):
        self._size += 1
        t = self._root = self._Node(e)
        return t
        
    def add_left(self, p, e):
        self._size += 1
        t = p._left = self._Node(e, p)         # t is current node and p is parent node
        return t
       
    def add_right(self, p, e):
        self._size +=1
        t = p._right = self._Node(e, p)
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
    
    def insert(root, value, letter):
    if root is None:
        return Node(value, letter)
    else:
        if  value < root.value:
            root.left = insert(root.left, value, letter)
        else:
            root.right = insert(root.right, value, letter)
        return root

def inorderTraversal(root):
    res = []
    if root:
        res = inorderTraversal(root._left)
        res.append(root._element)
        res = res + inorderTraversal(root._right)
    return res

def preorderTraversal(root):
    res = []
    if root:
        res.append(root._element)
        res = res + preorderTraversal(root._left)
        res = res + preorderTraversal(root._right)
    return res

def postorderTraversal(root):
    res = []
    if root:
        res = preorderTraversal(root._left)
        res = res + preorderTraversal(root._right)
        res.append(root._element)
    return res