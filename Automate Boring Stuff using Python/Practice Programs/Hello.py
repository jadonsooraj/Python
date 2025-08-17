# reverse a list without reverse function
def reverse_list(lst:list)->list:
    rev_list=lst[::-1]
    return rev_list

if __name__=='__main__':
    l1=[i for i in range(4)]
    print(l1)
    print(f'Reverse list {reverse_list(l1)}')