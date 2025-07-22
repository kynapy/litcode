# 146 https://leetcode.com/problems/lru-cache/description/
# Attempts: 2

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity
        self.current_size = 0
        self.tracker = {}
        self.current_use = 1

    def get(self, key: int) -> int:
        if key in self.cache:
            self.tracker[key] = self.current_use
            self.current_use += 1
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.tracker[key] = self.current_use
            self.current_use += 1
        else:
            if self.current_size < self.capacity:
                # Within capacity
                self.cache[key] = value
                self.tracker[key] = self.current_use
                self.current_use += 1
                self.current_size += 1
            else:
                # Exceed capacity
                minimum_use = float('inf')
                lru_key = 0
                for curr_key, use in self.tracker.items():
                    if use < minimum_use:
                        minimum_use = use
                        lru_key = curr_key
                
                del self.cache[lru_key]
                del self.tracker[lru_key]

                self.cache[key] = value
                self.tracker[key] = self.current_use
                self.current_use += 1
                
### TEST CASES ### 
cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))
