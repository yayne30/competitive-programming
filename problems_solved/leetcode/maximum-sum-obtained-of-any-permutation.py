class Solution:
    def maxSumRangeQuery(self, nums: List[int], request: List[List[int]]) -> int:
        prefix_array=[0]*len(nums)
        max_sum=0
        for i in range(len(request)):
            prefix_array[request[i][0]]+=1
            if request[i][1]<len(nums)-1:
                prefix_array[request[i][1]+1]-=1
        for j in range (1,len(nums)):
            prefix_array[j]+=prefix_array[j-1]
        prefix_array.sort()
        nums.sort()
        n=1e9+7
        for i in range(len(nums)):
            max_sum+=(prefix_array[i]*nums[i])%n
            max_sum%=n
        return int(max_sum)


            

       
      
        



        