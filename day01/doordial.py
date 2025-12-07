class State:
    def __init__(self):
        self.rotation = 50
        self.password = 0

    def rotate(self, rotation_code):
        if rotation_code[0] == 'L':
            rotation_distance = int(rotation_code[1:])
            self.rotation += rotation_distance
        else:
            rotation_distance = int(rotation_code[1:])
            self.rotation  -= rotation_distance
        
        if abs(self.rotation) % 100 == 0:
            self.password += 1

current_state = State()
sequence = open("input.txt", "r")
rotations = sequence.readlines()

for rotation in rotations:
    current_state.rotate(rotation)
print(current_state.password)
