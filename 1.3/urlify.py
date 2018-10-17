s= "Mr John Smith   ";
s=s.strip();

# finding pos of empty spaces
indexes = [pos for pos,c in enumerate(s) if c==" "]

start_index = 0
new_s = []
for index in indexes:
    new_s.append(s[start_index:index])
    new_s.append("%20")
    start_index = index+1
new_s.append(s[start_index:len(s)])

new_s = "".join(new_s)
print(new_s)