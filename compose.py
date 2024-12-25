def compose(*funcs):
    """
    Вернёт функцию, которая последовательно применяет функции из funcs,
    справа налево: compose(f, g)(x) = f(g(x)).
    """
    def inner(x):
        for f in reversed(funcs):
            x = f(x)
        return x
    return inner

def add_one(x):
    return x + 1

def double(x):
    return x * 2

pipeline = compose(add_one, double)
# pipeline(x) = add_one(double(x))

print(pipeline(3))  # Сначала double(3) = 6, потом add_one(6) = 7
