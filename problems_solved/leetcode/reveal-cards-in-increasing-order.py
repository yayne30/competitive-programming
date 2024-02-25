class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result=[0]*len(deck)
        deck.sort()
        q=deque(range(len(deck)))

        print(q)
        for i in deck:
            result[q.popleft()]=i
            if q:
                q.append(q.popleft())
        return result
        



        

        