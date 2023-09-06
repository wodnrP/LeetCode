# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1차
# class Solution:
#     def kthSmallest(self, root, k):
#         r = []
#         self.inorder(root, r)
#         r.sort()
#         return r[k-1]

#     def inorder(self,node,r):
#         r.append(node.val)
#         if node.left:
#             self.inorder(node.left,r)
#         if node.right:
#             self.inorder(node.right,r)

# 수정 후
class Solution:
    def kthSmallest(self, root, k):
        r = []
        node = root
        while True:
            # 노드 왼쪽만 탐색, stack의 방법으로 노드 저장
            while node is not None:
                r.append(node)
                node = node.left

            # r == None : root 노드 없음
            if not r:
                break

            # 가장 최근에 push한 노드 반환
            result = r.pop()
            k -= 1

            # k == 0 : k번째 push한 k번째 작은 값
            if k == 0:
                return result.val
            
            # 오른쪽 노드 탐색
            node = result.right