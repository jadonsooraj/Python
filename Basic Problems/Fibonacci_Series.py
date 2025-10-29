def fib_series(num:int):
    a, b = 0, 1
    for _ in range(num):
        print(a, end=' ')
        a, b = b, a + b

if __name__=='__main__':
    num=4
    fib_series(num)