class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # num에 Linked List 데이터 담기
        num=[]
        while head:
            num.append(head.val)
            head = head.next
        
        # num 값을 key, 중복 개수를 value로 하는 dict 
        num_dict={}
        for i in num:
            num_dict[i] = num_dict.get(i, 0) + 1
        
        # value > 1인 key 삭제
        duplicate = [key for key, value in num_dict.items() if value > 1]
        for i in duplicate:
            del num_dict[i]
        
        # key 기준 다시 리스트로 변경, 링크드 리스트로 재생성
        num = [i for i in num_dict.keys()]
        result = ListNode()
        curr = result
        i=0
        while len(num) > i:
            node = ListNode(num[i])
            curr.next = node
            curr = node
            i+=1
        return result.next