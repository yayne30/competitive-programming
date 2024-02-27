class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ttl=0
        refund=[]
        rttl=0
        for i in costs:
            ttl+=i[0]
            refund.append(i[1]-i[0])
        refund.sort()
        for i in range(len(costs)//2):
            ttl+=refund[i]
        return ttl
            

