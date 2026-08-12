class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def sum_tree(root):
    if root is None:
        return 0
    else:
        return root.value + sum_tree(root.left) + sum_tree(root.right)

root = TreeNode(6)
root.left = TreeNode(9)
root.right = TreeNode(7)

total_sum = sum_tree(root)
print(f"Total Sum: {total_sum}")