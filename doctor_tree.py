class DoctorNode:
    """
    Represents a doctor in the reporting hierarchy.

    Attributes:
        name (str): The doctor's name.
        left (DoctorNode or None): Left report.
        right (DoctorNode or None): Right report.
    """
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f"DoctorNode({self.name})"


class DoctorTree:
    """
    Manages the doctor reporting tree.

    Attributes:
        root (DoctorNode or None): The root of the tree.
    """
    def __init__(self, root=None):
        self.root = root

    def find(self, name):
        """Find a DoctorNode by name using breadth-first search."""
        if not self.root:
            return None
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.name == name:
                return current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return None

    def insert(self, parent_name, child_name, side):
        """
        Inserts a new DoctorNode under the specified parent on the given side ('left' or 'right').
        """
        parent = self.find(parent_name)
        if not parent:
            raise ValueError(f"Parent '{parent_name}' not found in the tree.")
        if side == "left":
            if parent.left is None:
                parent.left = DoctorNode(child_name)
            else:
                raise ValueError(f"Left child already exists for '{parent_name}'.")
        elif side == "right":
            if parent.right is None:
                parent.right = DoctorNode(child_name)
            else:
                raise ValueError(f"Right child already exists for '{parent_name}'.")
        else:
            raise ValueError("Side must be 'left' or 'right'.")

    def preorder(self, node):
        """Preorder traversal: root → left → right"""
        if node is None:
            return []
        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        """Inorder traversal: left → root → right"""
        if node is None:
            return []
        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        """Postorder traversal: left → right → root"""
        if node is None:
            return []
        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


def test_doctor_tree():
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    # Valid insertions
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    # Traversal checks
    assert tree.preorder(tree.root) == ["Dr. Croft", "Dr. Phan", "Dr. Morgan", "Dr. Carson", "Dr. Goldsmith"]
    assert tree.inorder(tree.root) == ["Dr. Morgan", "Dr. Phan", "Dr. Carson", "Dr. Croft", "Dr. Goldsmith"]
    assert tree.postorder(tree.root) == ["Dr. Morgan", "Dr. Carson", "Dr. Phan", "Dr. Goldsmith", "Dr. Croft"]
    print("✅ Traversal methods passed.")

    # Edge case: inserting under non-existent parent
    try:
        tree.insert("Dr. Who", "Dr. Strange", "left")
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")

    # Edge case: inserting with invalid side
    try:
        tree.insert("Dr. Croft", "Dr. House", "middle")
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")

    # Edge case: inserting where child already exists
    try:
        tree.insert("Dr. Croft", "Dr. SomeoneElse", "left")
    except ValueError as e:
        print(f"✅ Caught expected error: {e}")


# Run tests if this file is executed directly
if __name__ == "__main__":
    test_doctor_tree()
