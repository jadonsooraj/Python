
def triangular_sum(ls:list)->int:
    while len(ls) > 1:
        ls=[((ls[i]+ls[+1])%10) for i in range(len(ls)-1)]
    
    return ls[0]


if __name__=='__main__':
    nums=[ i for i in range(1,8) if i%2!=0]
    print(f'List: {nums}')
    print(f'Triangular Sum: {triangular_sum(nums)}')