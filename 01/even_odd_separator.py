def even_odd_separator(nums):
    even = []
    odd = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return (even, odd)


if __name__ == '__main__':
    assert even_odd_separator([0, 1, 2, 3, 4, 5, 6]) == ([0, 2, 4, 6], [1, 3, 5])
    assert even_odd_separator([0]) == ([0], [])
    assert even_odd_separator([]) == ([], [])
