# 排序链表
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next
        res.sort()
        cur = head
        for _, num in enumerate(res):
            cur.val = num
            cur = cur.next
        return head
    
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: 
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None
        left, right = self.sortList2(head), self.sortList2(mid)
        h = res =ListNode(0)
        while left and right:
            if left.val <= right.val: 
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next
    
    def sortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
