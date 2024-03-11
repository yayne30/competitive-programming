class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def maxScore(left, right, turn):
            if left > right:
                return 0
            # player one's turn
            if turn:
                option1 = nums[left] + maxScore(left + 1, right, not turn)
                option2 = nums[right] + maxScore(left, right - 1, not turn)                
                return max(option1, option2)            
            # player two's turn            
            else:
                option1 = -nums[left] + maxScore(left + 1, right, not turn)            
                option2 = -nums[right] + maxScore(left, right - 1, not turn)
                return min(option1, option2)
        score = maxScore(0, len(nums) - 1, True)
        return score >= 0





















        # l=0
        # r=len(nums)-1
        # while l<r:
        #     p=0
        #     if r-l>2:
        #         if nums[r]>nums[l]:
        #             if nums[r-1]>nums[r]:
        #                 p+=nums[l]
        #                 l+=1
        #             else:
        #                 p+=nums[r]
        #                 r-=1
        #         else:
        #             if nums[l+1]>nums[l]:
        #                 p+=nums[r]
        #                 r-=1
        #             else:
        #                 p+=nums[l]
        #                 l+=1
        #     else:
        #         if nums[r]>=nums[l]:
        #             p+=nums[r]
        #             r-=1
        #         else:
        #             p+=nums[l]
        #             l+=1
        #     p=
        # return True







        