from cmath import isclose
import math

def get_closest_to_zero(nums):
    diff = math.inf
    closest_nums = []
    for number in nums:
        if abs(number) < diff:
            while len(closest_nums) > 0 :
                closest_nums.pop()
            diff = abs(number)
            closest_nums.append(number)
        elif math.isclose(abs(number), diff): # it is not stated explicitly that we work only with int
            closest_nums.append(number)
    return closest_nums


if __name__ == '__main__':
    assert get_closest_to_zero([]) == []
    assert get_closest_to_zero([8]) == [8] 
    assert get_closest_to_zero([-1, -2, 1, 0.5, 7]) == [0.5]
    assert get_closest_to_zero([-5, 9, 6, -8]) == [-5]
    assert get_closest_to_zero([-1, 2, -5, 1, -1]) == [-1, 1, -1]
