# Getting data
with open('input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]


# print(data)


# Traversing every STRING in our DATA
max = 0
max2 = 0    # Elf with second greatest calories
max3 = 0    # Elf with third greatest cals
count = 0
for item in data:
    if item == '':
        count = 0       # Resetting the count | skipping to next Elf
    else:
        num = int(item) # Turning string to integer (so we can add)
        count += num    # Adding to the count if its a number

    # Finding max values
    # EDIT: We need to shift the previous max values found
    # before setting new values!!
    if count > max: 
        max3 = max2
        max2 = max
        max = count
    elif count > max2:
        max3 = max2
        max2 = count    # Elf with second to most 
    elif count > max3:
        max3 = count    # Elf with third to most 


# Answers
print("1 done: ", max)
print("2 done: ", max+max2+max3)













#________________________________________________________________________
# data = []

# with open('input.txt') as file:
#     score = 0
#     for line in file.readlines():
#         line = line.strip()
#         if line == "":
#             data.append(score)
#             score = 0
#         else:
#             score += int(line)

# print("1 done: ", max(data))

# data = sorted(data)
# print("2 done: ", data[-1] + data[-2] + data[-3])