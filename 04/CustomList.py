class CustomList(list):

    def __init__(self, *args):
        list.__init__(self, *args)

    def __add__(self, lst):
        cl = CustomList()
        longest_list = self if len(self) > len(lst)  else lst
        min_l = min(len(self), len(lst)) - 1
        for i in range(len(longest_list)):
            if i <= min_l:
                cl.append(self[i] + lst[i])
            else:
                cl.append(longest_list[i])
        return cl

    def __sub__(self, lst):
        lst = [-elem for elem in lst]
        return CustomList.__add__(self, lst)
    
    def __eq__(self, lst):
        return sum(self) == sum(lst)
    
    def __ne__(self, lst):
        return sum(self) != sum(lst)

    def __le__(self, lst):
        return True if sum(self) <= sum(lst) else False
    
    def __lt__(self, lst):
        return True if sum(self) < sum(lst) else False

    def __ge__(self, lst):
        return True if sum(self) >= sum(lst) else False
    
    def __gt__(self, lst):
        return True if sum(self) > sum(lst) else False

if __name__ == '__main__':
   print(CustomList([1, 2, 3, 4, 5]) + CustomList([1, 2, 3]))
   print(CustomList([1, 2, 3]) - CustomList([1, 2, 3, 4, 5]))
   print(CustomList([1, 2, 3]) == CustomList([6]))
   print(CustomList([1, 2, 3]) > CustomList([5]))
   print(CustomList([1, 2, 3]) >= CustomList([6]))
   print(CustomList([1, 2, 3]) < CustomList([9]))
   print(CustomList([1, 2, 3]) <= CustomList([6]))
   # TODO add summation with List
   # TODO add tests in a separated file


