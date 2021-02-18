# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        this_node = head
        prev_this = head

        target_node = head
        prev_target = head

        loop_index = 0

        while this_node.next != None:
            this_node = this_node.next
            prev_this = this_node

            if loop_index == n:
                target_node = this_node
                prev_target = prev_this
            elif loop_index > n:
                target_node = target_node.next
                prev_target = target_node
            loop_index += 1

        prev_target.next = target_node.next

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

o = s.removeNthFromEnd(a1, 2)

this = o
while this.next != None:
    print(this.val, end=">")
    this = this.next
print(this.val)
