# Task 3: Write to a File
# Creates a text file and writes some content to it using open() and write().

file = open("sample.txt", "w")   # "w" mode creates the file (or overwrites it)
file.write("Hello, this is my DevOps assignment.\n")
file.write("I am learning Python file handling.\n")
file.write("This file was created using open() and write().\n")
file.close()

print("File 'sample.txt' created and content written successfully.")
