# Last updated: 6/5/2026, 7:48:51 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        count = 0
9        curr = head
10
11        while curr:
12            count += 1
13            curr = curr.next
14        
15        number = count - n
16        n_count = 1
17
18        if number == 0:
19            return head.next
20
21        curr = head
22        while curr and curr.next:
23            if n_count == number:
24                curr.next = curr.next.next
25                break
26            n_count += 1
27            curr = curr.next
28        
29        return head