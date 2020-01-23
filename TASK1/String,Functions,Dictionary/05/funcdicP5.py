def reverse(d):
    for i,k in d.items():
        print(f" {k}:{i}",end=" ")
def dictsum(d):
    s=0
    for i in d.values():
        n=len(i)
        s=s+n
    return s
def dictsortkey(d):
    for i in sorted(d.keys()):
        print(i,end=" ")
temp={1:"seol",2:"pokemon",3:"maruti"}
print("keys in sorted order are:-")
dictsortkey(temp)
print("\nSum of values in dictionary:-")
print("In reverse order:-")
reverse(temp)



