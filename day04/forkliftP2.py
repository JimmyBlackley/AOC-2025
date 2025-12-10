with open("input.txt", "r") as f:
    text = f.readlines()

for i in range(len(text)):
    text[i] = text[i].strip()
    text[i] = [char for char in text[i]]

grid = text

def check_pos(x,y):
    num_paper = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            if grid[i][j] == '@':
                num_paper += 1
    if num_paper > 3:
        return False
    return True

for i in range(len(grid)):
    grid[i].insert(0, '.')
    grid[i].append('.')

grid.insert(0, ['.' for char in grid[0]])
grid.append(['.' for char in grid[0]])

for line in grid:
    for char in line:
        print(char, end="")
    print()

num_okay = 0

while True:
    temp_num_okay = num_okay
    for i in range(1,len(grid[0])-1):
        for j in range(1, len(grid) -1):
            if grid[i][j] == '@':
                if check_pos(i,j):
                    num_okay += 1
                    grid[i][j] = 'X'
    if num_okay == temp_num_okay:
        break

print(num_okay)

