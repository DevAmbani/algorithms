# Last updated: 1/29/2026, 11:34:35 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        if not head or not head.next:
12            return
13
14        # Find middle
15        slow = fast = head
16        while fast and fast.next:
17            slow = slow.next
18            fast = fast.next.next
19
20        # Reverse second half
21        prev = None
22        back = slow.next
23        slow.next = None  # keep front stream intact
24
25        while back:
26            nxt = back.next
27            back.next = prev
28            prev = back
29            back = nxt
30
31        # Weave: front (head) and back (prev)
32        front = head
33        back = prev
34        while back:
35            n1 = front.next
36            n2 = back.next
37
38            front.next = back
39            back.next = n1
40
41            front = n1
42            back = n2
43            
44        
45        
46        