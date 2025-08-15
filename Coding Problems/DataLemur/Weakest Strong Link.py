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

def find_weak_link(strength: list) -> int:
    rows = len(strength)
    cols = len(strength[0])
    # Check each position in the matrix
    for i in range(rows):
        for j in range(cols):
            current = strength[i][j]
            
            # Check if current element is minimum in its row
            is_min_in_row = all(current <= strength[i][j] for j in range(cols))
            
            # Check if current element is maximum in its column
            is_max_in_col = all(current >= strength[i][j] for i in range(rows))
            
            if is_min_in_row and is_max_in_col:
                return current
    
    return -1


if __name__=='__main__':
    strength1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    strength2 = [[9, 8, 10],[6, 15, 4]]
    display_matrix(strength2)
    print(f'Weak link: {find_weak_link(strength2)}')
