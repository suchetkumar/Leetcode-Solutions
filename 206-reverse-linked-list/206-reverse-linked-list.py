# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        start = head
        end = head
        while end.next:
            n = end.next
            end.next = n.next
            n.next = start
            start = n
        return start