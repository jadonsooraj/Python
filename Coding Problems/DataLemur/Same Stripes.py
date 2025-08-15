def display_matrix(matrix):
    print('MATRIX:')
    
    for i, row in enumerate(matrix):
        for j,ele in enumerate(row):
            print(ele, end="")
            if j<len(row)-1:
                print(" | ", end="")
        print()
        if i < len(matrix)-1:
            print('-'*(len(matrix[0])*4-3))
    print('='*40)
    return 

def check_stripes(matrix):
    diagonals={}
    if not matrix or not matrix[0]:
        return True
    
    diagonal={}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i-j in diagonals and diagonals[i-j] != matrix[i][j]:
                return False
            else:
                diagonals[i-j] =matrix[i][j]
  
    return True
            

if __name__=='__main__':
    matrix1=[[42, 7, 13, 99], [6, 42, 7, 13], [1, 6, 42, 7]]
    display_matrix(matrix1)
    if check_stripes(matrix1):
        print("TRUE")
    else:
        print("FALSE")
    