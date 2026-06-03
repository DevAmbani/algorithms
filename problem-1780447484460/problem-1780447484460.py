# Last updated: 6/2/2026, 7:44:44 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        curr1 = head
10        curr2 = head
11
12        while curr2 and curr2.next:
13            s1 = curr1.next
14            s2 = curr2.next.next
15
16            if s1 == s2:
17                return True
18            
19            curr1 = curr1.next
20            curr2 = curr2.next.next
21        
22        return False