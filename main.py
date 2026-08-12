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
            
    def search(self, key):
        if self.data == key:
            return True
        elif key < self.data:
            if self.left is None:
                return False
            else:
                return self.left.search(key)   
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(key)
        
root = Tree(15)
root.insert(13)
root.insert(17)
root.insert(7)
root.insert(3)
root.insert(9)
root.insert(4)
print(f'The inorder traversal is: ')
root.inorder_traversal()
key = int(input('\nWhat value do you want to search? '))
print(root.search(key))