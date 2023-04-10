import re
name = input("Enter file:")
handle = open(name)
total=0
totalNum=0
for line in handle:
    if 'New Revision' not in line:
        continue
    else:
        x=re.findall('[0-9]+',line)
        count=0
        for y in x:
            total=total+int(x[count])
            count=count+1
            totalNum=totalNum+1
print(int(total/totalNum))