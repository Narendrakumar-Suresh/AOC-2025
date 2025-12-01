f = open("inp1.txt",'r')
rotations = [line.strip() for line in f.readlines()] 

point = 50
count = 0

for rotation in rotations:
    direction = rotation[0]
    value = int(rotation[1:]) 

    if direction == "L":
        clicks_to_first_0 = point if point != 0 else 100
        
        if value >= clicks_to_first_0:
            hits = 1 + (value - clicks_to_first_0) // 100
            count += hits

        point = (point - value) % 100

    else:  # "R"
        # FIX 2: if point == 0 → first hit takes 100 clicks
        clicks_to_first_0 = (100 - point) % 100
        if clicks_to_first_0 == 0:
            clicks_to_first_0 = 100

        if value >= clicks_to_first_0:
            hits = 1 + (value - clicks_to_first_0) // 100
            count += hits

        point = (point + value) % 100

print(count)
