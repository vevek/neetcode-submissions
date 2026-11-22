# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1

        head = ListNode(0)
        cur = head
        carry = 0
        
        
        while l1 or l2 or carry > 0:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            val = sum % 10
            carry = sum // 10

            copy = ListNode(val)
            cur.next = copy
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
        




        