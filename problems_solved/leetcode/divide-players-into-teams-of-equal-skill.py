class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        start, end , product = 1, len(skill) - 2, 0
        currsum=skill[0]+skill[len(skill)-1]
        product += (skill[0]*skill[len(skill)-1])

        while start < end:

            currpro = skill[start] * skill[end]
            if currsum == (skill[start] + skill[end]):
                start += 1
                end -= 1
                print(currpro) 

                product += currpro
                
            else:
                return -1

        return product

            




        