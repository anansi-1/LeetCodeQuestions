# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
        current = head
        while current is not None:
            binary.append(current.val)
            current = current.next
        ans = 0
        for index,bit in enumerate(reversed(binary)):
                ans += bit * 2**index
        return ans