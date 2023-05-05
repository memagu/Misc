class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"BinaryTree(val={self.val}, left={self.left}, right={self.right})"

    def insert(self, val) -> None:
        if val < self.val:
            if self.left is None:
                self.left = BinaryTree(val)
                return

            self.left.insert(val)
            return

        if self.right is None:
            self.right = BinaryTree(val)
            return

        self.right.insert(val)


bt = BinaryTree()

bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
bt.insert(-1)
bt.insert(-2)
bt.insert(-3)

print(bt)
