s_file = open('hamlet.txt')  # Crashed !

# Recommended Way
with open('hamlet.txt',mode="r") as s_file:

# 1. Printing each line
for line in s_file.readlines():
    print(line.strip())

print("Finished")

#2. Print Each Word

for line in s_file.readlines():
    # words = line.split(" ")
    words = line.strip().split(" ")  # Removed BackSlash \n

    print(words)
print("Finished")

# 3. Count All Words
words_all = []

for line in s_file.readlines():
    words = line.strip().split(" ")  # Removed BackSlash \n

    words_all = words_all + words #Adding one list with another

print(words_all)
print(len(words_all)) #298 #All Words
print("Finished")


# Unique Words
words_all = []

for line in s_file.readlines():
    words = line.strip().split(" ")  # Removed BackSlash \n

    words_all = words_all + words #Adding one list with another


# print(words_all)
print(len(words_all)) #298 #All Words
unique_words = set(words_all)
print(len(unique_words)) #97 Duplicate Words
print("Finished")


# Saving All unique words in a new file :
with open('unique_words.txt',mode = "w") as write_file:
    i = 1
    for item in unique_words:
        write_file.write(f"{i}.")
        write_file.write(str(item).title())
        write_file.write("\n")
        i+=1