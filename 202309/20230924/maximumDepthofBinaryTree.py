# 수정 전
# class Solution:
#     def maxDepth(self, root):
#         depth=0
#         result=[]
#         self.preorder(root, depth, result)
#         result=sorted(set(result))
#         return result[-1]
#     def preorder(self, root, depth, result):
#         if root is None:
#             result.append(depth)
#             pass
#         else:
#             depth+=1
#             self.preorder(root.left, depth, result)
#             self.preorder(root.right, depth, result)

# 수정 후 
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1