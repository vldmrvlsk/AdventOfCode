data = []
delimiter = ' '

with open('input.txt') as file:
    for line in file.readlines():
        element = []
        for token in line.strip().split("!"):
            data.append(token.split())

# print(data)

head = [0, 0]
tail = [0, 0]
locations = {(0, 0)}

for movement in data:
    m = {'D':[0, 1], 'U':[0, -1], 'L':[-1, 0], 'R':[1, 0]}
    for i in range(int(movement[1])):
        head[0] += m[movement[0]][0]
        head[1] += m[movement[0]][1]
        dx = tail[0] - head[0]
        dy = tail[1] - head[1]
        if dx == -2 and dy == 0:
            tail[0] += 1
        elif dx == 2 and dy == 0:
            tail[0] -= 1
        elif dy == -2 and dx == 0:
            tail[1] += 1
        elif dy == 2 and dx == 0:
            tail[1] -= 1
        elif dy == 2 and dx == 1:
            tail[0] -= 1
            tail[1] -= 1
        elif dy == -2 and dx == 1:
            tail[0] -= 1
            tail[1] += 1
        elif dy == -2 and dx == -1:
            tail[0] += 1
            tail[1] += 1
        elif dy == 2 and dx == -1:
            tail[0] += 1
            tail[1] -= 1
        elif dy == 1 and dx == 2:
            tail[0] -= 1
            tail[1] -= 1
        elif dy == -1 and dx == 2:
            tail[0] -= 1
            tail[1] += 1
        elif dy == -1 and dx == -2:
            tail[0] += 1
            tail[1] += 1
        elif dy == 1 and dx == -2:
            tail[0] += 1
            tail[1] -= 1
        locations.add(tuple((tail[0], tail[1])))

print("1 done: ", len(locations))