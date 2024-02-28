class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num=numbers
        l=0
        r=len(num)-1
        ans=[0]*2
        while l!=r  and r>=0 and l<len(num)-1:
            if num[l]+num[r]==target:
                ans[0]=l+1
                ans[1]=r+1
                break
            elif num[l]+num[r]>target:
                r-=1
            else:
                l+=1
        return ans

        