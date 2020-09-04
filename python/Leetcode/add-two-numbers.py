# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# TOPICS: LINKEDLIST, MATH
# APPROACH: Add each node and just maintain the carry

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = l1
        prev = None
        while l1 and l2:  
            first = l1.val
            l1.val = (first + l2.val + carry) % 10
            carry = (first + l2.val + carry) // 10
            prev = l1
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            first = l1.val
            l1.val = (first + carry) % 10
            carry = (first + carry) // 10
            prev = l1
            l1 = l1.next
        
        while l2:
            first = l2.val
            val = (first + carry) % 10
            l = ListNode(val)
            prev.next = l
            prev = l
            carry = (first + carry) // 10
            l2 = l2.next
        
        if carry:
            l = ListNode(carry)
            prev.next = l
        return head