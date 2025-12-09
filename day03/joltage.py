with open("input.txt", "r") as f:
    joltages = f.readlines()

sum_val = 0

for i in range(len(joltages)):
    joltages[i] = joltages[i].strip()

    cells_upper = [int(char) for char in joltages[i][0:-1]]
    
    highest_upper = max(cells_upper)
    highest_index = cells_upper.index(highest_upper)

    cells_lower = [int(char) for char in joltages[i][highest_index + 1:]]
    
    highest_lower = max(cells_lower)

    sum_val += (highest_upper * 10) + highest_lower

print(len(joltages))
print(sum_val)
