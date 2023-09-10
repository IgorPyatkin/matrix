

def show_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]}", end=' ')
        print()




def fill_matrix(matrix):
    print("Введите кол-во строк матрицы:")
    strok = int(input())

    print("Введите кол-во столбцов в матрице")
    stolb = int(input())
    for i in range(strok):
        print(f"Введите {i+1} строку")
        suj = []
        for j in range(stolb):
            suj.append(int(input()))
        matrix.append(suj)
    return [strok, stolb]

def check_matrix_umn(stolb1,strok2):
    if stolb1 != strok2:
        raise ArithmeticError("Несовместимае матрицы")


def umn_matrix(matrix1,matrix2):
    result = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for s in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[s][j] += matrix1[s][k] * matrix2[k][j]
    return result

def check_matrix():
    if rows_A != rows_B or cols_A != cols_B:
        raise ArithmeticError("Несовместимае матрицы")

def matrix_sum(matrix1,matrix2):
    result = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
           result[i][j] = matrix1[i][j] + matrix2[i][j]
    return result

def sub_matrix(matrix1,matrix2):
    result = [[0 for row in range(cols_B)] for col in range(rows_A)]
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
           result[i][j] = matrix1[i][j] - matrix2[i][j]
    return result


def cls():
    print("\n" * 43)


arr = []
size1 = fill_matrix(arr)
arr2 = []
size2 = fill_matrix(arr2)
rows_A = len(arr)
cols_A = len(arr[0])
rows_B = len(arr2)
cols_B = len(arr2[0])
cls()
print("Выберите арифметическую операцию:")
print("1)Умножение")
print("2)Сложение")
print("3)Вычетание")
str = int(input())
if str == 1:
    check_matrix_umn(size1[1], size2[0])
    result = umn_matrix(arr, arr2)
    print("Ответ:")
    show_matrix(result)
elif str == 2:
    check_matrix()
    result = matrix_sum(arr,arr2)
    print("Ответ:")
    show_matrix(result)
elif str == 3:
    check_matrix()
    result = sub_matrix(arr,arr2)
    print("Ответ:")
    show_matrix(result)
else:
    raise NameError("Такой операции не существует")





