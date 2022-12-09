import time
import click
from classes import Human, HumanSlots, HumanWeakref


Adam = Human("male", 20, 80, None)
Eve = Human("female", 20, 60, None)
params = {"sex": "male",
          "age": 20,
          "weight": 80,
          "parent": Adam}


def create_obj(cls):
    return cls(**params)


def get_attr(obj):
    return obj.parent


def change_attr(obj):
    obj.parent = Eve


def delete_attr(obj):
    delattr(obj, "parent")


@click.command()
@click.option("--num_iter")
def measure_time(num_iter):
    num_iter = int(num_iter)
    for cls in [Human, HumanSlots, HumanWeakref]:
        print(f"\n Time of class: {cls.__name__}")

        start = time.time()
        objects = [create_obj(cls) for _ in range(num_iter)]
        print(f"\t\t Creation time: {time.time() - start}")

        start = time.time()
        _ = [get_attr(elem) for elem in objects]
        print(f"\t\t Get attribute time: {time.time() - start}")

        start = time.time()
        _ = [change_attr(elem) for elem in objects]
        print(f"\t\t Change attribute time: {time.time() - start}")

        start = time.time()
        _ = [delete_attr(elem) for elem in objects]
        print(f"\t\t Delete attribute time: {time.time() - start}")


if __name__ == "__main__":
    measure_time()
