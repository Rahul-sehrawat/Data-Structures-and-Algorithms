# link - https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry :
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            #adding here
            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum//10
            curr.next = ListNode(digit)
            curr = curr.next

            #updating the pointer
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next


# Intuition:
'''
1.always try to create dummy node in linked list problems.
2.use % for getting the digit and // for getting the carry 
3.note: the output result is also in reverse ,so the carry will go to the right side digit.
4.create a node with every result digit
5.move both list pointer to its next node
6, after while loop return next node of dummy
'''