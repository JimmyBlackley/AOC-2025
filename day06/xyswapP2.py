import math
with open("input.txt", "r") as f:
    file_read = f.readlines()


    width = len(file_read[0].strip())
    height = len(file_read) - 1
    operator_row = height
    operators = ['*', '+']

    answer = 0
    temp_string = ""

    temp_nums = []

    for i in range(width, -1, -1):
        temp_string = ""
        for j in range(0, height):
            temp_char = file_read[j][i]
            temp_char = temp_char.strip()
            if temp_char.isnumeric():
                temp_string += temp_char
    
        if temp_string != "":
            if temp_string.isnumeric():
                temp_nums.append(int(temp_string))
            else:
                print("non empty temp string:")
                print(temp_string)
        if str(file_read[operator_row][i]) in operators:
            op = file_read[operator_row][i]
            if op == '+':
                answer += sum(temp_nums)
                temp_nums.clear()
            elif op == '*':
                answer += math.prod(temp_nums)
                temp_nums.clear()
    print(answer)