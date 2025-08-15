def matrix_creator(n:int)->list:
    res=[[i*n+j+1 for j in range(n)] for i in range(n)]
    return res

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


if __name__=='__main__':
    matrix1=[[1,2,3],[4,5,6],[7,8,9]]
    display_matrix(matrix1)
    m1=matrix_creator(3)
    print(m1)
    display_matrix(m1)
