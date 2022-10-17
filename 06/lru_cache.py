class LRUCache:

    def __init__(self, limit = 42):
        self.capacity = limit
        self.data_dict = {}
        self.keys = []
        
    def get(self, key):
        if key not in self.keys:
            return -1
        elem = self.data_dict[key]
        self.keys.remove(key)
        self.keys.append(key)
        return elem
        
    def set(self, key, value):
        if key not in self.keys and len(self.data_dict.keys()) == self.capacity:
            key_to_delete = self.keys.pop(0)
            del self.data_dict[key_to_delete]
        if key in self.keys:
            self.keys.remove(key)
        self.data_dict[key] = value
        self.keys.append(key)
