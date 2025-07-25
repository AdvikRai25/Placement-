class Solution(object):
    def detectCycle(self, head):
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                slow = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow

        return None
