class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_key(self.root, key)

    def _insert_key(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self._insert_key(root.left, key)
        elif key > root.key:
            root.right = self._insert_key(root.right, key)

        return root

    def inorder(self):
        self._inorder_traverse(self.root)
        print()  # Add a newline after traversal

    def _inorder_traverse(self, root):
        if root:
            self._inorder_traverse(root.left)
            print(root.key, end=" ")
            self._inorder_traverse(root.right)

    def search_bst(self, root, key):
        if root is None or root.key == key:
            return root

        if root.key < key:
            return self.search_bst(root.right, key)

        return self.search_bst(root.left, key)


# Test the implementation
if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert(10)
    binary_search_tree.insert(90)
    binary_search_tree.insert(20)
    binary_search_tree.insert(80)
    binary_search_tree.insert(30)
    binary_search_tree.insert(70)
    binary_search_tree.insert(40)

    print("Inorder traversal of the given tree")
    binary_search_tree.inorder()

    print("Searching for 40 in the tree")
    search_result = binary_search_tree.search_bst(binary_search_tree.root, 40)
    if search_result:
        print(f"Found node with key {search_result.key}")
    else:
        print("Key not found in the tree.")