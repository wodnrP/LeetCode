# class Solution:
#     def isSameTree(self, p, q) -> bool:
#         # p와 q가 모두 None이거나 한쪽만 None일 경우
#         if p is None and q is None:
#             return True
#         if p is None or q is None:
#             return False
        
#         p_tree,q_tree=[],[]
#         self.level_search(p, p_tree)  
#         self.level_search(q, q_tree)
#         return p_tree == q_tree
    
#     # BFS
#     def level_search(self, node, l):
#         queue = [(node, 0)]
#         while queue:
#             node, level = queue.pop(0)
#             if node is not None:
#                 l.append(node.val)
#                 if node.left:
#                     queue.append((node.left, level+1))
#                 if node.right:
#                     queue.append((node.right, level+1))
#                 else:
#                     l.append(0)

# 개선 코드
class Solution:
    def isSameTree(self, p, q) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        queue = [(p, q)]
        while queue:
            np, nq = queue.pop(0)
            if np is None and nq is None:
                continue
            elif np is None or nq is None or np.val != nq.val:
                return False
            queue.append((np.left, nq.left))
            queue.append((np.right, nq.right))
        return True