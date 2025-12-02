import re

f=open("./day2/input.txt","r")
lis=f.read().split(',')
invalid=[]

def is_invalid(i):
    s=str(i)
    return re.fullmatch(r"(\d+)\1", s) is not None

for i in range(len(lis)):
    start,end=lis[i].split('-')
    start,end=int(start),int(end)

    for i in range(start,end+1):
        if is_invalid(i):
            invalid.append(i)

print(sum(invalid))


