import timeit
from traceback import print_tb


def gen_expr():
    result = "-".join(str(n) for n in range(100))
    return result


def list_comp():
    result = "-".join([str(n) for n in range(100)])
    return result


print(f"Generator:\t {timeit.timeit(gen_expr, number=1000):.6f}\t sec")
print(f"List Comp:\t {timeit.timeit(list_comp, number=1000):.6f}\t sec")
