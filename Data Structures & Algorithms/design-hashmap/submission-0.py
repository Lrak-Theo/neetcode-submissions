class MyHashMap:

    def __init__(self):
        self.hashmap = []
        self.keyvalue = []

    def put(self, key: int, value: int) -> None:
        x = 0
        while x <= len(self.hashmap)-1:
            if self.hashmap[x][0] == key: 
                self.hashmap[x][1] = value
                break
            else:
                x += 1

        # if no key exists yet then add it in the hashmap
        if x > len(self.hashmap) - 1:
            self.hashmap.append([key, value])       
        
    def get(self, key: int) -> int:
        x = 0
        while x <= len(self.hashmap)-1:
            if self.hashmap[x][0] == key: 
                return self.hashmap[x][1]
            else:
                x += 1
        
        # if no key exists then returrn -1
        if x > len(self.hashmap) - 1:
            return -1     
                

    def remove(self, key: int) -> None:
        for x in self.hashmap:
            if key == x[0]:
                self.hashmap.remove(x)
        
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)