data = []
delimiter = " "

with open("input.txt") as file:
    for line in file.readlines():
        element = []
        for token in line.strip().split(delimiter):
            data.append(token)

score = 0
for index in range(len(data)//3):
    aa = sorted(data[index*3])
    a = []
    [a.append(x) for x in aa if x not in a]

    bb = sorted(data[3*index+1])
    b = []
    [b.append(x) for x in bb if x not in b]

    cc = sorted(data[3*index+2])
    c = []
    [c.append(x) for x in cc if x not in c]

    for character in a: 
        if character in b: 
            if character in c:
                if character >= "a" and character <= "z":
                    score += (ord(character) - 96)
                elif character >= "A" and character <= "Z":
                    score += (ord(character) - 38)

print("2 done: ", score)