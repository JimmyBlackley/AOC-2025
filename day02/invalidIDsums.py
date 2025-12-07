sequence = open("input.txt", "r")
ranges = sequence.readline().strip()

ranges = ranges.split(',')

pairs = []
for pair in ranges:
    lower_bound, upper_bound = pair.split('-')
    pairs.append([int(lower_bound), int(upper_bound)])

invalid_sum = 0
# invalid ID's are always even number of digits long:
# we can reduce search space by removing odd sets, or moving lower bound to 10^even
# using string and len rather than log, as safer with very large numbers
def dig(num):
    return len(str(num))

list_to_pop = []

for i in range(0, len(pairs)):
    current_pair = pairs[i]
    if dig(current_pair[0])%2 == 1:
        if dig(current_pair[1])%2 == 1:
            print(f"Removing item {pairs[i]} since both bounds uneven in length")
            list_to_pop.insert(0, i)
        else:
            print(f"increasing lower bound from {pairs[i][0]} to {10**(dig(pairs[i][0]))}")
            pairs[i][0] = 10**(dig(pairs[i][0]))

    if dig(current_pair[1]) % 2 == 1:
        print(f"Reducing pair upper bound from {pairs[i][1]}  to {10**(dig(pairs[i][1])-1)-1}")
        pairs[i][1] = 10**(dig(pairs[i][1])-1)-1

for index in list_to_pop:
    pairs.pop(index)



for pair in pairs:
    num_digits = dig(pair[0]) 
    half_len = num_digits // 2
    
    divisor = 10**half_len
    
    start_prefix = pair[0] // divisor
    end_prefix = pair[1] // divisor
    
    for prefix in range(start_prefix, end_prefix + 1):
        candidate = int(str(prefix) + str(prefix))
        
        if pair[0] <= candidate <= pair[1]:
            invalid_sum += candidate


print(invalid_sum)
