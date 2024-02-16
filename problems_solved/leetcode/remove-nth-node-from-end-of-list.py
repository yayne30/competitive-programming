# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left=head
        right=head
        for i in range (n):
            right=right.next
        while right and right.next:
            left=left.next
            right=right.next
        if right==None :
            head=head.next
        if left.next!=None:
            left.next=left.next.next
        return head
    

        

        