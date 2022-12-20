data = []
delimiter = ","

with open("input.txt") as file:
    for line in file.readlines():
        element = []
        for token in line.strip().split(delimiter):
            token = token.split("-")
            element.append(token)
        data.append(element)

fully = 0
patrial = 0
for line in data:
    a = int(line[0][0])
    b = int(line[0][1])
    c = int(line[1][0])
    d = int(line[1][1])
    if a >= c and b <= d:
        fully += 1
    elif c >= a and d <= b:
        fully += 1
    if b >= c and d >= a:
        patrial += 1

print("1 done: " , fully)
print("2 done: " , patrial)

    