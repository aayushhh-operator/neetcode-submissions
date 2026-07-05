class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        stack = []
        l = 0

        node = head

        while node != None:
            stack.append(node.val)
            node = node.next
            l+=1
        
        if l >= 2:
            s = ListNode(stack.pop(-1))
            node = ListNode(stack.pop(-1))
            s.next = node

            while stack:
                temp = ListNode(stack.pop(-1))
                temp.next = None
                node.next = temp

                node = node.next
                temp = temp.next
        elif l == 1:
            s = ListNode(stack.pop(-1))

        return s