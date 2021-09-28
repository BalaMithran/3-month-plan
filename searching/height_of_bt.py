class Node:
    def _init_(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:

    # Function to find the height of a binary tree.
    def height(self, root):
        max = 0
        if root == None:
            return 0
        else:
            l = self.height(root.left)
            r = self.height(root.right)
            if l > r:
                return l+1
            else:
                return r+1
