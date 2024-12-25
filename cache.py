from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Простой рекурсивный вычислитель чисел Фибоначчи.
    Функция 'чистая': результат зависит только от n.
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30))        # Быстро получим результат, т.к. кэш сохраняет ранее вычисленное
print(fibonacci.cache_info())  
# cache_info() покажет статистику: количество хитов, промахов, размер кэша и т.д.


import requests

def api_memoize(func):
    cache = {}
    def wrapper(url):
        if url in cache:
            return cache[url]
        result = func(url)
        cache[url] = result
        return result
    return wrapper

@api_memoize
def get_json(url):
    print(f"Fetching from {url} ...")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

data1 = get_json("https://jsonplaceholder.typicode.com/todos/1")
data2 = get_json("https://jsonplaceholder.typicode.com/todos/1")  
# Второй раз запрос не уйдет в сеть, а возьмем из кэша


def fibonacci_iterative(n):
    """
    Итеративная версия Фибоначчи: для n >= 0.
    Возвращает n-е число Фибоначчи.
    """
    if n < 2:
        return n

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr