class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[-1]*len(nums1)
        for i in range(len(nums1)):
            stack=[-1]
            for j in range(len(nums2)-1,-1,-1):
                if nums2[j]>nums1[i]:
                    stack.append(nums2[j])
                elif nums2[j]==nums1[i]:
                    ans[i]=stack[-1]
                    break
        return ans
        

                


        