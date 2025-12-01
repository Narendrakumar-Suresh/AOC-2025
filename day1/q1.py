f=open("input.txt",'r')
# Read all lines and strip the newline character from each rotation string
rotations = [line.strip() for line in f.readlines()] 

point = 50
count = 0

for rotation in rotations:
    direction = rotation[0]    
    value = int(rotation[1:]) 

    if direction == "L":
        point = point - value
    else:
        point = point + value

    point = point % 100 
    
    if point < 0:
        point += 100
    
    if point == 0:
        count += 1

f.close()
print(count)