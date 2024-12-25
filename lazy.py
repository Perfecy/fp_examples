import itertools

def lines_with_error(file_path):
    """Генератор, yielding строки, где есть 'ERROR'."""
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            if "ERROR" in line:
                yield line.strip()

def main():
    lines = lines_with_error("data.txt")  # ленивое чтение
    first_five = itertools.islice(lines, 5)  
    upper_lines = map(str.upper, first_five)  # ленивое преобразование

    for line in upper_lines:
        print(line)

if __name__ == "__main__":
    main()

# Функция-генератор lines_with_error построчно выдаёт (yield) только строки с "ERROR". Мы не храним весь файл целиком.
# itertools.islice(lines, 5) берёт первые 5 таких строк (запрос идёт «на лету»).
# map(str.upper, ...) снова всё делает лениво.
# Таким образом, мы читаем файл до тех пор, пока не найдём 5 строк с «ERROR». Дальше чтение не происходит.




def main_imperative():
    with open("data.txt", encoding="utf-8") as f:
        lines = f.readlines()  # Считываем весь файл в список (память!)
    lines_with_error = []
    for line in lines:
        if "ERROR" in line:
            lines_with_error.append(line.strip())
    # Берём первые 5 
    first_five = lines_with_error[:5]
    # Делаем их верхним регистром
    upper_lines = [line.upper() for line in first_five]
    # Вывод
    for line in upper_lines:
        print(line)

if __name__ == "__main__":
    main_imperative()

# Мы сначала загружаем весь файл в память (f.readlines()).
# Даже если в файле гигантское число строк, или если «ERROR» встречается в самом начале, мы всё равно читаем файл до конца.
# Храним все найденные строки в lines_with_error, и только затем берём из них 5.
# Промежуточные структуры тратят память и время без необходимости.