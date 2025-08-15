list=[25,56,2,6,87,35,76]
n=7
def maximum(list):
    max=0
    for i in range(n-1):
        if(list[i]>max):
            max=list[i]
    return(max)
print(maximum(list))