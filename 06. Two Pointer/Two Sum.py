# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = l1
        num2 = l2
        carry = 0
        result = None
        resultList = None

        while num1.next != None or num2.next != None:
            tempSum = num1.val + num2.val + carry
            carry = tempSum // 10
            if resultList == None:
                resultList = ListNode(tempSum % 10)
                result = resultList
            else:
                resultList.next = ListNode(tempSum % 10)

            resultList = resultList.next
            num1 = ListNode(0) if num1.next == None else num1.next
            num2 = ListNode(0) if num2.next == None else num2.next

        return result


l = l1 = ListNode(2)
l1.next = ListNode(4)
l1 = l1.next
l1.next = ListNode(3)
l1 = l1.next

m = l2 = ListNode(7)
l2.next = ListNode(0)
l2 = l2.next
l2.next = ListNode(8)
l2 = l2.next

s = Solution()
s.addTwoNumbers(l, m)
