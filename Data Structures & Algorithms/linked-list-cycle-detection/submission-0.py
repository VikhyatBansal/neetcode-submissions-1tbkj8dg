# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm = {}
        while head:
            if head not in hm:
                hm[head] = True
            else:
                return hm[head]
            head = head.next
        return False