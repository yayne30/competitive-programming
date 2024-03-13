class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Optimized Solution
        n_fi = len(firstList)
        n_se = len(secondList)
        ans = []
        f = 0
        s = 0
        while f < n_fi and s < n_se:
            curr_left = max(firstList[f][0] , secondList[s][0])
            curr_right = min(firstList[f][1] , secondList[s][1])
            if curr_left <= curr_right:
                ans.append([curr_left , curr_right])
            if firstList[f][1] < secondList[s][1]:
                f += 1
            else: 
                s += 1 

        return ans
            




        #bruteforce solution 
        # n_fi = len(firstList)
        # n_se = len(secondList)
        # ans = []
        # for i in range(n_fi):
        #     mini = firstList[i][0]
        #     maxi = firstList[i][1]
        #     for j in range(n_se):
        #         minj = secondList[j][0]
        #         maxj = secondList[j][1]

        #         curr_left = max(mini , minj)
        #         curr_right = min(maxi , maxj)

        #         if curr_right >= curr_left:
        #             ans.append([curr_left , curr_right])
        #         else:
        #             if curr_left == minj:
        #                 break
        # return ans




        
        