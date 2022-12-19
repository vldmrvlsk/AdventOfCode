data = []
delimiter = " "

with open("input.txt") as file:
    for line in file.readlines():
        element = []
        for token in line.strip().split(delimiter):
            data.append(token)

score = 0
for bag in data:
    aa = sorted(bag[:len(bag)//2])
    a = []
    [a.append(x) for x in aa if x not in a]

    bb = sorted(bag[len(bag)//2:])
    b = []
    [b.append(x) for x in bb if x not in b]

    for character in a: 
        if character in b: 
            if character >= "a" and character <= "z":
                score += (ord(character) - 96)
            elif character >= "A" and character <= "Z":
                score += (ord(character) - 38)

print("1 done: ", score)

    