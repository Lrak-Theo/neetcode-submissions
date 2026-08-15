class MyHashSet:

    def __init__(self):
        self.hashmap = []
        

    def add(self, key: int) -> None:
        if key in self.hashmap:
            return
        
        self.hashmap.append(key)
        

    def remove(self, key: int) -> None:
        if key not in self.hashmap:
            return

        self.hashmap.remove(key)        

    def contains(self, key: int) -> bool:
        if key not in self.hashmap:
            return False
        
        return True
    


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
''' where key is distinct (assume)'''