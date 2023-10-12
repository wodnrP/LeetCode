class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1차        
# class Solution:
#     def mergeKLists(self, lists):
#         link=[]
#         i=0
#         while len(lists)-1 >= i:
#             if lists[i]:
#                 link.append(lists[i].val)
#             else:
#                 i+=1
#                 continue
#             lists[i]=lists[i].next
#         link=sorted(link)
#         result=ListNode()
#         curr=result
#         for i in link:
#             node=ListNode(i)
#             curr.next=node
#             curr=node
#         return result.next
    
# 개선     
class Solution:
    def mergeKLists(self, lists):
        link=[]
        i=0
        while len(lists)-1 >= i:
            if lists[i]:
                link.append(lists[i].val)
            else:
                i+=1
                continue
            lists[i]=lists[i].next
        link=sorted(link, reverse=True)
        result=None
        for i in link:
            result=ListNode(i, result)
        return result