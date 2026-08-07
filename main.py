class Tree:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data, end = ' ')
        if self.right:
            self.right.inorder_traversal()

    def insert(self,key):
        if key < self.data:
            if self.left is None: 
                self.left = Tree(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = Tree(key)
            else:
                self.right.insert(key)
            