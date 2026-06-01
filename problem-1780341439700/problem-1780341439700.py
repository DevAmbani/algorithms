# Last updated: 6/1/2026, 2:17:19 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        if not list1:
9            return list2
10        if not list2:
11            return list1
12
13        dummy = ListNode(0)
14        curr = dummy
15
16        while list1 and list2:
17            if list1.val <= list2.val:
18                curr.next = list1
19                list1 = list1.next
20            else:
21                curr.next = list2
22                list2 = list2.next
23            curr = curr.next
24        
25        if list1:
26            curr.next = list1
27        if list2:
28            curr.next = list2
29        
30        head = dummy.next  
31        return head