count=0
n1=int(input("Enter first number"))
n2=int(input("Enter second number"))
for i in range(1,n1+1):
    if(n1%i==0 and n2%i==0):
        count+=1
print(f"Total common divisors between {n1}&{n2} are = {count}")