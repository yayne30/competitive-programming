class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dictt = {}
        ans = []
        for i in range(len(names)):
            dictt[i] = heights[i]
        key_sort = sorted(dictt.items(), key = lambda x : x[1], reverse = True)

        for i in key_sort:
            ans.append(names[i[0]])
        

        return ans
        