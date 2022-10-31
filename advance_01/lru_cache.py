import logging
import logging.config
import argparse
from logger_configuration import log_conf
logging.config.dictConfig(log_conf)

class LRUCache:

    def __init__(self, stdout_logger = False, limit = 42):
        self.capacity = limit
        self.operation_counter = 0
        self.data_dict = {}
        self.order_dict = {}
        if stdout_logger:
            self.logger = logging.getLogger('file_and_stream_logger')
        else:
            self.logger = logging.getLogger('file_logger')
        self.logger.info('LRU Cache object created')
        if self.capacity <= 0:
            self.logger.critical('LRU Cache capacity = %s !', self.capacity)

    def get(self, key):
        if key not in self.data_dict:
            self.logger.warning('%s is not in keys', key)
            return
        elem = self.data_dict[key]
        self.operation_counter += 1
        self.order_dict[key] = self.operation_counter
        self.logger.info('%s is taken by key: %s', elem, key)
        return elem

    def set(self, key, value):
        if key not in self.data_dict and \
                len(self.data_dict.keys()) == self.capacity:
            key_to_delete = min(self.order_dict, key = self.order_dict.get)
            self.logger.warning('key: %s is going to be replaced', key_to_delete)
            del self.data_dict[key_to_delete]
            del self.order_dict[key_to_delete]
        self.data_dict[key] = value
        self.operation_counter += 1
        self.order_dict[key] = self.operation_counter
        self.logger.info('key: %s, value: %s are added', key, value)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action = 'store_true')
    args = parser.parse_args()

    lru = LRUCache(stdout_logger = args.s)

    lru.set(1, 'hello')
    lru.set(2, 'world')
    lru.set('test', 'case')

    lru.get('0')

    lru = LRUCache(stdout_logger = args.s, limit = 0)




