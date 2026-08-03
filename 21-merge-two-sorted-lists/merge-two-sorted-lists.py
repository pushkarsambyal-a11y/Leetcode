# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        lst = []
        temp = list1
        while temp:
            lst.append(temp.val)
            temp = temp.next

        temp1 = list2
        while temp1:
            lst.append(temp1.val)
            temp1 = temp1.next
        
        lst.sort()

        dummy = ListNode(0)
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

        
        
        