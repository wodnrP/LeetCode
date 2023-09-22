class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 개선 전
# class Solution:
#     def removeNthFromEnd(self, head, n):
#         dummy = []
#         while head:
#             dummy.append(head.val)
#             head = head.next
#         dummy.pop(-n)
#         if not dummy:
#             return 
#         for i in range(len(dummy)):
#             dummy[i] = ListNode(dummy[i])
#         from collections import deque
#         queue = deque(dummy)
#         result = queue.popleft()
#         curr = result
#         while queue:
#             node = queue.popleft()
#             curr.next = node
#             curr = node 
#         return result

# 개선 후 
class Solution:
    def removeNthFromEnd(self, head, n):
        slow, fast = head, head
        while n > 0:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        if fast:
            slow.next = slow.next.next
        else:
            head = head.next
        return head