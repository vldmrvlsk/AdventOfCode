data = []
delimiter = ' '

with open('input.txt') as file:
    for line in file.readlines():
        element = []
        for token in line.strip().split("!"):
            data.append(token.split())

# print(data)

head = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
locations = {(0, 0)}

for movement in data:
    m = {'D':[0, 1], 'U':[0, -1], 'L':[-1, 0], 'R':[1, 0]}
    for i in range(int(movement[1])):
        head[0][0] += m[movement[0]][0]
        head[0][1] += m[movement[0]][1]
        for j in range(1, 10):
            dx = head[j][0] - head[j-1][0]
            dy = head[j][1] - head[j-1][1]
            if dx < -1 and dy == 0:
                head[j][0] += 1
            elif dx > 1 and dy == 0:
                head[j][0] -= 1
            elif dy < -1 and dx == 0:
                head[j][1] += 1
            elif dy > 1 and dx == 0:
                head[j][1] -= 1
            elif dy > 1 and dx > 0:
                head[j][0] -= 1
                head[j][1] -= 1
            elif dy < -1 and dx > 0:
                head[j][0] -= 1
                head[j][1] += 1
            elif dy < -1 and dx < 0:
                head[j][0] += 1
                head[j][1] += 1
            elif dy > 1 and dx < 0:
                head[j][0] += 1
                head[j][1] -= 1
            elif dy > 0 and dx > 1:
                head[j][0] -= 1
                head[j][1] -= 1
            elif dy < 0 and dx > 1:
                head[j][0] -= 1
                head[j][1] += 1
            elif dy < 0 and dx < -1:
                head[j][0] += 1
                head[j][1] += 1
            elif dy > 0 and dx < -1:
                head[j][0] += 1
                head[j][1] -= 1
        locations.add(tuple((head[9][0], head[9][1])))

print("2 done: ", len(locations))