# Last updated: 1/24/2026, 11:38:14 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        curr, prev = head, None
9        while curr:
10            nxt = curr.next
11            curr.next = prev
12            prev = curr
13            curr = nxt
14        return prev
15        