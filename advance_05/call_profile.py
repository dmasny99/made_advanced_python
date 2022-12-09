import click
from classes import Human, HumanSlots, HumanWeakref
from profile_deco import profile_deco, run_example


Adam = Human("male", 20, 80, None)
Eve = Human("female", 20, 60, None)
params = {"sex": "male",
          "age": 20,
          "weight": 80,
          "parent": Adam}


@profile_deco
def create_obj(cls):
    return cls(**params)


@profile_deco
def get_attr(obj):
    return obj.parent


@profile_deco
def change_attr(obj):
    obj.parent = Eve


@profile_deco
def delete_attr(obj):
    delattr(obj, "parent")


@click.command()
@click.option("--class_type")
@click.option("--num_iter")
def run_profile(class_type, num_iter):
    num_iter = int(num_iter)
    for _ in range(num_iter):
        if class_type == "human":
            obj = create_obj(Human)
        elif class_type == "human slots":
            obj = create_obj(HumanSlots)
        elif class_type == "human wref":
            obj = create_obj(HumanWeakref)
        get_attr(obj)
        change_attr(obj)
        delete_attr(obj)

    create_obj.print_stats()
    get_attr.print_stats()
    change_attr.print_stats()
    delete_attr.print_stats()


if __name__ == "__main__":
    run_profile()
