# Last updated: 2/2/2026, 4:06:43 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        curr = dummy
10        carry = 0
11        while l1 or l2 or carry:
12            x = l1.val if l1 else 0
13            y = l2.val if l2 else 0
14
15            total = x + y + carry
16            carry = total // 10
17            curr.next = ListNode(total % 10)
18
19            curr = curr.next
20            if l1: l1 = l1.next
21            if l2: l2 = l2.next
22
23        return dummy.next
24