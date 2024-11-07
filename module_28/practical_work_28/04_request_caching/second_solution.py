class LRUCache:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self._cache = [None] * self.capacity
        self.queue = []

    
    def _hash_function(self, key):
        return hash(key) % self.capacity


    def _quadr_probing(self, key):
        hash_value = self._hash_function(key)
        start = hash_value
        i = 1

        while (self._cache[hash_value] is not None and
                self._cache[hash_value][0] != key):
            hash_value = (start + i ** 2) % self.capacity
            i += 1
            if i > self.capacity:
                raise Exception('Хеш таблица переполненна!')
            
        return hash_value


    def get(self, key):
        hash_value = self._quadr_probing(key)
        # print(self._cache[hash_value])

        if (self._cache[hash_value] is not None and
                self._cache[hash_value][0] == key):
            self.queue.remove(hash_value)
            self.queue.insert(0, hash_value)
            return self._cache[hash_value][1]
        
        return -1


    @property
    def cache(self):
        return self._cache


    @cache.setter
    def cache(self, key_value):
        key, value = key_value

        if len(self.queue) >= self.capacity:
            old_key = self.queue.pop()
            self._cache[old_key] = None

        hash_value = self._quadr_probing(key)

        if (self._cache[hash_value] is not None and
                self._cache[hash_value][0] == key):
            self._cache[hash_value] = (key, value)
            self.queue.remove(hash_value)
            self.queue.insert(0, hash_value)
            return
        else:
            self._cache[hash_value] = (key, value)
            self.queue.insert(0, hash_value)


    def print_cache(self):
        print('LRU Cache:')
        for key, val in self._cache:
            print(f'{key} : {val}')
    

cache = LRUCache()

cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

cache.print_cache()

print(cache.get("key2"))

cache.cache = ("key4", "value4")

cache.print_cache()
