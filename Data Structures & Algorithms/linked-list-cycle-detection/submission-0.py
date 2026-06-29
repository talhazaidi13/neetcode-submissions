# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head:
            if head.next in arr:
                return True
            arr.append(head.next)
            head = head.next
        return False