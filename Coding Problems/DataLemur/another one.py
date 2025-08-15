def numConverter(digits:list)->int:
    result=0
    for digit in digits:
        result=10*result+digit
    return result

#function to add one and return list
def listConverter(num:int)->list:
    num=num+1
    new_digit=[]
    while num>0:
        digit=num%10
        new_digit.append(digit)
        num=num//10
    new_digit.reverse()
    return new_digit

if __name__=='__main__':
    digits = [1, 2, 3]
    print(f'Number: {numConverter(digits)} after adding 1: {listConverter(numConverter(digits))}')
