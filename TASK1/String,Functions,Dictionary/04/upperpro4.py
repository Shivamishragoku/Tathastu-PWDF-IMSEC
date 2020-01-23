c1,c2=0,0
name=input("Enter your String")
for i in name:
    x=i.isupper()
    if x:
        c1+=1
    else:
        c2+=1
print(f"Number of Uppercase are {c1} and lowercase are {c2}")




