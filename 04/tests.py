from email.utils import collapse_rfc2231_value
from CustomList import CustomList

if __name__ == '__main__':
    # проверка выврода
    assert CustomList([1, 2, 3]).__str__() == '1 2 3 sum is 6.0'

    # проверка сравнений
    assert CustomList([1, 2, 3]) == CustomList([6])
    assert CustomList([1, 2, 3]) > CustomList([5])
    assert CustomList([1, 2, 3]) >= CustomList([6])
    assert CustomList([1, 2, 3]) < CustomList([9])
    assert CustomList([1, 2, 3]) <= CustomList([6])

    # проверка на корректный расчет значений
    tmp = CustomList([1, 2, 3, 4, 5]) + CustomList([1, 2, 3])
    res = CustomList([2, 4, 6, 4, 5])
    assert len(res) == 5
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]

    tmp = CustomList([1, 2, 3]) + CustomList([1, 2, 3, 4, 5]) 
    res = CustomList([2, 4, 6, 4, 5])
    assert len(res) == 5
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]

    tmp = CustomList([1, 2, 3]) - CustomList([1, 2, 3, 4, 5])
    res = CustomList([0, 0, 0, -4, -5])
    assert len(res) == 5
    for idx, elem in enumerate(tmp):
        assert elem == res[idx] 

    tmp = CustomList([1, 2, 3, 4, 5]) - CustomList([1, 2, 3]) 
    res = CustomList([0, 0, 0, 4, 5])
    assert len(res) == 5
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]

    tmp = [1, 2, 3] - CustomList([3, 3, 3, 3])
    res = CustomList([-2, -1, 0, -3])
    assert len(res) == 4
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]
    
    tmp = [1, 2, 3] + CustomList([3, 3, 3, 3])
    res = CustomList([4, 5, 6, 3])
    assert len(res) == 4
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]
    
    tmp = CustomList([3, 3]) + [1, 2, 3]
    res = CustomList([4, 5, 3])
    assert len(res) == 3
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]

    tmp = CustomList([3, 3]) - [1, 2, 3]
    res = CustomList([2, 1, -3])
    assert len(res) == 3
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]

    ### проверка на создание нового объекта
    cl1 = CustomList([1, 2, 3, 4, 5])
    cl2 = CustomList([1, 2, 3])
    tmp = cl1 + cl2
    assert (id(cl1) != id(tmp)) and (id(cl2) != id(tmp))

    cl1 = CustomList([1, 2, 3, 4, 5])
    cl2 = CustomList([1, 2, 3])
    tmp = cl1 - cl2
    assert (id(cl1) != id(tmp)) and (id(cl2) != id(tmp))

    cl1 = CustomList([1, 2, 3, 4, 5])
    cl2 = CustomList([1, 2, 3])
    tmp = cl2 + cl1
    assert (id(cl1) != id(tmp)) and (id(cl2) != id(tmp))

    cl1 = CustomList([1, 2, 3, 4, 5])
    cl2 = CustomList([1, 2, 3])
    tmp = cl2 - cl1
    assert (id(cl1) != id(tmp)) and (id(cl2) != id(tmp))

    cl1 = CustomList([3, 3])
    l2 = [1, 2, 3]
    tmp = cl1 - l2
    assert (id(cl1) != id(tmp)) and (id(l2) != id(tmp))

    cl1 = CustomList([3, 3])
    l2 = [1, 2, 3]
    tmp = cl1 + l2
    assert (id(cl1) != id(tmp)) and (id(l2) != id(tmp))

    cl1 = CustomList([3, 3])
    l2 = [1, 2, 3]
    tmp = l2 + cl1
    assert (id(cl1) != id(tmp)) and (id(l2) != id(tmp))

    cl1 = CustomList([3, 3])
    l2 = [1, 2, 3]
    tmp = l2 - cl1
    assert (id(cl1) != id(tmp)) and (id(l2) != id(tmp))

    # проверка, что новый объект это Custom list
    tmp = CustomList([1, 2, 3]) - CustomList([1, 2, 3, 4, 5])
    assert isinstance(tmp, CustomList)
    tmp = CustomList([1, 2, 3]) + CustomList([1, 2, 3, 4, 5])
    assert isinstance(tmp, CustomList)
    tmp = [1, 2, 3] - CustomList([3, 3, 3, 3])
    assert isinstance(tmp, CustomList)
    tmp = [1, 2, 3] + CustomList([3, 3, 3, 3])
    assert isinstance(tmp, CustomList)
    tmp = CustomList([3, 3, 3, 3]) + [1, 2, 3]
    assert isinstance(tmp, CustomList)
    tmp = CustomList([3, 3, 3, 3]) - [1, 2, 3]
    assert isinstance(tmp, CustomList)

    #проверка что исходные объекты не меняются
    cl1 = CustomList([1, 2, 3])
    cl2 = CustomList([1, 2, 3, 4, 5])
    tmp = cl1 + cl2
    assert cl1 == CustomList([1, 2, 3])
    assert cl2 == CustomList([1, 2, 3, 4, 5])

    cl1 = CustomList([1, 2, 3])
    cl2 = CustomList([1, 2, 3, 4, 5])
    tmp = cl1 - cl2
    assert cl1 == CustomList([1, 2, 3])
    assert cl2 == CustomList([1, 2, 3, 4, 5])
    
    l1 = [1, 2, 3]
    cl2 = CustomList([1, 2, 3, 4, 5])
    tmp = l1 + cl2
    assert l1 == [1, 2, 3]
    assert cl2 == CustomList([1, 2, 3, 4, 5])

    l1 = [1, 2, 3]
    cl2 = CustomList([1, 2, 3, 4, 5])
    tmp = l1 - cl2
    assert l1 == [1, 2, 3]
    assert cl2 == CustomList([1, 2, 3, 4, 5])

    l1 = [1, 2, 3]
    cl2 = CustomList([1, 2, 3, 4, 5])
    tmp = cl2 - l1
    assert l1 == [1, 2, 3]
    assert cl2 == CustomList([1, 2, 3, 4, 5])

    l1 = [1, 2, 3]
    cl2 = CustomList([1, 2, 3, 4, 5])
    tmp = cl2 + l1
    assert l1 == [1, 2, 3]
    assert cl2 == CustomList([1, 2, 3, 4, 5])
