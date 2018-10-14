s=input("Enter a string:\t")
d=dict()
unique = True
for char in s:
    if char in d.keys():
        unique=False
        break
    else:
        d[char]=1
if(unique):
    print(s,"is a unique string",sep=" ",end="\n")
else:
    print(s,"is not a unique string",sep=" ",end="\n")

