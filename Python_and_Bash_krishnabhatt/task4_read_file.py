# Task 4: Read from a File
# Opens the file in read mode and displays its content using file.read().

file = open("sample.txt", "r")   # "r" mode opens the file for reading
content = file.read()
file.close()

print("Content of sample.txt:")
print("-----------------------")
print(content)
