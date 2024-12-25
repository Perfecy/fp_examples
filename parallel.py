import math
from multiprocessing import Pool

def heavy_computation(x):
    # Эмулируем что-то ресурсоёмкое, например, математику
    return math.factorial(x) % 123456789

numbers = [10_000 + i for i in range(20)]  # Пример: 20 больших чисел

if __name__ == "__main__":
    with Pool() as pool:
        # pool.map - это функциональный способ "распараллелить map"
        results = pool.map(heavy_computation, numbers)
    print(results)
