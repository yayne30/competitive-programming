class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix_sum=[0]*1000
        for i in range(len(trips)):
           prefix_sum[trips[i][1]]+=trips[i][0]
           if trips[i][2]<1000:
               prefix_sum[trips[i][2]]-=trips[i][0]
        temp_sum=0
        for j in range(1000):
            temp_sum+=prefix_sum[j]
            if temp_sum>capacity:
                return False
        return True
