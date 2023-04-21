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
def makeLevelOrder(level):
    root=BT.add_root('A')
    print(root._element)
    h = level
    for i in range(1, h+1):
        makeCurrentLevel(root, i)

def makeCurrentLevel(root, level):
    if level == 1:
        return
    elif level > 1:
        makeCurrentLevel(BT.add_left(root,'B'), level-1)
        makeCurrentLevel(BT.add_right(root,'C'), level-1)

def preorderTraversal(root):
    res = []
    if root:
        res = preorderTraversal(root._left)
        res.append(root._label)
        res.append(root._quality)
        res = res + preorderTraversal(root._right)
    return res

BT=BinaryTree()

makeLevelOrder(3)

preorderTraversal(BT._root)