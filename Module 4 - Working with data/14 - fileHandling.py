
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists


# Creating a file

# createFile = open('./myFile.txt', 'x')


# ------------------ Writing in a file -----------------------

writeFile = open('./myFile.txt', 'w')
writeFile.write(
    "My name is Ahmad Faraz \nI am Blockchain dapp developer\nI have an expertise of 1.5 years in developing layer 2 solution dapps")
writeFile.close()


# ------------------ Reading a file -------------------------

# Here, you manually open the file and explicitly call close() after reading.
# If an error occurs before close() is called, the file might remain open, which can lead to resource leaks.

# readFile = open('./myFile.txt', 'r')
# print(readFile.read())
# readFile.close()


# ----------------- Appending content in a file ----------------------

# updateFile = open('./myFile.txt', 'a')
# updateFile.write(" and i am a blockchain developer")
# updateFile.close()


# The with statement ensures automatic file closure after the block is executed, even if an exception occu
with open('./myFile.txt', 'r') as readFile:
    fileContent = readFile.readline()  # My name is Ahmad Faraz
    print(fileContent)
