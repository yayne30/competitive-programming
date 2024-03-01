class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        sett = {'a', 'e', 'i', 'o', 'u'}
        ans=0
        print(len(s))
        
        currvow = 0
        for i in range(k):
            if s[i]  in sett:
                currvow += 1
        if currvow == len(s):
            return currvow
        
        left = 1
        right = k
        while right < len(s):
            print(currvow)
            if s[left-1] in sett and s[right] not in sett:
                nextvow = currvow-1
            elif s[left-1] not in sett and s[right] in sett:
                nextvow = currvow + 1
            else:
                nextvow = currvow
            left += 1
            right += 1   
            ans = max( ans, nextvow, currvow) 
            currvow= nextvow      

        return ans      


        

        # sett = {'a', 'e', 'i', 'o', 'u'}
        # left = 0
        # ans=0
        # for i in range(len(s)-k+1):
        #     vowel = 0
        #     start = i
        #     ind = i
        #     while ind - start < k:
        #         if s[ind] in sett:
        #             vowel += 1
        #         ind+=1
        #     ans = max(ans, vowel)

        # return ans
        