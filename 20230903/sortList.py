class Solution:
    def sortList(self, head): 
        if head is None or head.next is None:
            return head
        
        dummy = head
        current = dummy
        sort_list = []

        while head:
            sort_list.append(head.val)
            head = head.next
        
        sort_list.sort()
        for val in sort_list:
            current.val = val
            current = current.next
        
        return dummy