class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float(inf)
        for i in range(0 , len(blocks) - k + 1):
            j = i
            curr = 0
            while j < i + k and j < len(blocks):
                if blocks[j] == 'W':
                    curr += 1
                j += 1
            ans = min (ans , curr)
        return ans


        

        