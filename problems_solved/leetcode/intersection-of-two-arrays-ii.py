class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        result=[]
        if len(nums1)<=len(nums2):
            cnt=Counter(nums2)
            for i in nums1:
                if cnt[i]>0:
                    result.append(i)
                    cnt[i]-=1

            
        elif len(nums1)>len(nums2):
            cnt=Counter(nums1)
            for i in nums2:
                if cnt[i]>0:
                    result.append(i)
                    cnt[i]-=1
                    
        return result



        