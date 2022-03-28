splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh,...he's resting".""")

anotherSplitString = """This string has been \
split over \
several \
lines"""

# the backslash causes problems here, so add two backslashes so P knows to include them and not use the 't' and n'
print(anotherSplitString)
print("C:\\Users\\timbuchalka\\notes.txt")

# or you can prefext the string with an 'r' which stand for raw string, so \ is not interpreted as a command

print(r"C:\Users\timbuchalka\notes.txt")