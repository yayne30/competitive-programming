class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(l , r):
            if l > r:
                return -1
            mid = (r  + l) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                return binary(l , mid - 1)
            else:
                return binary( mid + 1 , r)

        return binary(0 ,len(nums) - 1)





        # if target not in nums:
        #     return -1
        # mid = len(nums) //  2 
        # if nums[mid] == target:
        #     return mid
        # elif target < nums[mid]:
        #     return self.search(nums[:mid] , target )
        # else:
        #     return self.search(nums[mid + 1 :], target)
       
    


        