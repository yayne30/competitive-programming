class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(mid):
            summ = 0
            d = 1
            for w in weights:
                summ += w
                if summ > mid:
                    summ = w
                    d += 1
            return d <= days
                
        l = max(weights)
        r = sum(weights)
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            elif not check(mid):
                l = mid + 1
        return l

                
            

                
                    








        # low = max(weights)
        # high = sum(weights)
        # mid =  high - low
        # def check (mid):
        #     temp_day = 0
        #     summ = 0
        #     for w in weights:
        #         summ += w
        #         if summ > mid:
        #             summ = w
        #             temp_day += 1
        # while low < high:
        #     mid = (high - low) // 2
        #     if check(mid):
        #         high = mid - 1
        #     else:
        #         low = mid + 1
                
        # return mid 
        
        
        

            
            


        