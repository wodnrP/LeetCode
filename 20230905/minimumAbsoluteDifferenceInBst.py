# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root):
        r = []
        self.inorder(root,r)
        r.sort()
        result = r[-1]
        l=0
        for i in range(1,len(r)):
            result = min(result, (r[i]-r[l]))
            l+=1
        return result

    def inorder(self,node,r):
        r.append(node.val)
        if node.left:
            self.inorder(node.left,r)

        if node.right:
            self.inorder(node.right,r)

# DFS 중위순회로 모든 값 리스트 담고 O(logn)
# 오름차순 정렬 (O(lon))
# 모든 값 돌며 뻬는 중에 가장 작은 값 갱신
