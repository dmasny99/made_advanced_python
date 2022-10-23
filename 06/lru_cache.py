class LRUCache:

    def __init__(self, limit = 42):
        self.capacity = limit
        self.operation_counter = 0
        self.data_dict = {}
        self.order_dict = {}

    def get(self, key):
        if key not in self.data_dict:
            return
        elem = self.data_dict[key]
        self.operation_counter += 1
        self.order_dict[key] = self.operation_counter
        return elem

    def set(self, key, value):
        if key not in self.data_dict and \
                len(self.data_dict.keys()) == self.capacity:
            key_to_delete = min(self.order_dict, key = self.order_dict.get)
            del self.data_dict[key_to_delete]
            del self.order_dict[key_to_delete]
        self.data_dict[key] = value
        self.operation_counter += 1
        self.order_dict[key] = self.operation_counter
