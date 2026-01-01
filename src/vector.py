from typing import Any

class Vector:
    def __init__(self):
        self._size = 0
        self._cap = 1
        self.vector = [None] * self._cap

    def _reallocate(self) -> None:
        new_cap = self._cap*2
        new_vector = [None] * new_cap

        for i in range(self._size):
            new_vector[i] = self.vector[i]

        self.vector = new_vector
        self._cap = new_cap

    def push_back(self, value: Any) -> None:
        if self._size == self._cap:
            self._reallocate()
        self.vector[self._size] = value
        self._size += 1

    def insert(self, index: int, value: Any) -> None:
        if 0 <= index <= self._size:
            if self._cap - self._size <= 1 :
                self._reallocate()
            for i in range(self._size, index, -1):
                self.vector[i] = self.vector[i - 1]
            self.vector[index] = value
            self._size += 1
        else:
            raise IndexError("Index out of range")
        
    def resize(self, new_size: int) -> None:
        if self._size > new_size:
            for _ in range(self._size - new_size):
                self.pop_back()
        elif self._size < new_size:
            while new_size > self._cap:
                self._reallocate()
            for i in range(self._size, new_size):
                self.vector[i] = None
            self._size = new_size
                
    def erase(self, index: int) -> None:
        if 0 <= index < self._size:

            for i in range(index+1, self._size):
                self.vector[i-1] = self.vector[i]

            self._size -=1
            self.vector[self._size] = None
        else:
            raise IndexError("Index out of range")
        
    def erase_range(self, start: int, end:int) -> None:
        count = end - start
        
        for i in range(start, self._size - count):
            self.vector[i] = self.vector[i + count]

        for i in range(self._size - count, self._size):
            self.vector[i] = None

        self._size -= count

    def front(self) -> Any:
        if not self.is_empty():
            return self.vector[0]
        else:
            raise IndexError("Can not get front element from empty vector")
    
    def back(self) -> Any:
        if not self.is_empty():
            return self.vector[self._size-1]
        else:
            raise IndexError("Can not get back element from empty vector")
        
    def pop_back(self) -> None:
        if not self.is_empty():
            self.vector[self._size-1] = None
            self._size-=1
        else:
            raise IndexError("Can not pop_back element from empty vector")
        
    def at(self, index:int) -> Any:
        if 0 <= index < self._size:
            return self.vector[index]
        else:
            raise IndexError("Index out of range")
        
    def size(self) -> int:
        return self._size
    
    def capacity(self) -> int:
        return self._cap
    
    def clear(self) -> None:
        self._size = 0
        self._cap = 1
        self.vector = [None] * self._cap
        
    def is_empty(self) -> bool:
        return self._size == 0