import time
from collections import defaultdict
import math

NUM_OF_POPS = defaultdict(int) # for asserts
MEAN_TIME = {}

def mean(k):
    statistic = []
    def _mean(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            working_time = time.time() - start_time
            statistic.append(working_time)
            if len(statistic) > k:
                statistic.pop(0)
                # for asserts
                #global NUM_OF_POPS pylint орал на эту строчку, поправил как тут сказано 
                # https://pylint.pycqa.org/en/latest/user_guide/messages/warning/global-variable-not-assigned.html
                NUM_OF_POPS[func.__name__] += 1
            print(f'Mean time over {k} last iterations for function {func.__name__}: \
                {sum(statistic) / len(statistic)}')
            MEAN_TIME[func.__name__] = sum(statistic) / len(statistic) # for asserts
            return res
        return wrapper
    return _mean

@mean(k = 2)
def function1(arg1):
    time.sleep(0.2)

@mean(k = 3)
def function2(arg1):
    time.sleep(0.4)


if __name__ == '__main__':
    NUM_OF_POPS = defaultdict(int) # for asserts
    for _ in range(5):
        function1('test 1')
    assert NUM_OF_POPS['function1'] == 3

    for _ in range(3):
        function2('test 2')
    assert NUM_OF_POPS['function2'] == 0

    for _ in range(5):
        function1('test 3')
    assert math.isclose(MEAN_TIME['function1'], 0.2, rel_tol = 3e-2)

    for _ in range(3):
        function1('test 4')
    assert math.isclose(MEAN_TIME['function2'], 0.4, rel_tol = 3e-2)