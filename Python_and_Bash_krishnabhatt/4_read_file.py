# Task 4: Read from a File
# Opens the file in read mode and displays its content using file.read().

file = open("notes.txt", "r")
content = file.read()
file.close()

print("Content of notes.txt:\n")
print(content)
