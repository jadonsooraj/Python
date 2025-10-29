# Write a python program to reverse an array after the kth position
def reverse_list(ls:list,k:int)->list:
    part1 = ls[:k]
    part2 = ls[k:]
    part2.reverse()
    return part1 + part2

if __name__=='__main__':
    l1=[i for i in range(1,7)]
    print(f'List: {l1}')
    # challange: reverse after index 3
    print(reverse_list(l1,3))