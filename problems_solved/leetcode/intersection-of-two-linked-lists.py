# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dictt=set()
        temp=headA
        while temp!=None:
            dictt.add(temp)
            temp=temp.next

        temp=headB
        while temp!=None:
            if temp in dictt:
                return temp
            temp=temp.next
        return None

        