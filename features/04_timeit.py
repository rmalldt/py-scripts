import timeit

mrange = range(100)


def gen_expr():
    result = ((x, x**2) for x in mrange)
    return result


def list_comp():
    result = [(x, x**2) for x in mrange]
    return result


def square(n):
    return (n, n**2)


def list_map():
    result = list(map(square, mrange))
    return result


print(
    f"Generator:\t {timeit.timeit(gen_expr, number=1000, globals=globals()):.6f}\t sec"
)

print(
    f"List Comp:\t {timeit.timeit(list_comp, number=1000, globals=globals()):.6f}\t sec"
)

print(
    f"List Map:\t {timeit.timeit(list_map, number=1000, globals=globals()):.6f}\t sec"
)
