# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tort=head
        rabb=head
        check=False
        while tort and tort.next:
            tort=tort.next.next
            rabb=rabb.next
            if tort==rabb:
                check=True
                break
        return check
        