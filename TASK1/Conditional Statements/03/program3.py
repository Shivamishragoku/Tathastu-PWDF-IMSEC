flag=0
number=int(input("Enter the number you want to check"))
for i in range(2,number):
    if number%i==0:
        flag=1
        break
if(flag==0):
    print(f"{number} is a prime number")
else:
    print(f"number was divisible by {i},Hence not a prime number")