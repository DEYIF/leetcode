from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next): 
                return None
            fast, slow = fast.next.next, slow.next
            if fast == slow: 
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

# solution = Solution()
# head = [3,2,0,-4]
# pos = 1
# print(solution.detectCycle(head))
