def check_prime(x:int)->bool:
    for num in range(2,x):
        if x%num==0:
            return False
    return True

def factorial(x:int)->int:
    if x==1:
        return 1
    else:
        return x*factorial(x-1)

def fib_series(x:int)->list:
    a,b=0,1
    ans=[]
    for i in range(x):
        ans.append(a)
        a,b=b,a+b
    
    return ans           

if __name__=='__main__':
    print(fib_series(4))