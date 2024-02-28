class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        costsum=costs[0]
        count=0
        i=1
        if sum(costs)<=coins:
            return len(costs)
        while costsum<=coins and i<len(costs):
            costsum+=costs[i]
            i+=1
            count+=1
        return count
        