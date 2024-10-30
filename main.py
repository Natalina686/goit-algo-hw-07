class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_rec(node.right, key)

    def find_max(self):
        return self._find_max_rec(self.root)

    def _find_max_rec(self, node):
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node.val

    def find_min(self):
        return self._find_min_rec(self.root)

    def _find_min_rec(self, node):
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node.val

    def sum_values(self):
        return self._sum_values_rec(self.root)

    def _sum_values_rec(self, node):
        if node is None:
            return 0
        return node.val + self._sum_values_rec(node.left) + self._sum_values_rec(node.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)

    print("Найбільше значення в дереві:", bst.find_max())  
    print("Найменше значення в дереві:", bst.find_min())  
    print("Сума всіх значень у дереві:", bst.sum_values()) 