class CustomList(list):
    
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

    def __radd__(self, lst):
        return self.__add__(lst)
    
    def __sub__(self, lst):
        lst = [-elem for elem in lst]
        return self.__add__(lst)
    
    def __rsub__(self, lst):
        # возможно коряво, по-другому не додумался 
        tmp = CustomList([-elem for elem in self])
        return tmp.__add__(lst)
    
    def __eq__(self, lst):
        return sum(self) == sum(lst)
    
    def __ne__(self, lst):
        return sum(self) != sum(lst)

    def __le__(self, lst):
        return sum(self) <= sum(lst) 
    
    def __lt__(self, lst):
        return sum(self) < sum(lst) 

    def __ge__(self, lst):
        return sum(self) >= sum(lst) 
    
    def __gt__(self, lst):
        return sum(self) > sum(lst) 

    def __str__(self):
        summ = 0
        string = ''
        for elem in self:
            string += f'{elem} '
            summ += float(elem) # в предположении, что могут быть только числа (не обязательно целые)
        string += f'sum is {summ}'
        return string 
    

