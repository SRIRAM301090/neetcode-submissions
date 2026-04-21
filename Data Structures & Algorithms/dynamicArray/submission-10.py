class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        if self.size > 0:
            return self.arr[i]

        raise ValueError("Index out of range")

    def set(self, i: int, n: int) -> None:
        if i < self.size:
            self.arr[i] = n
            return None
        
        raise ValueError("Index out of range")

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
        

    def popback(self) -> int:
        if self.size > 0:
            self.size -= 1
            return self.arr[self.size]
        raise ValueError("Cannot pop empty array")

    def resize(self) -> None:
        self.capacity *= 2
        newArr = [0] * self.capacity

        for idx in range(len(self.arr)):
            newArr[idx] = self.arr[idx]

        self.arr = newArr

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity
