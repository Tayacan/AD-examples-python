# -*- coding: utf-8 -*-

class BinarySearchTree:
    """An unbalanced binary search tree."""
    class _Node:
        """Represents a node with a key, a value, and two children."""
        def __init__(self,key,value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        """Create an empty tree."""
        self.root = None

    def __getitem__(self,key):
        """Return the value of the node with this key.

        Raises IndexError if there is no such key."""
        current = self.root
        while current is not None:
            if key == current.key:
                return current.value
            elif key > current.key:
                current = current.right
            else:
                current = current.left

        raise IndexError

    def __setitem__(self,key,value):
        """Insert a node with this key and value into the tree.

        If a node with the same key exists, replace it."""
        n = BinarySearchTree._Node(key,value)
        if self.root is None or self.root.key == key:
            self.root = n
            return

        current = self.root
        while True:
            if key > current.key:
                if current.right is None:
                    current.right = n
                    return
                elif current.right.key == key:
                    n.right = current.right.right
                    n.left = current.right.left
                    current.right = n
                    return
                else:
                    current = current.right
                    continue
            else:
                if current.left is None:
                    current.left = n
                    return
                elif current.left.key == key:
                    n.right = current.left.right
                    n.left = current.left.left
                    current.left = n
                    return
                else:
                    current = current.left
                    continue



