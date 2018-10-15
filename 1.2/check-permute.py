import sys
s1=input()
s2=input()

if(len(s1) != len(s2)):
    print(s1,s2," are not permutations of each other")
    sys.exit() 
d1=dict()
d2=dict()

for char in s1:
    if char in d1.keys():
        d1[char] +=1
    else:
        d1[char] = 1
for char in s2:
    if char in d2.keys():
        d2[char] +=1
    else:
        d2[char] = 1
if(d1==d2):
    print(s1,s2," are permutations of each other")
else:
    print(s1,s2," are not permutations of each other")

