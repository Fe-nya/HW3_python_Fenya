def IsSymmetric(A):
    r = len(A) # количество строк в матрице
    for i in range(r):   # перебираем строки матрицы
        for j in range(r):  # перебираем столбцы матрицы
            if A[i][j] != A[j][i]:
                return "NO"
    return "YES"  # если дошли до конца без прерывания, то матрица симметрична


n = int(input())
matrix = [] # создаем пустую матрицу
for _ in range(n):
    row = list(map(int, input().split()))  # вводим текущую строку матрицы и преобразуем её элементы в целые числа
    matrix.append(row)  # добавляем преобразованную строку в матрицу

print(IsSymmetric(matrix))
