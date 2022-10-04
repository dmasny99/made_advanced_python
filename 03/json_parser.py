import json 
from collections import defaultdict

def callback(storage, field):
    storage[field] += 1
   
def parse_json(json_str: str, required_fields = None, keywords = None, keyword_callback = None):
    if json_str is None or required_fields is None or keywords is None:
        print('Invalid input')
        return None
    json_doc = json.loads(json_str)
    statistic = defaultdict(int)
    for field in required_fields:
        if field in json_doc.keys():
            words = json_doc[field].split()
            for word in words:
                if word in keywords:
                    keyword_callback(statistic, field)
    return statistic

if __name__ == '__main__':
    assert parse_json(json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}',
                      required_fields = ["key1"], keywords = ["word2"],
                      keyword_callback = callback) == {'key1': 1}

    assert parse_json(json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}',
                      keyword_callback = callback) is None
                    
    assert parse_json(json_str = '{"key1": "word word word2", "key2": "word word1 word3"}',
                      required_fields = ["key1", "key2"], keywords = ["word"],
                      keyword_callback = callback) == {'key1': 2, 'key2': 1}

    assert parse_json(json_str = None,
                      required_fields = ["key1", "key2"], keywords = ["word"],
                      keyword_callback = callback) is None
