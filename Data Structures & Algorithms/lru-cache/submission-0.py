class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.lastUsed = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.lastUsed.remove(key)
            self.lastUsed.append(key)            
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache and self.size==self.capacity:
            lastkey = self.lastUsed.pop(0)
            self.cache.pop(lastkey)
            # self.lastUsed.append(key)
        elif key not in self.cache and self.size!=self.capacity:
            self.size+=1
            # self.lastUsed.append(key)
        # elif key in self.cache and self.size!=self.capacity:
        #     self.lastUsed.remove(key)
        else:
            self.lastUsed.remove(key)

        self.lastUsed.append(key)          
        self.cache[key] = value