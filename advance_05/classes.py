import weakref


class Human:
    def __init__(self, sex, age, weight, parent):
        self.sex = sex
        self.age = age
        self.weight = weight
        self.parent = parent


class HumanSlots:
    __slots__ = [
        "sex",
        "age",
        "weight",
        "parent",
    ]

    def __init__(self, sex, age, weight, parent):
        self.sex = sex
        self.age = age
        self.weight = weight
        self.parent = parent


class HumanWeakref:
    def __init__(self, sex, age, weight, parent):
        self.sex = sex
        self.age = age
        self.weight = weight
        self.parent = weakref.ref(parent)
