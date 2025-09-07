# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1st step: create dummy node and reach left-1 pos
        dummy = ListNode(0,head)
        leftPrev, curr = dummy, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next
        
        # 2nd step: reverse the subList
        prev = None
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 3rd step: attach the subList to Original List
        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next