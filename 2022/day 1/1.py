data = []

with open('input.txt') as file:
    score = 0
    for line in file.readlines():
        line = line.strip()
        if line == "":
            data.append(score)
            score = 0
        else:
            score += int(line)

print("1 done: ", max(data))

data = sorted(data)
print("2 done: ", data[-1] + data[-2] + data[-3])