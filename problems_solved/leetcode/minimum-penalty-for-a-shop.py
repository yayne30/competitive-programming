class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ty=customers.count('Y')
        tn=customers.count('N')
        cy=0
        cn=0
        result=+math.inf
        minind=0
        for j in range(len(customers)+1):
            if j!=len(customers):
                if customers[j]=='Y':
                    if result>cn+(ty-cy):
                        minind=j
                        result=cn+(ty-cy)
                    cy+=1
                elif customers[j]=='N':
                    if result>cn+(ty-cy):
                        minind=j
                        result=cn+(ty-cy)
                    cn+=1
            else:
                if result>cn+(ty-cy):
                    minind=j
                    result=cn+(ty-cy)
        return minind

                


        