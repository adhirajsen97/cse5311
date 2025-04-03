class RBNode:
    def __init__(self, data):
        self.data = data
        self.color = 1  # 1 for RED, 0 for BLACK
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.TNULL = RBNode(0)
        self.TNULL.color = 0  # BLACK
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # Preorder traversal
    def _pre_order_helper(self, node):
        if node != self.TNULL:
            print(node.data, end=" ")
            self._pre_order_helper(node.left)
            self._pre_order_helper(node.right)

    # Inorder traversal
    def _in_order_helper(self, node):
        if node != self.TNULL:
            self._in_order_helper(node.left)
            print(node.data, end=" ")
            self._in_order_helper(node.right)

    # Post order traversal
    def _post_order_helper(self, node):
        if node != self.TNULL:
            self._post_order_helper(node.left)
            self._post_order_helper(node.right)
            print(node.data, end=" ")

    # Search the tree
    def _search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.data:
            return node

        if key < node.data:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)

    # Balance the tree after deletion
    def _fix_delete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self._right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self._right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.left.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self._left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def _rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Delete the node with the given key
    def _delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self._fix_delete(x)

    # Rotate left at node x
    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # Rotate right at node x
    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    # Find the node with the minimum key
    def _minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    # Print the tree structure
    def print_tree(self):
        self._print_helper(self.root, "", True)

    def _print_helper(self, root, indent, last):
        if root != self.TNULL:
            print(indent, end="")
            if last:
                print("R----", end="")
                indent += "     "
            else:
                print("L----", end="")
                indent += "|    "

            s_color = "RED" if root.color == 1 else "BLACK"
            print(f"{root.data}({s_color})")
            self._print_helper(root.left, indent, False)
            self._print_helper(root.right, indent, True)

    # Preorder traversal
    def preorder(self):
        self._pre_order_helper(self.root)
        print()  # Add a newline

    # Inorder traversal
    def inorder(self):
        self._in_order_helper(self.root)
        print()  # Add a newline

    # Postorder traversal
    def postorder(self):
        self._post_order_helper(self.root)
        print()  # Add a newline

    # Search the tree
    def search_tree(self, k):
        return self._search_tree_helper(self.root, k)

    # Delete a node
    def delete_node(self, key):
        self._delete_node_helper(self.root, key)

    # Fix the red-black tree after insertion
    def _fix_insert(self, k):
        while k.parent and k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # Insert a new node
    def insert(self, key):
        node = RBNode(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  # RED

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = 0  # BLACK
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)


# Test the implementation
if __name__ == "__main__":
    bst = RedBlackTree()

    bst.insert(7)
    bst.insert(3)
    bst.insert(18)
    bst.insert(1)
    bst.insert(4)
    bst.insert(10)
    bst.insert(22)

    print("Red-Black Tree Structure:")
    bst.print_tree()

    print("Inorder traversal of the Red-Black Tree:")
    bst.inorder()

    bst.delete_node(10)
    print("\nAfter deleting node with key 10, the Red-Black Tree Structure:")
    bst.print_tree()