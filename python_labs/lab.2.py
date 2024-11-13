import numpy as np


def enter_matrix(name):
    print(f'Введіть матрицю 3x3 {name} :')
    matrix = []
    i = 1
    while i <= 3:
        row = list(map(int, input(f'Введіть матрицю {i} рядок через пробіл {name} : ').split()))
        if len(row) != 3:
            print('В рядку має і може бути тільки 3 числа!!!!')
        else:
            matrix.append(row)
            i+=1
    if(name == 'A'):
        matrix_A = np.array(matrix)
        return matrix_A 
    if(name == 'B'):
        matrix_B = np.array(matrix)
        return matrix_B 
    print()

def summ_matrix():
    result_matrix = np.add(matrix_A, matrix_B)
    return result_matrix

def subtr_matrix():
    result_matrix = np.subtract(matrix_A, matrix_B)
    return result_matrix

def multiply_matrix():
    result_matrix = np.dot(matrix_A, matrix_B)
    return result_matrix
    
def multiply_byNumber_matrix(number,matrix):
    result_matrix = np.dot(matrix, number)
    return result_matrix

def show_matrix_result(operation):
    print(f'A {operation} B = C')
    print(matrix_A[0],'   ', matrix_B[0],'   ', matrix_C[0])
    print(matrix_A[1],f' {operation} ', matrix_B[1],' = ', matrix_C[1])
    print(matrix_A[2],'   ', matrix_B[2],'   ', matrix_C[2])

def show_matrix_result_by_mupltyply_number(number, matrix_name, matrix):
        print(f'{matrix_name} * {number} = C')
        print(matrix[0],'   ', f'{' ':<5}', matrix_C[0])
        print(matrix[1],' * ', f'{number:<1}',' = ', matrix_C[1])
        print(matrix[2],'   ', f'{' ':<5}', matrix_C[2])

matrix_A = enter_matrix('A')
matrix_B = enter_matrix('B')

print()
print('   A', '       ', '  B')
print(matrix_A[0],'   ', matrix_B[0])
print(matrix_A[1],'   ', matrix_B[1])
print(matrix_A[2],'   ', matrix_B[2])

print()
print("Виберіть операцію над матрицями :")
print("1 - Додавання (А + B)")
print("2 - Віднімання (А - В)")
print("3 - Множення (А * В)")
print("4 - Множення матриці А або В на число")
print()

choise = int(input("Введіть операцію : "))
if(choise == 1):
    matrix_C = summ_matrix()
    show_matrix_result('+')
if(choise == 2):
    matrix_C = subtr_matrix()
    show_matrix_result('-')
if(choise == 3):
    matrix_C = multiply_matrix()
    show_matrix_result('*')
if(choise == 4):
    choise_ch = str(input('Виберіть матрицю А або В : '))
    number = int(input(f'Введіть число на яке помножити матрицю {choise_ch} : '))
   
    if(choise_ch == 'A'):
        matrix_C = multiply_byNumber_matrix(number, matrix_A)
        show_matrix_result_by_mupltyply_number(number,'A', matrix_A)
    if(choise_ch == 'B'):
        matrix_C = multiply_byNumber_matrix(number, matrix_B)
        show_matrix_result_by_mupltyply_number(number,'B', matrix_B)
