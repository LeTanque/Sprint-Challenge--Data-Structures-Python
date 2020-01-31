
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Each node needs to become itself a BST
    # Insert the given value into the tree
    def insert(self, value):
        # print('\nincoming value: ', value)
        # print(' starting values ------> ', "val", self.value, "left", self.left, "right", self.right)
        bst = BinarySearchTree
        # Compare root now
        if value < self.value:
            # if lesser go left child
            if not self.left:
                self.left = bst(value)
            else:
                # print("  > recursion value less than self.value < ")
                self.left.insert(value)
        else:   # Value is >= Node
            # if greater go right child
            if not self.right:
                self.right = bst(value)
            else:
                # If something is already there, recurse
                # print("  > recursion happens < ")
                self.right.insert(value)
        # print(' self.left ---> ', self.left)
        # print(' self.right ---> ', self.right)
        # print('self.value ---> ', self.value)
        # print(' final value: ', value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # JUst go right ->
        # BST most right is biggest
        # If there is nothing more right
        # You are at the largest node.
        # if not self.right:
        #     return self.value
        # else:
        #     return self.right.get_max()
        # ############ ALTERNATE
        # # Create a ref to the current node and update
        # # it as we traverse the tree
        max_value = self.value
        current = self  # < --- This is a cursor!
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # The purpose of this method is to call the
        # same function on each node in the tree
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
