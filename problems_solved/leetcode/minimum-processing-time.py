class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        processorTime.sort(reverse = True)
        tasks.sort()
        leng = len(processorTime)
        print(processorTime)
        print(tasks)
        maxx = 0
        tasind = 3
        k = len (tasks) % 4

        if len(tasks) <= 4:
            return processorTime[0] + tasks[len(tasks) - 1]
        else:
            for i in processorTime:
                maxx = max(maxx, i + tasks[tasind])
                tasind += 4
            if k != 0 :
                maxx = max (maxx, processorTime[leng - 1] + tasks[tasind + k])
            return maxx

                


           




        
        