

def create_matrix(rows: int, cols: int, default=0) -> list:
    form_matrix = [[default for j in range(cols)]for i in range(rows)]
    
    return form_matrix

def matrix_add(a: list, b: list) -> list:
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        for i in range(len(a)):
            for j in range(len(b[0])):
                a[i][j] += b[i][j]
                
        return a
    else:
        print("Error! Matrix sizes should be same")
        
def matrix_multiply(a: list, b: list) -> list:
    if (len(a[0]) == len(b)):
        
        c = create_matrix(len(a), len(b[0]))
        
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(a[0])):
                    c[i][j] += a[i][k] * b[k][j]
        
        return c
    else:
        print("Multiplication not possible!")
        return None
        
def transpose(matrix: list) -> list:
    return [[row[i] for row in matrix]for i in range(len(matrix[0]))]

def print_matrix(matrix: list) -> list:
    for row in matrix:
        print(" ".join(f"{val: 3}" for val in row))
        
def rotate_90_clockwise(matrix: list) -> list:
    transposed = transpose(matrix)
    
    for row in transposed:
        row.reverse()
        
    return transposed

def is_symmetric(matrix: list) -> bool:
    return matrix == transpose(matrix)

#inputs
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

print_matrix(A)
print_matrix(B)

#Addition
add_result = matrix_add(A, B)
print(f"Addition result: {add_result}")

#multi
multi_result = matrix_multiply(A, B)
print(f"Multi result: {multi_result}")

#Transpose
print(f"Transpose of A: {transpose(A)}")
print(f"Transpose of B: {transpose(B)}")

#rotation
print(f"Rotation A: {rotate_90_clockwise(A)}")
print(f"Rotation B: {rotate_90_clockwise(B)}")

#symmetric check
print(f"Symmetric check A: {is_symmetric(A)}")
print(f"Symmetric check B: {is_symmetric(B)}")