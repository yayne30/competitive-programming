# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp=head
        lessthan=ListNode(0)
        greaterthan=ListNode(0)
        templess=lessthan
        tempgreat=greaterthan
        while temp!=None:
            if temp.val<x:
                templess.next=temp
                templess=temp
            else:
                tempgreat.next=temp
                tempgreat=temp
            temp=temp.next 
        tempgreat.next=None
        templess.next=greaterthan.next

        return lessthan.next

                
        