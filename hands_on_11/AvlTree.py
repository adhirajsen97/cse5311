class AVLNode:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def max(self, a, b):
        return a if a > b else b

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = self.max(self.height(y.left), self.height(y.right)) + 1
        x.height = self.max(self.height(x.left), self.height(x.right)) + 1

        # Return the new root
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = self.max(self.height(x.left), self.height(x.right)) + 1
        y.height = self.max(self.height(y.left), self.height(y.right)) + 1

        # Return the new root
        return y

    def get_balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, node, data):
        if node is None:
            return AVLNode(data)

        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        else:  # Equal keys not allowed
            return node

        node.height = 1 + self.max(self.height(node.left), self.height(node.right))

        balance = self.get_balance(node)

        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete_node(self, root, data):
        if root is None:
            return root

        if data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)

            # Copy the inorder successor's data to this node
            root.data = temp.data

            # Delete the inorder successor
            root.right = self.delete_node(root.right, temp.data)

        if root is None:
            return root

        root.height = 1 + self.max(self.height(root.left), self.height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)


# Test the implementation
if __name__ == "__main__":
    tree = AVLTree()

    # Insert nodes
    tree.root = tree.insert(tree.root, 10)
    tree.root = tree.insert(tree.root, 90)
    tree.root = tree.insert(tree.root, 20)
    tree.root = tree.insert(tree.root, 80)
    tree.root = tree.insert(tree.root, 30)
    tree.root = tree.insert(tree.root, 70)
    tree.root = tree.insert(tree.root, 40)

    print("Inorder traversal of the constructed AVL tree is:")
    tree.inorder(tree.root)

    print("\n\nDelete 10")
    tree.root = tree.delete_node(tree.root, 10)
    print("Inorder traversal after deletion:")
    tree.inorder(tree.root)
    print()