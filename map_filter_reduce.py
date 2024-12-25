numbers = [1, 2, 3, 4, 5, 6]

# Используем filter для отбора чётных чисел
even_numbers = filter(lambda x: x % 2 == 0, numbers)  
# Используем map, чтобы возвести каждое число в квадрат
squares = map(lambda x: x**2, even_numbers)

print(list(squares))  # [4, 16, 36]


from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_numbers = reduce(lambda acc, x: acc + x, numbers, 0)
print(sum_numbers)  # 15



import itertools

numbers = range(1_000_000)  # Много чисел

# 1) Пропускаем первые 5
stream = itertools.islice(numbers, 5, None)

# 2) Берём следующие 10
stream = itertools.islice(stream, 10)

# 3) Возводим в квадрат (не создавая новый список)
stream = map(lambda x: x*x, stream)

# 4) Фильтрация
stream = filter(lambda x: x > 200, stream)

# Сразу выводим
for value in stream:
    print(value)
