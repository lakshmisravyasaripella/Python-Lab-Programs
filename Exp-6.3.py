def create_matrix(rows, cols):
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            v = int(input(f'Enter element at row {r}, column {c} :'))
            row.append(v)
        matrix.append(row)
    return matrix
def mat_add(first, second):
    matrix = []
    if len(first) == len(second) and len(first[0]) == len(second[0]):
        matrix = [[first[i][j] + second[i][j] for j in range(len(first[0]))] 
for i in range(len(first))]
    return matrix
def mat_mul(first, second):
    matrix = []
    if len(first[0]) == len(second):
        matrix = [[sum(a*b for a, b in zip(row, col)) for col in zip(*second)] 
for row in first]
    return matrix
def disp(matrix):
    for row in matrix:
        for val in row:
            print(f'{val:3d}', end=' ')
        print()
rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of columns: '))
print("\nEnter elements into Matrix 1: ");
mat1 = create_matrix(rows, cols)
print("\nEnter elements into Matrix 2: ");
mat2 = create_matrix(rows, cols)
print('\n------- MAT(1) ----------')
disp(mat1)
print('\n------- MAT(2) ----------')
disp(mat2)
res = mat_add(mat1, mat2)
print('\n------- ADDITION ----------')
disp(res)
res = mat_mul(mat1, mat2)
print('\n------- MULTIPLICATION ----------')
disp(res)
'''
Output:
Enter number of rows: 2
Enter number of columns: 2

Enter elements into Matrix 1: 
Enter element at row 0, column 0 :1
Enter element at row 0, column 1 :1
Enter element at row 1, column 0 :1
Enter element at row 1, column 1 :1

Enter elements into Matrix 2: 
Enter element at row 0, column 0 :2
Enter element at row 0, column 1 :2
Enter element at row 1, column 0 :2
Enter element at row 1, column 1 :2

------- MAT(1) ----------
  1   1 
  1   1 

------- MAT(2) ----------
  2   2 
  2   2 

------- ADDITION ----------
  3   3 
  3   3 

------- MULTIPLICATION ----------
  4   4 
  4   4
'''
