class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        track = Counter(words)
        buckets = [[] for _ in range(len(words))]

        for item in track:
            buckets[track[item] - 1].append(item)
        ans = []
        for i in range( len(buckets) - 1 , -1 ,-1):
            if len(ans) < k:
                if len(buckets[i])>0:
                    buckets[i].sort()
                    # print(buckets[i])
                    ans.extend(buckets[i])
            else:
                break
        return ans[:k]


    

        
        