# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodes_to_array(self, start_node: ListNode | None) -> list:
        array_out = []
        walker = start_node
        while walker is not None:
            array_out.append(walker.val)
            walker = walker.next
        return array_out
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        digits_a = self.nodes_to_array(l1)
        digits_b = self.nodes_to_array(l2)
        first_num = int("".join(map(str, digits_a[::-1])))
        second_num = int("".join(map(str, digits_b[::-1])))
        combined_total = first_num + second_num
        target_digits = list(str(combined_total))[::-1]
        anchor = ListNode(0)
        runner = anchor
        for char in target_digits:
            runner.next = ListNode(int(char))
            runner = runner.next
        return anchor.next