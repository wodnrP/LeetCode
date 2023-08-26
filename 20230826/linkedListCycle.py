# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # 빠른 이동, 느린 이동 포인터
        current=head
        slownode=head

        while current and slownode:
            # 느린 포인터 한 칸 이동
            slownode=slownode.next

            # 느린 포인터 None = 도달 = 순회없음
            if slownode is None:
                return False
            
            # 빠른 포인터 한 칸 이동
            current=current.next
            
            # 빠른 포인터 None = 도달 = 순회없음
            if current is None:
                return False

            # 빠른 포인터 한 칸 이동
            current=current.next
            
            # 두 노드가 만나면 = 순회
            if current==slownode:
                return True
        
        # 둘 중 하나라도 null이면 순회X
        return False