with open("input.txt") as file:
    commands = file.readlines()

dirs = {"/home":0}
path = "/home"

# Process every command
for command in commands:

    # Commands that start with $
    if command[0] == "$":
        
        # Do nothing 
        if command[2:4] == "ls":
            pass
        
        # Manage changing the path 
        elif command[2:4] == "cd":
            
            # # Go back to the root
            if command[5:6] == "/":
                path = "/home"

            # Go back in the path
            elif command[5:7] == "..":
                path = path[0:path.rfind("/")]

            # Change the path
            else:
                dir_name = command[5:]              # Get name of directory
                path = path + "/" + dir_name        # Add to the path
                dirs.update({path:0})               # Update our dictionary

    
    # Do nothing when listing directories available
    elif command[0:3] == "dir":
        pass

    else:
        size = int(command[:command.find(" ")])     # Get size of file
        
        # Update size for every directory down to /home
        dir = path
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]


total = 0

# space required - space unused (total space - space used)
limit = 30000000 - (70000000 - dirs["/home"])
valid_dirs = []

# Iterate through every path
for dir in dirs:
    
    # ==== PART 1 ====
    if dirs[dir] < 100000:
        total += dirs[dir]
    
    # ==== PART 2 ====
    if limit <= dirs[dir]:
        valid_dirs.append(dirs[dir])

smallest = min(valid_dirs)

print("1 done: ", total)
print("2 done: ", smallest)





















# __________________________________________________________________________________________________________
# data = []
# delimiter = ' '

# with open('input.txt') as file:
#     for line in file.readlines():
#         element = []
#         for token in line.strip().split(delimiter):
#             element.append(token)
#         data.append(element)

# # print("element is: ", element)
# # print("data is: ", data)

# total = 0

# def Sum (FileSystem):
#     global total
#     sum = 0
#     for element in FileSystem:
#         if len(element) == 2 and len(element[1]) == 0:
#             pass
#         elif type(element[0][1]) == str:
#             sum += int(element[0][1])
#         else:
#             sum += Sum(element)
#     if sum <= 100000:
#         total += sum
#     return sum

# def Add(File, Directory, FileSystem):
#     if Directory == []:
#         if File not in FileSystem:
#             FileSystem.append([File])
#     else:
#         found = False
#         for element in FileSystem:
#             if element[0][0] == Directory[0]:
#                 found = True
#                 Add(File, Directory[1:], element)
#         if found == False:
#             n = [[Directory[0], []]]
#             FileSystem.append(n)
#             Add(File, Directory[1:], n)

# directory = []
# files = []

# index = 0 
# while index < len(data) - 1:
#     if data[index][1] == "cd":
#         if data[index][2] == "/":
#             directory = []
#         elif data[index][2] == "..":
#             directory.pop()
#         else:
#             directory.append(data[index][2])
#         index += 1
#     elif data[index][1] == "ls":
#         index += 1
#         while data[index][0] != "$":
#             if data[index][0] != "dir":
#                 Add([data[index][1], data[index][0]], directory, files)
#             index += 1

# size = Sum(files)
# print("1 done: ", total)
# print("2 done: ", files)

