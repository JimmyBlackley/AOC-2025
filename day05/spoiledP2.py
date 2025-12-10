with open("input.txt", 'r') as f:
    input_text = f.readlines()

found_split = False
ranges = []
for i in range(len(input_text)):
    input_text[i] = input_text[i].strip()
    if len(input_text[i]) == 0:
        found_split =  True
        break
    lower, upper = input_text[i].split('-')
    ranges.append([int(lower), int(upper)])

# make new list, with size of each span, and index in original array
sizes = []
for i in range(0, len(ranges)):
    span = ranges[i][1] - ranges[i][0] + 1
    if span:
        sizes.append([span, i])

# sort by largest to smallest span
sizes.sort()
sizes = list(reversed(sizes))

# make new list, to cull spans that are completely engulfed by other spans
culled = []
culled.append(ranges[sizes[0][1]])
for i in range(1, len(sizes)):
    should_add = True
    current = ranges[sizes[i][1]]
    for cull in culled:
        if current[0] >= cull[0] and current[1] <= cull[1]:
            should_add = False
    
    if should_add:
        culled.append(ranges[sizes[i][1]])


# sort culled list from smallest to largest
culled.sort()

# if upper bound if overlaps, to be before the overlap
for i in range(0, len(culled)-1):
    culled[i][1] = min(culled[i][1], culled[i+1][0] - 1)

# find sum of all the spans, with no overlaps counted
sum_val = 0
for span in culled:
    sum_val += (span[1] - span[0] + 1)

print(sum_val)
