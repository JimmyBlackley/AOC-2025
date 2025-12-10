with open("input.txt", 'r') as f:
    input_text = f.readlines()


found_split = False
ranges = []
ids = []
for i in range(len(input_text)):
    input_text[i] = input_text[i].strip()
    if len(input_text[i]) == 0:
        found_split =  True
        continue
    
    if found_split:
        ids.append(int(input_text[i]))
    else:
        lower, upper = input_text[i].split('-')
        ranges.append([int(lower), int(upper)])

def check_in_range(number):
    for bounds in ranges:
        if number >= min(bounds[0], bounds[1]) and number <= max(bounds[0], bounds[1]):
            return True
    return False


num_ids = 0
num_checked = 0
for ingredient in ids:
    num_checked += 1
    if check_in_range(ingredient):
        num_ids += 1

print(num_ids)
print(num_checked)

