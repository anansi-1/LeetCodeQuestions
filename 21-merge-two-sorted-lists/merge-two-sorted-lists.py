# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy  
        
        i = list1
        j = list2
        
        while i is not None and j is not None:
            if i.val <= j.val:
                current.next = i  
                i = i.next        
            else:
                current.next = j  
                j = j.next        
            current = current.next  
        
        if i is not None:
            current.next = i
        elif j is not None:
            current.next = j
        
        return dummy.next