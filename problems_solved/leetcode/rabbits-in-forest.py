class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dicti=defaultdict(int)
        minrab=0
        for i in range(len(answers)):
            dicti[answers[i]]+=1

        for j in dicti:
            minrab+=((j+1)*(math.ceil((dicti[j])/(j+1))))
        return minrab






        