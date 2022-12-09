import click
from memory_profiler import profile
from classes import Human, HumanSlots, HumanWeakref


Adam = Human("male", 20, 80, None)
Eve = Human("female", 20, 60, None)
params = {"sex": "male",
          "age": 20,
          "weight": 80,
          "parent": Adam}


@profile
def create_obj(cls, num_iter):
    return [cls(**params) for _ in range(num_iter)]


@click.command()
@click.option("--num_iter")
def run_mem_profile(num_iter):
    num_iter = int(num_iter)
    for cls in [Human, HumanSlots, HumanWeakref]:
        print(f"Class name: {cls.__name__}")
        obj = create_obj(cls, num_iter)
        del obj


if __name__ == "__main__":
    run_mem_profile()
