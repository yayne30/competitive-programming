# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        length = 0
        result=[]
        while temp:
            length += 1
            temp = temp.next
        
        sub_len, rem = length // k, length % k
        curr=head
        for i in range(k):
            result.append(curr)
            
            for j in range((sub_len -1) + (1 if rem else 0)):
                
                if not curr:
                    break
                curr=curr.next
            rem -= (1 if rem else 0)
            if curr:
                curr.next, curr = None , curr.next
        return result


        
