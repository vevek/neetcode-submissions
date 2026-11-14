# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:



        


    def reorderList(self, head: Optional[ListNode]) -> None:
        # Have a list. Append all nodes within their rightful index in the list. Using the length of the list, we can now do the [0, n-1, 1, n-2, 2, n-3, ...] in a new list. We can access the rightful index appropriately. 
        # o(n), o(n)

        def reorder(root: Optional[ListNode], cur: Optional[ListNode]) -> ListNode:
            if not cur:
                return root
            
            root = reorder(root, cur.next)
            if not root:
                return None
            
            tmp = None
            if root == cur or root.next == cur:
                cur.next = None
            else:
                tmp = root.next
                root.next = cur
                cur.next = tmp

            return tmp
        
        head = reorder(head, head.next)


        # range of possible length of linked list
        # range of possible values in each list node
        # are cycles possible? 

        # store the listnodes in a single list which gives us a reference to every node
        # using 2 pointers from the start and end of the list, reconfigure the pointers

        # using recursion, recurse all the way to the end of the linked list
        # as we unwind the linked list, we link the current root node to the end node, then unwind and set the new root node to the node originally at index 1. 

