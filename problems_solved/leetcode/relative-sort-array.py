class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        nums1 = []
        nums2 = []
        ans = []

        for i in arr1:
            if i in arr2:
                nums1.append(i)
            else:
                nums2.append(i)
        cnt = Counter(nums1)
        for i in arr2:
            ans += [i] * cnt[i]
        return ans + sorted(nums2)



        


 
        # ans = []
        # diff = [x for x in arr1 if x not in arr2]
        # for i in arr2:
        #     for _ in range(arr1.count(i)):
        #         ans.append(i)
            
        # diff.sort()


        # return ans + diff


        