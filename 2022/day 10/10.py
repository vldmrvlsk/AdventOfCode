data = []

with open('input.txt') as file:
    for line in file.readlines():
        element = []
        for token in line.strip().split("X"):
            data.append(token.split())

# print(data)

values = [1]
for line in data:
    values.append(values[-1])
    if line[0] == "addx":
        values.append(int(line[1]) + values[-1])

total = 0
for x in range(20, 260, 40):
    total += (x * values[x-1])


print("1 done: ", total)


screen = ''

for i in range(len(values)):
    if abs(values[i] - (i % 40)) <= 1:
        screen += '#'
    else:
        screen += '.'

for i in range(7):
    text = screen[40*i:40*(i+1)]
    print(text)