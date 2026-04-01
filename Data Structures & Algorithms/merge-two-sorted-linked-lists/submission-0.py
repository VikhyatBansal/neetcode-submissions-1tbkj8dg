# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        st = []
        tmp1 = list1
        tmp2 = list2
        if not tmp1:
            return tmp2
        elif not tmp2:
            return tmp1
        else:
            while tmp1 and tmp2:
                if tmp1.val==tmp2.val:
                    st.append(tmp1.val)
                    st.append(tmp2.val)
                    tmp1 = tmp1.next
                    tmp2 = tmp2.next
                elif tmp1.val>tmp2.val:
                    st.append(tmp2.val)
                    tmp2 = tmp2.next
                else:
                    st.append(tmp1.val)
                    tmp1 = tmp1.next
            while tmp2:
                st.append(tmp2.val)
                tmp2 = tmp2.next
            while tmp1:
                st.append(tmp1.val)
                tmp1 = tmp1.next
            dum = ListNode(0)
            res = dum
            for i in st:
                dum.next = ListNode(i)
                dum = dum.next
            return res.next
        # tmp1 = list1
        # tmp2 = list2
        # while tmp1 or tmp2:
        #     if tmp1.val>tmp2.val:
        #         tmp2.next = tmp1
        #         tmp1 = tmp1.next
        #     elif tmp1.val<tmp2.val:

        #     else:
        #         tmp = tmp1.next
        #         tmp1.next = tmp2
        #         tmp2 = tmp2.next