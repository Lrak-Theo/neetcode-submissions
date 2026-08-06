class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.classArray = []

    def get(self, i: int) -> int:
        return self.classArray[i]

    def set(self, i: int, n: int) -> None:
        self.classArray[i] = n

    def resize(self) -> None:
        self.capacity = self.capacity*2

    def pushback(self, n: int) -> None:
        if len(self.classArray) == self.capacity:
            self.resize()

        self.classArray.append(n)

    def popback(self) -> int:
        return self.classArray.pop()

    def getSize(self) -> int:
        return len(self.classArray)
    
    def getCapacity(self) -> int:
        return self.capacity