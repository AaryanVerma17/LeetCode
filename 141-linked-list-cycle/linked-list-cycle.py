class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        second = head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False