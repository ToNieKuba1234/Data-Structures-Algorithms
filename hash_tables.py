# This is a simple hash table that imitates basic
# functions of Python's native dict data structure
# Complete list of features:
# - Constructor (__init__):
# - put(key, value):
# - get(key):
# - delete(key): 
# - _hash(key): 
# - __repr__(): 
class MyHashTable:
    def __init__(self, size=10, *pairs):  #Take's size as an argument, and optional key-value pairs
        self.size = size
        self.buckets = [[] for _ in range(size)]

        for pair in pairs:
            if not isinstance(pair, (tuple, list)) or len(pair) != 2:
                raise ValueError(f"Each pair must be a tuple (key, value), got: {pair}")
            k, v = pair
            self.put(k, v)
    
    def _hash(self, key):  #simple hashing function that calculate bucket's index
        if not isinstance(key, (str, int, float, tuple)):
            raise TypeError("Key must be immutable (str, int, float, tuple)")
        return sum(ord(ch) for ch in str(key)) % self.size
    
    def put(self, key, value):  #adds or updates a key-value pair
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
    
    def get(self, key):  #returns a value by it's key
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v
        
        raise KeyError(f"Key not found: {key}")

    def delete(self, key):  #delete's a value by it's key
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
        
        raise KeyError(f"Key not found: {key}")
    
    def __repr__(self):
        return str(self.buckets)

#makes this run only if the script is runned by python hash_tables.py
if __name__ == "__main__":
    #constructor func
    myHashTable = MyHashTable(12, ("🍎", "Apple"), ("🍊", "Orange")) 

    
    #add func
    myHashTable.put("🍋", "Lemon")

    
    #reading value
    print(myHashTable.get("🍎"))
    print(myHashTable.get("🍋"))


    #updating value of existing key
    myHashTable.put("🍋", "Citrus")
    print(myHashTable.get("🍋"))


    #deleting value by key
    myHashTable.delete("🍊")
    print(myHashTable.get("🍊"))


    #displaying whole hash table
    print(myHashTable)