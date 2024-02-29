class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        nums_set=set(nums)
        i=0
        
        print(sorted(nums_set))
        for j in sorted(nums_set):
            nums[i]=j
            i+=1
        
        return len(nums_set)
        