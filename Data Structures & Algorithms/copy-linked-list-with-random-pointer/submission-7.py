"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # range of length of the linkedlist
        # range of possible values in the linkedlist
        # can the random pointer point to itself
        # are the node values unique
        
        oldToCopy = collections.defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.val = cur.val
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]



