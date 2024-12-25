import time
from functools import lru_cache, wraps

def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__}({args}, {kwargs}) took {elapsed:.4f}s")
        return result
    return wrapper

def check_positive_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if any(a < 0 for a in args if isinstance(a, (int, float))):
            raise ValueError("Negative argument not allowed")
        return func(*args, **kwargs)
    return wrapper

@log_time
@lru_cache(None)
@check_positive_args
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(30))
print(fib(31))
