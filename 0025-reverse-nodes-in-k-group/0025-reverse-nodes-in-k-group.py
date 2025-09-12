# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grpPrev = dummy

        while True:
            kth = self.getKth(grpPrev, k)
            if not kth:
                break
            grpNext = kth.next

            # reverse grp
            prev, curr = grpNext, grpPrev.next
            while curr != grpNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # map grpPrev pointer
            tmp = grpPrev.next
            grpPrev.next = kth
            grpPrev = tmp
        return dummy.next