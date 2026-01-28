# Last updated: 1/28/2026, 12:57:38 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if head is None:
10            return False
11        p1 = head
12        p2 = head.next
13        while p2 and p2.next:
14            if p1 == p2:
15                return True
16            p1 = p1.next
17            p2 = p2.next.next
18        return False