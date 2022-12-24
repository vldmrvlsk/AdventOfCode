with open("input.txt") as file:
    data = [row.strip() for row in file.readlines()]

ROWS = len(data)            # num of rows
COLUMNS = len(data[0])      # num of columns

edges = (ROWS*2) + ((COLUMNS-2)*2)      # all trees on edges are visible
total = edges                           # add edges to total visible trees
scores = []                             # track the scenic scores

# Iterate through trees not on edges
for row in range(1, ROWS-1):
    for col in range(1, COLUMNS-1):
        tree = data[row][col]           # Tree that we are looking at

        # Get all horizontal & vertical trees
        left = [data[row][col-i] for i in range(1, col+1)]
        right = [data[row][col+i] for i in range(1, COLUMNS-col)]
        up = [data[row-i][col] for i in range(1, row+1)]
        down = [data[row+i][col] for i in range(1, ROWS-row)]

        # === PART 1 ===
        # Check if tallest tree on all sides blocks our view of the tree
        if max(left)<tree or max(right)<tree or max(up)<tree or max(down)<tree:
            total += 1

        # === PART 2 ===
        
        # Finding scenic score
        score = 1
        for lst in (left, right, up, down):
            tracker = 0
            for i in range(len(lst)):
                if lst[i] < tree:
                    tracker += 1
                elif lst[i] >= tree:
                    tracker += 1
                    break
            
            score *= tracker

        scores.append(score)

print("1 done: ", total)
print("2 done: ", max(scores))























# _____________________________________________________________________________________________________



# data = []


# with open('input.txt') as file:
#     for line in file.readlines():
#         data.append(line.strip())

# trees = 0 
# movements = [[1, 0],[-1, 0],[0, -1],[0, 1]]
# for x in range(len(data)):
#     for y in range(len(data[x])):
#         for i in range(4):
#             xx = x + movements[i][0]
#             yy = y + movements[i][1]
#             h = int(data[x][y])
#             okay = True
#             while xx >= 0 and xx < len(data) and yy >= 0 and yy < len(data[x]):
#                 if int(data[xx][yy]) >= h:
#                     okay = False
#                     break
#             xx += movements[i][0]
#             yy += movements[i][1]
#         if okay == True:
#             trees += 1
#             break

# print("1 done: ", trees)


# max_score = 0
# movements = [[1, 0], [-1, 0], [0, -1], [0, 1]]
# for x in range(len(data)):
#     for y in range(len(data[x])):
#         score = 1
#         for i in range(4):
#             xx = x + movements[i][0]
#             yy = y + movements[i][1]
#             h = int(data[x][y])
#             moves = 0
#             while xx >= 0 and xx < len(data) and yy >= 0 and yy < len(data[x]):
#                 moves += 1
#                 if int(data[xx][yy]) >= h:
#                     break
#             xx += movements[i][0]
#             yy += movements[i][1]
#         score *= moves
#     max_score = max(max_score, score)

# print("2 done: ", max_score)