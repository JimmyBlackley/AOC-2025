def make_list(number):
    number = str(number)
    return [int(char) for char in number]


with open("input.txt", "r") as f:
    total = 0
    numbers = f.readlines()

    # main loop
    for number in range(len(numbers):
        number = make_list(number)
        indice = []

        # first pass
        for i in range(9, -1, -1):
            for j in range(len(number)):
                if number[j] == i:
                    indice.append(j)
            if len(indice) > 0:
                break
        if len(indice) == 12:
            total += int(str(i)*12)
            break
        # the backward passes
        for i in range(8, -1, -1):
            for j in range(len(number), -1, -1):
                if number[j] == i:
                    # append to the correct index
                    number.append(j)
                    number.sort()
            if len(indice) == 12:
                total += int(str(
                        
                    
    
