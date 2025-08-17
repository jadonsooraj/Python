def decimalToBase13(num):
    if num == 0:
        return '0'
    
    digits = '0123456789ABC'
    result = ''
    negative = num < 0
    num = abs(num) 
    
    while num > 0:
        rem = num % 13
        result = digits[rem] + result
        num = num // 13
    
    if negative:
        result = '-' + result
    return result

if __name__ == '__main__':
    print("Decimal to Base 13 Converter")
    print("Enter 'break' to stop the program")
    print("=" * 40)
    
    while True:
        try:
            user_input = input("Enter your decimal number: ").strip()
            
            if user_input.lower() =='break':
                print("Goodbye!")
                break
            
            inputNum = int(user_input)
            result = decimalToBase13(inputNum)
            print(f'Base 13 conversion for {inputNum} is {result}')
            print('='*40)
            
        except ValueError:
            print("Invalid input! Please enter a valid integer or 'break' to exit.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break