class State:
    def __init__(self):
        self.abs_position = 50 
        self.zero_hits = 0

    def rotate(self, instruction):
        direction = instruction[0]
        amount = int(instruction[1:])

        old_pos = self.abs_position

        if direction == 'R':
            self.abs_position += amount
            self.zero_hits += (self.abs_position // 100) - (old_pos // 100)
            
        else:
            self.abs_position -= amount
            self.zero_hits += ((old_pos - 1) // 100) - ((self.abs_position - 1) // 100)

current_state = State()

with open("input.txt", "r") as f:
    rotations = f.readlines()

for rotation in rotations:
    current_state.rotate(rotation.strip())

print(current_state.zero_hits)
