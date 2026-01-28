# Last updated: 1/28/2026, 12:46:13 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        tracker = set()
10        curr = head
11        while curr:
12            if curr in tracker:
13                return True
14            tracker.add(curr)
15            curr = curr.next
16        return False