with open('input.txt') as file:
    input = file.read()


# === PART 1 ===
for i in range(4, len(input)):
    s = set(input[(i-4):i])
    if len(s) == 4:
        print("1 done: ", i)
        break

# === PART 2 ===
for i in range(14, len(input)):
    s = set(input[(i-14):i])
    if len(s) == 14:
        print("2 done: ", i)
        break