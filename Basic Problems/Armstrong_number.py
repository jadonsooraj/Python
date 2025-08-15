input_number=int(input("Enter number: "))
temp=input_number
ls=[]
sum=0 ; count=0

while(temp>0):
    count+=1
    ls.append(temp%10)
    temp=temp//10

power=count 


while(count>0):
    sum=sum+ls[count-1]**power
    count=count-1

if input_number==sum:
    print("yes")
else:
    print("no")