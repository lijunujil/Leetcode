# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        returnNode = ListNode(-1) # this is to track the real head for return val
        tempNode = returnNode # This is used for actual iteration


        while l1 is not None or l2 is not None:
            if l1.val < l2.val:
                tempNode.next = l1
                l1 = l1.next
            else:
                tempNode.next = l2
                l2 = l2.next

        tempNode.next = l1 if l2 is None else l2 # this is to deal with the remaining val, append all of them to the new list

        return returnNode.next


