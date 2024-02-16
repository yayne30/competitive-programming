class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count=1
        minum=points[0][1]
        for i in range(1,len(points)):
            if points[i][0]<=minum:
                minum=min(minum,points[i][1])
            else:
                count+=1
                minum=points[i][1]
        return count




        

        