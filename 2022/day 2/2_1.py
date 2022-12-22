# data = []

# delimiter = " "

# with open("input.txt") as file:
#     for line in file.readlines():
#         element = []
#         for token in line.strip().split(delimiter):
#             element.append(token)
#         data.append(element)

# score = 0
# for game in data:
#     if game[1] == "X":
#         score += 1
#     elif game[1] == "Y":
#         score += 2
#     elif game[1] == "Z":
#         score +=3

#     if game[0] == "B" and game[1] == "Z":
#         score += 6
#     elif game[0] == "A" and game[1] == "Y":
#         score += 6
#     elif game[0] == "C" and game[1] == "X":
#         score += 6
#     elif game[0] == "A" and game[1] == "X":
#         score += 3
#     elif game[0] == "B" and game[1] == "Y":
#         score += 3
#     elif game[0] == "C" and game[1] == "Z":
#         score += 3


# print("1 done: ", score)