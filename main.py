def find_largest_square(matrix):
    n = len(matrix)
    m = len(matrix[0])

    list = []
    for i in range(n):
        row = [0] * m
        list.append(row)

    max_size = 0
    max_i = 0
    max_j = 0

    # Начинаем проход по матрице
    for i in range(n):
        for j in range(m):
            # Для крайних элементов размер квадрата равен самому элементу
            if i == 0 or j == 0:
                list[i][j] = matrix[i][j]
            # Если элемент в матрице равен 1, ищем квадрат, содержащий текущий элемент
            elif matrix[i][j] == 1:
                list[i][j] = min(list[i - 1][j], list[i][j - 1], list[i - 1][j - 1]) + 1

            # Обновляем максимальный размер квадрата и его координаты
            if list[i][j] > max_size:
                max_size = list[i][j]
                max_i = i
                max_j = j

    return max_size, max_i - max_size + 1, max_j - max_size + 1


# 1. Выгружаем данные из файла
with open('test.txt', 'r') as file:
    matrix = [list(map(int, line.strip().split())) for line in file]
print(*matrix, sep="\n")

# 2. Вызываем функцию find_largest_square()
size, start_row, start_col = find_largest_square(matrix)

# 3. Объявляем и инициализируем переменные отвечающие за расположение
start_place = start_row, start_col
end_place = start_row + (size - 1), start_col + (size - 1)

# 4. Выводим полученные данные на экран
print("Размер самого большого квадрата из 1:", size)
print("Начало:", start_place)
print("Конец:", end_place)

# 5. Выводим найденный квадрат на экран
for i in range(start_row, start_row + size):
    for j in range(start_col, start_col + size):
        print(matrix[i][j], end=' ')
    print()
