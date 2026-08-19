# https://leetcode.com/problems/add-two-numbers/submissions/2112115657
# Runtime: 0 ms
# Memory: 19.22 MB


# Definition for singly-linked list.
class ListNode:
    val: int
    next: "ListNode | None"

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(0)
        carry = 0
        curr = dummy

        while l1 or l2 or carry:
            val1 = 0
            val2 = 0
            if l1 is not None:
                val1 = l1.val
            if l2 is not None:
                val2 = l2.val

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
