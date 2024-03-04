class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dictt = {}
        ans = 0
        # nums.sort()
        # print ( nums )
        for i in nums:
            dictt[i] = dictt.get(i, 0) + 1
        print(dictt)
        for i in nums:
            if k - i in dictt and dictt[k - i] > 0 and dictt[i] > 0:
                if k - i == i and dictt[k - i]< 2:
                    continue
                dictt[i] -= 1
                dictt[k - i] -= 1
                ans += 1
        
        return ans
        
        
        