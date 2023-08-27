# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 1차 시도 
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         더한 값을 담을 연결 노드 생성 

#         만약 l1.next와 l2.next가 없으면 반복 중지

#         만약 l1.val + l2.val이 10을 넘어가면
#             l1.val + l2.val에서 - 10을 생성된 노드에 추가

#         l1.val + l2.val을 dummy 첫번째 노드로 삽입
#         l1과 l2 다음 연결 노드로 이동

#         """
#         dummy=ListNode(0)
#         dummy2=ListNode(0)
#         current = dummy
#         save = dummy2

#         if l1.val==0 and l2.val==0:
#             return l1

#         while l1 or l2:
#             if (l1,l2) is None:
#                 break

#             if l1 is None:
#                 current.next = ListNode((l2.val+save.val)-10)
#                 l2 = l2.next
#                 current = current.next
            
#             if l2 is None:
#                 current.next = ListNode((l1.val+save.val)-10)
#                 l1 = l1.next
#                 current = current.next

#             if (l1 and l2) is not None:
#                 if l1.val + l2.val >= 10:
#                     if save != None:
#                         current.next = ListNode((l1.val + l2.val)-10 + save.val)
#                     else:
#                         current.next = ListNode((l1.val + l2.val)-10)
                    
#                     save = ListNode(1)

#                 else:
#                     if save != None:
#                         current.next = ListNode(l1.val + l2.val + save.val)

#                     else:
#                         current.next = ListNode(l1.val + l2.val)

                
#                 l1 = l1.next
#                 l2 = l2.next
#                 current = current.next

#         if current.val == 0:
#             current.next = ListNode(1)
        
#         return dummy.next
    

# 해결
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        (save를 신규 노드가 아닌 변수로 생각)
        더한 값을 담을 더미 노드 생성
        val 저장할 변수 생성 

        테스트 케이스 오류 [0,1,2~],[0,4,2~]>>만약 l1.val,l2.val이 없으면 l1 or l2 반환 

        l1, l2, save 중 하나라도 존재하면 반복
            만약 l1이 none이 아니면 
                l1.val을 더해감
                l1을 다음 노드로 이동
            만약 l2가 none이 아니면
                l2.val을 더해감
                l2를 다음 노드로 이동
            
            더미의 다음 노드에 새로운 노드 +=val % 10를 추가
            (l1.val+l2.val >= 10 이면 1의 자리 반환 == 나머지)
            
            더미 노드를 다음 노드로 이동 
            
            저장한 val을 10으로 나눔 == l1.val+l2.val >= 10 일 경우 십의 자리 반환

        """
        dummy=ListNode(0)
        current = dummy
        save = 0 

        while l1 or l2 or save:
            if l1 is not None:
                save+= l1.val
                l1 = l1.next
            if l2 is not None:
                save+= l2.val
                l2 = l2.next
            
            current.next = ListNode(save%10)
            
            current = current.next

            save = save//10
        return dummy.next
