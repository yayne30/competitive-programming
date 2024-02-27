class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l=0
        r=0
        dictt={}         # to store the last index of each character
        count=0
        ans=[]
        for i in range(len(s)):
            dictt[s[i]]=i
        while l<len(s) and r<len(s):
            if dictt[s[l]]>r:
                r=dictt[s[l]]
            count+=1
            if l==r:
                ans.append(count)
                count=0
            l+=1
        return ans
        