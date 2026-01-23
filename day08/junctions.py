import math

class point:
    def __init__(self, x, y, z, id):
        self.x = x
        self.y = y
        self.z = z
        self.id = id


class pairing:
    @staticmethod
    def distance_between(p1, p2):
        return  math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2)

    def __init__(self, p1, p2):
        self.distance = pairing.distance_between(p1, p2)
        self.p1 = p1
        self.p2 = p2

    
    def __repr__(self):
        return f"Point {self.p1.id} <-> Point {self.p2.id} : Distance {self.distance} \n"



# connect items to circuits, create new circuit, or merge cicruits
def handle_assignment(assignments_dict: dict, ids: list, p1: point, p2: point):

    # p1 already in a cuircuit, p2 is not

    if p1.id in assignments_dict and p2.id not in assignments_dict:
        assignments_dict[p2.id] = assignments_dict[p1.id]
    
    # p2 already in a circuit, p1 is not
    
    elif p2.id in assignments_dict and p1.id not in assignments_dict:
        assignments_dict[p1.id] = assignments_dict[p2.id]
    
    # neither are in circuits yet, create new id
    
    elif p1.id not in assignments_dict and p2.id not in assignments_dict:
        new_id = len(ids)
        assignments_dict[p1.id] = new_id
        assignments_dict[p2.id] = new_id
        ids.append(new_id)
    

    # both p1 and p2 are in the dictionary, but with different circuits
    
    elif p1.id in assignments_dict and p2.id in assignments_dict:
        if assignments_dict[p1.id] == assignments_dict[p2.id]:
            pass
        else:
            old_id = assignments_dict[p2.id]
            new_id = assignments_dict[p1.id]
            
            for key, value in assignments_dict.items():
                if value == old_id:
                    assignments_dict[key] = new_id
    else:
        print("something fucked up")
    


with open("input.txt","r") as f:
    junctions = f.readlines()

    points = []

    for i in range(len(junctions)):
        line = junctions[i].split(',')
        x = int(line[0])
        y = int(line[1])
        z = int(line[2])
        points.append(point(x,y,z,i))
    
    list_of_circuit_ids = []
    assignments = {}
    pairings = []

    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            pairings.append(pairing(points[i], points[j]))
    
    pairings = sorted(pairings, key=lambda p: p.distance)

    for i in range(0, 1000):  # handle the first 1000 shortest pairings
        handle_assignment(assignments,list_of_circuit_ids, pairings[i].p1, pairings[i].p2)
    
    circuit_sizes = [0] * len(list_of_circuit_ids)
    for key in assignments.keys():
        circuit_sizes[assignments[key]] += 1
    
    highest = max(circuit_sizes)
    index_of_highest = circuit_sizes.index(highest)
    print(highest)
    circuit_sizes.remove(highest)
    highest = max(circuit_sizes)
    index_of_highest = circuit_sizes.index(highest)
    print(highest)
    circuit_sizes.remove(highest)
    highest = max(circuit_sizes)
    index_of_highest = circuit_sizes.index(highest)
    print(highest)
    circuit_sizes.remove(highest)
    
    