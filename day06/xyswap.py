with open("input.txt", "r") as f:
    file_read = f.readlines()

for i in range(len(file_read)):
    file_read[i] = file_read[i].split()

calcs = len(file_read)
nums  = len(file_read[0])

print(calcs, nums)
better_array = []

for i in range(nums):
    calc_line = []
    for j in range(calcs):
        calc_line.append(file_read[j][i])
    better_array.append(calc_line)

sum_val = 0
for line in better_array:
    line_sum = 0
    if line[-1:][0] == '*':
        line_sum = int(line[0])
        other_nums = [int(num) for num in line[1:-1]]
        for num in other_nums:
            line_sum *= num
    elif line[-1:][0] == '+':
        line_sum = sum([int(num) for num in line[:-1]])
    sum_val += line_sum
print(sum_val)
