# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        left = dummy
        right = dummy.next
        ## moving right pointer by n
        while n>0:
            right = right.next
            n=n-1
        

        ### moving the pointers
        while right:
            left=left.next
            right=right.next

        ## deleting the node at nth
        left.next = left.next.next

        return dummy.next