# Last updated: 6/4/2026, 4:15:53 PM
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
11        fast = head
12        slow = head
13        
14        while fast and fast.next:
15            slow = slow.next
16            fast = fast.next.next
17        
18        mid = slow
19        prev = None
20
21        while mid:
22            temp = mid.next
23            mid.next = prev
24            prev = mid
25            mid = temp
26        
27        curr = head
28        while curr and prev and prev.next:
29            temp1 = curr.next
30            temp2 = prev.next
31            curr.next = prev
32            prev.next = temp1
33
34            curr = temp1
35            prev = temp2
36
37        return head