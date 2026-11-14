# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # range of the length of the linkedlist
        # range of values allowed in each ListNode
        # possible values of n in relation to number of nodes in linkedlist

        # L - n + 1

        l = 0
        curr = head
        while curr.next != None:
            l += 1
            curr = curr.next

        m = l - n + 1

        prev = None
        curr = head

        i = 0
        while i < m and curr.next != None:
            prev = curr
            curr = curr.next
            i += 1

        if prev != None and curr.next != None:
            prev.next = curr.next
        elif prev != None and curr.next == None:
            prev.next = None
        elif prev == None and curr.next != None:
            head = curr.next
        elif prev == None and curr.next == None:
            return None

        return head



