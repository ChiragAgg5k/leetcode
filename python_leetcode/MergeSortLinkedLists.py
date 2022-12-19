# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """Merging two already sorted linked lists

        Youtube explanation: https://www.youtube.com/watch?v=XIdigk956u0

        Args:
            list1 (LinkedList): list no. 1
            list2 (LinkedList): list no. 2

        Returns:
            ListNode: head of the merged linked list
        """
        dummy_node = ListNode()
        tail = dummy_node

        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy_node.next
