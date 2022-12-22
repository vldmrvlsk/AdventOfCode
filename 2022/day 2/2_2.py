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
#     if game[0] == "A" and game[1] == "X":
#         score += 3
#     elif game[0] == "A" and game[1] == "Y":
#         score += 4
#     elif game[0] == "A" and game[1] == "Z":
#         score += 8
#     elif game[0] == "B" and game[1] == "X":
#         score += 1
#     elif game[0] == "B" and game[1] == "Y":
#         score += 5
#     elif game[0] == "B" and game[1] == "Z":
#         score += 9
#     elif game[0] == "C" and game[1] == "X":
#         score += 2
#     elif game[0] == "C" and game[1] == "Y":
#         score += 6
#     elif game[0] == "C" and game[1] == "Z":
#         score += 7


# print("2 done: ", score)