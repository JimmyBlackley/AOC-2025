sequence = open("input.txt", "r")
ranges = sequence.readline().strip()

ranges = ranges.split(',')

pairs = []
for pair in ranges:
    lower_bound, upper_bound = pair.split('-')
    pairs.append([int(lower_bound), int(upper_bound)])

# invalid ID's are always even number of digits long:
# we can reduce search space by removing odd sets, or moving lower bound to 10^even
# using string and len rather than log, as safer with very large numbers
def dig(num):
    return len(str(num))



invalid_sum = 0
found_nums = set()


for pair in pairs:
    start, end = pair[0], pair[1]
    min_len = dig(start)
    max_len = dig(end)

    print(f"checking pair from {start} to {end}")
    for length in range(min_len, max_len + 1):  
        valid_nums_for_span_lower = max(start, 10**(length-1))
        valid_nums_for_span_upper = min(end, (10**length)-1)
        print(f" valid nums in span: {valid_nums_for_span_lower} - {valid_nums_for_span_upper}")
        
        for pattern_span in range(1, (length//2) + 1):
            if ((length % pattern_span) == 0): # pattern is correct width to fit
                pattern_repeats = length // pattern_span
                for number in range(valid_nums_for_span_lower,valid_nums_for_span_upper + 1):
                    pattern = int(str(number)[0:pattern_span]*pattern_repeats)
                    if pattern >= start and pattern <= end:
                        if pattern not in found_nums:
                            print(f"             {pattern}")
                            found_nums.add(pattern)
                            invalid_sum += pattern



   #for every search range pair
   #  for every number int hat search range inclusive
   #    for every sequencelength of digits in that search range (up to half number length since min repeats in 2 occurances)
   #       if the sequence length is a divisor of that number
   #         pattern = number[0:sequence length] repeated til same length as number
   #         if pattern in range:
   #           if pattern not seen before
   #             add pattern to set
   #             increment sum by pattern


print(invalid_sum)

             
