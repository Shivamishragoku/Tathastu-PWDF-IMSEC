str=""
name=input("Enter your String")
for i in range(0,len(name)):
    for j in range(0,i+1):
        if(name[i]==name[j]):
            break
    if i==j:
        str=str+name[i]
print(str)