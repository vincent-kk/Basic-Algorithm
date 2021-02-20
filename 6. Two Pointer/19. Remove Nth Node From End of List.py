# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        array_list = []
        node = head

        while node != None:
            array_list.append(node)
            node = node.next

        length = len(array_list)
        target = length - n
        if n == 1:
            if length > 1:
                array_list[-2].next = None
            else:
                head = None
        elif target == 0:
            head = head.next
        else:
            prev_node = array_list[target - 1]
            next_node = array_list[target + 1]
            prev_node.next = next_node

        return head


s = Solution()

a4 = ListNode(4)
a3 = ListNode(3, a4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)


this = a1
while this.next != None:
    print(this.val, end=">")
    this = this.next
print(this.val)

o = s.removeNthFromEnd(a1, 1)

this = o
while this.next != None:
    print(this.val, end=">")
    this = this.next
print(this.val)
