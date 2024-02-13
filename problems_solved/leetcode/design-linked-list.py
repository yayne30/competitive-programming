class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        count = 0
        current = self.head
        while index > 0 and current:
            current = current.next
            index -= 1
        if current:
            return current.value
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = Node(val)
            return
        currNode = self.head
        while currNode.next:
            currNode = currNode.next
        currNode.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        dummyNode = Node(0)
        dummyNode.next = self.head
        current = dummyNode
        while index > 0 and current:
            current = current.next
            index -= 1
        if not current:
            return
        newNode = Node(val)
        newNode.next = current.next
        current.next = newNode
        self.head = dummyNode.next

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return
        dummyNode = Node(0)
        dummyNode.next = self.head
        current = dummyNode
        while index > 0 and current.next:
            current = current.next
            index -= 1
        if not current.next:
            return
        current.next = current.next.next
        self.head = dummyNode.next
            



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)