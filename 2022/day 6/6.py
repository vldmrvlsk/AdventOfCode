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


# with open('input.txt') as file:
#     data = file.readline()

# lenghtNeeded = 4
# letters = [' '] * lenghtNeeded
# index = 0 
# for letter in data:
#     index += 1
#     letters = letters[1:]
#     letters.append(letter)
#     if len(set(letters)) == lenghtNeeded and letters[0] != ' ':
#         print("1 done: ", index)
#         break



# lenghtNeeded = 14
# letters = [' '] * lenghtNeeded
# index = 0 
# for letter in data:
#     index += 1
#     letters = letters[1:]
#     letters.append(letter)
#     if len(set(letters)) == lenghtNeeded and letters[0] != ' ':
#         print("2 done: ", index)
#         break