with open("input.txt", "r") as f:
    joltages = f.readlines()

sum_val = 0

for i in range(len(joltages)):
    joltages[i] = joltages[i].strip()
    temp_sum = 0
    w_start = 0
    # print(joltages[i])
    all_nums = [int(char) for char in joltages[i]]
    for w_end in range(11, -1, -1):
        if w_end == 0:
            cells = all_nums[w_start:]
        else:
            cells = all_nums[w_start:-w_end]
        # print(cells)
        highest = max(cells)
        index_of_newest = cells.index(highest)
        # print(f"Found a {highest} at {w_start}, new start is {w_start+index_of_newest+1}")
        w_start += index_of_newest + 1
        temp_sum = (temp_sum * 10) + highest
    print(temp_sum)
    sum_val += temp_sum
print(sum_val)
