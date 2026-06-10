# Last updated: 6/10/2026, 10:17:26 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        values = []
9        for l in lists:
10            while l:
11                values.append(l.val)
12                l = l.next
13
14        values.sort()
15        
16        dummy = ListNode(0)
17        curr = dummy
18        for v in values:
19            curr.next = ListNode(v)
20            curr = curr.next
21
22        return dummy.next
23