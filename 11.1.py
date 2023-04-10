import re
name = input("Enter a regular expression:")
str(name)
handle = open('mbox-short.txt')
count=0
for line in handle:
    if name not in line:
        continue
    else:
        count=count+1
print('mbox-short.txt had',count,"lines that matched",name)