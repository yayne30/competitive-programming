class Node:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr=Node(homepage)
        
    def visit(self, url: str) -> None:
        self.curr.next=Node(url,prev=self.curr)
        self.curr=self.curr.next
        return self.curr.val
    def back(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.prev:
                break
            self.curr=self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.curr.next:
                break
            self.curr=self.curr.next
        return self.curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)