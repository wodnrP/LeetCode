class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = []
        while head:
            dummy.append(head.val)
            head = head.next
        dummy.pop(-n)
        if not dummy:
            return 
        for i in range(len(dummy)):
            dummy[i] = ListNode(dummy[i])
        from collections import deque
        queue = deque(dummy)
        result = queue.popleft()
        curr = result
        while queue:
            node = queue.popleft()
            curr.next = node
            curr = node 
        return result