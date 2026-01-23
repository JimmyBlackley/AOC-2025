import math

class point:
    def __init__(self, x, y, z, id):
        self.x = x
        self.y = y
        self.z = z
        self.id = id


class pairing:
    @staticmethod
    def distance_between(p1: point, p2: point) -> float:
        return  math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2 + (p1.z-p2.z)**2)

    def __init__(self, p1: point, p2: point):
        self.distance = pairing.distance_between(p1, p2)
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return f"Point {self.p1.id} <-> Point {self.p2.id} : Distance {self.distance} \n"
    

def find_parent(parents: dict, index: int):
    if parents[index] != index:
        parents[index] = find_parent(parents, parents[index])
    return parents[index]

def join_circuits(parents: dict, p1: point, p2: point):
    root1 = find_parent(parents, p1.id)
    root2 = find_parent(parents, p2.id)
    if root1 != root2:
        parents[root2] = root1

def different_circuits(parents: dict, p1: point, p2: point) -> bool:
    return find_parent(parents, p1.id) != find_parent(parents, p2.id)


with open("input.txt","r") as f:
    junctions = f.readlines()

    points = []
    pairings = []
    parents = {}

    for i in range(len(junctions)):
        line = junctions[i].split(',')
        x = int(line[0])
        y = int(line[1])
        z = int(line[2])
        points.append(point(x,y,z,i))
        parents[i] = i



    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            pairings.append(pairing(points[i], points[j]))
    
    pairings = sorted(pairings, key=lambda p: p.distance)

    last_pair = ""
    num_circuits = len(points)
    for pairing in pairings:
        if different_circuits(parents, pairing.p1, pairing.p2):
            last_pair = pairing
            join_circuits(parents, pairing.p1, pairing.p2)
            num_circuits -= 1
            if num_circuits == 1:
                break
    
    print(last_pair)
    print(last_pair.p1.x * last_pair.p2.x)
    
