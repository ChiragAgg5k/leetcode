from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
        """Reversing a linked list
        Youtube explanation: https://www.youtube.com/watch?v=G0_I-ZF0S38

        Returns:
            void: inplace function
        """

        prev, curr = None, head

        while curr is not None:
            # temp assignment
            nxt = curr.next

            # link swap
            curr.next = prev

            # pointer moving forward
            prev = curr
            curr = nxt

        return prev
