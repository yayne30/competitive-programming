class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        left = 0 
        right = len(people) - 1
        boats = 0
        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit or left == right:
                boats += 1
                left += 1
                right -= 1
            elif people[left] + people[right] > limit:
                boats += 1
                right -= 1
               

        return boats
            

        