with open("input.txt", "r") as f:
    file_read = f.readlines()


sum_val = 0

for i in range(len(file_read[0])):
    
    temp_nums = [''] * (len(file_read) - 1)
    temp_sum = 0
    operation = ""
    for j in range(len(file_read)):
        char =   file_read[j][i]
        if char == '*':
            operation = "multiply"
            continue
        if char == '+':
            operation  = "sum"
            continue
        
        if char != ' ':
            print(char)
            temp_nums[i] += char

    if ((i+1) % 5) == 0:

        if operation == "multiply":
            print(temp_nums)
            exit()
        
            for k in range(len(temp_nums)):
                temp_nums[k] = int(str(temp_nums[k]))
        
            temp_sum = temp_nums[0]
            for l in range(1, (len(temp_nums))):
                temp_sum *= temp_nums[k]
        
        if operation == "sum":
            print(temp_nums)
            exit()

            for k in range(len(temp_nums)):
                temp_nums[k] = int(str(temp_nums[k]))
            temp_sum = sum(temp_nums)

    if char != ' ':
        temp_nums[i] += char
    sum_val += temp_sum
 
    
print(sum_val)

