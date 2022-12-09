import cProfile
import io
import pstats


def profile_deco(func):
    profiler = cProfile.Profile()
    out = io.StringIO()

    def wrapper(*args):
        profiler.enable()
        res = func(*args)
        profiler.disable()
        return res

    def print_stats():
        p_stats = pstats.Stats(profiler, stream=out)
        p_stats.print_stats()
        print(out.getvalue())

    wrapper.print_stats = print_stats
    return wrapper


def run_example():

    @profile_deco
    def add(a, b):
        return a + b

    @profile_deco
    def sub(a, b):
        return a - b

    add(1, 2)
    add(4, 5)

    add.print_stats()


if __name__ == "__main__":
    run_example()
