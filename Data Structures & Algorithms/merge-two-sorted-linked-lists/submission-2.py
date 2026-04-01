# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp1 = list1
        tmp2 = list2
        curr = ListNode(0)
        res = curr
        while tmp1 and tmp2:
            # print(tmp1.val,tmp2.val,curr.val)
            if tmp1.val<=tmp2.val:
                curr.next = tmp1
                tmp1 = tmp1.next
            else:
                curr.next = tmp2
                tmp2 = tmp2.next        
            curr = curr.next  
        while tmp1:
            curr.next = tmp1
            if not tmp1.next:
                break
            tmp1 = tmp1.next  
            curr = curr.next
        while tmp2:
            curr.next = tmp2
            if not tmp2.next:
                break
            tmp2 = tmp2.next  
            curr = curr.next
        return res.next        