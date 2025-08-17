# reverse a dictionary using dict comprehension
def reverse_dict(dict1:dict)->dict:
    rev_dict={value:key for key,value in dict1.items()}
    return rev_dict
# reverse a list without reverse function
def reverse_list(lst:list)->list:
    rev_list=lst[::-1]
    return rev_list

if __name__=='__main__':
    # generate a list using List Comprehension
    l1=[i for i in range(4)]
    print(f'List: {l1}')
    print(f'Reverse list: {reverse_list(l1)}')

    #generate a dictionary using dict comprehension
    dict1={i:f'item{i}' for i in range(3)}
    print(f'Dictionary: {dict1}')
    print(f'Reverse key<->Value: {reverse_dict(dict1)}')