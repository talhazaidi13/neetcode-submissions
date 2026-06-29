# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(lists, 0, len(lists) - 1)

    def divide (self, lists, l , r):
        # if not lists:
        #     return None
        # if len(lists) <= 1:
        #     return lists
        # mid = len(lists) // 2
        # left = divide(lists[:mid])
        # right = divide(lists[mid:])

        if l > r:
            return None
        if l == r:
            return lists[l]
        mid = l + (r - l) // 2
        left = self.divide(lists, l, mid)
        right = self.divide(lists, mid + 1, r)

        return self.merge(left, right)
    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return dummy.next

        # res = []
        # i = j = 0
        # while i<len(left) and j<len(right):
        #     if left[i] <= right[j]:
        #         res.append(left[i])
        #         i=i+1
        #     else:
        #         res.append(right[j])
        #         j=j+1
        
        # res.extend(left[i:])
        # res.extend(left[j:])
        # return res
