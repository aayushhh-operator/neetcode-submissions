class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2

        s = ListNode(-1)
        node = s

        while list1 != None and list2 != None:
            if list1.val<=list2.val:
                temp = ListNode(list1.val)
                print(temp.val)
                node.next = temp
                list1 = list1.next
                node = node.next
                del temp
            elif list1.val > list2.val:
                temp = ListNode(list2.val)
                print(temp.val)
                node.next = temp
                list2 = list2.next
                node = node.next
                del temp

        if list1 == None:
            while list2 != None:
                temp = ListNode(list2.val)
                node.next = temp
                list2 = list2.next
                node = node.next
                del temp
        else:
            while list1 != None:
                temp = ListNode(list1.val)
                node.next = temp
                list1 = list1.next
                node = node.next
                del temp
        return s.next
            