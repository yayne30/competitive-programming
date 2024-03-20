class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if x >= max(arr):
            return arr[n - k:]
        if x <= min(arr):
            return arr[0:k]

        start = 0
        end = n - k
        while start < end:
            mid = (start + end) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                print(abs(arr[mid] - x) ,abs(x - arr[mid + k]))
                print(x - arr[mid] , arr[mid + k] - x)
                print('#')
                end = mid
            else:
                start = mid + 1
        return arr[start : start + k]


            