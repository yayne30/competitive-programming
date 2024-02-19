class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        indice=defaultdict(list)
        for i, num in enumerate(nums):
            indice[num].append(i)
        for ind in indice.values():
            pre,suf=0,sum(ind)
            p,s=0,len(ind)
            for i in ind:
                pre+=i
                suf-=i
                p+=1
                s-=1
                result[i]=((i*p)-pre)+(suf-(i*s))
                

        return result

                

        return result






        