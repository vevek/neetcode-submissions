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
        
        map = {}   

        cur = head
        while cur:
            copy = Node(cur.val)
            map[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = map[cur]
            copy.next = map[cur.next] if cur.next else None
            copy.random = map[cur.random] if cur.random else None
            cur = cur.next

        return map[head] if head else None


