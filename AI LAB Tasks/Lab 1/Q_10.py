# 10.  Write a printASCIITable() function that displays the ASCII number and its corres-
# ponding text character, from 32 to 126. (These are called the printable ASCII characters.)

# Your solution is correct if calling printASCIITable() displays output that looks like the fol-
# lowing:

# 32
# 33 !
# 34 "
# 35
# --more--
# 124 |
# 125 }
# 126 ~
# Note that the character for ASCII value 32 is the space character, which is why it looks like
# nothing is next to 32 in the output.

def printASCIITable():
    for i in range(32, 127):
        print(i, chr(i))


printASCIITable()
