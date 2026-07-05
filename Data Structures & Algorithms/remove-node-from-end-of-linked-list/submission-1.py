# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        l = 0

        node = head
        while node:
            l += 1
            node = node.next

        n = l - n
        i = 1
        node = head

        if n == 0:
            return node.next

        while node:
            if i == n and node.next != None:
                node.next = node.next.next
            if i == n and node.next == None:
                del node.next
                node.next = None
            
            node = node.next
            i+=1

        return head