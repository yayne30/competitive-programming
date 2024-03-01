class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        pg = 0
        ps = 0
        result=0
        g.sort()
        s.sort()

        while pg < len(g) and ps < len(s):

            if g[pg] <= s[ps]:
                result += 1
                pg += 1
                ps += 1
            elif g[pg] > s[ps]:
                ps+=1
        
        return result
                
            

        