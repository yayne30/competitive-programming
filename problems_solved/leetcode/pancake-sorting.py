class Solution:
    def flip(self, arr, i):
        start = 0
        while start < i:
            arr[start] , arr[i] = arr[i], arr[start]
            start += 1
            i -= 1
    def pancakeSort(self, arr: List[int]) -> List[int]:
        num = len(arr)
        ans = []
        while num >= 1:
            ind = arr.index(num)
            if (ind + 1) != num:
                self.flip(arr, ind)
                ans.append(ind + 1)
                self.flip (arr , num-1)
                ans.append(num)
            num -= 1

        return ans


        