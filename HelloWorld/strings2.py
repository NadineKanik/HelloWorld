#
#       01234567890123 shows numbers 0-13 for each letter, because programs start counting at '0'.
#    (-)43210987654321 shows the negative indexing, so just done in reverse.
parrot="Norwegian Blue"

print(parrot[0:6:2]) # Nre, this is used when we want to add a step in a slice. In this case we step through the
# sequence in steps of 2
print(parrot[0:6:3]) # Nw, Here we step through the sequence in steps of 3

number = "9,223,372,036,854,775,807"
print(number[1::4]) # ,,,,,,   This illustrates how the steps work by outputting only the commas in the number
# sequence above. So here it is printing from position 1 and every 4th step for the whole sequence.

# Demo for later in course used to show value of above.
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val)for val in values])