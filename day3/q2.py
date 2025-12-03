TOTAL_DIGITS_TO_SELECT = 12
total_joltage = 0

try:
    with open('./day3/input.txt', 'r') as f:
        puzzle_input = f.read()
except FileNotFoundError:
    print("Error: 'input.txt' not found. Please ensure your puzzle input is in a file named 'input.txt'.")
    exit()

for line in puzzle_input.strip().split('\n'):
    digits = [int(c) for c in line.strip()]
    selected_digits = []
    current_start_index = 0
    
    for num_selected in range(TOTAL_DIGITS_TO_SELECT):
        L = TOTAL_DIGITS_TO_SELECT - num_selected
        
        max_search_index = len(digits) - L
        
        best_digit = -1
        best_index = -1
        
        for i in range(current_start_index, max_search_index + 1):
            if digits[i] > best_digit:
                best_digit = digits[i]
                best_index = i
        
        selected_digits.append(str(best_digit))
        current_start_index = best_index + 1

    max_joltage_str = "".join(selected_digits)
    total_joltage += int(max_joltage_str)

print(f"The new total output joltage is: {total_joltage}")