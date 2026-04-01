# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tmp1 = list1
        tmp2 = list2
        dum = res = ListNode(0)
        while tmp1 and tmp2:
            if tmp1.val<tmp2.val:
                dum.next = tmp1
                tmp1 = tmp1.next
            else:
                dum.next = tmp2
                tmp2 = tmp2.next
            dum = dum.next
        while tmp1:
            dum.next = tmp1
            tmp1 = tmp1.next
            dum = dum.next
        while tmp2:
            dum.next = tmp2
            tmp2 = tmp2.next
            dum = dum.next
        return res.next
