class MyCircularQueue:

    def __init__(self, k: int):
        self.q=[]
        self.max=k
    def enQueue(self, value: int) -> bool:
        if len(self.q)==max:
            return False
        if len(self.q)<self.max:
            self.q.append(value)
            return True
    def deQueue(self) -> bool:
        if len(self.q)==0:
            return False
        self.q.pop(0)
        return True

    def Front(self) -> int:
        if len(self.q)==0:
            return -1
        return self.q[0]
        

    def Rear(self) -> int:
        if len(self.q)>0:
            return self.q[-1]
        return -1
        

    def isEmpty(self) -> bool:
        if len(self.q)==0:
            return True
        

    def isFull(self) -> bool:
        if len(self.q)==self.max:
            return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()