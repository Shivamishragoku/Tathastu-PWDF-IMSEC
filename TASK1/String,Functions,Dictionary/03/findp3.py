#only for url which are .com
str=input('Enter your string')
x=str.find("http//www.")
if x>=0:
    print(f"URL Found from index {x}")
