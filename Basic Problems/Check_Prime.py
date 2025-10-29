def check_prime(nums:list)->list:
    check_list = []
    for num in nums:
        if num < 2:
            check_list.append(False)
            continue
        if num == 2:
            check_list.append(True)
            continue
        is_prime = True
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
        check_list.append(is_prime)
    return check_list

if __name__=='__main__':
    nums=[2,5,6,7,9,13,17,21]
    print(check_prime(nums))