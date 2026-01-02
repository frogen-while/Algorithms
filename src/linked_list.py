from typing import Any, Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional["Node"] = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def push_back(self, value: Any) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size+=1

    def push_front(self, value: Any) -> None:
        if self.head is None:
            self.push_back(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            self._size+=1

    def pop_front(self) -> None:
        if self.head is None:
            raise IndexError("Can not pop_front from empty list")
        
        self.head = self.head.next
        self._size-=1

        if self.head is None:
            self.tail = None
    
    def pop_back(self) -> None:
        if self.head is None:
            raise IndexError("Can not pop_back from empty list")
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            curNode = self.head
            while curNode.next != self.tail:
                curNode = curNode.next
            curNode.next = None
            self.tail = curNode
        
        self._size -= 1

    def insert(self, index:int, value:Any) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
        else:

            if index == 0:
                self.push_front(value)
                return
            
            if index == self._size:
                self.push_back(value)
                return

            newNode = Node(value)
            curNode = self.head

            for _ in range(index-1):
                curNode = curNode.next
                
            newNode.next = curNode.next
            curNode.next = newNode
            self._size+=1

    def get(self, index:int) -> Any:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        else:
            curNode = self.head
            for _ in range(index):
                curNode = curNode.next
            return curNode.value
        
    def clear(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

    def erase(self, index: int) -> None:
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")
        else:
            if index == 0:
                self.pop_front()
                return
            elif index == self._size-1:
                self.pop_back()
                return
            else:
                curNode = self.head
                for _ in range(index-1):
                    curNode = curNode.next
                curNode.next = curNode.next.next
                self._size -= 1
