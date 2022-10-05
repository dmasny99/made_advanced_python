from email.utils import collapse_rfc2231_value
from CustomList import CustomList

if __name__ == '__main__':
    # проверка выврода
    print(CustomList([1, 2, 3]))
    # проверка сравнений
    assert CustomList([1, 2, 3]) == CustomList([6])
    assert CustomList([1, 2, 3]) > CustomList([5])
    assert CustomList([1, 2, 3]) >= CustomList([6])
    assert CustomList([1, 2, 3]) < CustomList([9])
    assert CustomList([1, 2, 3]) <= CustomList([6])
    # проверка операций cl +- cl
    ## проверка на корректный расчет значений
    tmp = CustomList([1, 2, 3, 4, 5]) + CustomList([1, 2, 3])
    res = CustomList([2, 4, 6, 4, 5])
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]

    tmp = CustomList([1, 2, 3]) - CustomList([1, 2, 3, 4, 5])
    res = CustomList([0, 0, 0, -4, -5])
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]
    ### проверка на создание нового объекта
    cl1 = CustomList([1, 2, 3, 4, 5])
    cl2 = CustomList([1, 2, 3])
    tmp = cl1 + cl2
    assert (id(cl1) != id(tmp)) and (id(cl2) != id(tmp))
    #проверка на работу с обычным списком
    ## на правильность расчета элементов
    tmp = [1, 2, 3] - CustomList([3, 3, 3, 3])
    res = CustomList([-2, -1, 0, -3])
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]
    
    tmp = [1, 2, 3] + CustomList([3, 3, 3, 3])
    res = CustomList([4, 5, 6, 3])
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]
    
    tmp = CustomList([3, 3]) + [1, 2, 3]
    res = CustomList([4, 5, 3])
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]

    tmp = CustomList([3, 3]) - [1, 2, 3]
    res = CustomList([2, 1, -3])
    for idx, elem in enumerate(tmp):
        assert elem == res[idx]
    ## на то, что создается новый объект
    cl1 = CustomList([3, 3])
    l2 = [1, 2, 3]
    tmp = cl1 - l2
    assert (id(cl1) != id(tmp)) and (id(l2) != id(tmp))
    # проверка, что исходные объекты не меняются не делал, тк логика сложения 
    # построена не на добивке нулями