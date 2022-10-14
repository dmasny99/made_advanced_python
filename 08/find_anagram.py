from collections import defaultdict

def find_anagrams(text: str, pattern: str):
    res = []
    if pattern == '' or len(pattern) > len(text):
        return res
    pattern_dict = defaultdict(int)
    for el in pattern:
        pattern_dict[el] += 1
    l_ptr = 0
    while l_ptr <= len(text) - len(pattern):
        if l_ptr == 0:
            cur_dict = defaultdict(int)
            for i in range(len(pattern)):
                cur_dict[text[i]] += 1
        else:
            cur_dict[text[l_ptr + len(pattern) - 1]] += 1

        if cur_dict == pattern_dict:
            res.append(l_ptr)

        cur_dict[text[l_ptr]] -= 1
        if cur_dict[text[l_ptr]] == 0:
            del cur_dict[text[l_ptr]]
        l_ptr += 1

    return res

    