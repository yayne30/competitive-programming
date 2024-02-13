# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1ptr=list1
        list2ptr=list2

        if list1==None:
            return list2 
        if list2==None:
           return list1
       
        if list1.val>=list2.val:
            head=list2
            list2ptr=list2.next
        else:
            head=list1
            list1ptr=list1ptr.next
        temp=head
        while list1ptr and list2ptr:
            if list1ptr.val<=list2ptr.val:
                temp.next=list1ptr
                list1ptr=list1ptr.next
                
            else:
                temp.next=list2ptr
                list2ptr=list2ptr.next
            temp=temp.next
        if list1ptr:
            temp.next=list1ptr
        else:
            temp.next=list2ptr
        
        return head
                



        

        