class Pipe:
    """Обёртка, которая даёт возможность "прокидывать" данные через методы с помощью `|`."""
    def __init__(self, func):
        self.func = func

    def __ror__(self, other):
        """Переопределяем оператор `|` (right or). 
           Так что (value | self) = self.func(value)."""
        return self.func(other)

# Пример функции высшего порядка, обёрнутой в Pipe
@Pipe
def filter_even(iterable):
    return filter(lambda x: x % 2 == 0, iterable)

@Pipe
def square(iterable):
    return map(lambda x: x*x, iterable)

@Pipe
def take(n):
    """Вернём функцию, которая возьмёт первые n элементов итератора."""
    def _take(iterable):
        from itertools import islice
        return list(islice(iterable, n))
    return _take

# Теперь мы можем «складывать» вызовы в цепочку через `|`
numbers = range(1, 100)

result = numbers | filter_even | square | take(5)
print(result)  # [4, 16, 36, 64, 100]
