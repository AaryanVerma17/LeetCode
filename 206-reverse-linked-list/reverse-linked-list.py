class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        current = head
        
        while current:
            next_element = current.next
            current.next = result
            result = current
            current = next_element
            
        return result