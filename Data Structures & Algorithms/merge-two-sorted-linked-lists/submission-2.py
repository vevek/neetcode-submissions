# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            temp = list1
            list1 = list2
            list2 = temp

        head = list1
        currNode = head
        list1 = list1.next



        while list1 and list2:
            if list1.val <= list2.val:
                tempNode = list1
                list1 = list1.next
                currNode.next = tempNode
                currNode = currNode.next
            else:
                tempNode = list2
                list2 = list2.next
                currNode.next = tempNode
                currNode = currNode.next

        if list1:
            currNode.next = list1
        elif list2:
            currNode.next = list2

        return head