"""
Binary Search Tree Implementation
"""


class TreeNode:
    """BST Node"""

    def __init__(self, driver):
        self.driver = driver
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree for F1 Drivers"""

    def __init__(self):
        self.root = None

    def insert(self, driver):
        """Insert driver into BST by points"""
        if not self.root:
            self.root = TreeNode(driver)
        else:
            self._insert_recursive(self.root, driver)

    def _insert_recursive(self, node, driver):
        """Recursive insert helper"""
        if driver["points"] >= node.driver["points"]:
            if node.left is None:
                node.left = TreeNode(driver)
            else:
                self._insert_recursive(node.left, driver)
        else:
            if node.right is None:
                node.right = TreeNode(driver)
            else:
                self._insert_recursive(node.right, driver)

    def inorder_traversal(self):
        """Inorder: Left -> Root -> Right"""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.driver)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        """Preorder: Root -> Left -> Right"""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.driver)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """Postorder: Left -> Right -> Root"""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.driver)


def create_driver_bst(drivers):
    """Create BST from drivers list"""
    bst = BinarySearchTree()
    for driver in drivers:
        bst.insert(driver)
    return bst