from string import ascii_uppercase

# Getting input
with open('input.txt') as file:
    stack_strings, instructions = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))

"""
'stacks' is a dictionary that will store {stack number}:{[characters in stack]}
'indexes' is a list that stores the indexes in which the characters needed to fill 
    the stacks will be found. 
"""
stacks = {int(digit):[] for digit in stack_strings[-1].replace(" ","")}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != " "]

# Used to display the contents in each stack
def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")


# Loading the stacks off the input
def loadStacks():
    for string in stack_strings[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] == " ":
                pass
            else:
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

# Clearing the lists in every stack 
def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

# Used to get the characters at the end of every stack 
def getStackEnds():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return answer

# === PART 1 ===
loadStacks()
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    for crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)

print("1 done: ", getStackEnds())


# === PART 2 ===
emptyStacks()
loadStacks()
for instruction in instructions:
    instruction = instruction.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    instruction = [int(i) for i in instruction]

    crates = instruction[0]
    from_stack = instruction[1]
    to_stack = instruction[2]

    crates_to_remove = stacks[from_stack][-crates:]
    stacks[from_stack] = stacks[from_stack][:-crates]

    for crate in crates_to_remove:
        stacks[to_stack].append(crate)

print("2 done: ", getStackEnds())





#__________________________________________________________________________________________________
# data = []
# delimiter = ' '

# with open('input.txt') as file:
#     for line in file.readlines():
#         element = []
#         for token in line.strip().split(delimiter):
#             element.append(token)
#         data.append(element)

# stacks = [[" "], ["S", "P", "H", "V", "F", "G"], ["M", "Z", "D", "V", "B", "F", "J", "G"], ["N", "J", 'L', 'M', 'G'], ['P', 'W', 'D', 'V', 'Z', 'G', 'N'], ['B', 'C', 'R', 'V'], ['Z', 'L', 'W', 'P', 'M', 'S', 'R', 'V'], ['P', 'H', 'T'], ['V', 'Z', 'H', 'C', 'N', 'S', 'R', 'Q'], ['J', 'Q', 'V', 'P', 'G', 'L', 'F']]

# for item in data:
#     f = int(item[3])
#     t = int(item[5])
#     for times in range(int(item[1])):
#         letter = stacks[f][-1]
#         del(stacks[f][-1])
#         stacks[t].append(letter)

# solution = ''
# for stack in stacks:
#     solution += stack[-1]

# print("1 done: ", solution)



# stacks = [["-"], ["S", "P", "H", "V", "F", "G"], ["M", "Z", "D", "V", "B", "F", "J", "G"], ["N", "J", 'L', 'M', 'G'], ['P', 'W', 'D', 'V', 'Z', 'G', 'N'], ['B', 'C', 'R', 'V'], ['Z', 'L', 'W', 'P', 'M', 'S', 'R', 'V'], ['P', 'H', 'T'], ['V', 'Z', 'H', 'C', 'N', 'S', 'R', 'Q'], ['J', 'Q', 'V', 'P', 'G', 'L', 'F']]

# for item in data:
#     f = int(item[3])
#     t = int(item[5])
#     x = []
#     for times in range(int(item[1])):
#         letter = stacks[f][-1]
#         del(stacks[f][-1])
#         x.insert(0, letter)
#     for letter in x:
#         stacks[t].append(letter)

# solution = ''
# for stack in stacks:
#     solution += stack[-1]

# print("2 done: ", solution)