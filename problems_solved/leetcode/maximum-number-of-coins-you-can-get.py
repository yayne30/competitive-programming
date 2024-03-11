class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        length = len(piles)
        ans = 0
        cnt = 0
        for i in range(length - 2, (length // 3) - 1 , -2 ):
            ans += piles[i]
      

        return ans

        