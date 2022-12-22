# Getting data
with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]


# === PART 1 ===
pairs = 0
for entry in data:
    first, second = entry.split(",")
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] <= second[0] and first[1] >= second[1]:
        pairs += 1
    elif second[0] <= first[0] and second[1] >= first[1]:
        pairs += 1

print("1 done: ", pairs)

# === PART 2 ===
pairs = 0
for entry in data:
    first, second = entry.split(",")
    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")]

    if first[0] in range(second[0], second[1]+1) or first[1] in range(second[0], second[1]+1):
        pairs += 1
    elif second[0] in range(first[0], first[1]+1) or second[1] in range(first[0], first[1]+1):
        pairs += 1


print("2 done: ", pairs)










#___________________________________________________________________________________________________
# data = []
# delimiter = ","

# with open("input.txt") as file:
#     for line in file.readlines():
#         element = []
#         for token in line.strip().split(delimiter):
#             token = token.split("-")
#             element.append(token)
#         data.append(element)

# fully = 0
# patrial = 0
# for line in data:
#     a = int(line[0][0])
#     b = int(line[0][1])
#     c = int(line[1][0])
#     d = int(line[1][1])
#     if a >= c and b <= d:
#         fully += 1
#     elif c >= a and d <= b:
#         fully += 1
#     if b >= c and d >= a:
#         patrial += 1

# print("1 done: " , fully)
# print("2 done: " , patrial)

    