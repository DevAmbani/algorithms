# Last updated: 2/1/2026, 4:57:23 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution:
11    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
12        curr = head
13        mp = {None:None}
14
15        while curr:
16            copyNode = Node(curr.val)
17            mp[curr] = copyNode
18            curr = curr.next
19
20        curr = head
21        while curr:
22            copyNode = mp[curr]
23            copyNode.next = mp[curr.next]
24            copyNode.random = mp[curr.random]
25            curr = curr.next
26        
27        return mp[head]