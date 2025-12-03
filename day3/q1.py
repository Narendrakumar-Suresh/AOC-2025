total = 0

with open("./day3/input.txt") as f:
    for line in f:
        digits = [int(c) for c in line.strip()]
        best = 0
        
        # try every pair i < j
        for i in range(len(digits)):
            for j in range(i+1, len(digits)):
                value = digits[i] * 10 + digits[j]
                if value > best:
                    best = value
        
        total += best

print(total)
