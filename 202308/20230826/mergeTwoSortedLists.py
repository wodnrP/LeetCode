# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 더미 리스트, 현재 포인터 생성
        dummy = ListNode(0)
        current = dummy
        # 리스트 서로가 없으면 크로스 반환 
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        while list1 and list2:
            # 리스트1 데이터가 클 경우 
            if list1.val > list2.val:
                # 더미에 list2 연결
                current.next = list2
                # 리스트2는 다음 연결로 이동
                list2 = list2.next

            # 리스트2 데이터가 클 경우
            else:
                # 더미에 list1 연결
                current.next = list1
                # 리스트1은 다음 연결로 이동
                list1 = list1.next
            
            # 더미 리스트도 다음 연결로 이동
            current = current.next
        
        # 마지막 노드 지정
        if list1 is None:
            current.next = list2
        else:
            current.next = list1

        return dummy.next