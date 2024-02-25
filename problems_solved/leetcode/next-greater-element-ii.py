class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[-1]*n
        stack=[]
        for i in range(0,n*2):
            while stack and nums[stack[-1]]<nums[i%n]:
                t=stack.pop()
                result[t]=nums[i%n]
            stack.append(i%n)
        return result

                


        