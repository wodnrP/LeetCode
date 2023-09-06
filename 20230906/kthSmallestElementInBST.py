# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        r = []
        self.inorder(root, r)
        r.sort()
        return r[k-1]

    def inorder(self,node,r):
        r.append(node.val)
        if node.left:
            self.inorder(node.left,r)
        if node.right:
            self.inorder(node.right,r)