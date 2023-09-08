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


arr = []
size1 = fill_matrix(arr)
print(arr)
# show_matrix(arr)
arr2 = []
size2 = fill_matrix(arr2)
print(arr2)
# show_matrix(arr2)
check_matrix_umn(size1[1],size2[0])