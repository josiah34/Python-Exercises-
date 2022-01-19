# Write a Python program that prints the character at index i in the string s.
#
# If the index is out of range, the program should print "i is out of range"
#
# If the string is empty, the program should print "Empty String"

def string_index(i, string):
    if len(string) < i:
        print("I is out of range")
    elif len(string) == 0:
        print("Empty String")
    else:
        print(string[i])


string_index(5, "Wednesday")
