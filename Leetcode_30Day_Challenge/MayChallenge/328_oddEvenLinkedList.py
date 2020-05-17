# LC _328

#Input: 1->2->3->4->5->NULL
#Output: 1->3->5->2->4->NULL


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
    	for_odd = ListNode(0)
    	for_even = ListNode(0)
    	oHead = for_odd
    	eHead = for_even
    	isOdd = True
    	while head:
    		if isOdd:
    			for_odd.next = head
    			for_odd = for_odd.next
    		else:
    			for_even.next = head
    			for_even = for_even.next
    		isOdd = not isOdd
    		head = head.next
    	for_even.next = None
    	for_odd.next = ehead.next
    	return oHead.next
