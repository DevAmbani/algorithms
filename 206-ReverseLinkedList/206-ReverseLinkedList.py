# Last updated: 1/24/2026, 11:40:57 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        
        while cur is not None:
            # 1. 다음 노드를 잠시 저장 (연결 끊기기 전)
            next_node = cur.next
            # 2. 현재 노드의 방향을 뒤로 돌림
            cur.next = prev
            # 3. 한 칸씩 앞으로 이동
            prev = cur
            cur = next_node
            
        return prev