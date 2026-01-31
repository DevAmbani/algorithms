# Last updated: 1/31/2026, 12:04:08 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        arr = []
9        curr = head
10
11        while curr:
12            arr.append(curr)
13            curr = curr.next
14        arr.pop(len(arr)-n)
15
16        if not arr:
17            return None
18        
19        head = arr[0]
20        curr = head
21        for i in arr[1:]:
22            curr.next = i
23            curr = curr.next
24        curr.next = None
25        return head