class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        leftcount = 0
        countdict = {}
        ans = []
        for i in range(len(nums) + 1):
            if i != 0 and nums[i-1] == 0:
                leftcount += 1
            countdict[i] = leftcount

        rightcount=0
        for j in range(len(nums)-1,-1,-1):
            if nums[j] == 1:
                rightcount += 1
            countdict[j] += rightcount
        sorted_dict = sorted(countdict.items(), key=lambda x:x[1])
        ans.append(sorted_dict[len(sorted_dict) - 1][0])
        for i in range(len(sorted_dict) - 2, -1 ,-1):
            if sorted_dict[i][1] == sorted_dict[len(sorted_dict) - 1][1]:
                ans.append(sorted_dict[i][0])
            else:
                break
        return ans


        
        


            

            





        