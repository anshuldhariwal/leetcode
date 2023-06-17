# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        carryOver = 0
        current = result

        while l1 != None or l2 != None or carryOver != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            value = l1val + l2val + carryOver
            carryOver = value//10
            temp = ListNode(value % 10)
            current.next = temp
            current = temp
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return result.next
