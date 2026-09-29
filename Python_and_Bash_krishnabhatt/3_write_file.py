# Task 3: Write to a File
# Creates a text file and writes some content to it using open() and write().

file = open("notes.txt", "w")
file.write("Hello, this is my DevOps assignment.\n")
file.write("I am learning Python and Bash.\n")
file.write("This file was created using Python file handling.\n")
file.close()

print("File 'notes.txt' created and content written successfully.")
